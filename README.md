# GPT reasoning-effort and temperature compatibility test

This repository provides the Python code used to test API-level compatibility between `reasoning.effort` settings and `temperature control (herein set to 0.0)` in GPT-5.5 and -5.4 models.

The script records simply whether each request is accepted or rejected by the API.

## Files

- `run_compatibility.py`: Python script for compatibility testing
- `requirements.txt`: Required Python package

## Tested parameter combinations

The script tests the following models:

- `gpt-5.4`
- `gpt-5.5`

The script tests the following `reasoning.effort` values with `temperature=0.0`:

- `none`
- `low`
- `medium`
- `high`
- `xhigh`

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

## Setting the OpenAI API Key

This script requires an OpenAI API key. The key should be provided as an environment variable named `OPENAI_API_KEY`.

Do not write your API key directly in `run_compatibility.py`.

### macOS or Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### Windows Command Prompt

```cmd
set OPENAI_API_KEY=your_api_key_here
```

## Running the Script

After setting the environment variable, run:

```bash
python run_compatibility.py
```
