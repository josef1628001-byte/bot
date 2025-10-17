# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import os
import sys
import discord
import random # built-in time, os, sys # if -> import random as rd -> command(random) becomes rd
from discord.ext import commands
from bot_logic import gen_pass # bot_logic -> function name
import os
import requests
import math
import numpy as np
# import flask -> 3rd party library

sys.set_int_max_str_digits(1000000000) # The limit of how many numbers can be generated

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int): # -> $add 2 8 -> 10
    """Adds two numbers together."""
    await ctx.send(left + right)
# subtracting two numbers
@bot.command()
async def min(ctx, left: int, right: int): # -> $min 8 2 -> 6
    """Adds two numbers together."""
    await ctx.send(left - right)
# multiplication two numbers
@bot.command()
async def times(ctx, left: int, right: int): # -> $times 2 8 -> 16
    """Adds two numbers together."""
    await ctx.send(left*right)
# division two numbers
@bot.command()
async def divide(ctx, left: int, right: int): # $divide 8 2 -> 4
    """Adds two numbers together."""
    await ctx.send(left/right)
# exp two numbers
@bot.command()
async def exp(ctx, left: int, right: int): # $exp 2 3 -> 8
    """Adds two numbers together."""
    await ctx.send(left**right)
# modulo two numbers
@bot.command()
async def mod(ctx, left: int, right: int): # $mod 8 3 -> 2
    """Adds two numbers together."""
    await ctx.send(left % right)
# floor function
@bot.command()
async def floor(ctx, number: float): # $floor 3,14159265 -> 3
    """Returns the floor of the number."""
    await ctx.send(math.floor(number))
# Ceiling function
@bot.command()
async def ceil(ctx, number: float): # $ceil 3,14159265 -> 4
    """Returns the ceil of the number"""
    await ctx.send(math.ceil(number))
# Determinant
@bot.command()
async def det(ctx, *, matrix_str: str): # -> $det [[1,2],[3,4]] -> -2.0
    """Returns the determinant of a square matrix."""
    try:
        # Convert string input to a Python list safely
        matrix = eval(matrix_str, {"__builtins__": {}}) # Evaluate data
        arr = np.array(matrix, dtype=float)

        # To check if matrix is square shaped or not
        if arr.shape[0] != arr.shape[1]: # Check the array -> []
            await ctx.send("Matrix must be square (same number of rows and columns).")
            return

        # Calculate the determinant
        determinant = np.linalg.det(arr)
        await ctx.send(determinant)

    except Exception as e:
        await ctx.send(f"Error: {e}")
# Help commands
@bot.command()
async def commands(ctx):
    """Shows all available commands and their functions."""
    help_text = """
**Bot Command List**

__Math Operations__
`$add <a> <b>` — Adds two numbers.  
`$min <a> <b>` — Subtracts two numbers.  
`$times <a> <b>` — Multiplies two numbers.  
`$divide <a> <b>` — Divides two numbers.  
`$exp <a> <b>` — Raises a number to a power (a^b).  
`$mod <a> <b>` — Returns the remainder of a division.  
`$floor <number>` — Rounds down to the nearest integer.  
`$ceil <number>` — Rounds up to the nearest integer.  
`$det [[a,b],[c,d]]` — Calculates the determinant of a square matrix.

__Local Files__
`$local_drive` — Lists all files in the *files/* folder.  
`$showfile <filename>` — Sends a file from the *files/* folder.  
`$simpan` — Saves uploaded files into the *files/* folder.  

__Text Commands__
`$tulis <text>` — Writes new text to *kalimat.txt*.  
`$tambahkan <text>` — Add text to *kalimat.txt*.  
`$baca` — Reads the content of *kalimat.txt*.  

__Fun & Entertainment__
`$meme` — Sends a random image from the *images/* folder.  
`$dog` — Sends a random dog picture.  
`$duck` — Sends a random duck picture.  
`$coinflip` — Flips a coin (Heads/Tails).  
`$dice` — Rolls a dice (1 until 6).  
`$pw` — Generates a random password.  
`$repeat <times>` — Repeats any word multiple times.  
`$bye` — Sends a smile emoji.

__Member Info__
`$joined @user` — Shows when a user joined the server.

__Clear Messages__
`$clear <amount>` — Clear messages of the amount wanted ( Default clear is 5 ).

__Mandatory Info__
Use **$** before every command (example : `$add 3 7`).  
"""
    await ctx.send(help_text)
# Clear messages
@bot.command()
async def clear(ctx, amount: int = 5):
    """
    Deletes the last <amount> messages in the channel.
    Usage: $clear 10
    Default: 5 messages if no number given.
    """
    if amount < 1:
        await ctx.send("Please enter a number greater than 0.")
        return

    deleted = await ctx.channel.purge(limit=amount + 1)  # +1 to delete the command message itself
    await ctx.send(f"Message Has Been Deleted. {len(deleted) - 1} message(s).", delete_after=3)
    

# # give local meme see python folder Data Science drive 
@bot.command()
async def meme(ctx):
    # try by your self 2 min
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

# duck and dog API
def get_dog_image_url():
    url = 'https://random.dog/woof.json' #embeded link
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)

@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)

@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)
        
# spamming word
@bot.command()
async def repeat(ctx, times: int, *, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')
@bot.command()
async def bye(ctx):
    await ctx.send('\U0001f642')
# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore

#show local drive    
@bot.command()
async def local_drive(ctx):
    try:
      folder_path = "./files"  # Replace with the actual folder path # ./ -> Masuk # .. -> Keluar
      files = os.listdir(folder_path)
      file_list = "\n".join(files)
      await ctx.send(f"Files in the files folder:\n{file_list}")
    except FileNotFoundError:
      await ctx.send("Folder not found.") 
#show local file
@bot.command()
async def showfile(ctx, *, filename):
  """Sends a file as an attachment."""
  folder_path = "./files/"
  file_path = os.path.join(folder_path, filename)

  try:
    await ctx.send(file=discord.File(file_path))
  except FileNotFoundError:
    await ctx.send(f"File '{filename}' not found.")
# upload file to local computer
@bot.command()
async def simpan(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            # file_url = attachment.url  IF URL
            await attachment.save(f"./files/{file_name}")
            await ctx.send(f"Menyimpan {file_name}")
    else:
        await ctx.send("Anda lupa mengunggah :(")

bot.run('DISCORD_TOKEN')


