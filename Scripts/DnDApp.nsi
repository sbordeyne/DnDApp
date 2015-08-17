############################################################################################
#      NSIS Installation Script created by NSIS Quick Setup Script Generator v1.09.18
#               Entirely Edited with NullSoft Scriptable Installation System                
#              by Vlasis K. Barkas aka Red Wine red_wine@freemail.gr Sep 2006               
############################################################################################

!define APP_NAME "DnDApp"
!define COMP_NAME "DnDApp Inc."
!define WEB_SITE "http://www.github.com/dogeek/dndapp"
!define VERSION "00.2.31.00"
!define COPYRIGHT "Dogeek  © 2015"
!define DESCRIPTION "Play Dungeons and Dragons online with your friends !"
!define LICENSE_TXT "D:\SPYDERPROJECTS\DnDApp\LICENSE.txt"
!define INSTALLER_NAME "D:\SPYDERPROJECTS\DnDApp\build\setup.exe"
!define MAIN_APP_EXE "launch.exe"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

!define REG_START_MENU "Start Menu Folder"

var SM_Folder

######################################################################

VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

######################################################################

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
XPStyle on
InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$PROGRAMFILES\DnDApp"

######################################################################

!include "MUI.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!insertmacro MUI_PAGE_DIRECTORY

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "DnDApp"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

!define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_APP_EXE}"
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

######################################################################

Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\launch.exe"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\library.zip"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\PyQt4.QtCore.pyd"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\PyQt4.QtGui.pyd"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\python34.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\QtCore4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\QtGui4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\sip.pyd"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\stdout.log"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\unicodedata.pyd"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\_bz2.pyd"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\_hashlib.pyd"
SetOutPath "$INSTDIR\resources\sound"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\sound\diceroll.wav"
SetOutPath "$INSTDIR\resources\fonts"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\alchemst.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\ALPMAGI.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\Anarchy.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\BAJORAN2.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\ba______.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\CH'LANO.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\CIRTH.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\COURTHAN.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\CTHUR___.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\EICAP___.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\electroh.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\En'dankai Normal.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\eraser.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\FloralMajuscules.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\Georges.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\GINETTE.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\GRUNGE.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\jami.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\JUGEND__.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\karine.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\kilrathi.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\MERO_DEM.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\MICHELLE.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\Miss_clo.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\noel____.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\OLDTS___.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\Philing.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\rstimesm.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\SKAVEN.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\theban.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\UGARIT.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\valerie.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\Virginie.ttf"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\vtmeo___.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\WALROD__.TTF"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\fonts\XBand Rough.TTF"
SetOutPath "$INSTDIR\resources\cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\diseases.cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\gems.cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\jewels.cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\magic_items.cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\monsters.cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\npc-gen.cfg"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\resources\cfg\poison.cfg"
SetOutPath "$INSTDIR\imageformats"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qgif4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qico4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qjpeg4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qmng4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qsvg4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qtga4.dll"
File "D:\SPYDERPROJECTS\DnDApp\build\exe.win32-3.4\imageformats\qtiff4.dll"
SectionEnd

######################################################################

Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\DnDApp"
CreateShortCut "$SMPROGRAMS\DnDApp\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\DnDApp\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\DnDApp\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "Publisher" "${COMP_NAME}"

!ifdef WEB_SITE
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "URLInfoAbout" "${WEB_SITE}"
!endif
SectionEnd

######################################################################

Section Uninstall
${INSTALL_TYPE}
Delete "$INSTDIR\launch.exe"
Delete "$INSTDIR\library.zip"
Delete "$INSTDIR\PyQt4.QtCore.pyd"
Delete "$INSTDIR\PyQt4.QtGui.pyd"
Delete "$INSTDIR\python34.dll"
Delete "$INSTDIR\QtCore4.dll"
Delete "$INSTDIR\QtGui4.dll"
Delete "$INSTDIR\sip.pyd"
Delete "$INSTDIR\stdout.log"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\_bz2.pyd"
Delete "$INSTDIR\_hashlib.pyd"
Delete "$INSTDIR\resources\sound\diceroll.wav"
Delete "$INSTDIR\resources\fonts\alchemst.TTF"
Delete "$INSTDIR\resources\fonts\ALPMAGI.TTF"
Delete "$INSTDIR\resources\fonts\Anarchy.ttf"
Delete "$INSTDIR\resources\fonts\BAJORAN2.TTF"
Delete "$INSTDIR\resources\fonts\ba______.ttf"
Delete "$INSTDIR\resources\fonts\CH'LANO.TTF"
Delete "$INSTDIR\resources\fonts\CIRTH.TTF"
Delete "$INSTDIR\resources\fonts\COURTHAN.TTF"
Delete "$INSTDIR\resources\fonts\CTHUR___.TTF"
Delete "$INSTDIR\resources\fonts\EICAP___.TTF"
Delete "$INSTDIR\resources\fonts\electroh.ttf"
Delete "$INSTDIR\resources\fonts\En'dankai Normal.ttf"
Delete "$INSTDIR\resources\fonts\eraser.TTF"
Delete "$INSTDIR\resources\fonts\FloralMajuscules.ttf"
Delete "$INSTDIR\resources\fonts\Georges.ttf"
Delete "$INSTDIR\resources\fonts\GINETTE.TTF"
Delete "$INSTDIR\resources\fonts\GRUNGE.TTF"
Delete "$INSTDIR\resources\fonts\jami.ttf"
Delete "$INSTDIR\resources\fonts\JUGEND__.TTF"
Delete "$INSTDIR\resources\fonts\karine.ttf"
Delete "$INSTDIR\resources\fonts\kilrathi.TTF"
Delete "$INSTDIR\resources\fonts\MERO_DEM.TTF"
Delete "$INSTDIR\resources\fonts\MICHELLE.TTF"
Delete "$INSTDIR\resources\fonts\Miss_clo.ttf"
Delete "$INSTDIR\resources\fonts\noel____.ttf"
Delete "$INSTDIR\resources\fonts\OLDTS___.TTF"
Delete "$INSTDIR\resources\fonts\Philing.ttf"
Delete "$INSTDIR\resources\fonts\rstimesm.ttf"
Delete "$INSTDIR\resources\fonts\SKAVEN.TTF"
Delete "$INSTDIR\resources\fonts\theban.TTF"
Delete "$INSTDIR\resources\fonts\UGARIT.TTF"
Delete "$INSTDIR\resources\fonts\valerie.ttf"
Delete "$INSTDIR\resources\fonts\Virginie.ttf"
Delete "$INSTDIR\resources\fonts\vtmeo___.TTF"
Delete "$INSTDIR\resources\fonts\WALROD__.TTF"
Delete "$INSTDIR\resources\fonts\XBand Rough.TTF"
Delete "$INSTDIR\resources\cfg\diseases.cfg"
Delete "$INSTDIR\resources\cfg\gems.cfg"
Delete "$INSTDIR\resources\cfg\jewels.cfg"
Delete "$INSTDIR\resources\cfg\magic_items.cfg"
Delete "$INSTDIR\resources\cfg\monsters.cfg"
Delete "$INSTDIR\resources\cfg\npc-gen.cfg"
Delete "$INSTDIR\resources\cfg\poison.cfg"
Delete "$INSTDIR\imageformats\qgif4.dll"
Delete "$INSTDIR\imageformats\qico4.dll"
Delete "$INSTDIR\imageformats\qjpeg4.dll"
Delete "$INSTDIR\imageformats\qmng4.dll"
Delete "$INSTDIR\imageformats\qsvg4.dll"
Delete "$INSTDIR\imageformats\qtga4.dll"
Delete "$INSTDIR\imageformats\qtiff4.dll"
 
RmDir "$INSTDIR\imageformats"
RmDir "$INSTDIR\resources\cfg"
RmDir "$INSTDIR\resources\fonts"
RmDir "$INSTDIR\resources\sound"
 
Delete "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
Delete "$INSTDIR\${APP_NAME} website.url"
!endif

RmDir "$INSTDIR"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\DnDApp\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\DnDApp\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\DnDApp\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\DnDApp"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd

######################################################################

