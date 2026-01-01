#!/bin/bash
# JupyterLab起動スクリプト（general-analysis用）
# ノートブックは notebooks フォルダに保存されます

cd /Users/k-kawahara/Data-Science/general-analysis
/opt/homebrew/bin/uv run jupyter lab --notebook-dir=./notebooks
