#!python34
import requests, sys, sched, time, threading

s=requests.session()
username= sys.argv[1]
password= sys.argv[2]
login_credentials = {'username':username,'password':password}
s.get('http://127.0.0.1:8000/login',params=login_credentials)


def send_message(t):
    if t:
        params={'text':t}
        r = s.get('http://127.0.0.1:8000/send_message',params=params)
        if r.text=='OK':
            pass
        else:
            print('message not sent.')

def receive_message():
    r = s.get('http://127.0.0.1:8000/receive_message')
    if r:
        for a in r:
            print('Other: ',a.decode())
 
sch = sched.scheduler(time.time,time.sleep)
def munna(sc):
    receive_message()
    sch.enter(5,1,munna,(sc,))
def keep_receiving():
    sch.enter(5,1,munna,(s,))
    sch.run()
thread = threading.Thread(target=keep_receiving)
thread.daemon = True
thread.start()

def keep_typing():
    while True:
        message = str(input('Me: '))
        if message:
            if message!='logout':
                send_message(message)
            else:
                r=s.get('http://127.0.0.1:8000/logout')
                sys.exit()
        else:
            print('empty string')
keep_typing()

            
            
