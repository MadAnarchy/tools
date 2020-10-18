import os
import time

install = 'pkg install play-audio && pkg install termux-api'
os.system(install)

os.system('clear')

print(' Пожалуйста, сделайте звук на 100% для тихого приветствия программы! ')

usr = input(' Готово? Введите "да" или "нет" - ')

if usr == 'да':
    os.system('play-audio music.mp3')
if usr == 'нет':
    print(' Попробуйте заново. ')

time.sleep(1800)
