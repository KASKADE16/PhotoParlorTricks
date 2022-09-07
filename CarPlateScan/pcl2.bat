@echo off
for  %%I in (*.jpg) do python CarPlate.py "%%I"

for  %%I in (*.jfif) do python CarPlate.py "%%I"

for  %%I in (*.webp) do python CarPlate.py "%%I"

for  %%I in (*.png)(
    if %%I in (*_OUTPUT.png) do echo) else (
     python CarPlate.py "%%I" )

pause