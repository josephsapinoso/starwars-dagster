# Star Wars Dagster — GitHub repo setup script
# Run this once from the starwars_dagster directory:
#   cd "C:\Users\josep\Documents\Claude\Projects\Learning Data Engineering and Analytics\starwars_dagster"
#   .\create_github_repo.ps1

$ErrorActionPreference = "Stop"

$username  = "josephsapinoso"
$repoName  = "starwars-dagster"
$repoDesc  = "End-to-end Dagster pipeline pulling live Star Wars data (SWAPI) into DuckDB with SQL transforms and a Markdown analytics report."

Write-Host ""
Write-Host "GitHub repo setup for $username/$repoName" -ForegroundColor Cyan
Write-Host "--------------------------------------------"
Write-Host "You need a GitHub Personal Access Token with 'repo' scope."
Write-Host "Create one at: https://github.com/settings/tokens/new"
Write-Host ""
$token = Read-Host "Paste your GitHub token here" -AsSecureString
$plainToken = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto(
    [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($token)
)

Write-Host ""
Write-Host "Creating GitHub repository..." -ForegroundColor Yellow

$headers = @{
    Authorization = "Bearer $plainToken"
    Accept        = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

$body = @{
    name        = $repoName
    description = $repoDesc
    private     = $false
    auto_init   = $false
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod `
        -Uri "https://api.github.com/user/repos" `
        -Method POST `
        -Headers $headers `
        -Body $body `
        -ContentType "application/json"

    Write-Host "Repo created: $($response.html_url)" -ForegroundColor Green
} catch {
    if ($_.Exception.Response.StatusCode -eq 422) {
        Write-Host "Repo already exists — continuing with push." -ForegroundColor Yellow
    } else {
        Write-Host "Error creating repo: $_" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "Initialising git and committing files..." -ForegroundColor Yellow

git init -b main
git config user.name  "Joe Sapinoso"
git config user.email "josephsapinoso@gmail.com"
git add .
git commit -m "Initial commit: Star Wars Dagster pipeline

End-to-end data pipeline using Dagster OSS + SWAPI:
- Layer 1: Raw ingestion (films, people, planets, starships, species)
- Layer 2: DuckDB storage
- Layer 3: SQL transforms (enriched characters, film cast counts, starship stats)
- Layer 4: Markdown analytics report

Stack: Dagster 1.x, DuckDB, Pandas, SWAPI (swapi.info)"

Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow

$remoteUrl = "https://$($username):$($plainToken)@github.com/$username/$repoName.git"
git remote add origin $remoteUrl
git push -u origin main

Write-Host ""
Write-Host "Done! View your repo at:" -ForegroundColor Green
Write-Host "  https://github.com/$username/$repoName" -ForegroundColor Cyan
Write-Host ""
