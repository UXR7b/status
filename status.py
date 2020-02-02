import time,vk,os
tokenlink = input("TOKEN:")
token1 = tokenlink.rsplit("access_token=")
token2 = token1[1].rsplit("&expires_in")
token = token2[0]
session = vk.Session(access_token=token)
api = vk.API(session,v='5.92',lang='ru')
mess = input("Status:")

timeee = int(input("Начальные минуты:"))
tenss = 0
timee1= 0
timee=0
additional = str(input("Слова после минут:"))
timelen=int(len(str(timeee)))
timee=timeee%10
counter = 0
while True:
  if timee == 2 or timee == 3 or timee == 4:minutew=" минуты"
  elif timee == 1:minutew = " минуту"
  else :minutew = " минут"
  api.status.set(text=mess+" "+str(timeee)+minutew+" "+str(additional))
  if timee == 10:
    timee = 0
    tenss += 10
  timee += 1
  timeee+=1
  counter+=1
  os.system("clear")
  status1=str(api.status.get())
  status2=status1.rsplit("'")
  status=status2[3]
  print("Статус:"+status)
  print(str(counter)+" раз сменился статус")
  time.sleep(60)