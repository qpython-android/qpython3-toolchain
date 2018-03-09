#qpy:qpyapp
"""
Share script
"""
import glob
import os
import sys
import androidhelper
droid = androidhelper.Android()

_scripts = glob.glob("/sdcard/qpython/scripts3/*.py")
scripts = []
for x in _scripts:
    scripts.append(os.path.basename(x))

droid.dialogCreateAlert("Run QPython3 script...")
droid.dialogSetItems(scripts)
droid.dialogShow()

response = droid.dialogGetResponse().result

if 'item' in response:
    script = _scripts[response['item']]
    argv1 = len(sys.argv)>1 and sys.argv[1] or ''
    os.execle(sys.executable, os.path.basename(sys.executable), script, argv1, os.environ)
else:
    droid.makeToast("You cancel the share")
