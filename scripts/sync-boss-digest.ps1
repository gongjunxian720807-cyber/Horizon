[CmdletBinding()]
param(
    [string]$Destination = ''
)

$ErrorActionPreference = 'Stop'
$digestName = -join [char[]](0x8001, 0x677F, 0x884C, 0x4E1A, 0x65E5, 0x62A5)
if ([string]::IsNullOrWhiteSpace($Destination)) {
    $Destination = Join-Path 'D:\Obsidian' $digestName
}
$repository = 'gongjunxian720807-cyber/Horizon'
$archiveUrl = "https://github.com/$repository/archive/refs/heads/main.zip"
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("horizon-digest-" + [guid]::NewGuid().ToString('N'))
$zipPath = "$tempRoot.zip"

try {
    New-Item -ItemType Directory -Path $tempRoot | Out-Null
    Invoke-WebRequest -Uri $archiveUrl -OutFile $zipPath
    Expand-Archive -LiteralPath $zipPath -DestinationPath $tempRoot

    $source = Join-Path (Join-Path $tempRoot 'Horizon-main') $digestName
    if (-not (Test-Path -LiteralPath $source -PathType Container)) {
        throw "GitHub archive does not contain the digest folder."
    }

    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
    Get-ChildItem -LiteralPath $source | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
    }
    Write-Host "Boss industry digest synchronized to $Destination"
}
finally {
    if ([System.IO.File]::Exists($zipPath)) {
        [System.IO.File]::Delete($zipPath)
    }
    if ([System.IO.Directory]::Exists($tempRoot)) {
        [System.IO.Directory]::Delete($tempRoot, $true)
    }
}
