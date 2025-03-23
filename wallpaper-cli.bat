@echo off
setlocal

REM Get the short path name for the directory
for %%I in ("D:\wallpaper-cli-tool") do set "SHORT_PATH=%%~sI"

REM Check if the first argument is "fetch-and-set"
if "%1"=="fetch-and-set" (
    shift
    set "QUERY=%*"
    python "%SHORT_PATH%\src\main.py" --fetch-and-set "%QUERY%"
) else (
    echo Usage: wallpaper-cli fetch-and-set "search query"
)

endlocal