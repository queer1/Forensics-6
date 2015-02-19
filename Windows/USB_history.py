import _winreg

def findUSB(query):
  c=0
  try:
    while True:
      print _winreg.EnumKey(query ,c)
      c += 1
  except WindowsError:
  pass

def main():
  qu= _winreg.OpenKey( _winreg.HKEY_LOCAL_MACHINE ,r'SYSTEM\CurrentControlSet\Enum\USBSTOR' ,0 )
  findUSB(qu)
  
if __name__=='__main__':
  main()
