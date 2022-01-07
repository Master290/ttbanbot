#!/usr/bin/env python3
import re
import requests
import json
import threading
from colorama import Fore
import os
try:
# prosto ip
      ipurl = 'https://httpbin.org/ip'
      r = requests.get(ipurl)
      ipinf = json.loads(r.text)
      ip = ipinf['origin']
      os.system('cls') if os.name == 'nt' else os.system('clear')
      print(Fore.CYAN + "                  ███████████ █████ █████   ████"+ Fore.RED + "        ██████   █████ █████  █████ █████   ████ ██████████ ███████████  ")
      print(Fore.CYAN + "                 ░█░░░███░░░█░░███ ░░███   ███░ "+ Fore.RED + "        ░░██████ ░░███ ░░███  ░░███ ░░███   ███░ ░░███░░░░░█░░███░░░░░███ ")
      print(Fore.CYAN + "                     ░███  ░  ░███  ░███  ███   "+ Fore.RED + "         ░███░███ ░███  ░███   ░███  ░███  ███    ░███  █ ░  ░███    ░███ ")
      print(Fore.CYAN + "                     ░███     ░███  ░███████  █████"+ Fore.RED +"█████ ░███░░███░███  ░███   ░███  ░███████     ░██████    ░██████████  ")
      print(Fore.CYAN + "                     ░███     ░███  ░███░░███ ░░░░"+ Fore.RED+"░░░░░░ ░███ ░░██████  ░███   ░███  ░███░░███    ░███░░█    ░███░░░░░███ ")
      print(Fore.CYAN + "                     ░███     ░███  ░███ ░░███  "+ Fore.RED + "         ░███  ░░█████  ░███   ░███  ░███ ░░███   ░███ ░   █ ░███    ░███")
      print(Fore.CYAN + "                     █████    █████ █████ ░░████ "+ Fore.RED +"        █████  ░░█████ ░░████████   █████ ░░████ ██████████ █████   █████")
      print(Fore.CYAN + "                    ░░░░░    ░░░░░ ░░░░░   ░░░░  "+ Fore.RED+"         ░░░░░    ░░░░░   ░░░░░░░░   ░░░░░   ░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ ")
      print(f'Note that if you use this tool without having a vpn / proxy on you could get blacklisted from tiktoks services, Current IP : {ip}\n')
      global repamount
      repamount = 0
      print('Enter amount of threads you want to use.')
      amount_threads = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
      print('Video or account? 1/2')
      vid_or_acc = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
      if vid_or_acc == "1":
        print('Enter link to video. (Please use the dekstop website link or the script will not work!)')
        link_to_vid = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        print(Fore.CYAN + '''\nSelect Report method that you think would be best.
    [1] Misleading information
    [2] Dangerous organizations and individuals
    [3] Illegal activities and regulated goods
    [4] Frauds and scams
    [5] Violent and graphic content
    [6] Animal cruelty
    [7] Suicide, self-harm, and dangerous acts
    [8] Hate speech
    [9] Harassment or bullying
    [10] Pornography and nudity
    [11] Minor safety
    [12] Spam
    [13] Other
    ''')  
        methods = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        if methods == '1':
          print(Fore.CYAN + '''\n[1] Election Misinformation
    [2] Covid19 Misinformation
    [1] Other Misinformation\n''')
          method_video_m = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_m == '1':
            method_for_reporting = '1143'
          elif method_video_m == '2':
            method_for_reporting = '1141'
          elif method_video_m == '3':
            method_for_reporting = '1142'
          else:
            print('Please enter a valid method!')
            input()
            quit()
        elif methods == '2':
          print(Fore.CYAN + '''\n[1] Terrorism
    [2] Criminal Groups
    [3] Hate Groups\n''')
          method_video_d = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_d == '1':
            method_for_reporting = '1011'
          elif method_video_d == '2':
            method_for_reporting = '1012'
          elif method_video_d == '3':
            method_for_reporting = '1013'
          else:
            print('Please enter a valid method!')
            input()
            quit()
        elif methods == '3':
          print(Fore.CYAN + '''\n[1] Promotion of criminal activities
    [2] Sale or use of weapons = 1022
    [3] Drugs and controlled substances\n''')
          method_video_i = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_i == '1':
            method_for_reporting = '1021'
          elif method_video_i == '2':
            method_for_reporting = '1022'
          elif method_video_i == '3':
            method_for_reporting = '1023'
          else:
            print('Please enter a valid method!')
            input()
            quit()
        elif methods == '4':
          method_for_reporting = '1024'
        elif methods == '5':
          method_for_reporting = '103'
        elif methods == '6':
          method_for_reporting = '104'
        elif methods == '7':
          print(Fore.CYAN + '''\n[1] Suicide
    [2] Self-harm
    [3] Dangerous acts\n''')
          method_video_s = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_s == '1':
            method_for_reporting = '1051'
          elif method_video_s == '2':
            method_for_reporting = '1052'
          elif method_video_s == '3':
            method_for_reporting = '1053'
          else:
            print('Please enter a valid method!')
            input()
            quit()
        elif methods == '8':
          method_for_reporting = '106'
        elif methods == '9':
          print(Fore.CYAN + '''\n[1] Me
    [2] Someone I know
    [3] Celebrity
    [4] Others\n''')
          method_video_h = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_h == '1':
            method_for_reporting = '1001'
          elif method_video_h == '2':
            method_for_reporting = '1002'
          elif method_video_h == '3':
            method_for_reporting = '1003'
          elif method_video_h == '4':
            method_for_reporting = '1004'
          else:
            print('Please enter a valid method!')
            input()
            quit()
        elif methods == '10':
          method_for_reporting = '108'
        elif methods == '11':
          print(Fore.CYAN + '''\nUnderage delinquent behavior
    Inappropriate for minors
    Child abuse\n''')
          method_video_mi = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_mi == '1':
            method_for_reporting = '1091'
          elif method_video_mi == '2':
            method_for_reporting == '1092'
          elif method_video_mi == '3':
            method_for_reporting = '1093'
          else:
            print('Please enter a valid method!')
            input()
            quit()
        elif methods == '12':
          method_for_reporting = '110'
        elif methods == '13':
          method_for_reporting = '111'
        user = str(re.findall('https://www.tiktok.com/@(.*?)/video/', link_to_vid)).strip("['']")
        with open('config.json') as f:
          cookie = json.load(f)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
           }
        params = {
                                'is_copy_url': '1',
                                'is_from_webapp': 'v1'
                            }
        url = f"https://tiktok.com/@{user}?"
        response = requests.get(url, headers=headers, params=params)
        Json = json.loads('{' + response.text.split('crossorigin="anonymous">{')[1].split('</script><script')[0])
        worker = Json['props']['pageProps']['userInfo']
        id = worker['user']['id']
        url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id={id}&region=US&priority_region=&os=windows&referer=&root_referer=https:%2F%2F{link_to_vid}%2F&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.106+Safari%2F537.36&browser_online=true&verifyFp=verify_kkw5yl51_T9RSQuuQ_27PS_4Lm6_B7YJ_qePLnpAQMQc5&app_language=en&timezone_name=America%2FNew_York&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=5&battery_info=1'
        headers = {
      "cookie": cookie['cookie'],
      "origin": "https://www.tiktok.com",
      "referer": f'https://tiktok.com/@{user}'
    }
        def report_video():
                  data = {
                          'object_id': id,
                          'owner_id': id,
                          'reason': method_for_reporting,
                          'report_type': "video"
                                  }
                  global repamount
                  try:
                    while True:
                            res = requests.post(url, data=data, headers=headers)
                            if res.text == '{"statusCode":0,"body":{"statusCode":0,"errMsg":"Thanks for your feedback"},"errMsg":"Thanks for your feedback"}':
                              repamount += 1
                              print(Fore.GREEN + f"{repamount} REPORTS SENT TO {user.upper()}'S VIDEO")
                            elif "<TITLE>Access Denied</TITLE>" in res.text:
                              print(Fore.RED + "⚠  RATELIMITED  ⚠")
                            elif res.text == '{"statusCode":1,"errMsg":"Server is currently unavailable. Please try again later."}':
                              print(Fore.YELLOW + "SERVER DOWN")
                            else:
                              print(Fore.YELLOW + "ERROR REPORING")
                  except Exception as e:
                    print(e)
                    input()
        try:    
          threads = []
          for i in range(int(amount_threads)):
                    t = threading.Thread(target=report_video)
                    t.daemon = True
                    t.start()
                    threads.append(t)
          for thread in threads:
                    thread.join()
        except Exception as e:
          print(e)
          input()
      elif vid_or_acc == "2":
        print("Enter victims username.")
        user = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        print(Fore.CYAN + '''Select report option.
    [1] Pretending to Be Someone
    [2] Inappropriate Profile Info
    [3] Other''')
        method = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        if method == '1':
          print(Fore.CYAN + '''    [1] Me
    [2] Celebrity''')
          method_acc_p = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_acc_p == '1':
            method_for_reporting = '3131'
          else:
            method_for_reporting = "3003"
        elif method == '2':
          print(Fore.CYAN + '''[1] Profile Photo
    [2] Nickname
    [3] Username
    [4] Bio
    [5] Link''')
          method_acc_i = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_acc_i == '1':
            method_for_reporting = '3141'
          elif method_acc_i == '2':
            method_for_reporting = '3142'
          elif method_acc_i == '3':
            method_for_reporting = '3143'
          elif method_acc_i == '4':
            method_for_reporting = '3144'
          elif method_acc_i == '5':
            method_for_reporting = '3145'
        elif method == '3':
          method_for_reporting = '311'
        else:
          print('Please Select a Method!')
          input()
          quit()
        with open('config.json') as f:
                  cookie = json.load(f)
        headers = {
        'Cookie': cookie['cookie'],
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
           }
        params = {
                                'is_copy_url': '1',
                                'is_from_webapp': 'v1'
                            }
        url = f"https://tiktok.com/@{user}?"
        response = requests.get(url, headers=headers, params=params)
        Json = json.loads('{' + response.text.split('crossorigin="anonymous">{')[1].split('</script><script')[0])
        worker = Json['props']['pageProps']['userInfo']
        id = worker['user']['id']
        url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id={id}&region=US&priority_region=&os=windows&referer=&root_referer=https:%2F%2Fwww.tiktok.com%2F&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.106+Safari%2F537.36&browser_online=true&verifyFp=verify_kkw5yl51_T9RSQuuQ_27PS_4Lm6_B7YJ_qePLnpAQMQc5&app_language=en&timezone_name=America%2FNew_York&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=5&battery_info=1'
        def report_account():
            data = {
                  'object_id': id,
                  'owner_id': id,
                  'reason': method_for_reporting,
                  'report_type': "user"
                          }
            global repamount
            try:
                    while repamount < 200:
                            res = requests.post(url, data=data)
                            if res.text == '{"statusCode":0,"body":{"statusCode":0,"errMsg":"Thanks for your feedback"},"errMsg":"Thanks for your feedback"}':
                              repamount += 1
                              print(Fore.GREEN + f"{repamount} REPORTS SENT TO {user.upper()}")
                            elif "<TITLE>Access Denied</TITLE>" in res.text:
                              print(Fore.RED + "⚠  RATELIMITED  ⚠")
                            elif res.text == '{"statusCode":1,"errMsg":"Server is currently unavailable. Please try again later."}':
                              print(Fore.YELLOW + "SERVER DOWN")
                            else:
                              print(Fore.YELLOW + 'ERROR REPORTING')
            except Exception as e:
                    print(e)
        try:    
          threads = []
          for i in range(int(amount_threads)):
                    t = threading.Thread(target=report_account)
                    t.daemon = True
                    t.start()
                    threads.append(t)
          for thread in threads:
                    thread.join()
        except Exception as e:
          print(e)
except Exception as e:
	print(e)
