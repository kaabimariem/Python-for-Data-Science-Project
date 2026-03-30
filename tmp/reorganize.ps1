# Terminate processes
try { taskkill /F /IM python.exe } catch {}
try { taskkill /F /IM node.exe } catch {}

# Base directory
$base = "c:\Users\MSI\Desktop\projet ds2"

# 1. Rename app to frontend
if (Test-Path "$base\app") {
    Rename-Item -Path "$base\app" -NewName "frontend" -Force
}

# 2. Move files from Docker to root
if (Test-Path "$base\Docker") {
    if (Test-Path "$base\Docker\Dockerfile.backend") { Move-Item "$base\Docker\Dockerfile.backend" "$base\" -Force }
    if (Test-Path "$base\Docker\Dockerfile.frontend") { Move-Item "$base\Docker\Dockerfile.frontend" "$base\" -Force }
    Remove-Item "$base\Docker" -Recurse -Force
}

# 3. Move requirements.txt from code to root
if (Test-Path "$base\code\requirements.txt") {
    Move-Item "$base\code\requirements.txt" "$base\" -Force
}

# 4. Create missing folders
$folders = ".github\workflows", ".vscode", "Archives", "Software_Engineering_Project", "cours", "mlruns"
foreach ($f in $folders) {
    if (-not (Test-Path "$base\$f")) {
        New-Item -ItemType Directory -Path "$base\$f" -Force
    }
}

# 5. Create missing files
$files = ".gitignore", "docker-compose.yml", "guide_projet.pdf", "mlflow.db", "walkthrough.md"
foreach ($f in $files) {
    if (-not (Test-Path "$base\$f")) {
        New-Item -ItemType File -Path "$base\$f" -Force
    }
}
