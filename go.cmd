@echo off
cd /d "%~dp0"
E:\.venv-parakeet\Scripts\python.exe transcribe_channel.py %* >> run.log 2>> run.err
