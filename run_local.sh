#!/usr/bin/env bash
set -e

echo "1. Creating and activating a virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "2. Installing dependencies..."
pip install numpy rich pyserial huggingface_hub sentencepiece pillow ziglang

echo "3. Downloading the model..."
python3 -c "from huggingface_hub import hf_hub_download; import shutil, os; os.makedirs('model', exist_ok=True); shutil.copy(hf_hub_download('Cactus-Compute/needle2','needle2.cact'), 'model/needle2.cact')"

echo "4. Building the host engine for local testing..."
python3 build.py

echo "5. Running the TUI..."
python3 scripts/needle_tui.py --local --tools tools/custom_tools.json
