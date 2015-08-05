cd..
python "C:\Anaconda3\Lib\site-packages\PyQt4\uic\pyuic.py" -o "lib\connect_window_ui.py" -x "UI\connect_window.ui"
python "C:\Anaconda3\Lib\site-packages\PyQt4\uic\pyuic.py" -o "lib\main_window_ui.py" -x "UI\main_window.ui"
python "C:\Anaconda3\Lib\site-packages\PyQt4\uic\pyuic.py" -o "lib\host_window_ui.py" -x "UI\host_window.ui"
"C:\Anaconda3\Lib\site-packages\PyQt4\pyrcc4.exe" -py3 -o "lib\resources_rc.py" "resources\resources.qrc"
pause