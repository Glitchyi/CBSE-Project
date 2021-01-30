echo off
type Inttiisation.txt
pause
type EULA.txt
set pwd= %CD%
cd %ProgramFiles(x86)%
echo on
mysql -u root -p lakochi < LaKochi\Restraunt\commands.sql
pause