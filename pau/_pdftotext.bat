@echo off
set PATH=\Bin\ghostscript\bin;%PATH%
set PATH=\Bin\xpdf;%PATH%


for %%f in (*.pdf) do pdftotext.exe -layout  %%f  text\%%~nf.txt

pause