[CmdletBinding()]
param(
    [string]$Destination = 'D:\Obsidian\老板行业日报'
)

$ErrorActionPreference = 'Stop'
$repository = 'gongjunxian720807-cyber/Horizon'
$archiveUrl = "https://github.com/$repository/archive/refs/heads/main.zip"
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("horizon-digest-" + [guid]::NewGuid().ToString('N'))
$zipPath = "$tempRoot.zip"

try {
    New-Item -ItemType Directory -Path $tempRoot | Out-Null
    Invoke-WebRequest -Uri $archiveUrl -OutFile $zipPath
    Expand-Archive -LiteralPath $zipPath -DestinationPath $tempRoot

    $source = Join-Path $tempRoot 'Horizon-main\老板行业日报'
    if (-not (Test-Path -LiteralPath $source -PathType Container)) {
        throw "GitHub archive does not contain 老板行业日报."
    }

    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
    Get-ChildItem -LiteralPath $source | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
    }
    Write-Host "老板行业日报已同步到 $Destination"
}
finally {
    if ([System.IO.File]::Exists($zipPath)) {
        [System.IO.File]::Delete($zipPath)
    }
    if ([System.IO.Directory]::Exists($tempRoot)) {
        [System.IO.Directory]::Delete($tempRoot, $true)
    }
}
