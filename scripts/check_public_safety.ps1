param(
    [Parameter(Mandatory = $false)]
    [string]$Root = "."
)

$ErrorActionPreference = "Stop"
$resolvedRoot = (Resolve-Path -LiteralPath $Root).Path
$allowedExtensions = @(".md", ".py", ".ps1", ".json", ".yaml", ".yml", ".txt", ".toml")
$ignoredDirectories = @(".git", ".venv", "venv", "node_modules", "__pycache__")
$suspiciousNames = '(?i)(^\.env($|\.)|secret|credential|password|private[_-]?key|\.pem$|\.key$|\.pfx$|\.tmp$|\.temp$|\.bak$|~$)'
$contentPattern = '(?i)(api[_-]?key\s*[:=]|secret\s*[:=]|password\s*[:=]|bearer\s+[a-z0-9._-]+|BEGIN [A-Z ]*PRIVATE KEY|[A-Z]:\\Users\\[^\\]+|/Users/[^/]+|/home/[^/]+)'
$findings = New-Object System.Collections.Generic.List[object]

$files = Get-ChildItem -LiteralPath $resolvedRoot -Recurse -Force -File | Where-Object {
    $relative = $_.FullName.Substring($resolvedRoot.Length).TrimStart('\', '/')
    $parts = $relative -split '[\\/]'
    -not ($parts | Where-Object { $ignoredDirectories -contains $_ })
}

foreach ($file in $files) {
    $relative = $file.FullName.Substring($resolvedRoot.Length).TrimStart('\', '/')
    if ($file.Name -match $suspiciousNames) {
        $findings.Add([pscustomobject]@{ Type = "name"; File = $relative; Detail = "Suspicious filename" })
    }
    if (($allowedExtensions -contains $file.Extension.ToLowerInvariant()) -and ($relative -ne "scripts\check_public_safety.ps1")) {
        $lineNumber = 0
        foreach ($line in Get-Content -LiteralPath $file.FullName -ErrorAction Stop) {
            $lineNumber++
            if ($line -match $contentPattern) {
                $findings.Add([pscustomobject]@{ Type = "content"; File = $relative; Detail = "Sensitive pattern at line $lineNumber" })
            }
        }
    }
}

if ($findings.Count -gt 0) {
    $findings | ConvertTo-Json -Depth 3
    exit 1
}

[pscustomobject]@{
    status = "pass"
    root = $resolvedRoot
    scannedFiles = $files.Count
    findings = 0
} | ConvertTo-Json
