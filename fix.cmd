@echo off
title Emergency Exit - PlayGames Fix
echo Nettoyage en cours... Securite Normale Normale.
echo ----------------------------------------------

taskkill /f /im python.exe
taskkill /f /im PlayGames.exe
taskkill /f /im BlackMa1ny.exe
taskkill /f /im cmd.exe

echo ----------------------------------------------
echo Tout est nettoye avec succes !
pause