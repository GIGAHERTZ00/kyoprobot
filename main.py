import discord
from dotenv import load_dotenv
load_dotenv()


# --------input token------------
import os
TOKEN = os.getenv("KPBTOKEN")
# -------------------------------

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def nextContests():
  rtn1 = ""
  rtn2 = ""
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  import datetime
  html = urlopen("https://atcoder.jp/contests/").read().decode()
  data = BeautifulSoup(html, "html.parser").find("body").text.split('\n')
  contestData = {"ABC": [None, "AtCoder Beginner Contest"], \
                "ARC": [None, "AtCoder Regular Contest"], \
                "AHC": [None, "AtCoder Heuristic Contest"]}
  data = data[data.index("Upcoming Contests"):data.index("Recent Contests")]
  for i, j in enumerate(data):
    flg = False
    for c in contestData.values():
      if c[0] != None:
        continue
      flg = True
      if c[1] in j:
        contest = []
        j = j[j.index(c[1])+len(c[1]):].replace(")", "").replace("）", "").split()
        for k in j:
          if k.isdecimal():
            break
        contest.append(k)
        for k in range(8):
          if ':' in data[i+k]:
            contest.append(data[i+k])
            break
        for k in range(-4,0):
          if ':' in data[i+k]:
            break
        date = datetime.datetime.strptime(data[i+k][:19], \
                                          '%Y-%m-%d %H:%M:%S')
        contest.insert(1, date)
        c[0] = contest
    if not flg:
      break
  for text, contest in contestData.items():
    if contest[0] is None:
      rtn1 = ("次のコンテストの情報は得られませんでした")
      rtn2 = ""
      rtn3 = ""
      continue
    stoe = contest[0][1].timestamp() + datetime.datetime.strptime(contest[0][2], "%H:%M").timestamp()+2209021200
    rtn1 = ("次のコンテストは" + text + contest[0][0] + "です")
    rtn2 = (contest[0][1].strftime('%Y-%m-%d %H:%M:%S') + "から" + str(datetime.datetime.fromtimestamp(stoe)) + "までの" + contest[0][2] +  "の間開催されます")
    rtn3 = ("https://atcoder.jp/contests/" + text + contest[0][0])
    return(rtn1 + '\n' + rtn2 + '\n' + rtn3)

def nextABC():
  rtn1 = ""
  rtn2 = ""
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  import datetime
  html = urlopen("https://atcoder.jp/contests/").read().decode()
  data = BeautifulSoup(html, "html.parser").find("body").text.split('\n')
  contestData = {"ABC": [None, "AtCoder Beginner Contest"]}
  data = data[data.index("Upcoming Contests"):data.index("Recent Contests")]
  for i, j in enumerate(data):
    flg = False
    for c in contestData.values():
      if c[0] != None:
        continue
      flg = True
      if c[1] in j:
        contest = []
        j = j[j.index(c[1])+len(c[1]):].replace(")", "").replace("）", "").split()
        for k in j:
          if k.isdecimal():
            break
        contest.append(k)
        for k in range(8):
          if ':' in data[i+k]:
            contest.append(data[i+k])
            break
        for k in range(-4,0):
          if ':' in data[i+k]:
            break
        date = datetime.datetime.strptime(data[i+k][:19], \
                                          '%Y-%m-%d %H:%M:%S')
        contest.insert(1, date)
        c[0] = contest
    if not flg:
      break
  for text, contest in contestData.items():
    if contest[0] is None:
      rtn1 = ("次の" + text + "の情報は得られませんでした")
      rtn2 = ""
      continue
    stoe = contest[0][1].timestamp() + datetime.datetime.strptime(contest[0][2], "%H:%M").timestamp()+2209021200
    rtn1 = ("次の" + text + "は" + text + contest[0][0] + "です")
    rtn2 = (contest[0][1].strftime('%Y-%m-%d %H:%M:%S') + "から" + str(datetime.datetime.fromtimestamp(stoe)) + "までの" + contest[0][2] +  "の間開催されます")
    rtn3 = ("https://atcoder.jp/contests/" + text + contest[0][0])
    return(rtn1 + '\n' + rtn2 + '\n' + rtn3)

def nextARC():
  rtn1 = ""
  rtn2 = ""
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  import datetime
  html = urlopen("https://atcoder.jp/contests/").read().decode()
  data = BeautifulSoup(html, "html.parser").find("body").text.split('\n')
  contestData = {"ARC": [None, "AtCoder Regular Contest"]}
  data = data[data.index("Upcoming Contests"):data.index("Recent Contests")]
  for i, j in enumerate(data):
    flg = False
    for c in contestData.values():
      if c[0] != None:
        continue
      flg = True
      if c[1] in j:
        contest = []
        j = j[j.index(c[1])+len(c[1]):].replace(")", "").replace("）", "").split()
        for k in j:
          if k.isdecimal():
            break
        contest.append(k)
        for k in range(8):
          if ':' in data[i+k]:
            contest.append(data[i+k])
            break
        for k in range(-4,0):
          if ':' in data[i+k]:
            break
        date = datetime.datetime.strptime(data[i+k][:19], \
                                          '%Y-%m-%d %H:%M:%S')
        contest.insert(1, date)
        c[0] = contest
    if not flg:
      break
  for text, contest in contestData.items():
    if contest[0] is None:
      rtn1 = ("次の" + text + "の情報は得られませんでした")
      rtn2 = ""
      continue
    stoe = contest[0][1].timestamp() + datetime.datetime.strptime(contest[0][2], "%H:%M").timestamp()+2209021200
    rtn1 = ("次の" + text + "は" + text + contest[0][0] + "です")
    rtn2 = (contest[0][1].strftime('%Y-%m-%d %H:%M:%S') + "から" + str(datetime.datetime.fromtimestamp(stoe)) + "までの" + contest[0][2] +  "の間開催されます")
    rtn3 = ("https://atcoder.jp/contests/" + text + contest[0][0])
    return(rtn1 + '\n' + rtn2 + '\n' + rtn3)

def nextAHC():
  rtn1 = ""
  rtn2 = ""
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  import datetime
  html = urlopen("https://atcoder.jp/contests/").read().decode()
  data = BeautifulSoup(html, "html.parser").find("body").text.split('\n')
  contestData = {"AHC": [None, "AtCoder Heuristic Contest"]}
  data = data[data.index("Upcoming Contests"):data.index("Recent Contests")]
  for i, j in enumerate(data):
    flg = False
    for c in contestData.values():
      if c[0] != None:
        continue
      flg = True
      if c[1] in j:
        contest = []
        j = j[j.index(c[1])+len(c[1]):].replace(")", "").replace("）", "").split()
        for k in j:
          if k.isdecimal():
            break
        contest.append(k)
        for k in range(8):
          if ':' in data[i+k]:
            contest.append(data[i+k])
            break
        for k in range(-4,0):
          if ':' in data[i+k]:
            break
        date = datetime.datetime.strptime(data[i+k][:19], \
                                          '%Y-%m-%d %H:%M:%S')
        contest.insert(1, date)
        c[0] = contest
    if not flg:
      break
  for text, contest in contestData.items():
    if contest[0] is None:
      rtn1 = ("次の" + text + "の情報は得られませんでした")
      rtn2 = ""
      continue
    stoe = contest[0][1].timestamp() + datetime.datetime.strptime(contest[0][2], "%H:%M").timestamp()+2209021200
    rtn1 = ("次の" + text + "は" + text + contest[0][0] + "です")
    rtn2 = (contest[0][1].strftime('%Y-%m-%d %H:%M:%S') + "から" + str(datetime.datetime.fromtimestamp(stoe)) + "までの" + contest[0][2] +  "の間開催されます")
    rtn3 = ("https://atcoder.jp/contests/" + text + contest[0][0])
    return(rtn1 + '\n' + rtn2 + '\n' + rtn3)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$nextcontest"):
    await message.channel.send(nextContests())

  elif message.content.startswith("$nextABC"):
    await message.channel.send(nextABC())

  elif message.content.startswith("$nextARC"):
    await message.channel.send(nextARC())

  elif message.content.startswith("$nextAHC"):
    await message.channel.send(nextAHC())

# @client.slash_command(description="AtCoderSchedule", guild_ids=[GUILDID])
# async def sch(
#   ctx: discord.ApplicationContext,
# ):
#   ans = nextContests()
#   await ctx.respond(ans)

# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return
#
#   if message.content.startswith('$hello'):
#     await message.channel.send('Hello!')

client.run(TOKEN)
