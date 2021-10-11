import random
from discord.ext import commands

token = "NzcyMDg5MjA3NzQ0MzY0NjM1.X51mGw.b5p0KgrMFl3kEVmxTBE3SCjDoX4"
bot = commands.Bot(command_prefix = '.')


@bot.event
async def on_ready():
    print("Muthu disini, ganti.")

@bot.event
async def on_member_join(member):
    print("Member baru (" + (member) + ") masuk server Tadika Mesra")

@bot.event
async def on_member_remove(member):
    print((member) + "keluar dari server Tadika Mesra")

#.menu -- liat daftar command
@bot.command()
async def menu(ctx):
    print(f'{ctx.message.author.name}, {ctx.message.content}')
    await ctx.send('''Teh ada, Ice tea ada, Teh tarik ada, air kosong ada, semua pun ada.
    
    .koin   = lempar dua sisi koin.
    .dadu   = ambil angka acak.
    .ping   = cek ping.
    .tod    = pertanyaan random
    
Nak makan?''')

#.ping -- cek ping
@bot.command()
async def ping(ctx):
    ping = f'{int((bot.latency) * 1000)} ms'

    print(f'{ctx.message.author.name}, {ctx.message.content} = {ping}')
    await ctx.send(ping)

#.koin -- lempar dua sisi koin.
@bot.command()
async def koin(ctx):
    doku = ["Kepala! :smile:", "Ekor! :monkey:"]
    hasil = random.choice(doku)

    if hasil == doku[0] :
        print(f'{ctx.message.author.name}, {ctx.message.content} = kepala')
    else :
        print(f'{ctx.message.author.name}, {ctx.message.content} = ekor')

    await ctx.send(hasil)

#.dadu -- ambil angka acak
@bot.command()
async def dadu(ctx):
    print(f'{ctx.message.author.name}, {ctx.message.content}')
    await ctx.send('''Berapa sisi yang dadu ini punya?
(Masukan angka genap)''')

    def check(m):
        return int(m.content)%2 == 0 and m.author == ctx.message.author

    msg = await bot.wait_for('message', check=check) #nunggu member buat masukin angka genap
    acak = random.choice(range(2, int(msg.content)))
    hasil = str(acak)

    print(f'{msg.author.name}, {ctx.message.content} ({msg.content}) = {hasil}')
    await ctx.send("Hasil : " + hasil)

#.tod -- pertanyaan pertanyaan dari game TOD
@bot.command()
async def tod(ctx):
    questions = ('Kapan terakhir kali ngompol?',
                'Momen paling memalukan apa yang kamu rasakan sebulan terakhir?',
                'Kalau kamu bisa pilih kekuatan super, mau punya kekuatan apa?',
                'Kalau kamu bisa menghilang, apa hal pertama yang kamu lakukan?',
                'Kalau kamu bisa baca pikiran, pikiran siapa yang bakal kamu baca duluan?',
                'Siapa celebrity crush kamu?',
                'Mimpi paling aneh yang pernah kamu alami?',
                'Skenario paling aneh yang pernah terlintas di pikiranmu tentang kita?',
                'Video TikTok atau YouTube paling memalukan yang pernah kamu tonton?',
                'Film/serial/drama/anime paling memalukan yang pernah kamu tonton?',
                'Cerita Wattpad/fan fiction/buku paling memalukan yang pernah kamu baca?',
                'Kalau kamu cuma bisa makan satu jenis makanan seumur hidup, mau makan apa?',
                'Hal kecil apa yang pernah dilakukan (nama orang) dan bikin kamu senang banget?',
                'Apa kartun favorit kamu pas kecil?',
                'Kalau bisa jadi tokoh fiksi selama sehari, mau jadi apa?',
                'Siapa orang terakhir yang kamu stalking di media sosial?',
                'Kalau ada jin kasih kamu tiga permintaan, mau minta apa aja? (Ide bagus buat yang mau ulang tahun)',
                'Apa love language kamu?',
                'Apa quotes favoritmu?',
                'Artis atau lagu apa yang paling sering kamu putar pas lagi down?',
                'Apa insecurity terbesarmu?',
                'Kapan terakhir kali bohong ke orang tua?',
                'Hal apa yang kamu harapkan bisa kamu ubah dari diri sendiri?',
                'Apa pet peeve terbesarmu?',
                'Kapan terakhir kali bohong? (Dilarang bilang ”Aku gak pernah bohong, nah itu aku baru bohong“)',
                'Kapan terakhir kali menangis?',
                'Apa ketakutan terbesarmu?',
                'Apa penyesalan terbesarmu?',
                'Kalau kamu nggak bisa ketemu kita lagi besok, apa yang mau kamu sampaikan atau lakukan?'
                'Momen life-changing yang pernah kamu alami?')
    await ctx.send(random.choice(questions))

#notice kata-kata jorok dalam pesan
@bot.event
async def on_message(message):
    pesan = message.content.lower()

    katajorok = ['asu', 'tai', 'anjg', 'tolol', 'goblog', 'goblok', 'gblk', 'gblg', 'bgst', 'ajg', 'bgsd', 'kntl',
                 'jmbd', 'jmbt', 'jmbud', 'jmbut', 'jembt', 'jembd', 'kntol', 'kontl', 'bgset', 'bgsat',
                 'bajingn', 'ajgg']

    katajorok_full = ['bajingan', 'kontol', 'tolol', 'jembut', 'jembud', 'bangset', 'bangsat', 'bangsad', 'bangsed', 'bangzed', 'bangzat',
                      'bangzad', 'memek']

    responses = ['kasar anjing',
                 '''”Sesungguhnya tidak ada sesuatu apapun yang paling berat ditimbangan kebaikan seorang mu’min pada hari kiamat seperti akhlaq yang mulia, dan sungguh-sungguh (benar-benar) Allah benci dengan orang yang lisannya kotor dan kasar.”
(Hadits Riwayat At Tirmidzi nomor 2002, hadts ini hasan shahh, lafazh ini milik At Tirmidzi, lihat Silsilatul Ahadits Ash Shahihah No 876).''',

                 f'Niscaya siksa neraka Allah SWT atas ucapan kasarmu lebih pedih dari yang kamu bayangkan, {message.author.name}.',

                 '''“Barang siapa beriman kepada Allah dan hari akhir, maka berkatalah yang baik dan jika tidak maka diamlah.”
(HR. Bukhari no. 6018 dan Muslim no. 47)''',

                 '''Siapa yang tidak bisa mengendalikan lidahnya, berarti tidak bisa memahami agamanya.
– Hasan Al-Bashri''',

                 'Lidah memang tidak bertulang, tapi ia bisa merusak ikatan.'

                 ]

    for i in range(0, len(katajorok)):
        if katajorok[i] in pesan.split() and message.author.id != bot.user.id :
            await message.channel.send(f'> {message.content}\n{random.choice(responses)}')

    for i in range(0, len(katajorok_full)):
        if katajorok_full[i] in pesan and message.author.id != bot.user.id :
            await message.channel.send(f'> {message.content}\n{random.choice(responses)}')

    await bot.process_commands(message)


bot.run(token)