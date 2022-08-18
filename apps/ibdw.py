import os
def curl(url,name):
  os.system(f'curl {url} --output ./tools/{name}')
def download_tools():
  curl("https://aka.ms/vs/17/release/vc_redist.x64.exe","vc64.exe")
  curl("https://aka.ms/vs/17/release/vc_redist.x86.exe","vc86.exe")
  curl("https://download.microsoft.com/download/E/E/D/EEDF18A8-4AED-4CE0-BEBE-70A83094FC5A/BuildTools_Full.exe","bt.exe")
  curl("https://download.visualstudio.microsoft.com/download/pr/2d6bb6b2-226a-4baa-bdec-798822606ff1/9b7b8746971ed51a1770ae4293618187/ndp48-web.exe","nf.exe")
def exec(cmd):
  os.system(os.getcwd()+"/./tools/"+cmd)
def q(cm):
  return cm+" /q /silent /quiet"
def ea():
  exec(q("vc64.exe"))
  exec(q("vc86.exe"))
  exec(q("bt.exe"))
  exec(q("nf.exe"))
def ibdw_Exec():
  download_tools()
  ea()