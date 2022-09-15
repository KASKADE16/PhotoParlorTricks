@echo off

for %%i in (test) do (
    set str=%%~ai
    if "!str:~0,1!"=="d" (echo %%i 是文件夹) else echo %%i 是文件
)

pause
