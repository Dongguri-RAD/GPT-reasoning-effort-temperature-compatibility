# GPT reasoning-effort and temperature compatibility test

This repository provides the Python code used to test API-level compatibility between `reasoning.effort` settings and `temperature control (herein set to 0.0)` in GPT-5.5 and -5.4 models.

The script records simply whether each request is accepted or rejected by the API.

## Files

- `run_compatibility.py`: Python script for compatibility testing

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
