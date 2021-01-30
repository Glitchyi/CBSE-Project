Unicode True
# define the name of the installer
Outfile "MDDTS.exe"
 
# define the directory to install to, the desktop in this case as specified  
# by the predefined $DESKTOP variable
InstallDir C:\
 
 Icon file.ico
# default section
Section
 
# define the output path for this file
SetOutPath $INSTDIR
 

InitPluginsDir
; Call plug-in. Push filename to ZIP first, and the dest. folder last.
nsisunz::Unzip "Mysql.zip" $INSTDIR
Pop $0
StrCmp $0 "success" ok
  DetailPrint "$0" ;print error message to log
ok:

ExecShell "open" "C:\Mysql"
SectionEnd