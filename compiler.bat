@echo off
title Mon Compilateur PlayGames Unique
cls

echo ===================================================
echo   NETTOYAGE ET COMPILATION EMBARQUÉE (STITCH)
echo ===================================================
echo.

:: Suppression des anciens dossiers et résidus de cache
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist Main.spec del /q Main.spec

echo [1/1] Compilation forcee avec integration du fichier WAV...
:: L'argument --add-data injecte le son directement au coeur du binaire (.exe)
py -m PyInstaller --clean --onefile --noconsole --exclude pygame --add-data "MEME.wav;." Main.py

echo.
echo ===================================================
echo   COMPILATION TERMINEE AVEC SUCCES !
echo ===================================================
echo.
echo Tu peux maintenant :
echo 1. Aller dans le dossier 'dist' qui vient de se creer.
echo 2. Prendre 'Main.exe' et le renommer en 'PlayGames.exe'.
echo.
echo [*] Tu peux deplacer ce 'PlayGames.exe' n'importe ou TOUT SEUL.
echo     Il contient deja sa propre musique 'MEME.wav' integree !
echo.
pause