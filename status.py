import time,vk
tokenlink = input("TOKEN:")
token1 = tokenlink.rsplit("access_token=")
token2 = token1[1].rsplit("&expires_in")
token = token2[0]
session = vk.Session(access_token=token)
api = vk.API(session,v='5.92',lang='ru')
mess = input("Status:")
timee = 1
tenss = 0
while True:
  if timee == 2 or timee == 3 or timee == 4:minutew=" минуты."
  elif timee == 1:minutew = " минуту."
  else :minutew = " минут."
  api.status.set(text=mess+str(timee+tenss)+minutew)
  if timee == 10 :
    timee = 0
    tenss += 10
  timee += 0.5
  time.sleep(30)