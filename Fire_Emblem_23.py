import sys, time
import random
import pygame
from pygame.locals import *
from pygame import *
from tabulate import tabulate
import time

#path finding shit
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

displayOptions=False

InRange = False
OutOfRangeEnemy = True

DoOnceForTheirTurn = True

path=[]


#save
redTile1 = pygame.image.load("redTileFinalTry2.png")


PLAYER1 = pygame.image.load("player1.png")
PLAYER2 = pygame.image.load("draug.png")
PLAYER3 = pygame.image.load("player3.png")
PLAYER4 = pygame.image.load("player4.png")

ENEMY1 = pygame.image.load("enemy1.png")
ENEMY2 = pygame.image.load("enemy2.png")
ENEMY3 = pygame.image.load("enemy3.png")
ENEMY4 = pygame.image.load("enemy4.png")

gridMap=pygame.image.load("GRID_MAP2.png")

##

Draug = pygame.image.load("Draug.png")
Draug_Grey = pygame.image.load("Draug_Grey.png")

Warrior = pygame.image.load("Warrior.png")
Warrior_Grey = pygame.image.load("Warrior_Grey.png")

Gordon = pygame.image.load("Gordon.png")
Gordon_Grey = pygame.image.load("Gordon_Grey.png")

Marth = pygame.image.load("Marth.png")
Marth_Grey = pygame.image.load("Marth_Grey.png")

Enemy_Soldier = pygame.image.load("Enemy_Soldier.png")
Enemy_Soldier_Grey = pygame.image.load("Enemy_Soldier_Grey.png")


greenoccupy = pygame.image.load("green2.png")

MOV1 = pygame.image.load("blue_select.png") #"RedSelect.png"
MOV2 = pygame.image.load("red_select.png")

MOVING_TRANSPARENCY = MOV1


#blueTile = pygame.image.load("blueTileFinal.png")
blueTile = pygame.image.load("blueTileFinalTry2.png")

redTile = pygame.image.load("redTileFinalTry2.png")#justRed.png

EnemyPhase = pygame.image.load("EnemyPhase.png")
PlayerPhase = pygame.image.load("PlayerPhase.png")


PlayerSignCount = 0
EnemySignCount = 0

PlayerCountStart = True
EnemyCountStart = False


timer = 0
FindOut = False
SubtractDamage = False
enemy_list_brackets_x = 0

count33 = 0
Count333 = False

JustdidThatDmg = False
DoNotDisplay = False
Seize = False

widthh = 0

#

TurnNumber = 1

#colors
dark_blue = (47,62,124)
tan   = (200,184,144)
tan2  = (222,203,150)
tan3  = (179,166,129)
white = (255,255,255)
red   = (187,57,57)
blue  = (0,0,255)
grey  = (130,130,130)
red2  = (255,0,0)
blue2 = (0,0,255)
black = (0,0,0)

hb_yellow = (249,255,44)
hb_green  = (82,255,7)
hb_blue   = (47,255,221)

#MNTS,DOCK,DOC2,GRAS,WATR,COAL,WOOD,CSTL,CST2,HOUS,RDHO,RDVE,RDNE,RDSE,RDSW,RDNW,RDUP,RDLE,RDRI,SAND,SND2,SND3,SND4,SND5,SND6,SND7,SND8,SND9,POND,WELL,FORT,BOT1,BOT2,ARMY = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33
showEnemyMap=False
showEnemyMap=[]


InfoSelect = False
ShowMap = False
MakeFalse = False
WPressed = False
DisplayAttackInfo = False
DisplayMoveOrAttackOptions = False
Attack = False
CanAttack = False
DisplayWhoToAttack = False
UnmovePlayer = False
Check = False
Done = False
EnemyPhaseDisplay = False
MyTurn = True
TheirTurn = False

#

DisplayAttackInfo = False
DisplayRed = False
DisplayMoveOrAttackOptions = False
DisplayWhoToAttack = False



#

MNTS = pygame.image.load("[M] mountains4.png")
DOCK = pygame.image.load("[DOCKS} d.png")
DOC2 = pygame.image.load("newest docks docks as of 504.png")
GRAS = pygame.image.load("[G] grass2.png")
WATR = pygame.image.load("[water] water full.png")
WOOD = pygame.image.load("[W] woods2.png")
CSTL = pygame.image.load("[CASTLE] castle horizontal.png")
CST2 = pygame.image.load("[C] castle2 with road123.png")
HOUS = pygame.image.load("[H] house2.png")
RDHO = pygame.image.load("[R] road1 horizontal.png")
RDVE = pygame.image.load("[R] road2 vertical.png")
RDNE = pygame.image.load("[R] road2 NE.png")
RDSE = pygame.image.load("[R] road2 SE.png")
RDSW = pygame.image.load("[R] road2 SW.png")
RDNW = pygame.image.load("[R] road2 NW.png")
RDUP = pygame.image.load("[R] road2 NEW.png")
RDLE = pygame.image.load("[R] road2 NEW direction2.png")
RDRI = pygame.image.load("[R] road2 NEW direction1.png")
POND = pygame.image.load("[POND] pond in grass1.png")
WELL = pygame.image.load("[WELL] well2.png")
FORT = pygame.image.load("[F] fort2 fort.png")
SAND = pygame.image.load("[SAND] sand2.png")
SND2 = pygame.image.load("[SAND] sand2 with grass horizontal.png")
SND3 = pygame.image.load("[SAND] sand2 with grass corner.png")
SND4 = pygame.image.load("[SAND] sand2 with grass corner2.png")
SND5 = pygame.image.load("[SAND] sand2 with grass edge.png")
SND6 = pygame.image.load("[SAND] sand2 with grass edge2.png")
SND7 = pygame.image.load("[SAND] sand2 with grass horizontal DOWN.png")
SND8 = pygame.image.load("[SAND] sand2 with grass corner5.png")
SND9 = pygame.image.load("[SAND] sand2 with grass horizontal DOWN2.png")
BOT1 = pygame.image.load("[BOAT} front of boat2.png")
BOT2 = pygame.image.load("[BOAT} back of boat2.png")
ARMY = pygame.image.load("[FORT] FORT123.PNG")

attack_enemy=0
attack_ally=0
tilesize = 30
mapwidth = 24
mapheight = 16

showEnemyMapList=[]
free_space_list2=[]

GreyScreen = False

GreyScreen_x = -mapwidth*tilesize
GreyScreen_y = -mapheight*tilesize


tilemap = [
            [MNTS,WOOD,POND,WOOD,WOOD,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,GRAS,GRAS,GRAS,GRAS,GRAS,MNTS,MNTS,MNTS,MNTS,MNTS,HOUS,RDSW,MNTS],
            
            [MNTS,MNTS,WOOD,WOOD,WOOD,WOOD,MNTS,MNTS,MNTS,MNTS,GRAS,GRAS,GRAS,POND,WOOD,GRAS,GRAS,MNTS,MNTS,WELL,MNTS,GRAS,RDVE,MNTS],
            
            [MNTS,MNTS,FORT,WOOD,WOOD,GRAS,MNTS,MNTS,MNTS,GRAS,GRAS,WOOD,WOOD,WOOD,WOOD,GRAS,GRAS,GRAS,MNTS,MNTS,GRAS,GRAS,RDVE,MNTS],
            
            [MNTS,MNTS,WOOD,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,WOOD,WOOD,WOOD,WOOD,WOOD,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,RDVE,MNTS],
            
            [MNTS,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,RDSE,RDHO,RDHO,RDHO,RDHO,RDHO,RDHO,RDHO,RDSW,GRAS,GRAS,GRAS,GRAS,WOOD,WOOD,RDVE,WOOD],
            
            [GRAS,GRAS,RDSE,RDHO,RDHO,RDHO,RDHO,RDNW,GRAS,GRAS,GRAS,WOOD,WOOD,WOOD,WOOD,RDVE,FORT,GRAS,GRAS,WOOD,WOOD,RDSE,RDUP,RDHO],
            
            [GRAS,GRAS,RDVE,GRAS,GRAS,GRAS,GRAS,FORT,GRAS,GRAS,GRAS,GRAS,MNTS,MNTS,GRAS,RDNE,RDHO,RDHO,RDHO,RDHO,RDHO,RDLE,WOOD,WOOD],
            
            [CSTL,CSTL,RDVE,CSTL,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,GRAS,MNTS,MNTS,MNTS,GRAS,GRAS,GRAS,GRAS,GRAS,WOOD,WOOD,RDVE,WOOD,WOOD],
            
            [HOUS,RDSE,RDNW,HOUS,CSTL,GRAS,GRAS,GRAS,GRAS,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,GRAS,WOOD,GRAS,GRAS,GRAS,WOOD,RDVE,WOOD,WOOD],
            
            [HOUS,RDVE,GRAS,GRAS,WELL,CSTL,GRAS,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,GRAS,GRAS,WOOD,WOOD,GRAS,GRAS,GRAS,RDVE,GRAS,GRAS],
            
            [WOOD,RDVE,WOOD,ARMY,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,SND3,SND2,SND4,GRAS,GRAS,GRAS,GRAS,GRAS,RDVE,GRAS,GRAS],
            
            [CSTL,FORT,CSTL,MNTS,MNTS,POND,MNTS,MNTS,MNTS,MNTS,SND3,SND2,SND2,SND6,SAND,SND5,SND4,GRAS,GRAS,GRAS,FORT,RDVE,GRAS,GRAS],
            
            [WOOD,CSTL,MNTS,MNTS,MNTS,MNTS,MNTS,MNTS,DOCK,DOCK,DOCK,DOCK,DOCK,DOCK,SAND,SAND,SND7,GRAS,GRAS,GRAS,GRAS,RDVE,GRAS,MNTS],
            
            [WOOD,WOOD,MNTS,MNTS,POND,MNTS,MNTS,DOC2,DOC2,DOC2,DOC2,DOC2,DOCK,DOCK,DOCK,SAND,SND7,GRAS,GRAS,GRAS,GRAS,RDVE,MNTS,MNTS],
            
            [WOOD,WOOD,MNTS,MNTS,MNTS,MNTS,WATR,WATR,WATR,WATR,BOT1,BOT2,DOC2,DOCK,DOCK,SND9,SND8,GRAS,GRAS,GRAS,GRAS,RDNE,RDHO,RDHO],
            
            [WOOD,MNTS,MNTS,MNTS,MNTS,WATR,WATR,WATR,WATR,WATR,WATR,WATR,WATR,DOCK,DOCK,GRAS,GRAS,GRAS,GRAS,GRAS,MNTS,MNTS,MNTS,MNTS]
            
        ]




blueredmap = []
for row in range(mapheight):
    new_row = []
    for column in range(mapwidth):
        if tilemap[row][column] == MNTS or tilemap[row][column] == WATR or tilemap[row][column] == POND or tilemap[row][column] == CSTL:
            new_row.append(1)
        else:
            new_row.append(0)
    blueredmap.append(new_row)

grid = []
for row in blueredmap:
    grid.append(row)



def show_map(y, z):
    grid = [x[:] for x in blueredmap]
    #print len(enemy_sprites_no_edit), "length of enemy sprites no edit"
    pls_count_this=0
    for item in enemy_sprites_no_edit:
        #print "enemy at", item.x,item.y
        grid[item.y][item.x] = 1
        pls_count_this+=1
    #print pls_count_this, "enemy on grid is 1"
    
    for item in y:
        x,y = (item[0],item[1])
        if x+1 > mapwidth:
            check1 = x
        else:
            check1=x+1
        if x-1 < 0:
            check2=x
        else:
            check2=x-1

        if y+1 > mapheight:
            check3 = y
        else:
            check3=y+1
        if y-1 < 0:
            check4=y
        else:
            check4=y-1


        
        try:
            if grid[check1][y] is 0:
                if (check1,y) not in free_space_list:
                    free_space_list.append((check1,y))
                if (check1,y) not in new_player_list:
                    z.append((check1,y))
            if grid[check2][y] is 0:
                if (check2,y) not in free_space_list:
                    free_space_list.append((check2,y))
                if (check2,y) not in new_player_list:
                    z.append((check2,y))   
            if grid[x][check3] is 0:
                if (x,check3) not in free_space_list:
                    free_space_list.append((x,check3))
                if (x,check3) not in new_player_list:
                    z.append((x,check3))  
            if grid[x][check4] is 0:
                if (x,check4) not in free_space_list:
                    free_space_list.append((x,check4))
                if (x,check4) not in new_player_list:
                    z.append((x,check4))
        except IndexError:
            what = "what"


def show_map_enemy(y, z):
    grid = [x[:] for x in blueredmap]

    for item in ally_sprites:
        if item.hppart > 0:
            grid[item.y][item.x] = 1
    
    for item in y:
        x = item[0]
        y = item[1]

        if x+1 > mapwidth:
            check1 = x
        else:
            check1=x+1
        if x-1 < 0:
            check2=x
        else:
            check2=x-1

        if y+1 > mapheight:
            check3 = y
        else:
            check3=y+1
        if y-1 < 0:
            check4=y
        else:
            check4=y-1
        
        try:
            if grid[check1][y] is 0:
                if (check1,y) not in free_space_list2:
                    free_space_list2.append((check1,y))
                if (check1,y) not in new_player_list2:
                    z.append((check1,y))
            if grid[check2][y] is 0:
                if (check2,y) not in free_space_list2:
                    free_space_list2.append((check2,y))
                if (check2,y) not in new_player_list2:
                    z.append((check2,y))   
            if grid[x][check3] is 0:
                if (x,check3) not in free_space_list2:
                    free_space_list2.append((x,check3))
                if (x,check3) not in new_player_list2:
                    z.append((x,check3))  
            if grid[x][check4] is 0:
                if (x,check4) not in free_space_list2:
                    free_space_list2.append((x,check4))
                if (x,check4) not in new_player_list2:
                    z.append((x,check4))
        except IndexError:
            what = "what"

##########################################################################

def calculate_values(Person):
    #picture,name,clas,race,level,xp,hppart,hpfull,strength,skill,speed,luck,defense,resistance,weapon,move,rang,x,y,backup_grey,backup_normal):
    if Person.weapon == 'Axe':
        weapon_dmg = 7
    elif Person.weapon == 'Lance':
        weapon_dmg = 8
    elif Person.weapon == 'Bow':
        weapon_dmg = 6
    elif Person.weapon == 'Sword':
        weapon_dmg = 6
    elif Person.weapon == 'Dagger':
        weapon_dmg = 4
    elif Person.weapon == 'Spear':
        weapon_dmg = 4
    elif Person.weapon == 'Handaxe':
        weapon_dmg = 6
    else:
        weapon_dmg = 4
        print "weapon not recognized"
    


    if tilemap[Person.y][Person.x] == MNTS:
        tile = "Mountains"
        defense, resistance, avoid, heal = (10,0,15,0)
    elif tilemap[Person.y][Person.x] == DOCK or tilemap[Person.y][Person.x] == DOC2:
        tile = "Docks"
        defense, resistance, avoid, heal = (0,0,0,0)
    elif tilemap[Person.y][Person.x] == RDHO or tilemap[Person.y][Person.x] == RDVE or tilemap[Person.y][Person.x] == RDNE or tilemap[Person.y][Person.x] == RDSE or tilemap[Person.y][Person.x] == RDSW or tilemap[Person.y][Person.x] == RDNW or tilemap[Person.y][Person.x] == RDUP or tilemap[Person.y][Person.x] == RDLE or tilemap[Person.y][Person.x] == RDRI:
        tile = "Road"
        defense, resistance, avoid, heal = (0,0,0,0)
    elif tilemap[Person.y][Person.x] == SAND or tilemap[Person.y][Person.x] == SND2 or tilemap[Person.y][Person.x] == SND3 or tilemap[Person.y][Person.x] == SND4 or tilemap[Person.y][Person.x] == SND5 or tilemap[Person.y][Person.x] == SND6 or tilemap[Person.y][Person.x] == SND7 or tilemap[Person.y][Person.x] == SND8 or tilemap[Person.y][Person.x] == SND9:
        tile = "Sand"
        defense, resistance, avoid, heal = (0,10,0,0)
    elif tilemap[Person.y][Person.x] == POND:
        tile = "Pond"
        defense, resistance, avoid, heal = (0,0,10,0)
    elif tilemap[Person.y][Person.x] == WELL:
        tile = "Well"
        defense, resistance, avoid, heal = (5,0,5,0)
    elif tilemap[Person.y][Person.x] == FORT:
        tile = "Fort"
        defense, resistance, avoid, heal = (20,10,20,5)
    elif tilemap[Person.y][Person.x] == BOT1 or tilemap[Person.y][Person.x] == BOT2:
        tile = "Boat"
        defense, resistance, avoid, heal = (0,0,10,0)
    elif tilemap[Person.y][Person.x] == ARMY:
        tile = "Armory"
        defense, resistance, avoid, heal = (10,0,5,0)
    elif tilemap[Person.y][Person.x] == WATR:
        tile = "Water"
        defense, resistance, avoid, heal = (0,0,15,0)
    elif tilemap[Person.y][Person.x] == CSTL or tilemap[Person.y][Person.x] == CST2:
        tile = "Castle"
        defense, resistance, avoid, heal = (10,0,5,0)
    elif tilemap[Person.y][Person.x] == HOUS:
        tile = "House"
        defense, resistance, avoid, heal = (10,0,5,0)
    elif tilemap[Person.y][Person.x] == GRAS:
        tile = "Grass"
        defense, resistance, avoid, heal = (0,0,0,0)
    elif tilemap[Person.y][Person.x] == WOOD:
        tile = "Woods"
        defense, resistance, avoid, heal = (10,0,10,0)
    else:
        tile = "fdfdf"
        defense, resistance, avoid, heal = (0,0,0,0)

    #

    

        
    calculate_values.damage = int(Person.strength + weapon_dmg + Person.skill*0.5)
    calculate_values.critical = int(Person.luck*0.5 + Person.speed*0.2 + Person.skill*0.3)
    calculate_values.hit_precentage = int(Person.speed + Person.skill*2 + Person.luck + 60)
    calculate_values.avoid = int(Person.speed*0.75 + Person.skill*0.5 + int(avoid))
    calculate_values.weapon_dmg = int(weapon_dmg)
    calculate_values.combined_defense = int((int(defense)/5)+Person.defense)

    
def InfoSelected(person,backup_normal,name,clas,race,level,xp,hppart,hpfull,strength,skill,speed,luck,defense,resistance,weapon,move,rang,x,y):
    pygame.draw.rect(screen, tan, (0,0,720,480))

    if item in ally_sprites_no_edit:
        colour = dark_blue
    elif item in enemy_sprites_no_edit:
        colour = red
        
    pygame.draw.rect(screen, colour, (10,130,160,340))
    pygame.draw.rect(screen, colour, (180,130,130,340))
    pygame.draw.rect(screen, colour, (320,130,390,250))

    #dark tan rectangles
    pygame.draw.rect(screen, tan3, (140,10,570,110))
    pygame.draw.rect(screen, tan3, (320,390,390,80))

    adjusted_picture = pygame.transform.scale(backup_normal, (110,110))
    screen.blit(adjusted_picture,(15,10))

    Text = Font1.render("   Str", 1, tan2)
    screen.blit(Text, (25,150))
    Text = Font1.render(str(strength), 1, white)
    screen.blit(Text, (130,150))
    Text = Font1.render("  Skill", 1, tan2)
    screen.blit(Text, (25,205))
    Text = Font1.render(str(skill), 1, white)
    screen.blit(Text, (130,205))
    Text = Font1.render("   Spd", 1, tan2)
    screen.blit(Text, (25,260))
    Text = Font1.render(str(speed), 1, white)
    screen.blit(Text, (130,260))
    Text = Font1.render("   Lck", 1, tan2)
    screen.blit(Text, (25,315))
    Text = Font1.render(str(luck), 1, white)
    screen.blit(Text, (130,315))
    Text = Font1.render("   Def", 1, tan2)
    screen.blit(Text, (25,370))
    Text = Font1.render(str(defense), 1, white)
    screen.blit(Text, (130,370))
    Text = Font1.render("   Res", 1, tan2)
    screen.blit(Text, (25,425))
    Text = Font1.render(str(resistance), 1, white)
    screen.blit(Text, (130,425))
    Text = Font2.render(str(name), 1, colour)
    screen.blit(Text, (245,20))
    Text = Font2.render(str(clas), 1, colour)
    screen.blit(Text, (456,20))
    Text = FontSmall.render("Lvl", 1, colour)
    screen.blit(Text, (250,55))
    Text = Font2.render(str(level), 1, colour)
    screen.blit(Text, (290,51))
    Text = FontSmall.render("E", 1, colour)
    screen.blit(Text, (320,55))
    Text = Font2.render(str(xp), 1, colour)
    screen.blit(Text, (350,51))
    Text = FontSmall.render("HP", 1, colour)
    screen.blit(Text, (250,90))
    Text = Font2.render(str(hppart) + " / " + str(hpfull), 1, colour)
    screen.blit(Text, (300,86))
    Text = Font1.render("Mov", 1, tan2)
    screen.blit(Text, (200,150))
    Text = Font1.render(str(move), 1, white)
    screen.blit(Text, (270,150))
    Text = Font1.render("Rng", 1, tan2)
    screen.blit(Text, (200,200))
    Text = Font1.render(str(rang), 1, white)
    screen.blit(Text, (270,200))


    calculate_values(person)
    
    attack        = calculate_values.damage
    critical      = calculate_values.critical
    hit           = calculate_values.hit_precentage
    avoid         = calculate_values.avoid
    weapon_dmg    = calculate_values.weapon_dmg
    total_defense = calculate_values.combined_defense
    
    

    Text = FontSmall.render("Atk", 1, colour)
    screen.blit(Text, (460,55))
    Text = Font2.render(str(attack), 1, colour)
    screen.blit(Text, (510,51))
    Text = FontSmall.render("Crit", 1, colour)
    screen.blit(Text, (600,55))
    Text = Font2.render(str(critical), 1, colour)
    screen.blit(Text, (650,51))
    Text = FontSmall.render("Hit", 1, colour)
    screen.blit(Text, (460,90))
    Text = Font2.render(str(hit), 1, colour)
    screen.blit(Text, (510,86))
    Text = FontSmall.render("Avo", 1, colour)
    screen.blit(Text, (600,90))
    Text = Font2.render(str(avoid), 1, colour)
    screen.blit(Text, (650,86))
    Text = FontSmall.render("Weapon", 1, tan2)
    screen.blit(Text, (350,140))
    Text = Font2.render(str(weapon), 1, white)
    screen.blit(Text, (350,170))
    Text = FontSmall.render("Damage", 1, tan2)
    screen.blit(Text, (500,140))
    Text = Font2.render(str(weapon_dmg), 1, white)
    screen.blit(Text, (500,170))

    ##
    if tilemap[mov_y][mov_x] == MNTS:
        tile = "Mountains"
        defense, resistance, avoid, heal = (10,0,15,0)
    elif tilemap[mov_y][mov_x] == DOCK or tilemap[mov_y][mov_x] == DOC2:
        tile = "Docks"
        defense, resistance, avoid, heal = (0,0,0,0)
    elif tilemap[mov_y][mov_x] == RDHO or tilemap[mov_y][mov_x] == RDVE or tilemap[mov_y][mov_x] == RDNE or tilemap[mov_y][mov_x] == RDSE or tilemap[mov_y][mov_x] == RDSW or tilemap[mov_y][mov_x] == RDNW or tilemap[mov_y][mov_x] == RDUP or tilemap[mov_y][mov_x] == RDLE or tilemap[mov_y][mov_x] == RDRI:
        tile = "Road"
        defense, resistance, avoid, heal = (0,0,0,0)
    elif tilemap[mov_y][mov_x] == SAND or tilemap[mov_y][mov_x] == SND2 or tilemap[mov_y][mov_x] == SND3 or tilemap[mov_y][mov_x] == SND4 or tilemap[mov_y][mov_x] == SND5 or tilemap[mov_y][mov_x] == SND6 or tilemap[mov_y][mov_x] == SND7 or tilemap[mov_y][mov_x] == SND8 or tilemap[mov_y][mov_x] == SND9:
        tile = "Sand"
        defense, resistance, avoid, heal = (0,10,0,0)
    elif tilemap[mov_y][mov_x] == POND:
        tile = "Pond"
        defense, resistance, avoid, heal = (0,0,10,0)
    elif tilemap[mov_y][mov_x] == WELL:
        tile = "Well"
        defense, resistance, avoid, heal = (5,0,5,0)
    elif tilemap[mov_y][mov_x] == FORT:
        tile = "Fort"
        defense, resistance, avoid, heal = (20,10,20,5)
    elif tilemap[mov_y][mov_x] == BOT1 or tilemap[mov_y][mov_x] == BOT2:
        tile = "Boat"
        defense, resistance, avoid, heal = (0,0,10,0)
    elif tilemap[mov_y][mov_x] == ARMY:
        tile = "Armory"
        defense, resistance, avoid, heal = (10,0,5,0)
    elif tilemap[mov_y][mov_x] == WATR:
        tile = "Water"
        defense, resistance, avoid, heal = (0,0,15,0)
    elif tilemap[mov_y][mov_x] == CSTL or tilemap[mov_y][mov_x] == CST2:
        tile = "Castle"
        defense, resistance, avoid, heal = (10,0,5,0)
    elif tilemap[mov_y][mov_x] == HOUS:
        tile = "House"
        defense, resistance, avoid, heal = (10,0,5,0)
    elif tilemap[mov_y][mov_x] == GRAS:
        tile = "Grass"
        defense, resistance, avoid, heal = (0,0,0,0)
    elif tilemap[mov_y][mov_x] == WOOD:
        tile = "Woods"
        defense, resistance, avoid, heal = (10,0,10,0)
    else:
        tile = "fdfdf"
        defense, resistance, avoid, heal = (0,0,0,0)

            

    #text1 = Font2.render("Tile",True,(255,255,255))
    #text2 = Font1.render(str(tile),True,(255,255,255))
        
    text3 = Font2.render(("Def   " + str(defense)),True,(255,255,255))
    text4 = Font2.render(("Res  " + str(resistance)),True,(255,255,255))
    text5 = Font2.render(("Avo  " + str(avoid)),True,(255,255,255))
    text6 = Font2.render(("Heal " + str(heal)),True,(255,255,255))
        

    #RIGHT HERE
    #adjusted_picture = pygame.transform.scale(tilemap[mov_y][mov_x], (65,65))
    start_pic_x,start_pic_y=(mov_x*tilesize,mov_y*tilesize)
    adjusted_picture = gridMap
    #newadjusted_picture = pygame.transform.scale(adjusted_picture, (65,65))
    screen.blit(adjusted_picture,(329,398),(start_pic_x+1,start_pic_y+1,28,28))

    #screen.blit(text1,pygame.Rect(400,405,10,10))
    #screen.blit(text2,pygame.Rect(400,432,10,10))
        
    screen.blit(text3,pygame.Rect(410,405,10,10))
    screen.blit(text4,pygame.Rect(510,405,10,10))
    screen.blit(text5,pygame.Rect(410,440,10,10))
    screen.blit(text6,pygame.Rect(510,440,10,10))
        

##########################################################################

class Character(pygame.sprite.Sprite):

    num_of_characters = 0

    def __init__(self,picture,name,clas,race,level,xp,hppart,hpfull,strength,skill,speed,luck,defense,resistance,weapon,move,rang,x,y,backup_grey,backup_normal):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((tilesize,tilesize))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x=self.x*tilesize
        self.rect.y=self.y*tilesize
        
        self.image=picture

        self.picture = picture
        self.name = name
        self.clas = clas
        self.race = race
        self.level = level
        self.xp = xp
        self.hppart = hppart
        self.hpfull = hpfull
        self.strength = strength
        self.skill = skill
        self.speed = speed
        self.luck = luck
        self.defense = defense
        self.resistance = resistance
        self.name = name
        self.weapon = weapon
        self.move = move
        self.rang = rang
        
        self.backup_grey = backup_grey
        self.backup_normal = backup_normal

        self.path=[]
        
        Character.num_of_characters += 1


        ##


        
#############################################
        """
        Character.x = self.x
        Character.y = self.y
        Character.rect.x=self.
        Character.rect.y=Character.y*tilesize
        """

        
        Character.picture = self.picture
        Character.name = self.name
        Character.clas = self.clas
        Character.race = self.race
        Character.level = self.level
        Character.xp = self.xp
        Character.hppart = self.hppart
        Character.hpfull = self.hpfull
        Character.strength = self.strength
        Character.skill = self.skill
        Character.speed = self.speed
        Character.luck = self.luck
        Character.defense = self.defense
        Character.resistance = self.resistance
        Character.name = self.name
        Character.weapon = self.weapon
        Character.move = self.move
        Character.rang = self.rang
        
        Character.backup_grey = self.backup_grey
        Character.backup_normal = self.backup_normal
        




        Character.path=self.path

        


class Enemy(Character):
    pass        

class Ally(Character):
    pass

#picture,name,clas,race,level,xp,hppart,hpfull,strength,skill,speed,luck,defense,resistance,weapon,move,rang,x,y,backup_pic_grey,backup_pic
WarriorAlly = Ally(Warrior,'Barst','Fighter','Dwarf',1,0,18,18,7,4,5,6,5,2,'Handaxe',5,1.5,5,2,Warrior_Grey,Warrior)
GeneralAlly = Ally(Draug,'Draug','Knight','Orc',1,0,22,22,8,7,3,3,9,5,'Lance',6,1,1,4,Draug_Grey,Draug)
ArcherAlly  = Ally(Gordon,'Gordon','Archer','Human',1,0,16,16,5,6,7,5,5,4,'Bow',5,2,3,0,Gordon_Grey,Gordon)
HeroAlly    = Ally(Marth,'Marth','Hero','Elf',1,0,17,17,7,8,6,3,7,2,'Sword',6,1,2,2,Marth_Grey,Marth)

#WhoEnemy=Enemy(Enemy_Soldier,'only example out of range','Pirate','Human', 1,0,15,15,5,4,4,0,6,3,'Spear',5,1,-15,-15,Enemy_Soldier_Grey,Enemy_Soldier)

marth_to_move = HeroAlly
mov_x, mov_y = (marth_to_move.x,marth_to_move.y)#marth_to_move.x,marth_to_move.y

Soldier = Enemy(Enemy_Soldier,'Soldier','Pirate','Human', 1,0,15,15,5,4,4,0,6,3,'Spear',5,1,14,9,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier2 = Enemy(Enemy_Soldier,'Soldier2','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,4,4,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier3 = Enemy(Enemy_Soldier,'Soldier3','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,12,4,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier4 = Enemy(Enemy_Soldier,'Soldier4','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,11,5,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier5 = Enemy(Enemy_Soldier,'Soldier5','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,14,6,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier6 = Enemy(Enemy_Soldier,'Soldier6','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,1,11,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier7 = Enemy(Enemy_Soldier,'Soldier7','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,17,13,Enemy_Soldier_Grey,Enemy_Soldier)
Soldier8 = Enemy(Enemy_Soldier,'Soldier8','Pirate','Human',1,0,15,15,5,4,4,0,6,3,'Spear',5,1,18,12,Enemy_Soldier_Grey,Enemy_Soldier)


all_sprites=pygame.sprite.Group()
enemy_sprites=pygame.sprite.Group()
ally_sprites=pygame.sprite.Group()

#

for myAllies in [WarriorAlly,GeneralAlly,ArcherAlly,HeroAlly]:
    all_sprites.add(myAllies)
    ally_sprites.add(myAllies)

for myEnemies in [Soldier,Soldier2,Soldier3,Soldier4,Soldier5,Soldier6,Soldier7,Soldier8]:
    all_sprites.add(myEnemies)
    enemy_sprites.add(myEnemies)


ally_sprites_no_edit=ally_sprites.copy()
enemy_sprites_no_edit=enemy_sprites.copy()

pygame.init()

pygame.mouse.set_visible(False)


screen = pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize))

Font1 = pygame.font.Font(None, 40)
Font2 = pygame.font.Font(None, 30)
FontSmall = pygame.font.Font(None, 20)
FontTiny = pygame.font.Font(None,17)
FontTiny2 = pygame.font.Font(None,12)

Font3 = pygame.font.SysFont('simsunnsimsun', 27)
Font4 = pygame.font.SysFont('simsunnsimsun', 22)

clock = pygame.time.Clock()

count_up=0
count_down=0
count_left=0
count_right=0

speedTile=3
        
while True:

    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        InfoSelect = False

        count_up+=1
        if count_up==1:
            if ShowMap is False:
                if (mov_y - 1) >= 0:
                    mov_y -= 1
            elif ShowMap is True:
                if (mov_y-1) >= 0:
                    mov_y -= 1
        elif count_up==speedTile:
            count_up=0
    else:
        count_up=0


                    
    if keys[pygame.K_DOWN]:
        InfoSelect = False
        count_down+=1
        if count_down==1:
            if ShowMap is False:
                if (mov_y + 1) <= (mapheight-1):
                    mov_y += 1
            elif ShowMap is True:
                if (mov_y+1) >= 0:
                    mov_y += 1
        elif count_down==speedTile:
            count_down=0
    else:
        count_down=0
        
    if keys[pygame.K_LEFT]:
        InfoSelect = False
        count_left+=1
        if count_left==1:
            if ShowMap is False:
                if (mov_x - 1) >= 0:
                    mov_x -= 1
            elif ShowMap is True:
                if (mov_x-1) >= 0:
                    mov_x -= 1
        elif count_left==speedTile:
            count_left=0
    else:
        count_left=0
    if keys[pygame.K_RIGHT]:
        InfoSelect = False
        count_right+=1
        if count_right==1:
            if ShowMap is False:
                if (mov_x + 1) <= (mapwidth-1):
                    mov_x += 1
            elif ShowMap is True:
                if (mov_x+1) >= 0:
                    mov_x += 1
        elif count_right==speedTile:
            count_right=0
    else:
        count_right=0














##########################################################################################


            
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


            

            if event.key == K_s:
                if MyTurn is True:
                    if InfoSelect is False and ShowMap is False and DisplayMoveOrAttackOptions is False:
                        InfoSelect = True
                    else:
                        InfoSelect = False

            elif event.key == K_d:
                if DisplayMoveOrAttackOptions is True or Attack is True:# or JustdidThatDmg is True:
                    UnmovePlayer = True
                    print "004"
                    JustdidThatDmg = False

                if DisplayMoveOrAttackOptions is True or Attack is True:# or JustdidThatDmg is True:
                    deleteList=[]
                    for item in ally_sprites:
                        deleteList.append((item.x,item.y))
                    if (mov_x,mov_y) in deleteList:
                        UnmovePlayer = True
                        print "003"
                        JustdidThatDmg = False
                if DisplayWhoToAttack is True:
                    #print "22"
                    UnmovePlayer=True
                    print "002"
                    JustdidThatDmg = False
                    
                InfoSelect = False
                ShowMap = False
                WPressed = False
                MakeFalse = False
                DisplayAttackInfo = False
                DisplayRed = False
                DisplayMoveOrAttackOptions = False
                DisplayWhoToAttack = False
                displayOptions=False
                #Attack = False

                #showEnemyMap
                testForFalse=False
                for item in enemy_sprites_no_edit:
                    if (mov_y,mov_x) == (item.y,item.x):
                        
                        if item in showEnemyMapList:
                            showEnemyMapList.remove(item)
                        if len(showEnemyMapList)==0:
                            showEnemyMap=False
                            showEnemyMapList=[]
                gather=[]
                for item in enemy_sprites_no_edit:
                    gather.append((item.y,item.x))
                    
                if showEnemyMap is True:
                    if (mov_y,mov_x) not in gather:
                        showEnemyMap=False
                    
                            

            elif event.key == K_w:
                
                if Seize is True:
                    GreyScreen = True
                    Seize = False
                    #grey screen slide from left to right
                    

                    
                if MyTurn is True:
                    if Count333 is False:
                        myTempList=[]
                        for item in all_sprites:
                            if item.hppart > 0:
                                myTempList.append((item.x,item.y))

                        onAPlayer=False
                        for item in myTempList:
                            if (mov_x,mov_y) in myTempList:
                                onAPlayer=True
                        if onAPlayer is False and InfoSelect is False and WPressed is False and MakeFalse is False and ShowMap is False and DisplayAttackInfo is False and DisplayRed is False and DisplayMoveOrAttackOptions is False and DisplayWhoToAttack is False:
                            displayOptions=True
                            print ShowMap

                        ###################3

                        for item in enemy_sprites_no_edit:
                            if (mov_y,mov_x) == (item.y,item.x) and DisplayWhoToAttack is False:
                                showEnemyMap=True
                                #print "here 22"
                                if item not in showEnemyMapList:
                                    showEnemyMapList.append(item)

                        
                        #print len(ally_sprites)
                        for item in ally_sprites:
                            #print "a"
                            
                            if (mov_y, mov_x) == (item.y,item.x) and ShowMap is False and DisplayMoveOrAttackOptions is False:
                                #print "breaking"
                                Done = False
                                if ShowMap is True:
                                    ShowMap = False
                                elif ShowMap is False and DisplayWhoToAttack is False:
                                    ShowMap = True
                                    x1 = item.x
                                    y1 = item.y
                                    move1 = item.move
                                MoveWho = item
                                previousPlayerPos = [MoveWho.x,MoveWho.y]
                                break
                            #aha above is 'break'
                            #print ShowMap, "false or true"
                            if ShowMap is True and DisplayMoveOrAttackOptions is False:

                                if ShowMap is True:
                                    if (MoveWho.y,MoveWho.x) not in free_space_list:
                                        free_space_list.append((MoveWho.y,MoveWho.x))
                                    if (mov_y,mov_x) not in free_space_list:
                                        ShowMap=False
                                        break
                                #print "dawgg"
                                done=False
                                #
                                if (MoveWho.y,MoveWho.y) == (1,11):
                                    print "got there"
                                    #
                                    
                                if (MoveWho.y,MoveWho.x) not in free_space_list:
                                   # print "not in free space list"
                                    free_space_list.append((MoveWho.y,MoveWho.x))

                                    #

                                    TempList = []
                                    for item in ally_sprites_no_edit:
                                        TempList.append(item)
                                    TempList.remove(MoveWho)
                                    
                                    for Ally in TempList:
                                        if (Ally.y,Ally.x) in free_space_list:
                                            free_space_list.remove((Ally.y,Ally.x))

                                    #



                                    ########
                                if (mov_y,mov_x) in free_space_list: #above is kinda redundant since im auto places this int the free_space_list
                                   # print "in free space list"
                                    Okay = True
                                        
                                    if Okay is True:
                                        #print "ookay"
                                        #print (MoveWho.rect.x/tilesize),(MoveWho.rect.y/tilesize)
                                        MoveWho.x = mov_x
                                        MoveWho.y = mov_y
                                        MoveWho.rect.x=mov_x*tilesize
                                        MoveWho.rect.y=mov_y*tilesize

                                        #print (MoveWho.rect.x/tilesize),(MoveWho.rect.y/tilesize)
                                        #print "ookay done"
                                        ShowMap = False
                                        DisplayMoveOrAttackOptions = True
                                    
                    #Count333
                    #if

                    #try:
                    #print "test for count333", Count333
                    if DisplayWhoToAttack is True and (WhoEnemy.x,WhoEnemy.y) == (mov_x,mov_y):# and Count333 is False:

                        #print "ja pressed here"


                        if MoveWho.weapon == 'Axe':
                            add_dmg_me = 6
                        elif MoveWho.weapon == 'Lance':
                            add_dmg_me = 6
                        elif MoveWho.weapon == 'Bow':
                            add_dmg_me = 5
                        elif MoveWho.weapon == 'Sword':
                            add_dmg_me = 5
                        elif MoveWho.weapon == 'Dagger':
                            add_dmg_me = 4
                        elif MoveWho.weapon == 'Spear':
                            add_dmg_me = 4
                        elif MoveWho.weapon == 'Handaxe':
                            add_dmg_me = 6
                        else:
                            add_dmg_me = 4

                        if WhoEnemy.weapon == 'Axe':
                            add_dmg_them = 6
                        elif WhoEnemy.weapon == 'Lance':
                            add_dmg_them = 6
                        elif WhoEnemy.weapon == 'Bow':
                            add_dmg_them = 5
                        elif WhoEnemy.weapon == 'Sword':
                            add_dmg_them = 5
                        elif WhoEnemy.weapon == 'Dagger':
                            add_dmg_them = 4
                        elif MoveWho.weapon == 'Spear':
                            add_dmg_them = 4
                        elif MoveWho.weapon == 'Handaxe':
                            add_dmg_them = 6
                        else:
                            add_dmg_them = 4


                        calculate_values(MoveWho)
                       #print "calculating damages for ", MoveWho.name
                        
                        ally_damage = calculate_values.damage
                        ally_critical = calculate_values.critical
                        ally_hit_percentage = calculate_values.hit_precentage
                        ally_avoid = calculate_values.avoid
                        ally_weapon_dmg = calculate_values.weapon_dmg
                        ally_total_defense = calculate_values.combined_defense

                        calculate_values(WhoEnemy)
                        
                        enemy_damage = calculate_values.damage
                        enemy_critical = calculate_values.critical
                        enemy_hit_percentage = calculate_values.hit_precentage
                        enemy_avoid = calculate_values.avoid
                        enemy_weapon_dmg = calculate_values.weapon_dmg
                        enemy_total_defense = calculate_values.combined_defense


                        list_for_ally_hit = []
                        hit = (ally_hit_percentage - enemy_avoid)

                        for i in range(0,hit):
                            list_for_ally_hit.append(1)
                        for i in range(0,(100-hit)):
                            list_for_ally_hit.append(0)
                        choice = random.choice(list_for_ally_hit)

                        if choice == 0:
                            Hit_Ally = False
                        elif choice == 1:
                            Hit_Ally = True

                        #print "hit percentage is ", hit, ": and did they hit? ", Hit_Ally

                        ally_crit_list = []
                        for i in range(0,ally_critical):
                            ally_crit_list.append(1)
                        for i in range(0,(100-ally_critical)):
                            ally_crit_list.append(0)
                        choice = random.choice(ally_crit_list)

                        if choice == 0:
                            Crit_Ally = False
                        elif choice == 1:
                            Crit_Ally = True
                        #
                        list_for_enemy_hit = []
                        hit = (enemy_hit_percentage - ally_avoid)

                        for i in range(0,hit):
                            list_for_enemy_hit.append(1)
                        for i in range(0,(100-hit)):
                            list_for_enemy_hit.append(0)
                        choice = random.choice(list_for_enemy_hit)

                        if choice == 0:
                            Hit_Enemy = False
                        elif choice == 1:
                            Hit_Enemy = True

                        enemy_crit_list = []
                        for i in range(0,enemy_critical):
                            enemy_crit_list.append(1)
                        for i in range(0,(100-enemy_critical)):
                            enemy_crit_list.append(0)
                        choice = random.choice(enemy_crit_list)

                        if choice == 0:
                            Crit_Enemy = False
                        elif choice == 1:
                            Crit_Enemy = True

                            
                        #
                            

                        

                        

                        #

                            
                        DisplayMoveOrAttackOptions = False
                        Attack = False
                        JustdidThatDmg=True
                        
                        #MoveWho.picture = MoveWho.backup_grey
                        ally_sprites.remove(MoveWho)

                        
                        DisplayWhoToAttack = False

                        Count333 = True
                    #except NameError:
                        #UnmovePlayer=True
                    

                      #  InfoSelect = False
               # ShowMap = False
                #WPressed = False
                #MakeFalse = False

                    
                        
            elif event.key == K_q and DisplayMoveOrAttackOptions is True:
                for item in ally_sprites:
                    if (mov_x,mov_y) == (item.x,item.y) and item.hppart > 0:
                        TheAttackerIs = item
                        Attack = True

                getListEnemyPos=[]
                for item in enemy_sprites_no_edit:
                    getListEnemyPos.append((item.y,item.x))
                    
                if CanAttack is True:# and (mov_x,mov_y) in getListEnemyPos: #and is at the pos of an enemy
                    DisplayWhoToAttack = True
                else:
                    UnmovePlayer=True
                    print "001"
                    Attack = False
                    #DisplayWhoToAttack = False
                    #CanAttack=False
                    #
                    #Attack = False
                    DisplayMoveOrAttackOptions=False
                    print "no to q"

            elif event.key == K_e:
                if  DisplayMoveOrAttackOptions is True:

                    DisplayMoveOrAttackOptions = False
                    MoveWho.picture = MoveWho.backup_grey
                    ally_sprites.remove(MoveWho)
                    
                if displayOptions is True:#displayOptions
                    displayOptions=False
                    EnemySignCount = 0
                    EnemyPhaseDisplay = True
                    EnemyCountStart = True

                    MyTurn = False
                    
                    enemy_sprites_no_edit.empty()
                    
                    for item in enemy_sprites:
                        if item.hppart > 0:
                            enemy_sprites_no_edit.add(item)

                    for item in ally_sprites_no_edit:
                        item.picture = item.backup_normal

                        
    for row in range(mapheight):
        for column in range(mapwidth):
            screen.blit(tilemap[row][column], (column*tilesize,row*tilesize))

    screen.blit(gridMap,(0,0))
            
    screen.blit(greenoccupy,(1*tilesize,11*tilesize))

    if showEnemyMap is True:
        enemyDisplayMap=[]
        
        for item in showEnemyMapList:
            ##########################################################################################
            
            free_space_list2 = []
            second_new_player_list2 = []
            third_new_player_list2 = []

            
            y1 = item.y
            x1 = item.x
            move1 = item.move

            enemyrang=item.rang
            #PROBLEM HERE?
            new_player_list2 = [(y1,x1)]

                
            show_map_enemy(new_player_list2, second_new_player_list2)

            for i in range((move1-1)):
                show_map_enemy(second_new_player_list2, third_new_player_list2)
                        
                second_new_player_list2 = []
                        
                for item in third_new_player_list2:
                    second_new_player_list2.append(item)
                    
            #maybe prob below 1
            for item in ally_sprites_no_edit:
                if (item.y,item.x) in free_space_list2 and item.hppart > 0:
                    free_space_list2.remove((item.y,item.x))
            for item in enemy_sprites_no_edit:
                if (item.y,item.x) in free_space_list2 and item.hppart >0:
                    free_space_list2.remove((item.y,item.x))


            enemyRedList=[]
            if enemyrang==1:
                for item in free_space_list2:
                    if ((item[0]+1),item[1]) not in free_space_list2 and ((item[0]+1),item[1]) not in enemyRedList:
                        enemyRedList.append((item[0]+1,item[1]))
                        
                    #elif ((item[1]+1),item[0]) not in myRedList:
                        #blah=""

                    if ((item[0]-1),item[1]) not in free_space_list2 and ((item[0])-1,item[1]) not in enemyRedList:
                        enemyRedList.append((item[0]-1,item[1]))
                    #elif ((item[1]-1),item[0]) not in myRedList:
                        #myRedList.append((item[1]-1,item[0]))

                    if ((item[0]),item[1]+1) not in free_space_list2 and ((item[0]),item[1]+1) not in enemyRedList:
                        enemyRedList.append((item[0],item[1]+1))
                    #elif ((item[1]),item[0]+1) not in myRedList:
                        #myRedList.append((item[1],item[0]+1))

                    if ((item[0]),item[1]-1) not in free_space_list2 and ((item[0]),item[1]-1) not in enemyRedList:
                        enemyRedList.append((item[0],item[1]-1))
                    #elif ((item[1]),item[0]-1) not in myRedList:
                        #myRedList.append((item[1],item[0]-1))
            if enemyrang==1.5 or enemyrang==2:
                for item in free_space_list2:
                    #print item, "should be free sapce y then x"


                    if ((item[0]),item[1]-1) not in free_space_list2 and ((item[0]),item[1]-1) not in enemyRedList:
                        enemyRedList.append((item[0],item[1]-1))
                    if ((item[0]-1),item[1]) not in free_space_list2 and ((item[0])-1,item[1]) not in enemyRedList:
                        enemyRedList.append((item[0]-1,item[1]))
                    if (item[0],item[1]+1) not in free_space_list2 and (item[0],item[1]+1) not in enemyRedList:
                        enemyRedList.append((item[0],item[1]+1))
                    if ((item[0]+1),item[1]) not in free_space_list2 and ((item[0]+1),item[1]) not in enemyRedList:
                        enemyRedList.append((item[0]+1,item[1]))

                    if ((item[0]+2),item[1]) not in free_space_list2 and ((item[0])+2,item[1]) not in enemyRedList:
                        enemyRedList.append((item[0]+2,item[1]))
                    if ((item[0]-2),item[1]) not in free_space_list2 and ((item[0])-2,item[1]) not in enemyRedList:
                        enemyRedList.append((item[0]-2,item[1]))
                    if ((item[0]),item[1]+2) not in free_space_list2 and ((item[0]),item[1]+2) not in enemyRedList:
                        enemyRedList.append((item[0],item[1]+2))
                    if ((item[0]),item[1]-2) not in free_space_list2 and ((item[0]),item[1]-2) not in enemyRedList:
                        enemyRedList.append((item[0],item[1]-2))

                    if ((item[0])-1,item[1]-1) not in free_space_list2 and ((item[0])-1,item[1]-1) not in enemyRedList:
                        enemyRedList.append((item[0]-1,item[1]-1))
                    if ((item[0]-1),item[1]+1) not in free_space_list2 and ((item[0])-1,item[1]+1) not in enemyRedList:
                        enemyRedList.append((item[0]-1,item[1]+1))
                    if ((item[0])+1,item[1]+1) not in free_space_list2 and ((item[0])+1,item[1]+1) not in enemyRedList:
                        enemyRedList.append((item[0]+1,item[1]+1))
                    if ((item[0])+1,item[1]-1) not in free_space_list2 and ((item[0])+1,item[1]-1) not in enemyRedList:
                        enemyRedList.append((item[0]+1,item[1]-1))



            for item in free_space_list2:
                if item not in enemyDisplayMap:
                    enemyDisplayMap.append(item)

            for item in enemyRedList:
                if item not in enemyDisplayMap:
                    enemyDisplayMap.append(item)

            

        for item in enemyDisplayMap:
            screen.blit(redTile,(item[1]*tilesize,item[0]*tilesize))
        



            ##########################################################################################
            


    


            
    if PlayerCountStart is True:
        PlayerSignCount += 1
    if EnemyCountStart is True:
        EnemySignCount += 1

    
    if PlayerSignCount > 0 and PlayerSignCount < 80:
        PlayerPhaseDisplay = True
        
        MyTurn = False
        TheirTurn = False
    elif PlayerSignCount == 80:
        MyTurn = True
        PlayerPhaseDisplay = False
        
        for item in enemy_sprites_no_edit:
            item.picture = item.backup_normal
        

    if EnemySignCount > 0 and EnemySignCount < 80:
        EnemyPhaseDisplay = True

        MyTurn = False
        TheirTurn = False
    elif EnemySignCount == 80:
        TheirTurn = True
        EnemyPhaseDisplay = False
        #print "gah be"
        
        grid_for_enemy_map = []
        for row in grid:
            grid_for_enemy_map.append(row)

        

        

    for item in ally_sprites_no_edit:
        if item.hppart > 0:
            screen.blit((item.picture),(item.rect.x,item.rect.y))

            #get health
            hpfull = item.hpfull
            hppart = item.hppart
            #print hppart
                
            if hpfull < 30:
                color = hb_yellow
            elif hpfull < 40:
                color = hb_green
            elif hpfull >= 40:
                color = hb_blue
                

            s = pygame.Surface((tilesize,3))
            s.fill(black)
            screen.blit(s,pygame.Rect(item.rect.x,item.rect.y+27,tilesize,3))

            percentage = float(hppart)/float(hpfull)                    
            s = pygame.Surface((tilesize*percentage,3))
            s.fill(color)
            screen.blit(s,pygame.Rect(item.rect.x,item.rect.y+27,tilesize,3))

    for item in enemy_sprites_no_edit:
        if item.hppart > 0:
            #print 
            screen.blit((item.picture),(item.rect.x,item.rect.y))

            hpfull = item.hpfull
            hppart = item.hppart
                
            if hpfull < 30:
                color = hb_yellow
            elif hpfull < 40:
                color = hb_green
            elif hpfull >= 40:
                color = hb_blue
                

            s = pygame.Surface((tilesize,3))
            s.fill(black)
            screen.blit(s,pygame.Rect(item.rect.x,item.rect.y+27,tilesize,3))


            #
            percentage = float(hppart)/float(hpfull)
                
                   
            s = pygame.Surface((tilesize*percentage,3))
            s.fill(color)
            screen.blit(s,pygame.Rect(item.rect.x,item.rect.y+27,tilesize,3))
            
    if TheirTurn is True and len(enemy_sprites_no_edit)==0:

        for item in path:
           screen.blit(MOVING_TRANSPARENCY,(item[0]*tilesize,item[1]*tilesize))
        timer += 1
        #####################################################
 

        if DoOnceForTheirTurn is True:
            #print "#######################################################"


            
            MOVING_TRANSPARENCY = MOV2
            
            #below didnt work                        
            #EnemyChoice = enemy_sprites_no_edit[enemy_list_brackets_x]
            EnemyChoice=enemy_sprites_no_edit.sprites()[enemy_list_brackets_x]
            """
            try:
                EnemyChoice=enemy_sprites_no_edit.sprites()[enemy_list_brackets_x]
            except IndexError:
                print "all enemies dead"
            """
            
            the_number_of_enemies_is = 0
            for item in enemy_sprites:
                the_number_of_enemies_is += 1
                
          
            coouunntt = 0
            ally_sprites.empty()
            for item in ally_sprites_no_edit:
                coouunntt += 1
                if item.hppart > 0:
                    ally_sprites.add(item)

                
            for item in ally_sprites:
                item.picture = item.backup_normal


            ###########################################################################################

                
            free_space_list2 = []
            second_new_player_list2 = []
            third_new_player_list2 = []

            
            y1 = EnemyChoice.y
            x1 = EnemyChoice.x
            move1 = EnemyChoice.move
            #PROBLEM HERE?
            new_player_list2 = [(y1,x1)]

                
            show_map_enemy(new_player_list2, second_new_player_list2)

            for i in range((move1-1)):
                show_map_enemy(second_new_player_list2, third_new_player_list2)
                        
                second_new_player_list2 = []
                        
                for item in third_new_player_list2:
                    second_new_player_list2.append(item)
                    
            #maybe prob below 1
            for item in ally_sprites_no_edit:
                if (item.y,item.x) in free_space_list2 and item.hppart > 0:
                    free_space_list2.remove((item.y,item.x))
            for item in enemy_sprites_no_edit:
                if (item.y,item.x) in free_space_list2 and item.hppart >0:
                    free_space_list2.remove((item.y,item.x))


            ally_list = []#list of (x,y) coords for all allies
            
            for item in ally_sprites:
                if item.hppart > 0:
                    ally_list.append((item.x,item.y))

                    #x_position,y_position = item.x,item.y
                    grid[item.y][item.x] = 1
            



            for item in free_space_list2:

                if ((item[1]+1),item[0]) in ally_list:
                    InRange = True
                    #print "Ally in range boys"
                    #maybe porb below2@line 1615
                    for ally in ally_sprites:
                        if ((item[1]+1),item[0]) == (ally.x,ally.y):
                            AllyToAttack = ally
                            #print AllyToAttack[1],AllyToAttack[0],"fuck bro coord of ally to attack / think x then y"
                            FindOut = False
                    break
                elif ((item[1]-1),item[0]) in ally_list:
                    InRange = True
                   # print "Ally in range boys"
                    for ally in ally_sprites:
                        if ((item[1]-1),item[0]) == (ally.x,ally.y):
                            AllyToAttack = ally
                            #print AllyToAttack[1],AllyToAttack[0],"fuck bro coord of ally to attack / think x then y"
                            FindOut = False
                    break
                elif ((item[1]),item[0]-1) in ally_list:
                    InRange = True
                    #print "Ally in range boys"
                    for ally in ally_sprites:
                        if ((item[1]),item[0]-1) == (ally.x,ally.y):
                            AllyToAttack = ally
                            #print AllyToAttack[1],AllyToAttack[0],"fuck bro coord of ally to attack / think x then y"
                            FindOut = False
                    break
                elif ((item[1]),item[0]+1) in ally_list:
                    InRange = True
                    #print "Ally in range boys"
                    for ally in ally_sprites:
                        if ((item[1]),item[0]+1) == (ally.x,ally.y):
                            AllyToAttack = ally
                            #print AllyToAttack[1],AllyToAttack[0],"fuck bro coord of ally to attack / think x then y"
                            FindOut = False
                    break

                
                else:
                    InRange = False # if InRange is False: #this means that for basic free space list an ally to attack is NOT an adjacent square\\
                    
                    #print "not in range"

            #print InRange, "in range fro my guy at", EnemyChoice.x,EnemyChoice.y
#this is stage 2

############################################################################

#NOTE: keep in mind that inrange true/false WILL have diff path finding problems

############################################################################
            if InRange is False: #ally not in range, this is supposed to find closest, i think it works

                
                low_abso = 200
                for item in ally_sprites:
                    test_x,test_y=item.x,item.y

                    enemy_x,enemy_y = EnemyChoice.x,EnemyChoice.y

                    #

                    abso_x = abs(abs(test_x)-abs(enemy_x))
                    abso_y = abs(abs(test_y)-abs(enemy_y))

                    new_abso = abso_x+abso_y #total move


                    if new_abso < low_abso:
                        AllyToAttack = item
                       # print "this is the cheaper way"
                        low_abso = new_abso

                ################### trying transition rn ############


                matrix = []
                for row in range(mapheight):
                    new_row = []
                    for column in range(mapwidth):
                        if blueredmap[row][column] == 0:
                            new_row.append(1)
                        else:
                           new_row.append(0)
                    matrix.append(new_row)
                #i typeihnk
                ally_at_x,ally_at_y=(AllyToAttack.x,AllyToAttack.y)


                    
                #begin pathfinding program############################################

                y1 = EnemyChoice.y
                x1 = EnemyChoice.x
                move1 = EnemyChoice.move
                free_space_list = []
                

                #setup enemies as 0s (1 means free sapce, 0 means occupied)
                for item in ally_sprites_no_edit:
                    if item.hppart > 0:
                        matrix[item.y][item.x] = 0

                matrix[ally_at_y][ally_at_x] = 1

                grid_pathfind = Grid(matrix=matrix)

                start = grid_pathfind.node(x1,y1)
                end = grid_pathfind.node(ally_at_x,ally_at_y)

                finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
                path, runs = finder.find_path(start, end, grid_pathfind)

                
#                path = path[1:]
                #print x1,y1,ally_at_x,ally_at_y
                path=path[:(move1+2)]
                #print len(path), "test1"
                
                #del path[-1]#should e last item in path

                #
                """
                print "path[-1:]"
                for item in enemy_sprites_no_edit:
                    print path[-1:]
                    if (path[-1:])==(item.y,item.x):
                        print "at same location"
                """
                #print path[-2],"fu" #gives as (y,x)
                for item in enemy_sprites_no_edit:
                    #print path[-2]
                    try:
                        if (path[-2])==(item.x,item.y):
                            #print "EERRRRROOOOOORRRRRRRR" #FUCK YAAAAA IT WORKED
                            path=path[:-1]
                            
                    except IndexError:
                        print "error type 03"
                        
                
                for item in path:
                    free_space_list2.append((item[1],item[0]))

                EnemyChoice.path=[path]

                #



            elif InRange is True:

               

                        


                ###################################################################################################################################

                coouunntt = 0
                ally_sprites.empty()
                for item in ally_sprites_no_edit:
                    if item.hppart > 0:
                        coouunntt += 1
                        ally_sprites.add(item)


                    
                matrix = []
                for row in range(mapheight):
                    new_row = []
                    for column in range(mapwidth):
                        if blueredmap[row][column] == 0:
                            new_row.append(1)
                        else:
                           new_row.append(0)
                    matrix.append(new_row)
                    

                        
                #begin pathfinding program############################################


                #initiate required info
                y1 = EnemyChoice.y
                x1 = EnemyChoice.x
                move1 = EnemyChoice.move
                free_space_list2 = []

                #i think
                ally_at_x,ally_at_y=(AllyToAttack.x,AllyToAttack.y)

                #setup enemies as 0s (1 means free sapce, 0 means occupied)
                for item in ally_sprites_no_edit:
                    matrix[item.y][item.x] = 0

                #CANNOT DELETE THIS FOR SOME FUCKED UP REASON. FUCKKKKKKKK!!!!!!!!!!
                matrix[AllyToAttack.y][AllyToAttack.x] = 1

                grid_pathfind = Grid(matrix=matrix)

                start = grid_pathfind.node(x1,y1)
                end = grid_pathfind.node(AllyToAttack.x,AllyToAttack.y)

                finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
                path, runs = finder.find_path(start, end, grid_pathfind)


                #path = path[:-1]
                #delete start position
                #path = path[1:]


                path=path[:(move1+2)]

                print path, path[-2]

                newTempList3=[]
                for item in enemy_sprites_no_edit:
                    if (item.x,item.y)!=(x1,y1):
                        newTempList3.append((item.x,item.y))
                try:    
                    while path[-2] in newTempList3:
                        path=path[:-1]
                        print "new ",path, path[-2]

                
                        
                    
                except IndexError:
                    pass
                #
                """
                print "path[-2:][0],",path[-2:][0]
                for item in enemy_sprites_no_edit:
                    print (item.y,item.x)
                    if (path[-2:][0])==(item.y,item.x):
                        print "at same location"
                """
    




                #

                for item in path:
                    free_space_list2.append((item[1],item[0]))

                EnemyChoice.path=path


            DoOnceForTheirTurn = False

        
        #print AllyToAttack.name, "ally to attack",str(len(path)), "path length",EnemyChoice.name,"enemy name",path
                    

########################
###########################
########################
        """
        free_space_list=[]
        for item in path:
            free_space_list.append((item[1],item[0])) #this order keeps free space list as (y,x)
        """

        for item in ally_sprites:
            if (item.y,item.x) in free_space_list2:
                free_space_list2.remove((item.y,item.x))


                    #
                    


                    #OutOfRangeEnemy = False

        #print len(free_space_list), "LENGTH"
        free_space_list2 = free_space_list2[:5]
        #print len(free_space_list), "LENGTH"
       # print "next"

        #screen.blit(greenoccupy,(EnemyChoice.x*tilesize,EnemyChoice.y*tilesize))

        if timer > 0 and timer < 60:       
            #for item in free_space_list:
                #screen.blit(blueTile,(item[0]*tilesize,item[1]*tilesize))
                #screen.blit(MOVING_TRANSPARENCY, (EnemyChoice.x*tilesize,EnemyChoice.y*tilesize))


        #
            try:
                lastEnemyPos=(path[0][1],path[0][0])

                
                #print len(path)
                timer=3
                speedd=3
                
                if EnemyChoice.rect.y == (path[0][1]*tilesize):#x stays the same
                    if (EnemyChoice.rect.x)<(path[0][0]*tilesize):
                        EnemyChoice.rect.x += speedd
                       # print "plus x"

                        
                    elif (EnemyChoice.rect.x)>(path[0][0]*tilesize):
                        EnemyChoice.rect.x -= speedd
                        #print "minus x"

                        
                    else:
                        lastEnemyPos=(path[0][1],path[0][0])
                        path=path[1:]
                        #think i need t update the enmy.x, enemy.y etc
                        EnemyChoice.x=path[1][0]#should mean next item on path and the x

                elif EnemyChoice.rect.x == (path[0][0]*tilesize):
                    #print "here2"

                    if (EnemyChoice.rect.y)<(path[0][1]*tilesize):
                        EnemyChoice.rect.y += speedd
                      # print "plus y"
                        
                    elif (EnemyChoice.rect.y)>(path[0][1]*tilesize):
                        EnemyChoice.rect.y -= speedd
                        #print "plus x"
                        
                    else:
                        lastEnemyPos=(path[0][1],path[0][0])
                        EnemyChoice.path=path[1:]
                        
                        EnemyChoice.y=path[1][1]

            except IndexError:
                testme3=True
                timer=61
                EnemyChoice.x,EnemyChoice.y=(lastEnemyPos[1],lastEnemyPos[0])
                #print lastEnemyPos

        #



        #if 
        #if timer > 60 and timer < 120:

        if InRange is False and timer > 60:
            if (the_number_of_enemies_is) != (enemy_list_brackets_x+1):
                enemy_list_brackets_x += 1
                #grey out below
                #print "grey me"
                EnemyChoice.picture=EnemyChoice.backup_grey
                timer = 0
                FindOut = False
                SubtractDamage = False
                DoOnceForTheirTurn = True

            else:
                PlayerSignCount = 0
                PlayerPhaseDisplay = True
                PlayerCountStart = True
                DoOnceForTheirTurn = True
                TheirTurn = False

                for item in enemy_sprites_no_edit:
                    item.picture=item.backup_normal

                TurnNumber += 1

                qqq = 0
                qq = 0
                timer = 0
                FindOut = False
                SubtractDamage = False
                enemy_list_brackets_x = 0

                mov_x, mov_y = marth_to_move.x,marth_to_move.y

                ally_sprites.empty()
                for item in ally_sprites_no_edit:
                    ally_sprites.add(item)

                        
        elif InRange is True:
            
            if timer > 60 and timer < 100:
                screen.blit(redTile,(ally_at_x*tilesize,ally_at_y*tilesize))

                PlayerToBeAttacked=AllyToAttack
                    
                if AllyToAttack.weapon == 'Axe':
                    add_dmg_me = 6
                elif AllyToAttack.weapon == 'Lance':
                    add_dmg_me = 6
                elif AllyToAttack.weapon == 'Bow':
                    add_dmg_me = 5
                elif AllyToAttack.weapon == 'Sword':
                    add_dmg_me = 5
                elif AllyToAttack.weapon == 'Dagger':
                    add_dmg_me = 4
                else:
                    add_dmg_me = 4


                if EnemyChoice.weapon == 'Axe':
                    add_dmg_them = 6
                elif EnemyChoice.weapon == 'Lance':
                    add_dmg_them = 6
                elif EnemyChoice.weapon == 'Bow':
                    add_dmg_them = 5
                elif EnemyChoice.weapon == 'Sword':
                    add_dmg_them = 5
                elif EnemyChoice.weapon == 'Dagger':
                    add_dmg_them = 4
                else:
                    add_dmg_them = 4

            #####################################################################

                attack_me = int(int(add_dmg_me) + PlayerToBeAttacked.strength)            
                critical_me = int(((int(PlayerToBeAttacked.luck) + int(PlayerToBeAttacked.speed)))/2)
                hit_me = str(int(2*int(PlayerToBeAttacked.skill)) + int(PlayerToBeAttacked.speed))
                speed_me = str(((1/2) * int(PlayerToBeAttacked.skill)) + int(PlayerToBeAttacked.luck))

                attack_them = int(int(add_dmg_them) + EnemyChoice.strength)            
                critical_them = int(((int(EnemyChoice.luck) + int(EnemyChoice.speed)))/2)
                hit_them = str(int(2*int(EnemyChoice.skill)) + int(EnemyChoice.speed))
                speed_them = str(((1/2) * int(EnemyChoice.skill)) + int(EnemyChoice.luck))

########################################################################################################################################################3
############################################################################################################################################################

                calculate_values(AllyToAttack)
                        
                ally_damage = calculate_values.damage
                ally_critical = calculate_values.critical
                ally_hit_percentage = calculate_values.hit_precentage
                ally_avoid = calculate_values.avoid
                ally_weapon_dmg = calculate_values.weapon_dmg
                ally_total_defense = calculate_values.combined_defense

                calculate_values(EnemyChoice)
                    
                enemy_damage = calculate_values.damage
                enemy_critical = calculate_values.critical
                enemy_hit_percentage = calculate_values.hit_precentage
                enemy_avoid = calculate_values.avoid
                enemy_weapon_dmg = calculate_values.weapon_dmg
                enemy_total_defense = calculate_values.combined_defense


                list_for_ally_hit = []
                hit_ally = (ally_hit_percentage - enemy_avoid)

                for i in range(0,hit_ally):
                    list_for_ally_hit.append(1)
                for i in range(0,(100-hit_ally)):
                    list_for_ally_hit.append(0)
                choice = random.choice(list_for_ally_hit)

                if choice == 0:
                    Hit_Ally = False
                elif choice == 1:
                    Hit_Ally = True
                #
                list_for_enemy_hit = []
                hit_enemy = (enemy_hit_percentage - ally_avoid)

                for i in range(0,hit_enemy):
                    list_for_enemy_hit.append(1)
                for i in range(0,(100-hit_enemy)):
                    list_for_enemy_hit.append(0)
                choice = random.choice(list_for_enemy_hit)

                if choice == 0:
                    Hit_Enemy = False
                elif choice == 1:
                    Hit_Enemy = True

                ##
                
                ##


                attack_ally = int(ally_damage) - int(enemy_total_defense)
                #if MoveWho.rang == item.rang:
                attack_enemy = int(enemy_damage) - int(ally_total_defense)
                                                    

                if PlayerToBeAttacked.rang == EnemyChoice.rang:
                    check_attack_ally = attack_ally
                    check_ally_hit_percentage = hit_ally
                    check_ally_critical = ally_critical
                else:
                    check_attack_ally = "-"
                    check_ally_hit_percentage = "-"
                    check_ally_critical = "-"
########################################################################################################################################################3
########################################################################################################################################################3



            if timer > 100 and timer < 131:
                """
                for player in ally_sprites:
                    if (player.y,player.x) == (ally_at_y,ally_at_x):
                        PlayerToBeAttacked = player
                        break
                """
###################################################################################################################################
                #get diretion--> EnemyChoice and  AllyToAttack
                if EnemyChoice.rang ==1:
                    if EnemyChoice.x < PlayerToBeAttacked.x:
                        move_direction=(1,0)#x speed then y
                    elif EnemyChoice.x > PlayerToBeAttacked.x:
                        move_direction=(-1,0)
                    elif EnemyChoice.y < PlayerToBeAttacked.y:
                        move_direction=(0,1)
                    elif EnemyChoice.y > PlayerToBeAttacked.y:
                        move_direction=(0,-1)

                    #print move_direction

                    #print count33, "mycount"
                    if timer <= 115:
                        EnemyChoice.rect.x+=move_direction[0]
                        EnemyChoice.rect.y+=move_direction[1]
                    else:
                        EnemyChoice.rect.x-=move_direction[0]
                        EnemyChoice.rect.y-=move_direction[1]

                    if timer == 115:
                        if Hit_Enemy is True:
                            if (int(enemy_damage) - int(ally_total_defense)) < 0:
                                PlayerToBeAttacked.hppart += 0
                            else:
                                PlayerToBeAttacked.hppart -= (int(enemy_damage) - int(ally_total_defense))
                    
                if Hit_Enemy is True:
                    pygame.draw.circle(screen,(255,255,255),(PlayerToBeAttacked.x*tilesize+15,PlayerToBeAttacked.y*tilesize+15),10,0)
                    Text = FontTiny.render(("-"+str(attack_enemy)), 1, blue2)
                    screen.blit(Text, (((PlayerToBeAttacked.x*tilesize)+(5)),((PlayerToBeAttacked.y*tilesize)+(10))))
                elif Hit_Enemy is False:
                    pygame.draw.circle(screen,(255,255,255),(PlayerToBeAttacked.x*tilesize+15,PlayerToBeAttacked.y*tilesize+15),10,0)
                    Text = FontTiny2.render("Miss", 1, blue2)
                    screen.blit(Text, (((PlayerToBeAttacked.x*tilesize)+(5)),((PlayerToBeAttacked.y*tilesize)+(10))))

            if timer >= 131 and timer < 161:

                if PlayerToBeAttacked.rang ==1 and EnemyChoice.rang == PlayerToBeAttacked.rang:
                    if EnemyChoice.x < PlayerToBeAttacked.x:
                        move_direction=(1,0)#x speed then y
                    elif EnemyChoice.x > PlayerToBeAttacked.x:
                        move_direction=(-1,0)
                    elif EnemyChoice.y < PlayerToBeAttacked.y:
                        move_direction=(0,1)
                    elif EnemyChoice.y > PlayerToBeAttacked.y:
                        move_direction=(0,-1)

                    #print move_direction

                    #print count33, "mycount"
                    if timer < 146:
                        PlayerToBeAttacked.rect.x-=move_direction[0]
                        PlayerToBeAttacked.rect.y-=move_direction[1]
                    else:
                        PlayerToBeAttacked.rect.x+=move_direction[0]
                        PlayerToBeAttacked.rect.y+=move_direction[1]

                    if timer == 146:
                        if Hit_Ally is True:
                            if EnemyChoice.hppart > int(0):
                                if PlayerToBeAttacked.rang == EnemyChoice.rang:
                                    if (int(ally_damage) - int(enemy_total_defense)) < 0:
                                        EnemyChoice.hppart += 0
                                    else:
                                        EnemyChoice.hppart -= int(int(ally_damage) - int(enemy_total_defense))
                           # else:
                                #EnemyChoice.xp += 50

                        
                if Hit_Ally is True:
                    if PlayerToBeAttacked.hppart > 0 and EnemyChoice.rang == PlayerToBeAttacked.rang:
                        pygame.draw.circle(screen,(255,255,255),(EnemyChoice.x*tilesize+15,EnemyChoice.y*tilesize+15),10,0)
                        Text = FontTiny.render(("-"+str(attack_ally)), 1, red2)
                        screen.blit(Text, (((EnemyChoice.x*tilesize)+(5)),((EnemyChoice.y*tilesize)+(10))))
                elif Hit_Ally is False:
                    if PlayerToBeAttacked.hppart > 0 and EnemyChoice.rang == PlayerToBeAttacked.rang:
                        pygame.draw.circle(screen,(255,255,255),(EnemyChoice.x*tilesize+15,EnemyChoice.y*tilesize+15),10,0)
                        Text = FontTiny2.render("Miss", 1, red2)
                        screen.blit(Text, (((EnemyChoice.x*tilesize)+(5)),((EnemyChoice.y*tilesize)+(10))))
                #print WhoEnemy.rect
            elif timer == 162:
                EnemyChoice.picture = EnemyChoice.backup_grey


                if (the_number_of_enemies_is) != (enemy_list_brackets_x+1):
                    enemy_list_brackets_x += 1
                    timer = 0
                    FindOut = False
                    SubtractDamage = False
                    DoOnceForTheirTurn = True

                else:
                    PlayerSignCount = 0
                    PlayerPhaseDisplay = True
                    PlayerCountStart = True
                    DoOnceForTheirTurn = True
                    TheirTurn = False

                    for item in enemy_sprites_no_edit:
                        item.picture=item.backup_normal

                    TurnNumber += 1

                    qqq = 0
                    qq = 0
                    timer = 0
                    FindOut = False
                    SubtractDamage = False
                    enemy_list_brackets_x = 0

                    mov_x, mov_y = marth_to_move.x,marth_to_move.y

                    ally_sprites.empty()
                    for item in ally_sprites_no_edit:
                        ally_sprites.add(item)


    elif TheirTurn is True and len(enemy_sprites_no_edit)==0:
        print "enemy all dead"
        PlayerSignCount = 0
        PlayerPhaseDisplay = True
        PlayerCountStart = True
        DoOnceForTheirTurn = True
        TheirTurn = False

        for item in enemy_sprites_no_edit:
            item.picture=item.backup_normal

        TurnNumber += 1

        qqq = 0
        qq = 0
        timer = 0
        FindOut = False
        SubtractDamage = False
        enemy_list_brackets_x = 0

        mov_x, mov_y = marth_to_move.x,marth_to_move.y

        ally_sprites.empty()
        for item in ally_sprites_no_edit:
            ally_sprites.add(item)

##################################################################################

    


    if MyTurn is True:


 
      
        if ShowMap is True:
            grid = [x[:] for x in blueredmap]

            for item in enemy_sprites:
                if item.hppart < 0:
                    enemy_sprites.remove(item)
                    all_sprites.remove(item)
            for item in enemy_sprites_no_edit:
                if item.hppart < 0:
                    enemy_sprites_no_edit.remove(item)
                    all_sprites.remove(item)
                    
            for item in enemy_sprites_no_edit:#think i fixed it, fuck it didnt work- where else would this happen, check with print to see if @ right part
                if item.hppart > 0:
                    grid[item.y][item.x] = 1
                    
            if Done is False:
                #print 
                free_space_list = []
                second_new_player_list = []
                third_new_player_list = []

                
                y1 = MoveWho.y
                x1 = MoveWho.x
                move1 = MoveWho.move
                new_player_list = [(y1,x1)]

             

                show_map(new_player_list, second_new_player_list)

                for i in range((move1-1)):
                    show_map(second_new_player_list, third_new_player_list)
                    
                    second_new_player_list = []
                    
                    for item in third_new_player_list:
                        second_new_player_list.append(item)
                #for item in enemy_sprites_no_edit:
                    #print "enemy rect",item.rect.x/tilesize,item.rect.y/tilesize,"enemy x y",item.x,item.y
                #
                
                #
                
                for item in ally_sprites_no_edit:
                    if (item.y,item.x) in free_space_list:
                        free_space_list.remove((item.y,item.x))

                #why was is it not doing anything
                #Done = True
                
                #for item in free_space_list:
                    #print item, "x,y free"
                #print "INT", int(-1)


                for i in range(150):
                    for item in free_space_list:
                        x_test,y_test=(float(item[0]),float(item[1]))
                        #print y_test
                        
                        if x_test < int(0) or x_test > mapwidth:
                            #print "remove2"
                            free_space_list.remove(item)
                        if y_test < int(0) or y_test > mapheight:
                            #print "remove1"
                            free_space_list.remove(item)
                        
                
                #for item in free_space_list:
                    #print item, "x,y free"
                
                #[x for x in a if x >= 0 ]
                myRedList=[]
                if MoveWho.rang==1:
                    for item in free_space_list:
                        if ((item[0]+1),item[1]) not in free_space_list and ((item[0]+1),item[1]) not in myRedList:
                            myRedList.append((item[0]+1,item[1]))
                            
                        #elif ((item[1]+1),item[0]) not in myRedList:
                            #blah=""

                        if ((item[0]-1),item[1]) not in free_space_list and ((item[0])-1,item[1]) not in myRedList:
                            myRedList.append((item[0]-1,item[1]))
                        #elif ((item[1]-1),item[0]) not in myRedList:
                            #myRedList.append((item[1]-1,item[0]))

                        if ((item[0]),item[1]+1) not in free_space_list and ((item[0]),item[1]+1) not in myRedList:
                            myRedList.append((item[0],item[1]+1))
                        #elif ((item[1]),item[0]+1) not in myRedList:
                            #myRedList.append((item[1],item[0]+1))

                        if ((item[0]),item[1]-1) not in free_space_list and ((item[0]),item[1]-1) not in myRedList:
                            myRedList.append((item[0],item[1]-1))
                        #elif ((item[1]),item[0]-1) not in myRedList:
                            #myRedList.append((item[1],item[0]-1))
                if MoveWho.rang==1.5 or MoveWho.rang==2:
                    for item in free_space_list:
                        #print item, "should be free sapce y then x"


                        if ((item[0]),item[1]-1) not in free_space_list and ((item[0]),item[1]-1) not in myRedList:
                            myRedList.append((item[0],item[1]-1))
                        if ((item[0]-1),item[1]) not in free_space_list and ((item[0])-1,item[1]) not in myRedList:
                            myRedList.append((item[0]-1,item[1]))
                        if (item[0],item[1]+1) not in free_space_list and (item[0],item[1]+1) not in myRedList:
                            myRedList.append((item[0],item[1]+1))
                        if ((item[0]+1),item[1]) not in free_space_list and ((item[0]+1),item[1]) not in myRedList:
                            myRedList.append((item[0]+1,item[1]))

                        if ((item[0]+2),item[1]) not in free_space_list and ((item[0])+2,item[1]) not in myRedList:
                            myRedList.append((item[0]+2,item[1]))
                        if ((item[0]-2),item[1]) not in free_space_list and ((item[0])-2,item[1]) not in myRedList:
                            myRedList.append((item[0]-2,item[1]))
                        if ((item[0]),item[1]+2) not in free_space_list and ((item[0]),item[1]+2) not in myRedList:
                            myRedList.append((item[0],item[1]+2))
                        if ((item[0]),item[1]-2) not in free_space_list and ((item[0]),item[1]-2) not in myRedList:
                            myRedList.append((item[0],item[1]-2))

                        if ((item[0])-1,item[1]-1) not in free_space_list and ((item[0])-1,item[1]-1) not in myRedList:
                            myRedList.append((item[0]-1,item[1]-1))
                        if ((item[0]-1),item[1]+1) not in free_space_list and ((item[0])-1,item[1]+1) not in myRedList:
                            myRedList.append((item[0]-1,item[1]+1))
                        if ((item[0])+1,item[1]+1) not in free_space_list and ((item[0])+1,item[1]+1) not in myRedList:
                            myRedList.append((item[0]+1,item[1]+1))
                        if ((item[0])+1,item[1]-1) not in free_space_list and ((item[0])+1,item[1]-1) not in myRedList:
                            myRedList.append((item[0]+1,item[1]-1))

                



                for item in myRedList:
                    if item[0] < 0 or item[1] < 0:
                        #print "remove red"
                        myRedList.remove(item)

                while (MoveWho.y,MoveWho.x) in myRedList:
                    myRedList.remove((MoveWho.y,MoveWho.x))

                    


                Done = True

                

            
            
            for item in myRedList:
                screen.blit(redTile1,(item[1]*tilesize,item[0]*tilesize))

            for item in free_space_list:
                    #print item[1], item[0]
                screen.blit(blueTile,(item[1]*tilesize,item[0]*tilesize))

      #  if DisplayAttackInfo is True:
          #  for item in EnemiesYouCanAttack:
            #    notagoodsign = "why is nothing actually being done here?"

        if UnmovePlayer is True:
            one = previousPlayerPos[0]
            two = previousPlayerPos[1]
            
            MoveWho.x = one
            MoveWho.y = two
            MoveWho.rect.x=one*tilesize
            MoveWho.rect.y=two*tilesize

            UnmovePlayer = False


        #If my turn is over
        #print len(ally_sprites)
        if len(ally_sprites) == 0 and MyTurn is True:
            print "hereeee boy"
            
            for item in ally_sprites_no_edit:
                ally_sprites.add(item)

            EnemySignCount = 0
            EnemyPhaseDisplay = True
            EnemyCountStart = True

            MyTurn = False
            
            enemy_sprites_no_edit.empty()
            
            for item in enemy_sprites:
                if item.hppart > 0:
                    enemy_sprites_no_edit.add(item)

        

        
                
        
            
            
        if DisplayMoveOrAttackOptions is True:
            
            if MoveWho.rang == 1:
                screen.blit(redTile, ((MoveWho.x-MoveWho.rang)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x+MoveWho.rang)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y-MoveWho.rang)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y+MoveWho.rang)*tilesize))

                maybe_enemies_in_range = []
                for item in enemy_sprites:
                    if ((MoveWho.x-MoveWho.rang),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x+MoveWho.rang),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y+MoveWho.rang)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y-MoveWho.rang)) == (item.x,item.y):
                        maybe_enemies_in_range.append(item)
                
            elif MoveWho.rang == 2:
                screen.blit(redTile, ((MoveWho.x-MoveWho.rang)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x+MoveWho.rang)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y-MoveWho.rang)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y+MoveWho.rang)*tilesize))
                screen.blit(redTile, ((MoveWho.x-1)*tilesize,(MoveWho.y-1)*tilesize))
                screen.blit(redTile, ((MoveWho.x+1)*tilesize,(MoveWho.y+1)*tilesize))
                screen.blit(redTile, ((MoveWho.x-1)*tilesize,(MoveWho.y+1)*tilesize))
                screen.blit(redTile, ((MoveWho.x+1)*tilesize,(MoveWho.y-1)*tilesize))

                maybe_enemies_in_range = []
                           
                for item in enemy_sprites:
                    if ((MoveWho.x-1),(MoveWho.y+1)) == (item.x,item.y) or ((MoveWho.x+1),(MoveWho.y+1)) == (item.x,item.y) or ((MoveWho.x+1),(MoveWho.y-1)) == (item.x,item.y) or ((MoveWho.x-1),(MoveWho.y-1)) == (item.x,item.y):
                        maybe_enemies_in_range.append(item)
                    if ((MoveWho.x-MoveWho.rang),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x+MoveWho.rang),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y-MoveWho.rang)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y+MoveWho.rang)) == (item.x,item.y):
                        maybe_enemies_in_range.append(item)
            #
            elif MoveWho.rang == 1.5:
                screen.blit(redTile, ((MoveWho.x-1)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x+1)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y-1)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y+1)*tilesize))
                
                screen.blit(redTile, ((MoveWho.x-2)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x+2)*tilesize,(MoveWho.y)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y-2)*tilesize))
                screen.blit(redTile, ((MoveWho.x)*tilesize,(MoveWho.y+2)*tilesize))
                screen.blit(redTile, ((MoveWho.x-1)*tilesize,(MoveWho.y-1)*tilesize))
                screen.blit(redTile, ((MoveWho.x+1)*tilesize,(MoveWho.y+1)*tilesize))
                screen.blit(redTile, ((MoveWho.x-1)*tilesize,(MoveWho.y+1)*tilesize))
                screen.blit(redTile, ((MoveWho.x+1)*tilesize,(MoveWho.y-1)*tilesize))

                maybe_enemies_in_range = []
                           
                for item in enemy_sprites:
                    if ((MoveWho.x-1),(MoveWho.y+1)) == (item.x,item.y) or ((MoveWho.x+1),(MoveWho.y+1)) == (item.x,item.y) or ((MoveWho.x+1),(MoveWho.y-1)) == (item.x,item.y) or ((MoveWho.x-1),(MoveWho.y-1)) == (item.x,item.y):
                        maybe_enemies_in_range.append(item)
                    if ((MoveWho.x-2),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x+2),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y-2)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y+2)) == (item.x,item.y):
                        maybe_enemies_in_range.append(item)
                    if ((MoveWho.x-2),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x+2),(MoveWho.y)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y+2)) == (item.x,item.y) or ((MoveWho.x),(MoveWho.y-2)) == (item.x,item.y):
                        maybe_enemies_in_range.append(item)

            #

            if maybe_enemies_in_range == []:
                DisplayQ = False
            else:
                DisplayQ = True
                
            if MoveWho.rang == 1:
                adds  = 60
            elif MoveWho.rang == 2:
                adds = 90
            elif MoveWho.rang == 1.5:
                adds = 90
                
            if (MoveWho.y,MoveWho.x) != (11,1):
                
                if DisplayQ is True:
                    pygame.draw.rect(screen, grey, ((MoveWho.x*tilesize+adds),(MoveWho.y*tilesize),75,40))
                    
                    Text = FontSmall.render("[Q] Attack", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+adds+2),(MoveWho.y*tilesize+3)))
                    Text = FontSmall.render("[E] Wait", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+adds+2),(MoveWho.y*tilesize+20+3)))

                    CanAttack = True
                else:
                    pygame.draw.rect(screen, grey, ((MoveWho.x*tilesize+adds),(MoveWho.y*tilesize),75,20))
                    
                    Text = FontSmall.render("[E] Wait", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+adds+2),(MoveWho.y*tilesize+3)))

                    CanAttack = False
            else:
                pygame.draw.rect(screen, grey, ((MoveWho.x*tilesize+adds),(MoveWho.y*tilesize),75,20)) 
                Text = FontSmall.render("[W] Seize", 1, white)
                screen.blit(Text, ((MoveWho.x*tilesize+adds+2),(MoveWho.y*tilesize+3)))

                Seize = True
                
        screen.blit(MOVING_TRANSPARENCY, (mov_x*tilesize,mov_y*tilesize))

        if InfoSelect is True:
            for item in all_sprites:
                if (mov_x,mov_y) == (item.x,item.y) and item.hppart > 0:
                    print item.name
                    InfoSelected(item,item.backup_normal,item.name,item.clas,item.race,item.level,item.xp,item.hppart,item.hpfull,item.strength,item.skill,item.speed,item.luck,item.defense,item.resistance,item.weapon,item.move,item.rang,item.x,item.y)
                    DoNotDisplay = True
        else:
            DoNotDisplay = False

        if DisplayWhoToAttack is True:
            MOVING_TRANSPARENCY = MOV2

            DisplayMoveOrAttackOptions = False
            
            n = 0
            for item in maybe_enemies_in_range:
                n += 1

                if (mov_x,mov_y) == (item.x,item.y):
                    pygame.draw.rect(screen, tan, ((MoveWho.x*tilesize+100),(0*tilesize),300,405))
                    
                    pygame.draw.rect(screen, tan3, ((MoveWho.x*tilesize+107),(0*tilesize+7),139,75))
                    pygame.draw.rect(screen, tan3, ((MoveWho.x*tilesize+253),(0*tilesize+7),139,75))
                    
                    pygame.draw.rect(screen, dark_blue, ((MoveWho.x*tilesize+107),(0*tilesize+89),98,265))
                    pygame.draw.rect(screen, red, ((MoveWho.x*tilesize+293),(0*tilesize+89),98,265))

                    Text = Font3.render(MoveWho.name, 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+115),(0*tilesize+10)))

                    Text = Font3.render(item.name, 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+260),(0*tilesize+10)))


                    Text = Font1.render("HP", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+231),(0*tilesize+100)))

                    Text = Font1.render("ATK", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+220),(0*tilesize+165)))

                    Text = Font1.render("HIT", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+224),(0*tilesize+230)))

                    Text = Font1.render("CRIT", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+215),(0*tilesize+295)))

                    Text = Font1.render("[w] to confirm", 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+157),(0*tilesize+365)))
                    

                    if MoveWho.weapon == 'Axe':
                        add_dmg_me = 6
                    elif MoveWho.weapon == 'Lance':
                        add_dmg_me = 6
                    elif MoveWho.weapon == 'Bow':
                        add_dmg_me = 5
                    elif MoveWho.weapon == 'Sword':
                        add_dmg_me = 5
                    elif MoveWho.weapon == 'Dagger':
                        add_dmg_me = 4
                    elif MoveWho.weapon == 'Spear':
                        add_dmg_me = 4
                    elif MoveWho.weapon == 'Handaxe':
                        add_dmg_me = 6
                    else:
                        add_dmg_me = 4

                    if item.weapon == 'Axe':
                        add_dmg_them = 6
                    elif item.weapon == 'Lance':
                        add_dmg_them = 6
                    elif item.weapon == 'Bow':
                        add_dmg_them = 5
                    elif item.weapon == 'Sword':
                        add_dmg_them = 5
                    elif item.weapon == 'Dagger':
                        add_dmg_them = 4
                    elif item.weapon == 'Spear':
                        add_dmg_them = 4
                    elif item.weapon == 'Handaxe':
                        add_dmg_them = 6
                    else:
                        add_dmg_them = 4

                    

                    calculate_values(MoveWho)
                        
                    ally_damage = calculate_values.damage
                    ally_critical = calculate_values.critical
                    ally_hit_percentage = calculate_values.hit_precentage
                    ally_avoid = calculate_values.avoid
                    ally_weapon_dmg = calculate_values.weapon_dmg
                    ally_total_defense = calculate_values.combined_defense

                    calculate_values(item)
                        
                    enemy_damage = calculate_values.damage
                    enemy_critical = calculate_values.critical
                    enemy_hit_percentage = calculate_values.hit_precentage
                    enemy_avoid = calculate_values.avoid
                    enemy_weapon_dmg = calculate_values.weapon_dmg
                    enemy_total_defense = calculate_values.combined_defense


                    list_for_ally_hit = []
                    hit_ally = (ally_hit_percentage - enemy_avoid)

                    for i in range(0,hit_ally):
                        list_for_ally_hit.append(1)
                    for i in range(0,(100-hit_ally)):
                        list_for_ally_hit.append(0)
                    choice = random.choice(list_for_ally_hit)

                    if choice == 0:
                        Hit_Ally = False
                    elif choice == 1:
                        Hit_Ally = True
                    #
                    list_for_enemy_hit = []
                    hit_enemy = (enemy_hit_percentage - ally_avoid)

                    for i in range(0,hit_enemy):
                        list_for_enemy_hit.append(1)
                    for i in range(0,(100-hit_enemy)):
                        list_for_enemy_hit.append(0)
                    choice = random.choice(list_for_enemy_hit)

                    if choice == 0:
                        Hit_Enemy = False
                    elif choice == 1:
                        Hit_Enemy = True

                    ##
                    
                    ##


                    attack_ally = int(ally_damage) - int(enemy_total_defense)


                    if MoveWho.rang == item.rang:
                        attack_enemy = int(enemy_damage) - int(ally_total_defense)
                                                        

                    if MoveWho.rang == item.rang:
                        check_attack_enemy = attack_enemy
                        check_enemy_hit_percentage = hit_enemy
                        check_enemy_critical = enemy_critical
                    else:
                        check_attack_enemy = "-"
                        check_enemy_hit_percentage = "-"
                        check_enemy_critical = "-"
                        
                        


                    Text = Font2.render(MoveWho.weapon, 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+115),(0*tilesize+50)))

                    Text = Font2.render(item.weapon, 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+260),(0*tilesize+50)))
                    #hp
                    Text = Font1.render(str(MoveWho.hppart)+ " / " + str(MoveWho.hpfull), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+115),(0*tilesize+100)))

                    Text = Font1.render(str(item.hppart) + " / " + str(item.hpfull), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+298),(0*tilesize+100)))
                    #attack
                    Text = Font1.render(str(attack_ally), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+135),(0*tilesize+163)))

                    Text = Font1.render(str(check_attack_enemy), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+324),(0*tilesize+163)))
                    #hit
                    Text = Font1.render(str(hit_ally), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+135),(0*tilesize+230)))

                    Text = Font1.render(str(check_enemy_hit_percentage), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+324),(0*tilesize+230)))
                    #crit
                    Text = Font1.render(str(ally_critical), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+135),(0*tilesize+294)))

                    Text = Font1.render(str(check_enemy_critical), 1, white)
                    screen.blit(Text, ((MoveWho.x*tilesize+324),(0*tilesize+294)))


                    WhoEnemy = item

        else:
            MOVING_TRANSPARENCY = MOV1
    """   
    for item in ally_sprites_no_edit:
        if (mov_x,mov_y) == (item.x,item.y):
            Count333 = False
    """      
                    
    if Count333 is True:
        #print "count333 is hhheeeerrrr"
        
        """
        if Hit_Ally is True:
            if (int(ally_damage) - int(enemy_total_defense)) < 0:
                WhoEnemy.hppart += 0
            else:
                WhoEnemy.hppart -= (int(ally_damage) - int(enemy_total_defense))
                
        elif Hit_Ally is False:
            pygame.draw.circle(screen,(255,255,255),(WhoEnemy.x*tilesize+15,WhoEnemy.y*tilesize+15),10,0)
            Text = FontTiny2.render("Miss", 1, blue2)
            screen.blit(Text, (((WhoEnemy.x*tilesize)+(5)),((WhoEnemy.y*tilesize)+(10))))
            
        #else: need to display a miss


        if Hit_Enemy is True:
            if WhoEnemy.hppart > int(0):
                if MoveWho.rang == WhoEnemy.rang:
                    if (int(enemy_damage) - int(ally_total_defense)) < 0:
                        MoveWho.hppart += 0
                    else:
                        MoveWho.hppart -= int(int(enemy_damage) - int(ally_total_defense))
            else:
                MoveWho.xp += 50
                
        elif Hit_Enemy is False:
            if WhoEnemy.hppart > 0 and WhoEnemy.rang == MoveWho.rang:
                pygame.draw.circle(screen,(255,255,255),(MoveWho.x*tilesize+15,MoveWho.y*tilesize+15),10,0)
                Text = FontTiny2.render("Miss", 1, red2)
                screen.blit(Text, (((MoveWho.x*tilesize)+(5)),((MoveWho.y*tilesize)+(10))))
        """
        count33 += 1
        if count33 > 0 and count33 < 31:
            #get diretion
            if MoveWho.rang ==1:
                if MoveWho.x < WhoEnemy.x:
                    move_direction=(1,0)#x speed then y
                elif MoveWho.x > WhoEnemy.x:
                    move_direction=(-1,0)
                elif MoveWho.y < WhoEnemy.y:
                    move_direction=(0,1)
                elif MoveWho.y > WhoEnemy.y:
                    move_direction=(0,-1)

                #print move_direction

                #print count33, "mycount"
                if count33 <= 15:
                    MoveWho.rect.x+=move_direction[0]
                    MoveWho.rect.y+=move_direction[1]
                else:
                    MoveWho.rect.x-=move_direction[0]
                    MoveWho.rect.y-=move_direction[1]

            if count33 == 15:
                if Hit_Ally is True:
                    if (int(ally_damage) - int(enemy_total_defense)) < 0:
                        WhoEnemy.hppart += 0
                    else:
                        WhoEnemy.hppart -= (int(ally_damage) - int(enemy_total_defense))
            
            if Hit_Ally is True:
                pygame.draw.circle(screen,(255,255,255),(WhoEnemy.x*tilesize+15,WhoEnemy.y*tilesize+15),10,0)
                Text = FontTiny.render(("-"+str(attack_ally)), 1, blue2)
                screen.blit(Text, (((WhoEnemy.x*tilesize)+(5)),((WhoEnemy.y*tilesize)+(10))))
            elif Hit_Ally is False:
                pygame.draw.circle(screen,(255,255,255),(WhoEnemy.x*tilesize+15,WhoEnemy.y*tilesize+15),10,0)
                Text = FontTiny2.render("Miss", 1, blue2)
                screen.blit(Text, (((WhoEnemy.x*tilesize)+(5)),((WhoEnemy.y*tilesize)+(10))))

        if count33 >= 31 and count33 < 61:

            if WhoEnemy.rang ==1 and WhoEnemy.rang == MoveWho.rang:
                if WhoEnemy.x < MoveWho.x:
                    move_direction=(1,0)#x speed then y
                elif WhoEnemy.x > MoveWho.x:
                    move_direction=(-1,0)
                elif WhoEnemy.y < MoveWho.y:
                    move_direction=(0,1)
                elif WhoEnemy.y > MoveWho.y:
                    move_direction=(0,-1)

                #print move_direction

                #print count33, "mycount"
                if count33 < 46:
                    WhoEnemy.rect.x+=move_direction[0]
                    WhoEnemy.rect.y+=move_direction[1]
                else:
                    WhoEnemy.rect.x-=move_direction[0]
                    WhoEnemy.rect.y-=move_direction[1]

                if count33 == 46:
                    if Hit_Enemy is True:
                        if WhoEnemy.hppart > int(0):
                            if MoveWho.rang == WhoEnemy.rang:
                                if (int(enemy_damage) - int(ally_total_defense)) < 0:
                                    MoveWho.hppart += 0
                                else:
                                    MoveWho.hppart -= int(int(enemy_damage) - int(ally_total_defense))
                        else:
                            MoveWho.xp += 50

                    
            if Hit_Enemy is True:
                if WhoEnemy.hppart > 0 and WhoEnemy.rang == MoveWho.rang:
                    pygame.draw.circle(screen,(255,255,255),(MoveWho.x*tilesize+15,MoveWho.y*tilesize+15),10,0)
                    Text = FontTiny.render(("-"+str(attack_enemy)), 1, red2)
                    screen.blit(Text, (((MoveWho.x*tilesize)+(5)),((MoveWho.y*tilesize)+(10))))
            elif Hit_Enemy is False:
                if WhoEnemy.hppart > 0 and WhoEnemy.rang == MoveWho.rang:
                    pygame.draw.circle(screen,(255,255,255),(MoveWho.x*tilesize+15,MoveWho.y*tilesize+15),10,0)
                    Text = FontTiny2.render("Miss", 1, red2)
                    screen.blit(Text, (((MoveWho.x*tilesize)+(5)),((MoveWho.y*tilesize)+(10))))
            #print WhoEnemy.rect
        elif count33 == 62:
            MoveWho.picture = MoveWho.backup_grey
            DisplayWhoToAttack = False
            count33 = 0
            Count333 = False
            #print Count333, "made it here"
                    

    if PlayerPhaseDisplay is True:

        for item in ally_sprites_no_edit:
            if item.hppart > 0:
                #screen.blit((item.picture),(item.x*tilesize,item.y*tilesize))
                done = "done"
            else:
                ally_sprites_no_edit.remove(item)

        for item in enemy_sprites:
            if item.hppart > 0:
                done = "done"
                #screen.blit((item.picture),(item.x*tilesize,item.y*tilesize))

        screen.blit(PlayerPhase,(40,120))
        

    if EnemyPhaseDisplay is True:
            
        for item in ally_sprites_no_edit:
            if item.hppart > 0:
                #screen.blit((item.picture),(item.x*tilesize,item.y*tilesize))
                done = "done"
            else:
                ally_sprites.remove(item)

        

        screen.blit(EnemyPhase,(40,120))

   
    if DoNotDisplay is False:
        text2 = Font2.render(("Turn: " + str(TurnNumber)),True,(255,255,255))
        s2 = pygame.Surface((75,25))
        s2.fill(grey)
        s2.blit(text2,pygame.Rect(3,4,10,10))
        s2.set_alpha(500)
        screen.blit(s2,pygame.Rect(625,15,10,10))


        #print textures[tilemap[mov_y][mov_x]]
        if tilemap[mov_y][mov_x] == MNTS:
            tile = "Mountains"
            defense, resistance, avoid, heal = (10,0,15,0)
        elif tilemap[mov_y][mov_x] == DOCK or tilemap[mov_y][mov_x] == DOC2:
            tile = "Docks"
            defense, resistance, avoid, heal = (0,0,0,0)
        elif tilemap[mov_y][mov_x] == RDHO or tilemap[mov_y][mov_x] == RDVE or tilemap[mov_y][mov_x] == RDNE or tilemap[mov_y][mov_x] == RDSE or tilemap[mov_y][mov_x] == RDSW or tilemap[mov_y][mov_x] == RDNW or tilemap[mov_y][mov_x] == RDUP or tilemap[mov_y][mov_x] == RDLE or tilemap[mov_y][mov_x] == RDRI:
            tile = "Road"
            defense, resistance, avoid, heal = (0,0,0,0)
        elif tilemap[mov_y][mov_x] == SAND or tilemap[mov_y][mov_x] == SND2 or tilemap[mov_y][mov_x] == SND3 or tilemap[mov_y][mov_x] == SND4 or tilemap[mov_y][mov_x] == SND5 or tilemap[mov_y][mov_x] == SND6 or tilemap[mov_y][mov_x] == SND7 or tilemap[mov_y][mov_x] == SND8 or tilemap[mov_y][mov_x] == SND9:
            tile = "Sand"
            defense, resistance, avoid, heal = (0,10,0,0)
        elif tilemap[mov_y][mov_x] == POND:
            tile = "Pond"
            defense, resistance, avoid, heal = (0,0,10,0)
        elif tilemap[mov_y][mov_x] == WELL:
            tile = "Well"
            defense, resistance, avoid, heal = (5,0,5,0)
        elif tilemap[mov_y][mov_x] == FORT:
            tile = "Fort"
            defense, resistance, avoid, heal = (20,10,20,5)
        elif tilemap[mov_y][mov_x] == BOT1 or tilemap[mov_y][mov_x] == BOT2:
            tile = "Boat"
            defense, resistance, avoid, heal = (0,0,10,0)
        elif tilemap[mov_y][mov_x] == ARMY:
            tile = "Armory"
            defense, resistance, avoid, heal = (10,0,5,0)
        elif tilemap[mov_y][mov_x] == WATR:
            tile = "Water"
            defense, resistance, avoid, heal = (0,0,15,0)
        elif tilemap[mov_y][mov_x] == CSTL or tilemap[mov_y][mov_x] == CST2:
            tile = "Castle"
            defense, resistance, avoid, heal = (10,0,5,0)
        elif tilemap[mov_y][mov_x] == HOUS:
            tile = "House"
            defense, resistance, avoid, heal = (10,0,5,0)
        elif tilemap[mov_y][mov_x] == GRAS:
            tile = "Grass"
            defense, resistance, avoid, heal = (0,0,0,0)
        elif tilemap[mov_y][mov_x] == WOOD:
            tile = "Woods"
            defense, resistance, avoid, heal = (10,0,10,0)
        else:
            tile = "fdfdf"
            defense, resistance, avoid, heal = (0,0,0,0)
 
        text1 = FontTiny.render("Tile",True,(255,255,255))
        text2 = FontSmall.render(str(tile),True,(255,255,255))
        
        text3 = FontTiny.render(("Def   " + str(defense)),True,(255,255,255))
        text4 = FontTiny.render(("Res  " + str(resistance)),True,(255,255,255))
        text5 = FontTiny.render(("Avo  " + str(avoid)),True,(255,255,255))
        text6 = FontTiny.render(("Heal " + str(heal)),True,(255,255,255))
        
        s2 = pygame.Surface((105,65))
        s2.fill(grey)
        #
        start_pic_x,start_pic_y=(mov_x*tilesize,mov_y*tilesize)
        adjusted_picture = gridMap
        #newadjusted_picture = pygame.transform.scale(adjusted_picture, (65,65))
        s2.blit(adjusted_picture,(4,4),(start_pic_x+1,start_pic_y+1,28,28))
        #
        #adjusted_picture = pygame.transform.scale(tilemap[mov_y][mov_x], (25,25))
        #s2.blit(adjusted_picture,(4,4))

        s2.blit(text1,pygame.Rect(38,4,10,10))
        s2.blit(text2,pygame.Rect(38,16,10,10))
        
        s2.blit(text3,pygame.Rect(5,35,10,10))
        s2.blit(text4,pygame.Rect(60,35,10,10))
        s2.blit(text5,pygame.Rect(5,50,10,10))
        s2.blit(text6,pygame.Rect(60,50,10,10))
        
        s2.set_alpha(500)
        screen.blit(s2,pygame.Rect(605,405,10,10))

        #

        text11 = FontSmall.render("Objective:",True,(255,255,255))
        text22 = FontSmall.render("Capture Throne",True,(255,255,255))

        
        s2 = pygame.Surface((120,40))
        s2.fill(grey)

        
        adjusted_picture = pygame.transform.scale(greenoccupy, (18,18))
        s2.blit(adjusted_picture,(74,3))


        s2.blit(text11,pygame.Rect(3,5,10,10))
        s2.blit(text22,pygame.Rect(3,23,10,10))
        
        s2.set_alpha(500)
        screen.blit(s2,pygame.Rect(15,425,10,10))

        #
    if GreyScreen is True:
        if widthh < (tilesize*mapwidth+10):
            widthh += 10
        else:
            done = "done"

            pygame.quit()
            sys.exit()
            

        pygame.draw.rect(screen, grey, (0,0,widthh,tilesize*mapheight))


    if displayOptions is True:
        print "my options are"

        #^^

        pygame.draw.rect(screen, grey, ((mov_x*tilesize+30),(mov_y*tilesize),92,20))
        Text = FontSmall.render("[E] End Turn", 1, white)
        screen.blit(Text, ((mov_x*tilesize+30+2),(mov_y*tilesize+3)))


    #if TheirTurn is True:
        #for item in lisst_LL:
            #pygame.draw.rect(screen,(15,222,15),(item[0]*tilesize,item[1]*tilesize,tilesize,tilesize))

    for item in ally_sprites:
        if item.hppart <= 0:
            ally_sprites.remove(item)
            ally_sprites_no_edit.remove(item)
            all_sprites.remove(item)
    for item in enemy_sprites:
        if item.hppart <= 0:
            enemy_sprites.remove(item)
            enemy_sprites_no_edit.remove(item)
            all_sprites.remove(item)
    for item in showEnemyMapList:
        if item.hppart <= 0:
            showEnemyMapList.remove(item)
    
    pygame.display.update()
    clock.tick(40)


    
