echo off
type Inttiisation.txt
pause
type EULA.txt
set pwd= %CD%
cd \
echo on
echo %pwd%
mysql -u root -p lakochi < %pwd%\commands.sql
pause