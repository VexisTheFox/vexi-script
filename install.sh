#!/bin/bash

echo "🐾 Vexi Installer Script"

INSTALL_URL="https://raw.githubusercontent.com/VexisTheFox/vexi-script/main/install.py"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed!"
    exit 1
fi

# Try to use venv
echo "🔍 Checking for virtual environment support..."
python -m venv vexi_env 2>/dev/null

if [ -d "vexi_env" ]; then
    echo "✅ Created virtual environment!"
    source vexi_env/bin/activate
    python -c "import urllib.request; exec(urllib.request.urlopen('$INSTALL_URL').read())"
    deactivate
else
    echo "⚠️ Could not create virtual environment. Using --break-system-packages..."

    python -c "
import urllib.request
import subprocess
import sys

print('🌐 Downloading install.py...')
code = urllib.request.urlopen('$INSTALL_URL').read()
exec(compile(code, 'install.py', 'exec'))
" || echo "❌ Installer failed. You might need to install manually or use pipx."
fi
