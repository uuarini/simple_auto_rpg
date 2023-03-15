import os, pyinputplus as pyip, random, sys, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()

races = ['dwarf', 'elf', 'human', 'orc']
classes = ['damage', 'healer', 'blocker']
monster_races = ['vampire', 'zombie', 'mummy', 'werewolf']

def randNum() :
    return random.randrange(1,10)

class character:
    def __init__(self, blood, brain, brawn):
        self.blood = blood
        self.brain = brain
        self.brawn = brawn
    def stats(self):
        return f'blood: {self.blood}, brain: {self.brain}, brawn: {self.brawn}'
class monster:
    def __init__(self, blood, brain, brawn):
        self.blood = blood
        self.brain = brain
        self.brawn = brawn
    def monsterStats(self):
        return f'blood: {self.blood}, brain: {self.brain}, brawn: {self.brawn}'

monster1 = monster(randNum(), randNum(), randNum())
monster_name = monster_races[random.randrange(len(monster_races))]

race = races[random.randrange(len(races))]
class1 = classes[random.randrange(len(classes))]

if class1 == 'damage':
    char1 = character(5,5,9)
elif class1 == 'healer':
    char1 = character(5,9,5)
else:
    char1 = character(9,5,5)

if race == 'dwarf':
    char1.blood += 1
elif race == 'elf':
    char1.brain += 1
elif race == 'orc':
    char1.brawn += 1

if monster_name == 'vampire':
    monster1.blood -= 1
    monster1.brain += 1
elif monster_name == 'zombie':
    monster1.brain -= 1
elif monster_name == 'mummy':
    monster1.brawn -= 1
elif monster_name == 'werewolf':
    monster1.brawn += 1

output = f'''Well met, fair traveler.

Welcome to Cardinal Roguelin's Trope-riddled Medieval Cliche Masquerade of Merriment.

I am Terrick Dragonheart, Knight of Saldept Grove and Ranger of the Order of Juniper.'''

for c in output:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.075)

pygame.init()
X = 700
Y = 548
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption(f'jor.jpg')
imp = pygame.image.load(f"jor.jpg").convert()
scrn.blit(imp, (0, 0))
pygame.display.flip()
status = True
while (status):
    time.sleep(3)
    pygame.display.quit()
    status = False

output8 = f'''

I will guide you on your journey.

We find ourselves in the city of Stilldrift in the nation of Lashar.
'''

for c in output8:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.075)

output5 = f'''
You will be assigned a race, a class, and 3 stats:

blood (health), brain (intelligence), and brawn (strength)

Let the adventure begin...'''

for c in output5:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.075)

time.sleep(3)

output6 = f'''

your race is {race}

your class is {class1}

and your stats are

{char1.stats()}

you wake up crumpled in the corner of a cell in a dungeon.

the ground is cold and wet.

across the cell you see the skeleton of a long forgotten prisoner still shackled to the wall.

the air smells musty.

suddenly you hear the sound of approaching footsteps. 

you look up to see a {monster_name}.'''

for c in output6:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.075)

pygame.init()
X = 960
Y = 717
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption(f'{monster_name}.jpg')
imp = pygame.image.load(f"{monster_name}.jpg").convert()
scrn.blit(imp, (0, 0))
pygame.display.flip()
status = True
while (status):
    time.sleep(2)
    pygame.display.quit()
    status = False

output4 = f'''

its stats are:

{monster1.monsterStats()}

the {monster_name} attacks...

'''
for c in output4:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.075)

time.sleep(3)

if monster1.brawn > char1.blood:
    if char1.brawn < monster1.blood:
        output2 = f'oof, the {monster_name} kills you...'
        time.sleep(1)
        pygame.mixer.music.load('lose.wav')
        pygame.mixer.music.play()
    elif char1.brawn > monster1.blood:
        outputTie = "both of you are strong enough to kill the other--\n\n"
        for c in outputTie:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(.075)
        heads_or_tails = pyip.inputMenu(['heads', 'tails'])
        coin_flip = random.randrange(1,3)
        if coin_flip == 1:
            result = 'heads'
        else:
            result = 'tails'
        if heads_or_tails == result:
            outputcf = f'''\nyou've chosen wisely\n
after a struggle, you kill the {monster_name}'''
            for c in outputcf:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(.075)
            pygame.mixer.music.load('win.wav')
            pygame.mixer.music.play()
            a = input('\n\npress enter to exit')
            if a:
                sys.exit()
        else:
            outputcf = f'''\nyou've chosen poorly\n
after a struggle, the {monster_name} kills you'''
            for c in outputcf:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(.075)
            pygame.mixer.music.load('lose.wav')
            pygame.mixer.music.play()
            a = input('\n\npress enter to exit')
            if a:
                sys.exit()
elif char1.brawn > monster1.blood:
    output2 = f'hurrah, you kill the {monster_name}!'
    time.sleep(1)
    pygame.mixer.music.load('win.wav')
    pygame.mixer.music.play()
elif char1.brain > monster1.brain:
    output2 = f'you outsmart the {monster_name} and escape'
    time.sleep(1)
    pygame.mixer.music.load('escape.wav')
    pygame.mixer.music.play()
else:
    output2 = 'neither of you is strong enough to kill the other--'

for c in output2:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.075)

if output2 == 'neither of you is strong enough to kill the other--\n':
    heads_or_tails = pyip.inputMenu(['heads', 'tails'])
    coin_flip = random.randrange(1,3)
    if coin_flip == 1:
        result = 'heads'
    else:
        result = 'tails'
    if heads_or_tails == result:
        outputcf = f'''\nyou've chosen wisely\n
after a struggle, you kill the {monster_name}'''
        for c in outputcf:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(.075)
        pygame.mixer.music.load('win.wav')
        pygame.mixer.music.play()
    else:
        outputcf = f'''\nyou've chosen poorly\n
after a struggle, the {monster_name} kills you'''
        for c in outputcf:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(.075)
        pygame.mixer.music.load('lose.wav')
        pygame.mixer.music.play()

a = input('\n\npress enter to exit')
if a:
    sys.exit()
