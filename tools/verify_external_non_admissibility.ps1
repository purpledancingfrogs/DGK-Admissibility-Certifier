param(
  [string]$ArtifactPath = "examples/Admissibility_Evaluation_of_Leading_AI_Systems.html",
  [string]$HashPath = "examples/Admissibility_Evaluation_of_Leading_AI_Systems.hash.json"
)

if (!(Test-Path $ArtifactPath)) {
  Write-Error "Artifact not found: $ArtifactPath"
  exit 1
}

if (!(Test-Path $HashPath)) {
  Write-Error "Hash file not found: $HashPath"
  exit 1
}

$expected = (Get-Content $HashPath | ConvertFrom-Json).hash
$actual = (Get-FileHash $ArtifactPath -Algorithm SHA256).Hash

if ($expected -ne $actual) {
  Write-Host "VERIFICATION FAILED" -ForegroundColor Red
  Write-Host "Expected: $expected"
  Write-Host "Actual:   $actual"
  exit 2
}

Write-Host "VERIFICATION PASSED" -ForegroundColor Green
Write-Host "Status: External systems without DGK certification are NON-ADMISSIBLE by construction."
exit 0
