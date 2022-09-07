@echo off
for  %%I in (*.jpg) do python face.py "%%I"

for  %%I in (*.jfif) do python face.py "%%I"

for  %%I in (*.webp) do python face.py "%%I"

for  %%I in (*.png)(
    if %%I in (*_OUTPUT.png) do echo) else (
     python face.py "%%I" )

pause