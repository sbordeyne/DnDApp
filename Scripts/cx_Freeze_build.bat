cd..
python setup.py build

pause

del "build\exe.win32-3.4\resources\cfg\*.*" /Q
del "build\exe.win32-3.4\resources\sound\*.*" /Q
del "build\exe.win32-3.4\resources\fonts\*.*" /Q

robocopy "resources\cfg" "build\exe.win32-3.4\resources\cfg" /E
robocopy "resources\sound" "build\exe.win32-3.4\resources\sound" /E
robocopy "resources\fonts" "build\exe.win32-3.4\resources\fonts" /E

pause