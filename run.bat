@echo off
REM
set SCRIPT_NAME=main.py

REM
python3 %SCRIPT_NAME%
if %ERRORLEVEL% neq 0 (
    REM 
    python %SCRIPT_NAME%
)

REM
pause
