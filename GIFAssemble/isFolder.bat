@echo off

for %%i in (test) do (
    set str=%%~ai
    if "!str:~0,1!"=="d" (echo %%i ���ļ���) else echo %%i ���ļ�
)

pause
