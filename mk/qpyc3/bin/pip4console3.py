#qpy:console
import os,os.path,sys
#sys.dont_write_bytecode = True

def modcmd(arg):
  os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)

if not(os.path.exists(sys.prefix+"/bin/pip3")):
  print("You need to install pip3 first.")
print("Input pip commands, ie: pip3 install {module}")
while(True):
  cmd=input("-->")
  if (cmd==""): break;
  modcmd(cmd)
