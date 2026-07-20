"""
Layer 4: Analytics / Reporting Assets
======================================
Final output layer — produces a human-readable Markdown report summarizing
key insights from the galaxy far, far away.

Key Dagster concept — asset metadata:
  We use context.add_output_metadata() to attach previews and stats to the
  asset in the Dagster UI, so you can inspect results without opening files.

Asset lineage here:
  characters_enriched ───┐
  film_character_counts ─┤
  starship_stats ────────┼──► galaxy_report (Markdown file)
  character_stats ───────┤
  character_biographies ─┘
"""

import json

import pathlib
import pandas as pd
from dagster import asset, AssetExecutionContext, MetadataValue

_GROUP = "03_analytics"
OUTPUT_DIR = pathlib.Path("data/output")


@asset(
    group_name=_GROUP,
    description="Markdown summary report — the galaxy by the numbers",
)
def galaxy_report(
    context: AssetExecutionContext,
    characters_enriched: pd.DataFrame,
    film_character_counts: pd.DataFrame,
    starship_stats: pd.DataFrame,
    character_stats: pd.DataFrame,
    character_biographies: pd.DataFrame,
) -> str:
    """
    Assembles a Markdown report from the five transform assets.

    This is your 'presentation layer' — what a stakeholder or analyst would
    consume. In a real pipeline you might push this to Slack, email, or Notion.
    """

    # ── Characters by homeworld ───────────────────────────────────────────────
    homeworld_counts = (
        characters_enriched.groupby("homeworld")
        .size()
        .reset_index(name="characters")
        .sort_values("characters", ascending=False)
        .head(10)
    )

    # ── Gender breakdown ─────────────────────────────────────────────────────
    # rename_axis + reset_index(name=...) works on pandas 1.x and 2.x+ alike;
    # the old reset_index().rename(columns={"index": ...}) idiom silently
    # produces two "count" columns on pandas >= 2.0
    gender_counts = (
        characters_enriched["gender"]
        .value_counts()
        .rename_axis("gender")
        .reset_index(name="count")
    )

    # ── Climate of characters' homeworlds ────────────────────────────────────
    # Counts CHARACTERS (one row each), not distinct planets — label accordingly
    climate_counts = (
        characters_enriched["homeworld_climate"]
        .dropna()
        .value_counts()
        .head(8)
    )
    climate_known = int(characters_enriched["homeworld_climate"].notna().sum())
    homeworld_known = int(characters_enriched["homeworld"].notna().sum())

    # ── Screen persistence (per-character grain) ──────────────────────────────
    total_characters = len(character_stats)
    one_film = int((character_stats["film_count"] == 1).sum())
    six_film_names = sorted(
        character_stats.loc[character_stats["film_count"] == 6, "character_name"]
    )
    pilots = int((character_stats["starships_flown"] > 0).sum())
    top_pilot = (
        character_stats.nlargest(1, "starships_flown")[["character_name", "starships_flown"]]
        .to_dict("records")
    )

    # ── Second-source enrichment (akabab profiles) ────────────────────────────
    # Nested-denominator law (panel, 2026-07-20): every number from this sparse
    # enrichment join names BOTH the matched denominator and the field-present
    # denominator. "On file" vocabulary throughout — the source records
    # sequel-era deaths and lags canon, so presence is the only honest claim.
    matched = character_biographies[character_biographies["profile_id"].notna()]
    matched_count = len(matched)
    aff_present = int(matched["affiliation_count"].notna().sum())
    aff_nonzero = int((matched["affiliation_count"] > 0).sum())
    affiliation_counts = (
        pd.Series(
            [
                name
                for cell in matched["affiliations"].dropna()
                for name in json.loads(cell)
            ]
        )
        .value_counts()
        .head(10)
        .rename_axis("affiliation")
        .reset_index(name="characters")
        if aff_nonzero
        else pd.DataFrame(columns=["affiliation", "characters"])
    )
    masters_on_file = int((matched["master_count"] > 0).sum())
    apprentices_on_file = int((matched["apprentice_count"] > 0).sum())
    deaths_on_file = int(matched["died_year_aby"].notna().sum())

    # ── Best hyperdrive ships ─────────────────────────────────────────────────
    best_ships = (
        starship_stats
        .dropna(subset=["hyperdrive_rating"])
        .nsmallest(5, "hyperdrive_rating")[["name", "model", "hyperdrive_rating", "starship_class"]]
    )

    # ── Build the Markdown ────────────────────────────────────────────────────
    def df_to_md(df: pd.DataFrame) -> str:
        """Render a small DataFrame as a Markdown table."""
        header = "| " + " | ".join(str(c) for c in df.columns) + " |"
        sep = "| " + " | ".join("---" for _ in df.columns) + " |"
        rows = [
            "| " + " | ".join(str(v) for v in row) + " |"
            for row in df.itertuples(index=False)
        ]
        return "\n".join([header, sep] + rows)

    report_lines = [
        "# 🌌 Star Wars Galaxy Report",
        "",
        "> *Generated by the Star Wars Dagster Pipeline*",
        "",
        "---",
        "",
        "## 🎬 Films at a Glance",
        "",
        df_to_md(film_character_counts[["title", "episode_id", "release_date", "character_count", "starship_count"]]),
        "",
        "---",
        "",
        "## 👥 Characters",
        "",
        f"**Total characters tracked:** {len(characters_enriched)}",
        "",
        "### Gender Breakdown",
        "",
        df_to_md(gender_counts),
        "",
        "### Top 10 Homeworlds by Character Count",
        "",
        f"*{homeworld_known} of {len(characters_enriched)} characters have a known homeworld.*",
        "",
        df_to_md(homeworld_counts),
        "",
        "### Homeworld Climate Distribution",
        "",
        f"*Among the {climate_known} of {len(characters_enriched)} characters whose homeworld climate is known.*",
        "",
        "\n".join(f"- **{climate}**: {count} characters" for climate, count in climate_counts.items()),
        "",
        "### Screen Persistence",
        "",
        f"- **{one_film} of {total_characters}** characters appear in exactly one film",
        f"- Only **{len(six_film_names)}** appear in all six: {', '.join(six_film_names) if six_film_names else '—'}",
        f"- **{pilots} of {total_characters}** are ever listed at a starship's controls",
        "\n".join(
            f"- Most starships flown: **{r['character_name']}** ({r['starships_flown']})"
            for r in top_pilot
        ),
        "",
        "---",
        "",
        "## 🤝 Affiliations & Apprenticeships",
        "",
        f"*{matched_count} of {total_characters} census characters matched to a curated "
        "profile (akabab dataset — fan-curated, MIT); per-field coverage noted per table.*",
        "",
        "### Top Affiliations",
        "",
        f"*Among the {matched_count} matched, {aff_present} carry an affiliations list "
        f"and {aff_nonzero} list at least one.*",
        "",
        df_to_md(affiliation_counts),
        "",
        "### Apprenticeships",
        "",
        f"- **{masters_on_file} of {matched_count}** matched profiles have a master on file",
        f"- **{apprentices_on_file} of {matched_count}** matched profiles have an apprentice on file",
        "",
        "### Deaths on File",
        "",
        f"- **{deaths_on_file} of {matched_count}** matched profiles record a death",
        "",
        "*'On file' means the curated source records it — absence is not survival.*",
        "",
        "---",
        "",
        "## 🚀 Starships",
        "",
        f"**Total starships tracked:** {len(starship_stats)}",
        "",
        "### Top 5 Fastest Hyperdrives (lower rating = faster)",
        "",
        df_to_md(best_ships),
        "",
        "### By Starship Class",
        "",
        df_to_md(
            starship_stats["starship_class"]
            .value_counts()
            .rename_axis("class")
            .reset_index(name="count")
        ),
        "",
        "---",
        "",
        "*May the Force be with your data pipeline.*",
    ]

    report = "\n".join(report_lines)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUT_DIR / "galaxy_report.md"
    report_path.write_text(report, encoding="utf-8")

    # Attach a preview directly in the Dagster UI asset page
    context.add_output_metadata(
        {
            "report_path": str(report_path),
            "preview": MetadataValue.md(report[:2000] + "\n\n*(truncated)*"),
        }
    )

    return str(report_path)
