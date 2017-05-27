'''

The following shows the batch script that could go into a folder, open all the files underneath (or in subdirectories), then return the lines that contain special words - e.g. "[CR";then get rid off other contents, only save the CR string to the new file.

'''

@echo off
setlocal
pushd <Path where you have placed the .cs files>

rem case-insensitive search for the string "SOME TEXT" in all html files
rem in the current directory, piping the output to the results.txt file
rem in teh same directory

findstr /s /ip /c:"[CR" *.cs > results.txt
for /f "tokens=2 delims=[]" %%a in (results.txt) do echo %%a >> results1.txt

'''

In order to save time, we can use EditPlus++'s TextFX tools to remove useless lines, and also sort them in an order (also use unique option to remove duplicate lines.
Afterwards, use bash script to execute the python script with parameter coming from results1.txt

'''

$while read p; do python ASPX_Crawler.py $p done <results2.txt

'''

Go to the .htm files created, we will need the CR number and status only. Among all CRs we need those that are open.

'''

pushd C:\temp\FindCRs\CRs
findstr /s /ip /c:"lblCrStatus" *.htm > results3.txt
findstr /s /ip /c:"Open" *.txt > results4.txt

'''

Now open results4.txt in EditPlus++, and remove the <div></div> etc. form related strings. We will then have a pure text file that contains CR# and the status open.

'''
