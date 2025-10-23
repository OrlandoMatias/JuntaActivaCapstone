param(
  [string]$Url = 'http://127.0.0.1:5000',
  [int]$Retries = 40,
  [int]$DelayMs = 500
)

# Ensure script runs from project root
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location (Join-Path $scriptDir '..')

Write-Host "Starting dev server in a new PowerShell window (running: npm run esbuild:dev)"

# Start dev server in a new window so this helper can exit/continue
$cwd = (Get-Location).Path
Start-Process powershell -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-Command',"cd `"$cwd`"; npm run esbuild:dev") -WorkingDirectory $cwd -WindowStyle Normal

Write-Host "Waiting for $Url to respond... (up to $Retries attempts)"

$up = $false
for ($i = 0; $i -lt $Retries; $i++) {
  try {
    $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 2 -ErrorAction Stop
    if ($resp.StatusCode -ge 200 -and $resp.StatusCode -lt 400) {
      $up = $true
      break
    }
  } catch {
    # ignore - server not ready
  }
  Start-Sleep -Milliseconds $DelayMs
}

if ($up) {
  Write-Host "Dev server is up. Opening browser -> $Url"
  Start-Process $Url
} else {
  Write-Warning "Server did not respond after $Retries attempts. Opening browser anyway."
  Start-Process $Url
}

Pop-Location
