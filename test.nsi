# define the name of the installer
Outfile "MDDTS.exe"
 
# define the directory to install to, the desktop in this case as specified  
# by the predefined $DESKTOP variable
InstallDir C:\
 
 Icon logo.ico
# default section
Section
 
# define the output path for this file
SetOutPath $INSTDIR
 

ZipDLL::extractall "D:\Advaith\Python\Project\Mysql.zip" C:\Program Files (x86)\Zip


ExecShell "open" "C:\Mysql"
SectionEnd