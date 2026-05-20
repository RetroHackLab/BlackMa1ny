@echo off
title Compiler My Project
cls

echo ===================================================
echo   Clean & Stitching
echo ===================================================
echo.

:: Delete all Caches (If Exist)
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist Main.spec del /q Main.spec

echo [1/1] Stitching Audio to Main Executable Project & Build Executable...
:: Preparation PyInstaller & Build Binary & Convert Python Package (*.py) to Executable (.exe)
py -m PyInstaller --clean --onefile --noconsole --exclude pygame --add-data "MEME.wav;." Main.py

echo.
echo ===================================================
echo   Complication Propably Done !
echo ===================================================
echo.
echo You can now  :
echo 1. Go to /dist/.
echo 2. Get 'Main.exe' & rename it to 'PlayGames.exe'.
echo.
echo [*] You can  deplace  'PlayGames.exe' werever Folder or Standlonely.
echo     Audio Stitching Done !
echo.
pause
