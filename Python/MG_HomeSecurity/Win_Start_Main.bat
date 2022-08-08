@echo off
start cmd.exe /k "F:\PERSO\Elec-Robot\Projets Vision Maison\RPI4\PROG\MG_HomeSecurity\Win_Start_MG_HomeSecurity.bat"
timeout 0
start cmd.exe /k "F:\PERSO\Elec-Robot\Projets Vision Maison\RPI4\PROG\MG_HomeSecurity\Win_Start_MG_HomeSecurity_HMI.bat"
timeout 5
start cmd.exe /k "F:\PERSO\Elec-Robot\Projets Vision Maison\RPI4\PROG\MG_HomeSecurity\Win_Start_MG_HomeSecurity_Cam1.bat"
timeout 0
pause