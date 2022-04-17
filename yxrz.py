from subprocess import run, PIPE
import requests
import time
def login(oucid, pwd):
    url = 'https://yxrz.ouc.edu.cn'  
    data = {
        "DDDDD": oucid,   
        "upass": pwd,      
        "R1": "0",
        "R3": "0",
        "R6": "0",
        "para": "00",
        "0MKKey": "123456",
    }

    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN ,zh;q=0.9",
        "Connectin": "keep-alive",
        "Host": "https://yxrz.ouc.edu.cn",
        "Referer": "https://yxrz.ouc.edu.cn/a79.htm",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    }
    response = requests.post(url, data, headers=header).status_code
    print("回应代码{}".format(response))

oucid = input('please input your OUC id: ')
pwd = input('please input your password: ')
for i in range(3):
    print('WARNING! make sure the above information is correct, which will NOT be automatically checked by this program')
    time.sleep(1)
while True:
    r = run('curl www.baidu.com',
        stdout=PIPE,
        stderr=PIPE,
        stdin=PIPE,
        shell=True)
    if len(str(r.stdout, 'UTF-8'))==0:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'  正在重新连接')
        login(oucid, pwd)
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'  连接成功')
    time.sleep(1) #单位 s
