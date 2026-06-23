[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path

Push-Location $RepoRoot
try {
    & python 60_automation\workspace_maintenance\audit_workspace.py --write-report
    $auditExit = $LASTEXITCODE

    & python 60_automation\workspace_maintenance\refresh_live_indexes.py --write
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }

    & python 60_automation\workspace_maintenance\consolidate_learning_candidates.py --write
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }

    & git diff --check
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }

    if ($auditExit -ne 0) {
        exit $auditExit
    }
}
finally {
    Pop-Location
}
