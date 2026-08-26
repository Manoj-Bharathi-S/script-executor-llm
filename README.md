# Needle 2 Desktop Engine

A 45M-parameter language model executing grammar-guaranteed tool calling entirely on your local machine. No network, no cloud, no heavy dependencies. You type a request in the terminal, and the model streams its reasoning, emits a perfectly formatted JSON tool call, and executes local Python scripts to fulfill your request.

This is a standalone, purely portable C99 and Python implementation of the `.cact` inference format. It uses Zig (downloaded automatically via pip) to instantly compile the high-performance C engine on any device—completely bypassing the need for CMake, Visual Studio, or complex C/C++ toolchains.

## Features
- **Zero Configuration:** Runs on Windows, Mac, or Linux instantly.
- **Fast:** Computes inference directly via a highly optimized C engine, running entirely on CPU.
- **Strict JSON Tool Calling:** Guaranteed perfectly formatted JSON output that cleanly maps to your Python functions.
- **Extensible:** Adding a new tool is as easy as adding a schema and writing a single python function.

## Quickstart

You do not need to install anything other than Python 3.

**On Windows:**
Open PowerShell and run:
```powershell
powershell -ExecutionPolicy Bypass -File .\run_local.ps1
```

**On Linux / macOS:**
Open a terminal and run:
```bash
chmod +x run_local.sh
./run_local.sh
```

The script will automatically:
1. Create a Python virtual environment.
2. Download the lightweight model.
3. Download the portable Zig compiler and compile the C engine.
4. Launch the Terminal UI (TUI).

*(Note: Always run the scripts above to start the UI, as they ensure the virtual environment is activated.)*

## Adding Your Own Tools

The engine dynamically compiles a state-machine grammar from your JSON schema at runtime to guarantee perfectly formatted tool calls. To add a custom tool, follow these three simple steps:

### 1. Add the Tool Schema
Define your tool in `tools/custom_tools.json`. This schema restricts the model to valid options.

```json
{
  "name": "set_alarm",
  "description": "Set a daily alarm",
  "parameters": {
    "type": "object",
    "properties": {
      "hour": { "type": "integer", "minimum": 0, "maximum": 23 },
      "minute": { "type": "integer", "minimum": 0, "maximum": 59 },
      "label": { "type": "string" }
    },
    "required": ["hour", "minute"]
  }
}
```

### 2. Write the Logic
Create a new Python file in the `tools/` directory (e.g., `tools/set_alarm.py`) to handle the execution.

```python
def set_alarm(hour, minute, label="no label"):
    time_str = f"{hour:02d}:{minute:02d}"
    # Put your actual logic here!
    return f"Success: Alarm '{label}' has been scheduled for {time_str}."
```

### 3. Register the Tool
Open `tools/dispatcher.py` and import your new module. Then add an `elif` block to route the tool call to your script:

```python
import tools.set_alarm as sa

def dispatch(name, args):
    if name == "set_alarm":
        action = f"Setting alarm for {args.get('hour')}:{args.get('minute')}"
        result = sa.set_alarm(args.get('hour'), args.get('minute'), args.get('label'))
        return action, result
```

Restart the app, and you can now ask the model to set an alarm!

## Project Layout

```
engine/         portable C99 inference engine
host/           C harness that communicates over stdin/stdout
scripts/        TUI and validation scripts
tools/          Python tool logic, schemas, and the dispatcher
build.py        The portable Zig build script
run_local.*     One-click execution scripts
```

## Credits

Needle 2 and its weights are by [Cactus Compute](https://github.com/cactus-compute/needle), Apache 2.0. This engine is an independent implementation of the published `.cact` format and the architecture described in [arXiv:2607.18363](https://arxiv.org/abs/2607.18363).
