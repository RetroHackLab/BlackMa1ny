@echo off
title Emergency Exit - PlayGames Fix
echo Cleaning Tasks & Emergency Exit .
echo ----------------------------------------------

taskkill /f /im python.exe
taskkill /f /im PlayGames.exe
taskkill /f /im BlackMa1ny.exe
taskkill /f /im cmd.exe

echo ----------------------------------------------
echo All Tasks cleaned succesfuly !
pause
