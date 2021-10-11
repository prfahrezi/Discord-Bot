import discord
import random
from discord.ext import commands

token = "NzcyMDg5MjA3NzQ0MzY0NjM1.X51mGw.b5p0KgrMFl3kEVmxTBE3SCjDoX4"
bot = commands.Bot(command_prefix = '.')


@bot.event
async def on_ready():
    print("Bot is here.")

@bot.event
async def on_member_join(member):
    print("Member baru (" + (member) + ") masuk server Tadika Mesra")

@bot.event
async def on_member_remove(member):
    print((member) + "keluar dari server Tadika Mesra")

@bot.command()
async def menu(ctx):
    await ctx.send('''Teh ada, Ice tea ada, Teh tarik ada, air kosong ada, semua pun ada.
    
    .koin   = lempar dua sisi koin.
    .dadu   = ambil angka acak.
    .ping   = cek ping.
    
Nak makan apa?''')

#tes ping
@bot.command()
async def ping(ctx):
	print(f'{ctx.message.author}, ctx.message.content')
    await ctx.send(f'{int((bot.latency)*1000)} ms')

#.koin -- lempar dua sisi koin.
@bot.command()
async def koin(ctx):
    doku = ["Kepala! :smile:", "Ekor! :monkey:"]
    await ctx.send(random.choice(doku))

#.dadu -- ambil angka acak
@bot.command()
async def dadu(ctx):
    await ctx.send('''Berapa sisi yang dadu ini punya?
(Masukan angka genap)''')

    def check(m):
        return int(m.content)%2 == 0 and m.author == ctx.message.author

    msg = await bot.wait_for('message', check=check)

    acak = random.choice(range(2, int(msg.content)))
    await ctx.send("Hasil : " + str(acak))

@bot.event
async def on_message(message):

    katajorok = ['asu', 'tai', 'anjg', 'tolol', 'goblok', 'gblk', 'gblg', 'bgst', 'ajg', 'bgsd', 'kontol', 'kntl', 'bangsat', 'bangset', 'jmbd', 'jmbt', 'jembut', 'jembud']

    for i in range(0, len(katajorok)):
        responses = [f'kasar {message.author.name.lower()} anjing',
                     '''”Sesungguhnya tidak ada sesuatu apapun yang paling berat ditimbangan kebaikan seorang mu’min pada hari kiamat seperti akhlaq yang mulia, dan sungguh-sungguh (benar-benar) Allah benci dengan orang yang lisannya kotor dan kasar.”
(Hadits Riwayat At Tirmidzi nomor 2002, hadts ini hasan shahh, lafazh ini milik At Tirmidzi, lihat Silsilatul Ahadits Ash Shahihah No 876).''',

                     f'{message.author.name}, niscaya siksa neraka Allah SWT atas ucapan kasarmu lebih pedih dari yang kamu bayangkan.',

                     '''“Barang siapa beriman kepada Allah dan hari akhir, maka berkatalah yang baik dan jika tidak maka diamlah.”
(HR. Bukhari no. 6018 dan Muslim no. 47)''',

                     '''Siapa yang tidak bisa mengendalikan lidahnya, berarti tidak bisa memahami agamanya.
– Hasan Al-Bashri''',

                     'Lidah memang tidak bertulang, tapi ia bisa merusak ikatan.'

]
        if katajorok[i] in message.content.lower() and message.author.id != bot.user.id :
            await message.channel.send(f'> {message.content}\n{random.choice(responses)}')
    await bot.process_commands(message)


bot.run(token)