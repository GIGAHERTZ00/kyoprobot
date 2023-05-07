import discord

# --------input token------------
print("Please input a token:",end=' ')
TOKEN = input()
# -------------------------------

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# client=commands.Bot(command_prefix=".")

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
      rtn1 = ("次の" + text + "の情報は得られませんでした")
      rtn2 = ""
      continue
    rtn1 = ("次の" + text + "は" + text + contest[0][0] + "です")
    rtn2 = (contest[0][1].strftime('%Y-%m-%d %H:%M:%S') + "から" + contest[0][2] + "の期間開催されます")
    return(rtn1 + '\n' + rtn2)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$nextcontest"):
    await message.channel.send(nextContests())

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
