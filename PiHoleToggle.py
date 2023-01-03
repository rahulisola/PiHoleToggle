import requests, os, winshell, sys
from win32com.client import Dispatch

BaseURL='http://{Pi_Hole_IP}/admin/api.php'
wDir = sys.path[0]
target = sys.path[0] + r"\PiHoleToggle.bat"
icon = r"C:\Windows\System32\SHELL32.dll"
token = "PI_HOLE_API_TOKEN"

print('Current dir: ' + os.getcwd())

r = requests.get(BaseURL + '?status&auth=' + token)
if r.json()['status'] == 'enabled':
	action = requests.get(BaseURL + '?disable&auth=' + token)
	# os.rename(r'PiHole\Disable PiHole.lnk', r'PiHole\Enable PiHole.lnk')
	try:
		os.remove(r'PiHole\Disable PiHole.lnk')
	except:
		print('Unable to delete old shortcut')
	path = "PiHole\Enable PiHole.lnk"
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.IconLocation = icon + ",296"
	shortcut.WorkingDirectory = wDir
	shortcut.save()
else:
	action = requests.get(BaseURL + '?enable&auth=' + token)
	# os.rename(r'PiHole\Enable PiHole.lnk', r'PiHole\Disable PiHole.lnk')
	try:
		os.remove(r'PiHole\Enable PiHole.lnk')
	except:
		print('Unable to delete old shortcut')
	path = "PiHole\Disable PiHole.lnk"
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.IconLocation = icon + ",109"
	shortcut.WorkingDirectory = wDir
	shortcut.save()
print('Previous Status: ' + r.json()['status'] + ', New Status: ' + action.json()['status'])
