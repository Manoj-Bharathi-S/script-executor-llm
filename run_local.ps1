# 1. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install numpy rich pyserial huggingface_hub sentencepiece pillow

# 3. Download the model
python -c "from huggingface_hub import hf_hub_download; import shutil, os; os.makedirs('model', exist_ok=True); shutil.copy(hf_hub_download('Cactus-Compute/needle2','needle2.cact'), 'model/needle2.cact')"

# 4. Build the host engine for local testing using the portable Python build script
python build.py

# 5. Run the TUI in local mode with the custom tools
python scripts/needle_tui.py --local --tools tools/custom_tools.json
