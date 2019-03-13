"""This game is similar to jepordy in that the user picks questions which are worth a certai number of points
and plays his/her partner until they win. The questions are randomly selected from a question bank.
NOTE all code was written by me. Not even a single chrachter was taken from online
"""
import pygame
import datetime # Still yet to do
from random import randint
from time import sleep
pygame.init()
#Colors in RGB format
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (4, 81, 17)
Red = (255, 0, 0)
Blue = (0,0,255)
Buttons = (46,130,150)
B1 = (46,132,255)
user = (45,46,48)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Jeopardy")
clock = pygame.time.Clock()

#All images used are uploded into python here

sounding = pygame.mixer.Sound("Sound1.wav")
sounding1 = pygame.mixer.Sound("halfhour.wav")
Background1 = pygame.image.load('Background1.jpg')
Background3 = pygame.image.load('Background3.jpg')
Background4 = pygame.image.load('Background4.jpg')
Background5 = pygame.image.load('Background5.jpg')
Background6 = pygame.image.load('Background6.jpg')
Background7 = pygame.image.load('Background7.jpg')
Background8 = pygame.image.load('Background8.jpg')
adgk = pygame.image.load('adjk.jpg')
qrto = pygame.image.load('qrto.jpg')
qrto1 = pygame.image.load('qrto1.jpg')
qrto2 = pygame.image.load('qrto2.jpg')
Text1241 = pygame.image.load('Text1241.png')
Background2 = pygame.image.load('a1456.jpg')
testing = pygame.image.load('Test.gif')
testing1 = pygame.image.load('Test1.png')
testing2 = pygame.image.load('Test2.jpg')
testing3 = pygame.image.load('Test3.jpg')
testing4 = pygame.image.load('Test4.jpg')
testing5 = pygame.image.load('Test5.jpg')
testing6 = pygame.image.load('Test6.jpg')
testing7 = pygame.image.load('Test7.jpg')
testing8 = pygame.image.load('Test8.jpg')
testing9 = pygame.image.load('Test9.jpg')
testing10 = pygame.image.load('Test10.jpg')
testing11 = pygame.image.load('Test11.jpg')
testing12 = pygame.image.load('Test12.jpg')
testing13 = pygame.image.load('Test13.jpg')
testing14 = pygame.image.load('Test14.jpg')
testing15 = pygame.image.load('Test15.jpg')
testing16 = pygame.image.load('Test16.jpg')
testing17 = pygame.image.load('Test17.jpg')
testing18 = pygame.image.load('Test18.jpg')
testing19 = pygame.image.load('Test19.jpg')
testing20 = pygame.image.load('Test20.jpg')
testing21 = pygame.image.load('Test21.jpg')
testing22 = pygame.image.load('Test22.jpg')
testing23 = pygame.image.load('Test23.jpg')
testing24 = pygame.image.load('Test24.jpg')
testing26 = pygame.image.load('Test26.jpg')
testing27 = pygame.image.load('Test27.jpg')
testing28 = pygame.image.load('Test28.jpg')
testing29 = pygame.image.load('Test29.jpg')
testing30 = pygame.image.load('Test30.jpg')
testing31 = pygame.image.load('Test31.jpg')
testing32 = pygame.image.load('Test32.jpg')
testing33 = pygame.image.load('Test33.jpg')
testing34 = pygame.image.load('Test34.jpg')
testing36 = pygame.image.load('Test36.png')
testing37 = pygame.image.load('Test37.jpg')
testing38 = pygame.image.load('Test38.jpg')
testing39 = pygame.image.load('Test39.jpg')
testing40 = pygame.image.load('Test40.jpg')
testing41 = pygame.image.load('Test41.jpg')
testing42 = pygame.image.load('Test42.jpg')
testing43 = pygame.image.load('Test43.jpg')
testing44 = pygame.image.load('Test44.png')
testing45 = pygame.image.load('Test45.gif')
testing46 = pygame.image.load('Test46.jpg')
testing47 = pygame.image.load('Test47.jpg')
testing48 = pygame.image.load('Test48.jpg')
testing49 = pygame.image.load('Test49.jpg')
testing50 = pygame.image.load('Test50.jpg')
testing51 = pygame.image.load('Test51.gif')
testing52 = pygame.image.load('Test52.jpg')
testing53 = pygame.image.load('Test53.jpg')
testing54 = pygame.image.load('Test54.jpg')
testing55 = pygame.image.load('Test55.jpg')
testing56 = pygame.image.load('Test56.jpg')
testing57 = pygame.image.load('Test57.jpg')
testing58 = pygame.image.load('Test58.jpg')
testing59 = pygame.image.load('Test59.gif')
testing60 = pygame.image.load('Test60.png')
testing61 = pygame.image.load('Test61.jpg')
testing62 = pygame.image.load('Test62.jpg')
testing63 = pygame.image.load('Test63.jpg')
testing64 = pygame.image.load('Test64.jpg')
testing65 = pygame.image.load('Test65.jpg')
testing66 = pygame.image.load('Test66.jpg')
testing67 = pygame.image.load('Test67.png')
testing68 = pygame.image.load('Test68.jpg')
testing69 = pygame.image.load('Test69.jpg')
testing70 = pygame.image.load('Test70.jpg')
testing1111 = pygame.image.load('Test1111.jpg')
testing1112 = pygame.image.load('Test1112.jpg')
testing1113 = pygame.image.load('Test1113.jpg')
testing1114 = pygame.image.load('Test1114.jpg')
testing1115 = pygame.image.load('Test1115.jpg')
testing71 = pygame.image.load('Test71.jpg')
testing72 = pygame.image.load('Test72.jpg')
testing73 = pygame.image.load('Test73.jpg')
testing74 = pygame.image.load('Test74.jpg')
testing75 = pygame.image.load('Test75.jpg')
testing76 = pygame.image.load('Test76.jpg')
testing77 = pygame.image.load('Test77.jpg')
testing78 = pygame.image.load('Test78.jpg')
testing79 = pygame.image.load('Test79.jpg')
testing80 = pygame.image.load('Test80.jpg')
testing81 = pygame.image.load('Test81.jpg')
testing82 = pygame.image.load('Test82.jpg')
testing83 = pygame.image.load('Test83.jpg')
testing84 = pygame.image.load('Test84.jpg')
testing85 = pygame.image.load('Test85.jpg')
testing1024 = pygame.image.load('Test1024.jpg')
testing101 = pygame.image.load('MC1.jpg')
testing102 = pygame.image.load('MC2.jpg')
testing103 = pygame.image.load('MC3.jpg')
testing104 = pygame.image.load('MC4.jpg')
testing106 = pygame.image.load('MC6.jpg')
testing107 = pygame.image.load('MC7.jpg')
testing108 = pygame.image.load('MC8.jpg')
testing109 = pygame.image.load('MC9.jpg')
testing110 = pygame.image.load('MC10.jpg')
testing111 = pygame.image.load('MC11.jpg')
testing112 = pygame.image.load('MC12.jpg')
testing113 = pygame.image.load('MC13.jpg')
testing114 = pygame.image.load('MC14.jpg')
testing115 = pygame.image.load('MC15.jpg')
testing116 = pygame.image.load('MC16.jpg')
testing117 = pygame.image.load('MC17.jpg')

alpha = True
foxtrot = True
beta = True
# These variable are changed to random values between 0-4 inorder to select randm question from the banks
v1 = None
v2 = None
v3 = None
v4 = None
v5 = None
v6 = None
v7 = None
v8 = None
v9 = None
v10 = None
v11 = None
v12 = None
v13 = None
v14 = None
v15 = None
v16 = None
v17 = None
v18 = None
v19 = None
v20 = None
v21 = None
v22 = None
v23 = None
v24 = None
v25 = None

#Used to control while loop
charlie = True
charlie1 = True
charlie2 = True
charlie3 = True
charlie4 = True
charlie5 = True
charlie6 = True
charlie7 = True
charlie8 = True
charlie9 = True
charlie10 = True
charlie12 = True
charlie13 = True
charlie14 = True
charlie15 = True
charlie16 = True
charlie17 = True
charlie18 = True
charlie19 = True
charlie20 = True
charlie21 = True
charlie22 = True
charlie23 = True
charlie24 = True

#Used to control while loop
golf = True

#Used to control while loop
hotel = True

#Used to control while loop
india = True

#Also used to control while loops
juliet = True
juliet1 = True
juliet2 = True
juliet3 = True
juliet4 = True
juliet5 = True
juliet6 = True
juliet7 = True
juliet8 = True
juliet9 = True
juliet10 = True
juliet11 = True
juliet12 = True
juliet13 = True
juliet14 = True
juliet15 = True
juliet16 = True
juliet17 = True
juliet18 = True
juliet19 = True
juliet20 = True
juliet21 = True
juliet22 = True
juliet23 = True
juliet24 = True

#Are used to Control While loops
kilo = True
kilo1 = True
kilo2 = True
kilo3 = True
kilo4 = True
kilo5 = True
kilo6 = True
kilo7 = True
kilo8 = True
kilo9 = True
kilo10 = True
kilo11 = True
kilo12 = True
kilo13 = True
kilo14 = True
kilo15 = True
kilo16 = True
kilo17 = True
kilo18 = True
kilo19 = True
kilo20 = True
kilo21 = True
kilo22 = True
kilo23 = True
kilo24 = True

#These variable are chnaged to false inorder the change the color of the boxes in Quick Play as well as to find who is next
c1 = True
c2 = True
c3 = True
c4 = True
c5 = True
c6 = True
c7 = True
c8 = True
c9 = True
c10 = True
c11 = True
c12 = True
c13 = True
c14 = True
c15 = True
c16 = True
c17 = True
c18 = True
c19 = True
c20 = True
c21 = True
c22 = True
c23 = True
c24 = True
c25 = True
c26 = True
c27 = True
c28 = True
c29 = True

#This empty dictionary is appended to inorder to calculate the following persons turn.
Zulu = []

# The len of the dictionary is stored into this variable
counter = None

#This variable is also used for a while loop later
echo = True

#These variables are used to control while loops
alpha1 = True
alpha0 = True
alpha1 = True
alpha2 = True
alpha3 = True
alpha4 = True
alpha5 = True
alpha6 = True
alpha7 = True
alpha8 = True
alpha9 = True
alpha10 = True
alpha11 = True
alpha12 = True
alpha13 = True
alpha14 = True
alpha15 = True
alpha16 = True
alpha17 = True
alpha18 = True
alpha19 = True
alpha20 = True
alpha21 = True
alpha22 = True
alpha23 = True
alpha24 = True
tanas = True

#These variables are also used to control while loops
golf1 = True
golf2 = True
golf3 = True
golf4 = True
golf5 = True
golf6 = True
golf6 = True
golf7 = True
golf8 = True
golf9 = True
golf10 = True
golf11 = True
golf13 = True
golf14 = True
golf15 = True
golf16 = True
golf17 = True
golf18 = True
golf19 = True
golf20 = True
golf21 = True
golf22 = True
golf23 = True
golf24 = True
finsihing = True

#This fuction checkes to see which variables are true inorder to know which player is next
def controllers():
	global c1
	global c2
	global c3
	global c4
	global c5
	global c6
	global c7
	global c8
	global c9
	global c10
	global c11
	global c12
	global c13
	global c14
	global c15
	global c16
	global c17
	global c18
	global c19
	global c20
	global c21
	global c22
	global c23
	global c24
	global c25
	global c26
	global c27
	global c28
	global c28
	global zulu
	global counter
	if c1 == False: 
		Zulu.append(c1)
	elif c2 == False: 
		Zulu.append(c2)
	elif c3 == False: 
		Zulu.append(c3)
	elif c4 == False: 
		Zulu.append(c4)
	elif c5 == False: 
		Zulu.append(c5)
	elif c6 == False: 
		Zulu.append(c6)
	elif c7 == False: 
		Zulu.append(c7)
	elif c8 == False: 
		Zulu.append(c8)
	elif c9 == False: 
		Zulu.append(c9)
	elif c10 == False: 
		Zulu.append(c10)
	elif c11 == False: 
		Zulu.append(c11)
	elif c12 == False: 
		Zulu.append(c12)
	elif c13 == False: 
		Zulu.append(c13)
	elif c14 == False: 
		Zulu.append(c14)
	elif c15 == False: 
		Zulu.append(c15)
	elif c16 == False: 
		Zulu.append(c16)
	elif c17 == False: 
		Zulu.append(c17)
	elif c18 == False: 
		Zulu.append(c18)
	elif c19 == False: 
		Zulu.append(c19)
	elif c20 == False: 
		Zulu.append(c20)
	elif c21 == False: 
		Zulu.append(c21)
	elif c22 == False: 
		Zulu.append(c22)
	elif c23 == False: 
		Zulu.append(c23)
	elif c24 == False: 
		Zulu.append(c24)
	elif c25 == False: 
		Zulu.append(c25)
	elif c26 == False: 
		Zulu.append(c26)
	elif c27 == False: 
		Zulu.append(c27)
	elif c28 == False: 
		Zulu.append(c28)
	elif c29 == False: 
		Zulu.append(c29)
	counter = len(Zulu)

#Question banks begin here
#Counries Bank
Countrie1 = ["Which of these is not a province in Canada?",
"France is part of which continent?",
"The Rocky Mountains lie in which country?",
"The largest country in the world is?",
"Kim Jun Ung is the lead of which country?",] 
Countrie2 = ["What territory/province a city Iqaluit part of?",
"Which country is hosting the 2018 Olympics?", 
"Which country did not partake in WWII?",
"Which ocean does Iceland lie within?",
"New Zeland borders how many other countries?"] 
Countrie3 = ["What country has the largest population?",
"What hemisphere are the alpine mountains in?",
"The great barrier reef is near which country?",
"Mount Everest is in which country?",
"Banff national park is part of which country?"]
Countrie4 = ["Name the ocean that borders Canada's most northerly areas?",
"Uzbekistan is part of which continent?",
"What is the smallest continent by area?",
"Greenland is part of which country?",
"Japan lies in what body of water?"]
Countrie5 = ["What is the smallest country in the world?",
"What US shares shores with the Pacfic ocean?",
"Lima the capital of which country?",
"Easter Island is in which continent?",
"The longest river is present in which country?"]

#Math bank
Mathematics1 = ["Who is not a math teacher at SLSS?",
"What is the value of x in 2x+3=5", 
"Which order of operations is done first?",
"What is this expression equal to? (2+2) ^ 2 - 2",
"What is the most common variable in math?"]
Mathematics2 = ["What relationship best models the given function? f(x)=(3)2^x", 
"What degree does a cubic equation consist of?",
"What is the smallest prime number?",
"What are the first 3 multiples of 3?",
"1/0 is equal to what?"]
Mathematics3 = ["The symbol sigma represents what task?",
"What variable is most often used to represent angles?",
"Mathematics deals with all but which branch?",
"Trigonometric identities are used to do what in mathematics?",
"What is the Pythagorean identity?"]
Mathematics4 = ["What letter is used to represent imaginary numbers?",
"How many solutions for y^x?", 
"Is 0.245 a real number?",
"A saddle point is often also called a what point?",
"Derivatives deal with finding what?"]
Mathematics5 = ["Who is one of the two fathers of calculus?",
"What limit does h approach in the first principle of calculus?",
"Cos(x) is symmetrical about what?",
"What is the symbol for factorial?",
"What graph is cot(x) the recipricol of?"]
                
#General knowledge bank
                
GK1 = ["What is the largest passenger aircraft in the world?",
"The closest planet to the sun is?",
"The SI unit of weight is?",
"Our galaxy is named?",
"Ontario's national flower is what?"]
GK2 = ["Another name given to asphalt is?",
"Computers use what counting system?",
"Lift is created through which aircraft part?",
"The most widely consumed cereal grain is?",
"Bad conductors are called?"]
GK3 = ["CBC stands for?",
"The world's tallest building is in which continent?",
"From all the territories and provinces in Canada the largest is?", 
"Compost is primarily broken down by what?",
"By 2100 Earths population will exceed?"]
GK4 = ["The milky way galaxy will crash with which other galaxy?",
"Vector graphic do not use what?",
"The acronym USB stands for what?",
"Plastics are made up of?", 
"The numbers between 1-100 add up to what?"]
GK5 = ["What was the name of the land mass before continental drift?",
"Down used in jackets comes from which bird?",
"Li-on stands for?",
"Horseshoe crab blood is what color?",
"Humans are incapable of producing which vitamin?",]
                
#Science bank
Sci1 = ["What is the color of blood in veins?",
"The sun produces energy through which process?",
"Who came up with the idea of natural selection?",
"The second shell in an atom can hold how many electrons?",
"The shifting of tectonic plates can cause what catastrophic event?"]
Sci2 = ["Air is made mostly out of what gas?",
"Soil contains sand silt and what other substance?",
"The pancreas secretes what substance?",
"The SI unit of energy is?",
"Which macro nutrient contains the most energy?"]
Sci3 = ["Entropy is also known as?",
"One mole of carbon 12 would weigh how many grams?",
"A spleen filters what substance?",
"What is molten rock called under the crust?",
"Metals contain ... electrons?"]
Sci4 = ["Di-hydrogen monoxide is a fancy name for what?", 
"What gas is produced with incomplete combustion?",
"Hair is made up of what protein?",
"Cell membranes are made of from?", 
"What enzyme is created to break down maltose?"]
Sci5 = ["What isotope of uranium is used for nuclear energy?",
"What compound is used to conduct electrons and is transparent?",
"Skin contains which protein?",
"Which is not a nucleotide base?",
"Which proteins pack DNA together?"]
              
#Medicine bank            
Med1 = ["The most common antibiotic is?",
"A cadavar is a dead ...?",
"Tiny air sacs within the lungs are called?",
"A flexible material found within joints is called?",
"When white blood cells consume other cells is called?"]
Med2 = ["Red blood cells lack what?",
"Biological catalysts are also known as?",
"Epipens contain what medication?",
"Blood clots are facilitated by what component of blood?",
"How many nucleotide bases are present within DNA?"]
Med3 = ["Ligaments connect bone to ...?",
"Lymph is what color?",
"Hemoglobin has how many active sites for the bonding of oxygen?",
"Enzymes are made of up of which substance?",
"Photosynthesis consists of how many photosystems?"]
Med4 = ["Opiates are derived from what plant?",
"The humerus is within what body part?",
"Mesentry holds what organ together in the abdomen?",
"Enzymes that lose there shape are said to be?",
"What is the compound that is an electron carrier in cellular respiration?"]
Med5 = ["The generic name for tylenol is?",
"The liver produces and stores what polysaccharide?",
"The distal radial ulnar joint is found in which body part?",
"Synovial fluid is found within what?",
"What nucleotide base differentiates RNA from DNA that is found within RNA?"]

#Inital points of both players nickname created here and set to zero
points_jackk = 0
points_Taha = 0

#These fucntions are used to control while loops setting them to false when a button is clicken upon
def alteration():
	global alpha
	alpha = False

def india_fasle():
	global india
	india = False

def alteration1():
	global juliet 
	juliet	= False

def alteration2():
	global juliet1
	juliet1 = False

def alteration3():
	global juliet2
	juliet2 = False

def alteration4():
	global juliet3
	juliet3 = False

def alteration5():
	global juliet4
	juliet4 = False

def alteration6():
	global juliet5
	juliet5 = False

def alteration7():
	global juliet6
	juliet6 = False

def alteration8():
	global juliet7
	juliet7 = False

def alteration9():
	global juliet8
	juliet8 = False

def alteration10():
	global juliet9
	juliet9 = False

def alteration11():
	global juliet10
	juliet10 = False

def alteration12():
	global juliet11
	juliet11 = False

def alteration13():
	global juliet12
	juliet12 = False

def alteration14():
	global juliet13
	juliet13 = False


def alteration15():
	global juliet14
	juliet14 = False

def alteration16():
	global juliet15
	juliet15 = False

def alteration17():
	global juliet16
	juliet16 = False

def alteration18():
	global juliet17
	juliet17 = False

def alteration19():
	global juliet18
	juliet18 = False

def alteration20():
	global juliet19
	juliet19 = False

def alteration21():
	global juliet20
	juliet20 = False

def alteration22():
	global juliet21
	juliet21 = False

def alteration23():
	global juliet22
	juliet22 = False

def alteration24():
	global juliet23
	juliet23 = False

def alteration25():
	global juliet24
	juliet24 = False

def back():
	global charlie
	charlie = False
def back1():
	global charlie1
	charlie1 = False

def back2():
	global charlie2
	charlie2 = False

def back3():
	global charlie3
	charlie3 = False

def back4():
	global charlie4
	charlie4 = False

def back5():
	global charlie5
	charlie5 = False

def back6():
	global charlie6
	charlie6 = False

def back7():
	global charlie7
	charlie7 = False

def back8():
	global charlie8
	charlie8 = False

def back9():
	global charlie9
	charlie9 = False

def back10():
	global charlie10
	charlie10 = False

def back11():
	global charlie11
	charlie11 = False

def back12():
	global charlie12
	charlie12 = False

def back13():
	global charlie13
	charlie13 = False

def back14():
	global charlie14
	charlie14 = False

def back15():
	global charlie15
	charlie15 = False

def back16():
	global charlie16
	charlie16 = False

def back17():
	global charlie17
	charlie17 = False

def back18():
	global charlie18
	charlie18 = False

def back19():
	global charlie19
	charlie19 = False

def back20():
	global charlie20
	charlie20 = False

def back21():
	global charlie21
	charlie21 = False

def back22():
	global charlie22
	charlie22 = False

def back23():
	global charlie23
	charlie23 = False

def back24():
	global charlie24
	charlie24 = False
#These fucntions are used to control while loops setting them to false when a button is clicken upon as well as to call other functions when buttons are clicked
def alter():
	global c1
	c1 = False
	alteration()
	PlayDisplay()

def alter1():
	global c2
	c2 = False
	alteration1()
	PlayDisplay()

def alter2():
	global c3
	c3 = False
	alteration2()
	PlayDisplay()

def alter3():
	global c4
	c4 = False
	alteration3()
	PlayDisplay()

def alter4():
	global c5
	c5 = False
	alteration4()
	PlayDisplay()

def alter5():
	global c6
	c6 = False
	alteration5()
	PlayDisplay()

def alter6():
	global c7
	c7 = False
	alteration6()
	PlayDisplay()

def alter7():
	global c8
	c8 = False
	alteration7()
	PlayDisplay()

def alter8():
	global c9
	c9 = False
	alteration8()
	PlayDisplay()

def alter9():
	global c10
	c10 = False
	alteration9()
	PlayDisplay()

def alter10():
	global c11
	c11 = False
	alteration10()
	PlayDisplay()

def alter11():
	global c12
	c12 = False
	alteration11()
	PlayDisplay()

def alter12():
	global c13
	c13 = False
	alteration12()
	PlayDisplay()

def alter13():
	global c14
	c14 = False
	alteration13()
	PlayDisplay()

def alter14():
	global c15
	c15 = False
	alteration14()
	PlayDisplay()

def alter15():
	global c16
	c16 = False
	alteration15()
	PlayDisplay()

def alter16():
	global c17
	c17 = False
	alteration16()
	PlayDisplay()

def alter17():
	global c18
	c18 = False
	alteration17()
	PlayDisplay()

def alter18():
	global c19
	c19 = False
	alteration18()
	PlayDisplay()

def alter19():
	global c20
	c20 = False
	alteration19()
	PlayDisplay()

def alter20():
	global c21
	c21 = False
	alteration20()
	PlayDisplay()

def alter21():
	global c22
	c22 = False
	alteration21()
	PlayDisplay()

def alter22():
	global c23
	c23 = False
	alteration22()
	PlayDisplay()

def alter23():
	global c24
	c24 = False
	alteration23()
	PlayDisplay()

def alter24():
	global c25
	c25 = False
	alteration24()
	PlayDisplay()

#These fucntions are used to control while loops setting them to false when a button is clicken upon
def change():
	global foxtrot
	foxtrot = False

def juliet_false():
	global juliet
	juliet = False

def golf_false():
	global golf
	golf = False

def golf1_false():
	global golf1
	golf1 = False

def golf2_false():
	global golf2
	golf2 = False

def golf3_false():
	global golf3
	golf3 = False


def golf4_false():
	global golf4
	golf4 = False


def golf5_false():
	global golf5
	golf5 = False


def golf6_false():
	global golf6
	golf6 = False


def golf7_false():
	global golf7
	golf7 = False



def golf8_false():
	global golf8
	golf8 = False


def golf9_false():
	global golf9
	golf9 = False


def golf10_false():
	global golf10
	golf10 = False



def golf11_false():
	global golf11
	golf11 = False


def golf12_false():
	global golf12
	golf12 = False


def golf13_false():
	global golf13
	golf13 = False


def golf14_false():
	global golf14
	golf14 = False


def golf15_false():
	global golf15
	golf15 = False


def golf16_false():
	global golf16
	golf16 = False


def golf17_false():
	global golf17
	golf17 = False


def golf18_false():
	global golf18
	golf18 = False


def golf19_false():
	global golf19
	golf19 = False


def golf20_false():
	global golf20
	golf20 = False


def golf21_false():
	global golf21
	golf21 = False


def golf22_false():
	global golf22
	golf22 = False


def golf23_false():
	global golf23
	golf23 = False


def golf24_false():
	global golf24
	golf24 = False

def tanas_false():
	global tanas
	tanas = False

def finishing_false():
	global finsihing
	finsihing = False

#This fucntion is used to create a text object that is used by later fucntions
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#This function is used to display text with color location size and the actual text
def message_display(text, XC, YC, size, color):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf,TextRect = text_objects(text, largeText, color)
    TextRect = ((XC), (YC))
    gameDisplay.blit(TextSurf, TextRect)
    #pygame.display.update()

#This fucntion is used to center text
def center(text,size,x,y, color):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf,TextRect = text_objects(text, largeText, color)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)

#This is the inital screen when the game starts. Background is black and says my name
gameDisplay.fill(Black)
center("Jeopardy", 37, display_width/2, display_height/2, White)
message_display ("Devloped By: Shaheer Nadeem", display_width/2 -150 , display_height/2 + 23 , 20, White)
pygame.display.update()
sleep(2)
pygame.mixer.Sound.play(sounding1)

def starts(message, x, y, width, height, inactive, active, size, action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + width > mouse[0] > x and y + height > mouse[1] > y:
		pygame.draw.rect(gameDisplay, active, (x,y,width,height))
		if click[0] == 1 and action != None:
			pygame.mixer.Sound.play(sounding)
			if action == "Quick Play":
				intro_screen()
			elif action == "Instructions":
				instructions1()
			elif action == "Help":
				Help1()
			elif action == "Oks":
				tanas_false()
			elif action == "Finish":
				finishing_false()
				game_boot()
			else: 
				pygame.quit()
				quit() 


	else:
		pygame.draw.rect(gameDisplay, inactive, (x,y,width,height))
	center(message, size, (x + (width/2)), (y + (height/2)), White)

#This function displays the name of the differnt categories in quick play
def catagories(message, x, y, width, height, size):
	pygame.draw.rect(gameDisplay, Buttons, (x,y,width,height))
	center(message, size, (x + (width/2)), (y + (height/2)), White)

"""
This function is checks to see where users mouse is.
If it is on the button it changes color to make it look interactive
If clicked on the button calls a funtion
used as the main function if questions are right or wrong
"""
def options(messageee, xee, yee, widthee, heightee, activeee, inactiveee, sizeee, actionee = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	pygame.draw.rect(gameDisplay, activeee, (xee,yee,widthee,heightee))
	if xee + widthee > mouse[0] > xee and yee + heightee > mouse[1] > yee:
		if click[0] == 1 and actionee != None:
			pygame.mixer.Sound.play(sounding)
			if actionee == "Right1":
				correct(100)
			elif actionee == "Rights1":
				steal_correct(100)
			elif actionee == "Right2":
				correct1(200)
			elif actionee == "Rights2":
				steal_correct1(200)
			elif actionee == "Right3":
				correct2(300)
			elif actionee == "Rights3":
				steal_correct2(300)
			elif actionee == "Right4":
				correct3(400)
			elif actionee == "Rights4":
				steal_correct3(400)
			elif actionee == "Right5":
				correct4(500)
			elif actionee == "Rights5":
				steal_correct4(500)
			elif actionee == "Right6":
				correct5(100)
			elif actionee == "Rights6":
				steal_correct5(100)
			elif actionee == "Right7":
				correct6(200)
			elif actionee == "Rights7":
				steal_correct6(200)
			elif actionee == "Right8":
				correct7(300)
			elif actionee == "Rights8":
				steal_correct7(300)
			elif actionee == "Right9":
				correct8(400)
			elif actionee == "Rights9":
				steal_correct8(400)
			elif actionee == "Right10":
				correct9(500)
			elif actionee == "Rights10":
				steal_correct9(500)
			elif actionee == "Right11":
				correct10(100)
			elif actionee == "Rights11":
				steal_correct10(100)
			elif actionee == "Right12":
				correct11(200)
			elif actionee == "Rights12":
				steal_correct11(200)
			elif actionee == "Right13":
				correct12(300)
			elif actionee == "Rights13":
				steal_correct12(300)
			elif actionee == "Right14":
				correct13(400)
			elif actionee == "Rights14":
				steal_correct13(400)
			elif actionee == "Right15":
				correct14(500)
			elif actionee == "Rights15":
				steal_correct14(500)
			elif actionee == "Right16":
				correct15(100)
			elif actionee == "Rights16":
				steal_correct15(100)
			elif actionee == "Right17":
				correct16(200)
			elif actionee == "Rights17":
				steal_correct16(200)
			elif actionee == "Right18":
				correct17(300)
			elif actionee == "Rights18":
				steal_correct17(300)
			elif actionee == "Right19":
				correct18(400)
			elif actionee == "Rights19":
				steal_correct18(400)
			elif actionee == "Right20":
				correct19(500)
			elif actionee == "Rights20":
				steal_correct19(500)
			elif actionee == "Right21":
				correct20(100)
			elif actionee == "Rights21":
				steal_correct20(100)
			elif actionee == "Right22":
				correct21(200)
			elif actionee == "Rights22":
				steal_correct21(200)
			elif actionee == "Right23":
				correct22(300)
			elif actionee == "Rights23":
				steal_correct22(300)
			elif actionee == "Right24":
				correct23(400)
			elif actionee == "Rights24":
				steal_correct23(400)
			elif actionee == "Right25":
				correct24(500)
			elif actionee == "Rights25":
				steal_correct24(500)
			elif actionee == "wrong1":
				oops_yes_retry()
			elif actionee == "wrongs1":
				oops_no_retry()
			elif actionee == "wrong2":
				oops_yes_retry1()
			elif actionee == "wrongs2":
				oops_no_retry1()
			elif actionee == "wrong3":
				oops_yes_retry2()
			elif actionee == "wrongs3":
				oops_no_retry2()
			elif actionee == "wrong4":
				oops_yes_retry3()
			elif actionee == "wrongs4":
				oops_no_retry3()
			elif actionee == "wrong5":
				oops_yes_retry4()
			elif actionee == "wrongs5":
				oops_no_retry4()
			elif actionee == "wrong6":
				oops_yes_retry5()
			elif actionee == "wrongs6":
				oops_no_retry5()
			elif actionee == "wrong7":
				oops_yes_retry6()
			elif actionee == "wrongs7":
				oops_no_retry6()
			elif actionee == "wrong8":
				oops_yes_retry7()
			elif actionee == "wrongs8":
				oops_no_retry7()
			elif actionee == "wrong9":
				oops_yes_retry8()
			elif actionee == "wrongs9":
				oops_no_retry8()
			elif actionee == "wrong10":
				oops_yes_retry9()
			elif actionee == "wrongs10":
				oops_no_retry9()
			elif actionee == "wrong11":
				oops_yes_retry10()
			elif actionee == "wrongs11":
				oops_no_retry10()
			elif actionee == "wrong12":
				oops_yes_retry11()
			elif actionee == "wrongs12":
				oops_no_retry11()
			elif actionee == "wrong13":
				oops_yes_retry12()
			elif actionee == "wrongs13":
				oops_no_retry12()
			elif actionee == "wrong14":
				oops_yes_retry13()
			elif actionee == "wrongs14":
				oops_no_retry13()
			elif actionee == "wrong15":
				oops_yes_retry14()
			elif actionee == "wrongs15":
				oops_no_retry14()
			elif actionee == "wrong16":
				oops_yes_retry15()
			elif actionee == "wrongs16":
				oops_no_retry15()
			elif actionee == "wrong17":
				oops_yes_retry16()
			elif actionee == "wrongs17":
				oops_no_retry16()
			elif actionee == "wrong18":
				oops_yes_retry17()
			elif actionee == "wrongs18":
				oops_no_retry17()
			elif actionee == "wrong19":
				oops_yes_retry18()
			elif actionee == "wrongs19":
				oops_no_retry18()
			elif actionee == "wrong20":
				oops_yes_retry19()
			elif actionee == "wrongs20":
				oops_no_retry19()
			elif actionee == "wrong21":
				oops_yes_retry20()
			elif actionee == "wrongs21":
				oops_no_retry20()
			elif actionee == "wrong22":
				oops_yes_retry21()
			elif actionee == "wrongs22":
				oops_no_retry21()
			elif actionee == "wrong23":
				oops_yes_retry22()
			elif actionee == "wrongs23":
				oops_no_retry22()
			elif actionee == "wrong24":
				oops_yes_retry23()
			elif actionee == "wrongs24":
				oops_no_retry23()
			elif actionee == "wrong25":
				oops_yes_retry24()
			elif actionee == "wrongs25":
				oops_no_retry24()
			else: 
				pygame.quit()
				quit() 
	else:
		pygame.draw.rect(gameDisplay, inactiveee, (xee,yee,widthee,heightee))
	center(messageee, sizeee, (xee + (widthee/2)), (yee + (heightee/2)), White)

"""
This function is checks to see where users mouse is.
If it is on the button it changes color to make it look interactive
If clicked on the button calls a funtion
Used for all other buttons
also sleeps for some instances to prvent the button behind from being clicked VERY IMPORTANT
"""
def Levels(messagee, xe, ye, widthe, heighte, inactivee, activee, sizee, actione = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if xe + widthe > mouse[0] > xe and ye + heighte > mouse[1] > ye:
		pygame.draw.rect(gameDisplay, activee, (xe,ye,widthe,heighte))
		if click[0] == 1 and actione != None:
			pygame.mixer.Sound.play(sounding)
			if actione == "Run1":
				sleep(0.25)
				a1()
			elif actione == "Run2":
				sleep(0.25)
				a2()
			elif actione == "Run3":
				sleep(0.25)
				a3()
			elif actione == "Run4":
				sleep(0.25)
				a4()
			elif actione == "Run5":
				sleep(0.25)
				a5()
			elif actione == "Run6":
				sleep(0.25)
				a6()
			elif actione == "Run7":
				sleep(0.25)
				a7()
			elif actione == "Run8":
				sleep(0.25)
				a8()
			elif actione == "Run9":
				sleep(0.25)
				a9()
			elif actione == "Run10":
				sleep(0.25)
				a10()
			elif actione == "Run11":
				sleep(0.25)
				a11()
			elif actione == "Run12":
				sleep(0.25)
				a12()
			elif actione == "Run13":
				sleep(0.25)
				a13()
			elif actione == "Run14":
				sleep(0.25)
				a14()
			elif actione == "Run15":
				sleep(0.25)
				a15()
			elif actione == "Run16":
				sleep(0.25)
				a16()
			elif actione == "Run17":
				sleep(0.25)
				a17()
			elif actione == "Run18":
				sleep(0.25)
				a18()
			elif actione == "Run19":
				sleep(0.25)
				a19()
			elif actione == "Run20":
				sleep(0.25)
				a20()
			elif actione == "Run21":
				sleep(0.25)
				a21()
			elif actione == "Run22":
				sleep(0.25)
				a22()
			elif actione == "Run23":
				sleep(0.25)
				a23()
			elif actione == "Run24":
				sleep(0.25)
				a24()	
			elif actione == "Run25":
				sleep(0.25)
				a25()	
			elif actione == "VORK":
				alter()
			elif actione == "Back":
				sleep(0.25)
				alter()
			elif actione == "Back1":
				sleep(0.25)
				alter1()
			elif actione == "Back2":
				sleep(0.25)
				alter2()
			elif actione == "Back3":
				sleep(0.25)
				alter3()
			elif actione == "Back4":
				sleep(0.25)
				alter4()
			elif actione == "Back5":
				sleep(0.25)
				alter5()
			elif actione == "Back6":
				sleep(0.25)
				alter6()
			elif actione == "Back7":
				sleep(0.25)
				alter7()
			elif actione == "Back8":
				sleep(0.25)
				alter8()
			elif actione == "Back9":
				sleep(0.25)
				alter9()
			elif actione == "Back10":
				sleep(0.25)
				alter10()
			elif actione == "Back11":
				sleep(0.25)
				alter11()
			elif actione == "Back12":
				sleep(0.25)
				alter12()
			elif actione == "Back13":
				sleep(0.25)
				alter13()
			elif actione == "Back14":
				sleep(0.25)
				alter14()
			elif actione == "Back15":
				sleep(0.25)
				alter15()
			elif actione == "Back16":
				sleep(0.25)
				alter16()
			elif actione == "Back17":
				sleep(0.25)
				alter17()
			elif actione == "Back18":
				sleep(0.25)
				alter18()
			elif actione == "Back19":
				sleep(0.25)
				alter19()
			elif actione == "Back20":
				sleep(0.25)
				alter20()
			elif actione == "Back21":
				sleep(0.25)
				alter21()
			elif actione == "Back22":
				sleep(0.25)
				alter22()
			elif actione == "Back23":
				sleep(0.25)
				alter23()
			elif actione == "Back24":
				sleep(0.25)
				alter24()
			elif actione == "Back25":
				sleep(0.25)
				alter25()
			elif actione == "Back to Screen":
				back()
				alter()
				PlayDisplay()
			elif actione == "Back to Screen1":
				back1()
				alter1()
				PlayDisplay()
			elif actione == "Back to Screen2":
				back2()
				alter2()
				PlayDisplay()
			elif actione == "Back to Screen3":
				back3()
				alter3()
				PlayDisplay()
			elif actione == "Back to Screen4":
				back4()
				alter4()
				PlayDisplay()
			elif actione == "Back to Screen5":
				back5()
				alter5()
				PlayDisplay()
			elif actione == "Back to Screen6":
				back6()
				alter6()
				PlayDisplay()
			elif actione == "Back to Screen7":
				back7()
				alter7()
				PlayDisplay()
			elif actione == "Back to Screen8":
				back8()
				alter8()
				PlayDisplay()
			elif actione == "Back to Screen9":
				back9()
				alter9()
				PlayDisplay()
			elif actione == "Back to Screen10":
				back10()
				alter10()
				PlayDisplay()
			elif actione == "Back to Screen11":
				back11()
				alter11()
				PlayDisplay()
			elif actione == "Back to Screen12":
				back12()
				alter12()
				PlayDisplay()
			elif actione == "Back to Screen13":
				back13()
				alter13()
				PlayDisplay()
			elif actione == "Back to Screen14":
				back14()
				alter14()
				PlayDisplay()
			elif actione == "Back to Screen15":
				back15()
				alter15()
				PlayDisplay()
			elif actione == "Back to Screen16":
				back16()
				alter16()
				PlayDisplay()
			elif actione == "Back to Screen17":
				back17()
				alter17()
				PlayDisplay()
			elif actione == "Back to Screen18":
				back18()
				alter18()
				PlayDisplay()
			elif actione == "Back to Screen19":
				back19()
				alter19()
				PlayDisplay()
			elif actione == "Back to Screen20":
				back20()
				alter20()
				PlayDisplay()
			elif actione == "Back to Screen21":
				back21()
				alter21()
				PlayDisplay()
			elif actione == "Back to Screen22":
				back22()
				alter22()
				PlayDisplay()
			elif actione == "Back to Screen23":
				back23()
				alter23()
				PlayDisplay()
			elif actione == "Back to Screen24":
				back24()
				alter24()
				PlayDisplay()
			elif actione == "Back to Screen25":
				back25()
				alter25()
				PlayDisplay()
			elif actione == "Previous":
				sleep(0.25)
				golf_false()
				alteration()
				a1s()
			elif actione == "Previous1":
				sleep(0.25)
				golf1_false()
				alteration1()
				a2s()
			elif actione == "Previous2":
				sleep(0.25)
				golf2_false()
				alteration2()
				a3s()
			elif actione == "Previous3":
				sleep(0.25)
				golf3_false()
				alteration3()
				a4s()
			elif actione == "Previous4":
				sleep(0.25)
				golf4_false()
				alteration4()
				a5s()
			elif actione == "Previous5":
				sleep(0.25)
				golf5_false()
				alteration5()
				a6s()
			elif actione == "Previous6":
				sleep(0.25)
				golf6_false()
				alteration6()
				a7s()
			elif actione == "Previous7":
				sleep(0.25)
				golf7_false()
				alteration7()
				a8s()
			elif actione == "Previous8":
				sleep(0.25)
				golf8_false()
				alteration8()
				a9s()
			elif actione == "Previous9":
				sleep(0.25)
				golf9_false()
				alteration9()
				a10s()
			elif actione == "Previous10":
				sleep(0.25)
				golf10_false()
				alteration10()
				a11s()
			elif actione == "Previous11":
				sleep(0.25)
				golf11_false()
				alteration11()
				a12s()
			elif actione == "Previous12":
				sleep(0.25)
				golf12_false()
				alteration12()
				a13s()
			elif actione == "Previous13":
				sleep(0.25)
				golf13_false()
				alteration13()
				a14s()
			elif actione == "Previous14":
				sleep(0.25)
				golf14_false()
				alteration14()
				a15s()
			elif actione == "Previous15":
				sleep(0.25)
				golf15_false()
				alteration15()
				a16s()
			elif actione == "Previous16":
				sleep(0.25)
				golf16_false()
				alteration16()
				a17s()
			elif actione == "Previous17":
				sleep(0.25)
				golf17_false()
				alteration17()
				a18s()
			elif actione == "Previous18":
				sleep(0.25)
				golf18_false()
				alteration18()
				a19s()
			elif actione == "Previous19":
				sleep(0.25)
				golf19_false()
				alteration19()
				a20s()
			elif actione == "Previous20":
				sleep(0.25)
				golf20_false()
				alteration20()
				a21s()
			elif actione == "Previous21":
				sleep(0.25)
				golf21_false()
				alteration21()
				a22s()
			elif actione == "Previous22":
				sleep(0.25)
				golf22_false()
				alteration22()
				a23s()
			elif actione == "Previous23":
				sleep(0.25)
				golf23_false()
				alteration23()
				a24s()
			elif actione == "Previous24":
				sleep(0.25)
				golf24_false()
				alteration24()
				a25s()
			elif actione == "Previous25":
				sleep(0.25)
				golf24_false()
				alteration25()
				a26s()
			else: 
				pygame.quit()
				quit() 
	else:
		pygame.draw.rect(gameDisplay, inactivee, (xe,ye,widthe,heighte))
	center(messagee, sizee, (xe + (widthe/2)), (ye + (heighte/2)), White)

"""
This function is used if two wrong gusses are done by both players
it displays the points that each player has
The fucntions below are all similar but the buttons each call differnt functions
This allows for the to not be able to select the same question over
The reasont there are so many functions is that each changes the color of a diffent point caterogry
"""
def oops_no_retry():
	global points_Taha
	global points_jackk
	global charlie
	charlie = True
	while charlie:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry1():
	global points_Taha
	global points_jackk
	global charlie1
	charlie1 = True
	while charlie1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen1")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry2():
	global points_Taha
	global points_jackk
	global charlie2
	charlie2 = True
	while charlie2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen2")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry3():
	global points_Taha
	global points_jackk
	global charlie3
	charlie3 = True
	while charlie3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen3")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry4():
	global points_Taha
	global points_jackk
	global charlie4
	charlie4 = True
	while charlie4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen4")
		pygame.display.update()
		clock.tick(10)


def oops_no_retry5():
	global points_Taha
	global points_jackk
	global charlie5
	charlie5 = True
	while charlie5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen5")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry6():
	global points_Taha
	global points_jackk
	global charlie6
	charlie6 = True
	while charlie6:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen6")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry7():
	global points_Taha
	global points_jackk
	global charlie7
	charlie7 = True
	while charlie7:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen7")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry8():
	global points_Taha
	global points_jackk
	global charlie8
	charlie8 = True
	while charlie8:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen8")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry9():
	global points_Taha
	global points_jackk
	global charlie9
	charlie9 = True
	while charlie9:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen9")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry10():
	global points_Taha
	global points_jackk
	global charlie10
	charlie10 = True
	while charlie10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen10")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry11():
	global points_Taha
	global points_jackk
	global charlie11
	charlie11 = True
	while charlie11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen11")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry12():
	global points_Taha
	global points_jackk
	global charlie12
	charlie12 = True
	while charlie12:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen12")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry13():
	global points_Taha
	global points_jackk
	global charlie13
	charlie13 = True
	while charlie13:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen13")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry14():
	global points_Taha
	global points_jackk
	global charlie14
	charlie14 = True
	while charlie14:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen14")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry15():
	global points_Taha
	global points_jackk
	global charlie15
	charlie15 = True
	while charlie15:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen15")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry16():
	global points_Taha
	global points_jackk
	global charlie16
	charlie16 = True
	while charlie16:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen16")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry17():
	global points_Taha
	global points_jackk
	global charlie17
	charlie17 = True
	while charlie17:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen17")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry18():
	global points_Taha
	global points_jackk
	global charlie18
	charlie18 = True
	while charlie18:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen18")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry19():
	global points_Taha
	global points_jackk
	global charlie19
	charlie19 = True
	while charlie19:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen19")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry20():
	global points_Taha
	global points_jackk
	global charlie20
	charlie20 = True
	while charlie20:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen20")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry21():
	global points_Taha
	global points_jackk
	global charlie21
	charlie21 = True
	while charlie21:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen21")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry22():
	global points_Taha
	global points_jackk
	global charlie22
	charlie22 = True
	while charlie22:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen22")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry23():
	global points_Taha
	global points_jackk
	global charlie23
	charlie23 = True
	while charlie23:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen23")
		pygame.display.update()
		clock.tick(10)

def oops_no_retry24():
	global points_Taha
	global points_jackk
	global charlie24
	charlie24 = True
	while charlie24:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-20, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back to Screen24")
		pygame.display.update()
		clock.tick(10)

"""
This function is used if ONE wrong guess is done by one player
it displays the points that each player has
The fucntions below are all similar but the buttons each call differnt functions
This allows for the to not be able to select the same question over
The reasont there are so many functions is that each changes the color of a diffent point caterogry
"""

def oops_yes_retry():
	global points_Taha
	global points_jackk
	global golf
	golf = True
	while golf:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry1():
	global points_Taha
	global points_jackk
	global golf1
	golf1 = True
	while golf1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous1")
		pygame.display.update()
		clock.tick(10)

def oops_yes_retry2():
	global points_Taha
	global points_jackk
	global golf2
	golf2 = True
	while golf2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous2")
		pygame.display.update()
		clock.tick(10)

def oops_yes_retry3():
	global points_Taha
	global points_jackk
	global golf3
	golf3 = True
	while golf3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous3")
		pygame.display.update()
		clock.tick(10)

def oops_yes_retry4():
	global points_Taha
	global points_jackk
	global golf4
	golf4 = True
	while golf4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous4")
		pygame.display.update()
		clock.tick(10)

def oops_yes_retry5():
	global points_Taha
	global points_jackk
	global golf5
	golf5 = True
	while golf5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous5")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry6():
	global points_Taha
	global points_jackk
	global golf6
	golf6 = True
	while golf6:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous6")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry7():
	global points_Taha
	global points_jackk
	global golf7
	golf7 = True
	while golf7:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous7")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry8():
	global points_Taha
	global points_jackk
	global golf8
	golf8 = True
	while golf8:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous8")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry9():
	global points_Taha
	global points_jackk
	global golf9
	golf9 = True
	while golf9:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous9")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry10():
	global points_Taha
	global points_jackk
	global golf10
	golf10 = True
	while golf10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous10")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry11():
	global points_Taha
	global points_jackk
	global golf11
	golf11 = True
	while golf11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous11")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry12():
	global points_Taha
	global points_jackk
	global golf12
	golf12 = True
	while golf12:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous12")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry13():
	global points_Taha
	global points_jackk
	global golf13
	golf13 = True
	while golf13:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous13")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry14():
	global points_Taha
	global points_jackk
	global golf14
	golf14 = True
	while golf14:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous14")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry15():
	global points_Taha
	global points_jackk
	global golf15
	golf15 = True
	while golf15:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous15")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry16():
	global points_Taha
	global points_jackk
	global golf16
	golf16 = True
	while golf16:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous16")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry17():
	global points_Taha
	global points_jackk
	global golf17
	golf17 = True
	while golf17:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous17")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry18():
	global points_Taha
	global points_jackk
	global golf18
	golf18 = True
	while golf18:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous18")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry19():
	global points_Taha
	global points_jackk
	global golf19
	golf19 = True
	while golf19:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous19")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry20():
	global points_Taha
	global points_jackk
	global golf20
	golf20 = True
	while golf20:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous20")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry21():
	global points_Taha
	global points_jackk
	global golf21
	golf21 = True
	while golf21:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous21")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry22():
	global points_Taha
	global points_jackk
	global golf22
	golf22 = True
	while golf22:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous22")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry23():
	global points_Taha
	global points_jackk
	global golf23
	golf23 = True
	while golf23:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous23")
		pygame.display.update()
		clock.tick(10)


def oops_yes_retry24():
	global points_Taha
	global points_jackk
	global golf24
	golf24 = True
	while golf24:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto1, (0,0))
		center("OOPS! That's incorrect",45,display_width/2  ,display_height/2-70, Red)
		center("Opposing player get's to steal.",45,display_width/2  ,display_height/2-30, Red)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Previous24")
		pygame.display.update()
		clock.tick(10)

"""
These functions is used to give points to the player who deserves them based on the turns 
it displays the points that each player has and also adds the ponits gained
These functions are if one player gets the question wrong and the opposite player gets the points
The fucntions below are all similar but the buttons each call differnt functions
This allows for the to not be able to select the same question over
The reason there are so many functions is that each changes the color of a diffent point caterogry
"""
def steal_correct(question_rank):
	global points_Taha
	global points_jackk
	hotel = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back")
		pygame.display.update()
		clock.tick(10)

def steal_correct1(question_rank):
	global points_Taha
	global points_jackk
	hotel1 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back1")
		pygame.display.update()
		clock.tick(10)

def steal_correct2(question_rank):
	global points_Taha
	global points_jackk
	hotel2 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back2")
		pygame.display.update()
		clock.tick(10)

def steal_correct3(question_rank):
	global points_Taha
	global points_jackk
	hotel3 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back3")
		pygame.display.update()
		clock.tick(10)

def steal_correct4(question_rank):
	global points_Taha
	global points_jackk
	hotel4 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back4")
		pygame.display.update()
		clock.tick(10)

def steal_correct5(question_rank):
	global points_Taha
	global points_jackk
	hotel5 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back5")
		pygame.display.update()
		clock.tick(10)

def steal_correct6(question_rank):
	global points_Taha
	global points_jackk
	hotel6 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel6:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back6")
		pygame.display.update()
		clock.tick(10)

def steal_correct7(question_rank):
	global points_Taha
	global points_jackk
	hotel7 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel7:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back7")
		pygame.display.update()
		clock.tick(10)

def steal_correct8(question_rank):
	global points_Taha
	global points_jackk
	hotel8 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel8:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back8")
		pygame.display.update()
		clock.tick(10)

def steal_correct9(question_rank):
	global points_Taha
	global points_jackk
	hotel9 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel9:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back9")
		pygame.display.update()
		clock.tick(10)

def steal_correct10(question_rank):
	global points_Taha
	global points_jackk
	hotel10 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back10")
		pygame.display.update()

def steal_correct11(question_rank):
	global points_Taha
	global points_jackk
	hotel11 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back11")
		pygame.display.update()
		clock.tick(10)

def steal_correct12(question_rank):
	global points_Taha
	global points_jackk
	hotel12 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel12:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back12")
		pygame.display.update()
		clock.tick(10)

def steal_correct13(question_rank):
	global points_Taha
	global points_jackk
	hotel13 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel13:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back13")
		pygame.display.update()
		clock.tick(10)

def steal_correct14(question_rank):
	global points_Taha
	global points_jackk
	hotel14 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel14:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back14")
		pygame.display.update()
		clock.tick(10)

def steal_correct15(question_rank):
	global points_Taha
	global points_jackk
	hotel15 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel15:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back15")
		pygame.display.update()
		clock.tick(10)

def steal_correct16(question_rank):
	global points_Taha
	global points_jackk
	hotel16 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel16:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back16")
		pygame.display.update()
		clock.tick(10)

def steal_correct17(question_rank):
	global points_Taha
	global points_jackk
	hotel17 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel17:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back17")
		pygame.display.update()
		clock.tick(10)

def steal_correct18(question_rank):
	global points_Taha
	global points_jackk
	hotel18 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel18:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back18")
		pygame.display.update()
		clock.tick(10)

def steal_correct19(question_rank):
	global points_Taha
	global points_jackk
	hotel19 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel19:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back19")
		pygame.display.update()
		clock.tick(10)

def steal_correct20(question_rank):
	global points_Taha
	global points_jackk
	hotel20 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel20:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back20")
		pygame.display.update()
		clock.tick(10)

def steal_correct21(question_rank):
	global points_Taha
	global points_jackk
	hotel21 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel21:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back21")
		pygame.display.update()
		clock.tick(10)

def steal_correct22(question_rank):
	global points_Taha
	global points_jackk
	hotel22 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel22:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back22")
		pygame.display.update()
		clock.tick(10)

def steal_correct23(question_rank):
	global points_Taha
	global points_jackk
	hotel23 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel23:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back23")
		pygame.display.update()
		clock.tick(10)

def steal_correct24(question_rank):
	global points_Taha
	global points_jackk
	hotel24 = True
	if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter  == 9 or counter == 11 or counter  == 13 or counter == 15 or counter == 17 or counter == 19 or counter  == 21 or counter == 23 or counter == 25:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while hotel24:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back24")
		pygame.display.update()
		clock.tick(10)

"""
These functions is used to give points to the player who deserves them based on the turns 
it displays the points that each player has and also adds the ponits gained
These functions are if the player who clicks on the question gets it right
The fucntions below are all similar but the buttons each call differnt functions
This allows for the to not be able to select the same question over
The reason there are so many functions is that each changes the color of a diffent point caterogry
"""
def correct24(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha24:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back24")
		pygame.display.update()
		clock.tick(10)

def correct23(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha23:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back23")
		pygame.display.update()
		clock.tick(10)


def correct22(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha22:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back22")
		pygame.display.update()
		clock.tick(10)

def correct21(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha21:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back21")
		pygame.display.update()
		clock.tick(10)

def correct20(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha20:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back20")
		pygame.display.update()
		clock.tick(10)

def correct19(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha19:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back19")
		pygame.display.update()
		clock.tick(10)

def correct18(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha18:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back18")
		pygame.display.update()
		clock.tick(10)

def correct17(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha17:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back17")
		pygame.display.update()
		clock.tick(10)

def correct16(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha16:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back16")
		pygame.display.update()
		clock.tick(10)

def correct15(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha15:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back15")
		pygame.display.update()
		clock.tick(10)

def correct14(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha14:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back14")
		pygame.display.update()
		clock.tick(10)

def correct13(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha13:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back13")
		pygame.display.update()
		clock.tick(10)

def correct12(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha12:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back12")
		pygame.display.update()
		clock.tick(10)

def correct11(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back11")
		pygame.display.update()
		clock.tick(10)

def correct10(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back10")
		pygame.display.update()
		clock.tick(10)

def correct9(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha9:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back9")
		pygame.display.update()
		clock.tick(10)

def correct8(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha8:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back8")
		pygame.display.update()
		clock.tick(10)

def correct7(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha7:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back7")
		pygame.display.update()
		clock.tick(10)

def correct6(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha6:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back6")
		pygame.display.update()
		clock.tick(10)

def correct5(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back5")
		pygame.display.update()
		clock.tick(10)

def correct4(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back4")
		pygame.display.update()
		clock.tick(10)

def correct3(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back3")
		pygame.display.update()
		clock.tick(10)

def correct2(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back2")
		pygame.display.update()
		clock.tick(10)

def correct1(question_rank):
	global points_Taha
	global points_jackk
	alpha1 = True
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while alpha1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back1")
		pygame.display.update()
		clock.tick(10)

def correct(question_rank):
	global points_Taha
	global points_jackk
	if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter  == 10 or counter == 12 or counter  == 14 or counter == 16 or counter == 18 or counter == 20 or counter  == 22 or counter == 24:
		points_jackk += question_rank
	else:
		points_Taha += question_rank
	while foxtrot:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(qrto2, (0,0))
		center("Your Correct",45,display_width/2 ,display_height/2-20, Green)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display(str(points_Taha),575,500,30, Blue)
		Levels("OK!", display_width/2-47, display_height/2 + 40,100,70,Buttons, B1,28,"Back")
		pygame.display.update()
		clock.tick(10)

""" These below functions are argubaly the most important.
They are used to randomly select questions from a question bank
With if staement each question has been centered and proper picture has been added
Also, the s version of the function stands for steal and differs from the other ones in that it allows for the 
opposite player to get the points.
"""

def a1s():
	global v1
	global india
	india = True
	while india:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v1 == 0:
			gameDisplay.blit(testing, (display_width/2 - 182,display_height/2-220)) 
			message_display(Countrie1[v1],60,30,32,White)
			options("Ontario", 50, 400, 250, 80, Black, user, 35, "wrongs1")
			options("Nova Scotia", 525, 500, 250, 80, Black, user, 35, "wrongs1")
			options("Nunavut", 525, 400, 250, 80, Black,user, 35, "Rights1")
			options("Quebec", 50, 500, 250, 80, Black, user, 35, "wrongs1")
		elif v1 == 1:
			message_display(Countrie1[v1],130,30,32,White)
			gameDisplay.blit(testing1, (display_width/2 - 182,display_height/2-228))
			options("Asia", 50, 500, 250, 80, Black, user, 35, "wrongs1")
			options("North America", 525, 500, 250, 80, Black, user, 35, "wrongs1")
			options("Europe", 50, 400, 250, 80, Black,user, 35, "Rights1")
			options("Africa", 525, 400, 250, 80, Black, user, 35, "wrongs1")
		elif v1 == 2:
			gameDisplay.blit(testing2, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie1[v1],60,30,32,White)
			options("Nepal", 50, 400, 250, 80, Black, user, 35, "wrongs1")
			options("North America", 50, 500, 250, 80, Black, user, 35, "wrongs1")
			options("Canada", 525, 500, 250, 80, Black,user, 35, "Rights1")
			options("Switzerland", 525, 400, 250, 80, Black, user, 35, "wrongs1")	
		elif v1 == 3:
			gameDisplay.blit(testing3, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie1[v1],124,30,32,White)
			options("China", 50, 400, 250, 80, Black, user, 35, "wrongs1")
			options("Canada", 525, 500, 250, 80, Black, user, 35, "wrongs1")
			options("Russia", 525, 400, 250, 80, Black,user, 35, "Rights1")
			options("India", 50, 500, 250, 80, Black, user, 35, "wrongs1")	
		elif v1 == 4:
			gameDisplay.blit(testing4, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie1[v1],60,30,32,White)
			options("China", 50, 400, 250, 80, Black, user, 35, "wrongs1")
			options("Vietnam", 525, 500, 250, 80, Black, user, 35, "wrongs1")
			options("North Korea", 525, 400, 250, 80, Black,user, 35, "Rights1")
			options("Zimbabwe", 50, 500, 250, 80, Black, user, 35, "wrongs1")
		pygame.display.update()
		clock.tick(15)

#CHECK
def a1():
	global v1
	global alpha
	v1 = randint(0,4)
	alpha = True
	while alpha:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0)) 
		if v1 == 0:
			gameDisplay.blit(testing, (display_width/2 - 182,display_height/2-220)) 
			message_display(Countrie1[v1],60,30,32,White)
			options("Ontario", 50, 400, 250, 80, Black, user, 35, "wrong1")
			options("Nova Scotia", 50, 500, 250, 80, Black, user, 35, "wrong1")
			options("Nunavut", 525, 500, 250, 80, Black,user, 35, "Right1")
			options("Quebec", 525, 400, 250, 80, Black, user, 35, "wrong1")
		elif v1 == 1:
			gameDisplay.blit(testing1, (display_width/2 - 182,display_height/2-228))
			message_display(Countrie1[v1],130,30,32,White)
			options("Asia", 50, 400, 250, 80, Black, user, 35, "wrong1")
			options("North America", 50, 500, 250, 80, Black, user, 35, "wrong1")
			options("Europe", 525, 500, 250, 80, Black,user, 35, "Right1")
			options("Africa", 525, 400, 250, 80, Black, user, 35, "wrong1")	
		elif v1 == 2:
			gameDisplay.blit(testing2, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie1[v1],60,30,32,White)
			options("Nepal", 50, 500, 250, 80, Black, user, 35, "wrong1")
			options("North America", 525, 500, 250, 80, Black, user, 35, "wrong1")
			options("Canada", 50, 400, 250, 80, Black,user, 35, "Right1")
			options("Switzerland", 525, 400, 250, 80, Black, user, 35, "wrong1")	
		elif v1 == 3:
			gameDisplay.blit(testing3, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie1[v1],124,30,32,White)
			options("China", 50, 400, 250, 80, Black, user, 35, "wrong1")
			options("Canada", 525, 500, 250, 80, Black, user, 35, "wrong1")
			options("Russia", 525, 400, 250, 80, Black,user, 35, "Right1")
			options("India", 50, 500, 250, 80, Black, user, 35, "wrong1")
		elif v1 == 4:
			gameDisplay.blit(testing4, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie1[v1],60,30,32,White)
			options("China", 50, 400, 250, 80, Black, user, 35, "wrong1")
			options("Vietnam", 50, 500, 250, 80, Black, user, 35, "wrong1")
			options("North Korea", 525, 500, 250, 80, Black,user, 35, "Right1")
			options("Zimbabwe", 525, 400, 250, 80, Black, user, 35, "wrong1")	
		pygame.display.update()
		clock.tick(15)

def a2s():
	global v2
	global kilo
	kilo = True
	while kilo:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v2 == 0:
			gameDisplay.blit(testing5, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie2[v2],50,30,32,White)
			options("PEI", 50, 500, 250, 80, Black, user, 35, "wrongs2")
			options("Nova Scotia", 525, 500, 250, 80, Black, user, 35, "wrongs2")
			options("Nunavut", 50, 400, 250, 80, Black,user, 35, "Rights2")
			options("Alberta", 525, 400, 250, 80, Black, user, 35, "wrongs2")
		elif v2 == 1:
			gameDisplay.blit(testing6, (display_width/2 - 180,display_height/2-210))
			message_display(Countrie2[v2],57,30,32,White)
			options("China", 50, 400, 250, 80, Black, user, 35, "wrongs2")
			options("Vietnam", 525, 500, 250, 80, Black, user, 35, "wrongs2")
			options("South Korea", 525, 400, 250, 80, Black,user, 35, "Rights2")
			options("Sochi", 50, 500, 250, 80, Black, user, 35, "wrongs2")
		elif v2 == 2:
			gameDisplay.blit(testing101, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie2[v2],100,30,32,White)
			options("Uk", 50, 500, 250, 80, Black, user, 35, "wrongs2")
			options("Japan", 525, 500, 250, 80, Black, user, 35, "wrongs2")
			options("Vietnam", 50, 400, 250, 80, Black,user, 35, "Rights2")
			options("Us", 525, 400, 250, 80, Black, user, 35, "wrongs2")
		elif v2 == 3:
			gameDisplay.blit(testing102, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie2[v2],115,30,32,White)
			options("Artic", 50, 400, 250, 80, Black, user, 35, "wrongs2")
			options("Pacific", 50, 500, 250, 80, Black, user, 35, "wrongs2")
			options("Atlantic", 525, 500, 250, 80, Black,user, 35, "Rights2")
			options("India", 525, 400, 250, 80, Black, user, 35, "wrongs2")
		elif v2 == 4:
			gameDisplay.blit(testing7, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie2[v2],20,30,32,White)
			options("1", 50, 400, 250, 80, Black, user, 35, "wrongs2")
			options("3", 525, 500, 250, 80, Black, user, 35, "wrongs2")
			options("0", 50, 500, 250, 80, Black,user, 35, "Rights2")
			options("4", 525, 400, 250, 80, Black, user, 35, "wrongs2")


		pygame.display.update()
		clock.tick(15)

def a2():
	global v2
	global juliet
	v2 = randint(0,4)
	juliet = True
	while juliet:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v2 == 0:
			gameDisplay.blit(testing5, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie2[v2],50,30,32,White)
			options("PEI", 50, 500, 250, 80, Black, user, 35, "wrong2")
			options("Nova Scotia", 525, 500, 250, 80, Black, user, 35, "wrong2")
			options("Nunavut", 50, 400, 250, 80, Black,user, 35, "Right2")
			options("Alberta", 525, 400, 250, 80, Black, user, 35, "wrong2")
		elif v2 == 1:
			gameDisplay.blit(testing6, (display_width/2 - 180,display_height/2-210))
			message_display(Countrie2[v2],57,30,32,White)
			options("China", 50, 400, 250, 80, Black, user, 35, "wrong2")
			options("Vietnam", 50, 500, 250, 80, Black, user, 35, "wrong2")
			options("South Korea", 525, 500, 250, 80, Black,user, 35, "Right2")
			options("Sochi", 525, 400, 250, 80, Black, user, 35, "wrong2")
		elif v2 == 2:
			gameDisplay.blit(testing101, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie2[v2],100,30,32,White)
			options("Uk", 50, 400, 250, 80, Black, user, 35, "wrong2")
			options("Japan", 525, 500, 250, 80, Black, user, 35, "wrong2")
			options("Vietnam", 525, 400, 250, 80, Black,user, 35, "Right2")
			options("US", 50, 500, 250, 80, Black, user, 35, "wrong2")
		elif v2 == 3:
			gameDisplay.blit(testing102, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie2[v2],115,30,32,White)
			options("Artic", 50, 400, 250, 80, Black, user, 35, "wrong2")
			options("Pacific", 525, 500, 250, 80, Black, user, 35, "wrong2")
			options("Atlantic", 525, 400, 250, 80, Black,user, 35, "Right2")
			options("India", 50, 500, 250, 80, Black, user, 35, "wrong2")
		elif v2 == 4:
			gameDisplay.blit(testing7, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie2[v2],20,30,32,White)
			options("1", 50, 500, 250, 80, Black, user, 35, "wrong2")
			options("3", 525, 500, 250, 80, Black, user, 35, "wrong2")
			options("0", 50, 400, 250, 80, Black,user, 35, "Right2")
			options("4", 525, 400, 250, 80, Black, user, 35, "wrong2")

		pygame.display.update()
		clock.tick(15)

def a3s():
	global v3
	global kilo1
	kilo1 = True
	while kilo1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v3 == 0:
			gameDisplay.blit(testing103, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie3[v3],70,30,32,White)
			options("Uk", 50, 400, 250, 80, Black, user, 35, "wrongs3")
			options("India", 50, 500, 250, 80, Black, user, 35, "wrongs3")
			options("China", 525, 500, 250, 80, Black,user, 35, "Rights3")
			options("Russia", 525, 400, 250, 80, Black, user, 35, "wrongs3")
		elif v3 == 1:
			gameDisplay.blit(testing8, (display_width/2 - 182,display_height/2-160))
			message_display(Countrie3[v3],30,30,32,White)
			options("Southern", 50, 400, 250, 80, Black, user, 35, "wrongs3")
			options("Western", 525, 500, 250, 80, Black, user, 35, "wrongs3")
			options("Northern", 50, 500, 250, 80, Black,user, 35, "Rights3")
			options("Eastern", 525, 400, 250, 80, Black, user, 35, "wrongs3")
		elif v3 == 2:
			gameDisplay.blit(testing9, (display_width/2 - 182,display_height/2-190))
			message_display(Countrie3[v3],40,30,32,White)
			options("USA", 50, 400, 250, 80, Black, user, 35, "wrongs3")
			options("Hawaii", 525, 500, 250, 80, Black, user, 35, "wrongs3")
			options("Australia", 50, 500, 250, 80, Black,user, 35, "Rights3")
			options("Italy", 525, 400, 250, 80, Black, user, 35, "wrongs3")
		elif v3 == 3:
			gameDisplay.blit(testing10, (display_width/2 - 182,display_height/2-190))
			message_display(Countrie3[v3],116,30,32,White)
			options("Canada", 50, 400, 250, 80, Black, user, 35, "wrongs3")
			options("Switzerland", 50, 500, 250, 80, Black, user, 35, "wrongs3")
			options("Nepal", 525, 500, 250, 80, Black,user, 35, "Rights3")
			options("India", 525, 400, 250, 80, Black, user, 35, "wrongs3")
		elif v3 == 4:
			gameDisplay.blit(testing11, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie3[v3],45,30,32,White)
			options("Mexico", 50, 500, 250, 80, Black, user, 35, "wrongs3")
			options("USA", 525, 500, 250, 80, Black, user, 35, "wrongs3")
			options("Canada", 50, 400, 250, 80, Black,user, 35, "Rights3")
			options("Indonesia", 525, 400, 250, 80, Black, user, 35, "wrongs3")
		

		pygame.display.update()
		clock.tick(15)

def a3():
	global v3
	global juliet1
	v3 = randint(0,4)
	juliet1 = True
	while juliet1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v3 == 0:
			gameDisplay.blit(testing103, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie3[v3],70,30,32,White)
			options("Uk", 50, 400, 250, 80, Black, user, 35, "wrong3")
			options("India", 525, 500, 250, 80, Black, user, 35, "wrong3")
			options("China", 525, 400, 250, 80, Black,user, 35, "Right3")
			options("Russia", 50, 500, 250, 80, Black, user, 35, "wrong3")
		elif v3 == 1:
			gameDisplay.blit(testing8, (display_width/2 - 182,display_height/2-160))
			message_display(Countrie3[v3],30,30,32,White)
			options("Southern", 50, 400, 250, 80, Black, user, 35, "wrong3")
			options("Western", 525, 500, 250, 80, Black, user, 35, "wrong3")
			options("Northern", 525, 400, 250, 80, Black,user, 35, "Right3")
			options("Eastern", 50, 500, 250, 80, Black, user, 35, "wrong3")
		elif v3 == 2:
			gameDisplay.blit(testing9, (display_width/2 - 182,display_height/2-190))
			message_display(Countrie3[v3],40,30,32,White)
			options("USA", 50, 400, 250, 80, Black, user, 35, "wrong3")
			options("Hawaii", 50, 500, 250, 80, Black, user, 35, "wrong3")
			options("Australia", 525, 500, 250, 80, Black,user, 35, "Right3")
			options("Italy", 525, 400, 250, 80, Black, user, 35, "wrong3")
		elif v3 == 3:
			gameDisplay.blit(testing10, (display_width/2 - 182,display_height/2-190))
			message_display(Countrie3[v3],116,30,32,White)
			options("Canada", 50, 500, 250, 80, Black, user, 35, "wrong3")
			options("Switzerland", 525, 500, 250, 80, Black, user, 35, "wrong3")
			options("Nepal", 50, 400, 250, 80, Black,user, 35, "Right3")
			options("India", 525, 400, 250, 80, Black, user, 35, "wrong3")
		elif v3 == 4:
			gameDisplay.blit(testing11, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie3[v3],45,30,32,White)
			options("Mexico", 50, 400, 250, 80, Black, user, 35, "wrong3")
			options("USA", 525, 500, 250, 80, Black, user, 35, "wrong3")
			options("Canada", 525, 400, 250, 80, Black,user, 35, "Right3")
			options("Indonesia", 50, 500, 250, 80, Black, user, 35, "wrong3")
		pygame.display.update()
		clock.tick(15)

def a4():
	global juliet2
	global v4
	v4 = randint(0,4)
	juliet2 = True
	while juliet2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v4 == 0:
			gameDisplay.blit(testing12, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie4[v4],15,30,26,White)
			options("Atlantic", 50, 500, 250, 80, Black, user, 35, "wrong4")
			options("Pacific", 525, 500, 250, 80, Black, user, 35, "wrong4")
			options("Arctic", 50, 400, 250, 80, Black,user, 35, "Right4")
			options("Indian", 525, 400, 250, 80, Black, user, 35, "wrong4")
		elif v4 == 1:
			gameDisplay.blit(testing104, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie4[v4],70,30,35,White)
			options("Africa", 50, 400, 250, 80, Black, user, 35, "wrong4")
			options("North America", 50, 500, 250, 80, Black, user, 35, "wrong4")
			options("Asia", 525, 500, 250, 80, Black,user, 35, "Right4")
			options("Europe", 525, 400, 250, 80, Black, user, 35, "wrong4")
		elif v4 == 2:
			gameDisplay.blit(testing13, (display_width/2 - 182,display_height/2-185))
			message_display(Countrie4[v4],70,30,35,White)
			options("Africa", 50, 400, 250, 80, Black, user, 35, "wrong4")
			options("Asia", 50, 500, 250, 80, Black, user, 35, "wrong4")
			options("Australia", 525, 500, 250, 80, Black,user, 35, "Right4")
			options("Antartica", 525, 400, 250, 80, Black, user, 35, "wrong4")
		elif v4 == 3:
			gameDisplay.blit(testing14, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie4[v4],90,30,35,White)
			options("Norway", 50, 500, 250, 80, Black, user, 35, "wrong4")
			options("Iceland", 525, 500, 250, 80, Black, user, 35, "wrong4")
			options("Denmark", 50, 400, 250, 80, Black,user, 35, "Right4")
			options("Sweden", 525, 400, 250, 80, Black, user, 35, "wrong4")
		elif v4 == 4:
			gameDisplay.blit(testing15, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie4[v4],110,30,35,White)
			options("Indian ocean", 50, 400, 250, 80, Black, user, 35, "wrong4")
			options("Atlantic ocean", 525, 500, 250, 80, Black, user, 34, "wrong4")
			options("Pacfic ocean", 525, 400, 250, 80, Black,user, 35, "Right4")
			options("China sea", 50, 500, 250, 80, Black, user, 35, "wrong4")

		pygame.display.update()
		clock.tick(15)

def a4s():
	global v4
	global kilo2
	kilo2 = True
	while kilo2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v4 == 0:
			gameDisplay.blit(testing12, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie4[v4],15,30,26,White)
			options("Atlantic", 50, 400, 250, 80, Black, user, 35, "wrongs4")
			options("Pacific", 50, 500, 250, 80, Black, user, 35, "wrongs4")
			options("Arctic", 525, 500, 250, 80, Black,user, 35, "Rights4")
			options("Indian", 525, 400, 250, 80, Black, user, 35, "wrongs4")
		elif v4 == 1:
			gameDisplay.blit(testing104, (display_width/2 - 182,display_height/2-220))
			message_display(Countrie4[v4],70,30,35,White)
			options("Africa", 50, 500, 250, 80, Black, user, 35, "wrongs4")
			options("North America", 525, 500, 250, 80, Black, user, 35, "wrongs4")
			options("Asia", 50, 400, 250, 80, Black,user, 35, "Rights4")
			options("Europe", 525, 400, 250, 80, Black, user, 35, "wrongs4")
		elif v4 == 2:
			gameDisplay.blit(testing13, (display_width/2 - 182,display_height/2-185))
			message_display(Countrie4[v4],70,30,35,White)
			options("Africa", 50, 400, 250, 80, Black, user, 35, "wrongs4")
			options("Asia", 50, 500, 250, 80, Black, user, 35, "wrongs4")
			options("Australia", 525, 500, 250, 80, Black,user, 35, "Rights4")
			options("Antartica", 525, 400, 250, 80, Black, user, 35, "wrongs4")
		elif v4 == 3:
			gameDisplay.blit(testing14, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie4[v4],90,30,35,White)
			options("Norway", 50, 400, 250, 80, Black, user, 35, "wrongs4")
			options("Iceland", 525, 500, 250, 80, Black, user, 35, "wrongs4")
			options("Denmark", 50, 500, 250, 80, Black,user, 35, "Rights4")
			options("Sweden", 525, 400, 250, 80, Black, user, 35, "wrongs4")
		elif v4 == 4:
			gameDisplay.blit(testing15, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie4[v4],110,30,35,White)
			options("Indian ocean", 50, 500, 250, 80, Black, user, 35, "wrongs4")
			options("Atlantic ocean", 525, 500, 250, 80, Black, user, 34, "wrongs4")
			options("Pacfic ocean", 50, 400, 250, 80, Black,user, 35, "Rights4")
			options("China sea", 525, 400, 250, 80, Black, user, 35, "wrongs4")
		pygame.display.update()
		clock.tick(15)

def a5():
	global juliet3
	global v5
	v5 = randint(0,4)
	juliet3 = True
	while juliet3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v5 == 0:
			gameDisplay.blit(testing16, (display_width/2 - 182,display_height/2-185))
			message_display(Countrie5[v5],70,30,32,White)
			options("Italy", 50, 400, 250, 80, Black, user, 35, "wrong5")
			options("Hawaii", 525, 500, 250, 80, Black, user, 35, "wrong5")
			options("Vatican City", 525, 400, 250, 80, Black,user, 35, "Right5")
			options("Fiji", 50, 500, 250, 80, Black, user, 35, "wrong5")
		elif v5 == 1:
			gameDisplay.blit(testing17, (display_width/2 - 182,display_height/2-189))
			message_display(Countrie5[v5],10,30,33,White)
			options("New-York", 50, 400, 250, 80, Black, user, 35, "wrong5")
			options("Arizona", 50, 500, 250, 80, Black, user, 35, "wrong5")
			options("Hawaii", 525, 500, 250, 80, Black,user, 35, "Right5")
			options("Florida", 525, 400, 250, 80, Black, user, 35, "wrong5")
		elif v5 == 2:
			gameDisplay.blit(testing18, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie5[v5],110,30,35,White)
			options("Argentina", 50, 400, 250, 80, Black, user, 35, "wrong5")
			options("Brazil", 525, 500, 250, 80, Black, user, 35, "wrong5")
			options("Peru", 525, 400, 250, 80, Black,user, 35, "Right5")
			options("Congo", 50, 500, 250, 80, Black, user, 35, "wrong5")
		elif v5 == 3:
			gameDisplay.blit(testing19, (display_width/2 - 182,display_height/2-190))
			message_display(Countrie5[v5],110,30,35,White)
			options("Africa", 50, 500, 250, 80, Black, user, 35, "wrong5")
			options("Europe", 525, 500, 250, 80, Black, user, 35, "wrong5")
			options("South America", 50, 400, 250, 80, Black,user, 33, "Right5")
			options("Australia", 525, 400, 250, 80, Black, user, 35, "wrong5")
		elif v5 == 4:
			gameDisplay.blit(testing20, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie5[v5],10,30,35,White)
			options("Uganda", 50, 400, 250, 80, Black, user, 35, "wrong5")
			options("Egypt", 525, 500, 250, 80, Black, user, 35, "wrong5")
			options("Brazil", 50, 500, 250, 80, Black,user, 33, "Right5")
			options("Nepal", 525, 400, 250, 80, Black, user, 35, "wrong5")
		pygame.display.update()
		clock.tick(15)

def a5s():
	global v5
	global kilo3
	kilo3 = True
	while kilo3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background3, (0,0))
		if v5 == 0:
			gameDisplay.blit(testing16, (display_width/2 - 182,display_height/2-185))
			message_display(Countrie5[v5],70,30,32,White)
			options("Italy", 50, 500, 250, 80, Black, user, 35, "wrongs5")
			options("Hawaii", 525, 500, 250, 80, Black, user, 35, "wrongs5")
			options("Vatican City", 50, 400, 250, 80, Black,user, 35, "Rights5")
			options("Fiji", 525, 400, 250, 80, Black, user, 35, "wrongs5")
		elif v5 == 1:
			gameDisplay.blit(testing17, (display_width/2 - 182,display_height/2-189))
			message_display(Countrie5[v5],10,30,35,White)
			options("New-York", 50, 500, 250, 80, Black, user, 35, "wrongs5")
			options("Arizona", 525, 500, 250, 80, Black, user, 35, "wrongs5")
			options("Hawaii", 50, 400, 250, 80, Black,user, 35, "Rights5")
			options("Florida", 525, 400, 250, 80, Black, user, 35, "wrongs5")
		elif v5 == 2:
			gameDisplay.blit(testing18, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie5[v5],110,30,35,White)
			options("Argentina", 50, 400, 250, 80, Black, user, 35, "wrongs5")
			options("Brazil", 50, 500, 250, 80, Black, user, 35, "wrongs5")
			options("Peru", 525, 500, 250, 80, Black,user, 35, "Rights5")
			options("Congo", 525, 400, 250, 80, Black, user, 35, "wrongs5")
		elif v5 == 3:
			gameDisplay.blit(testing19, (display_width/2 - 182,display_height/2-190))
			message_display(Countrie5[v5],110,30,35,White)
			options("Africa", 50, 400, 250, 80, Black, user, 35, "wrongs5")
			options("Europe", 50, 500, 250, 80, Black, user, 35, "wrongs5")
			options("South America", 525, 500, 250, 80, Black,user, 33, "Rights5")
			options("Australia", 525, 400, 250, 80, Black, user, 35, "wrongs5")
		elif v5 == 4:
			gameDisplay.blit(testing20, (display_width/2 - 182,display_height/2-200))
			message_display(Countrie5[v5],10,30,35,White)
			options("Uganda", 50, 400, 250, 80, Black, user, 35, "wrongs5")
			options("Egypt", 525, 500, 250, 80, Black, user, 35, "wrongs5")
			options("Brazil", 525, 400, 250, 80, Black,user, 33, "Rights5")
			options("Nepal", 50, 500, 250, 80, Black, user, 35, "wrongs5")
		pygame.display.update()
		clock.tick(15)

def a6s():
	global v6 
	global kilo4
	kilo4 = True
	while kilo4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1111, (display_width/2 - 182,display_height/2-180))
		if v6 == 0:
			message_display(Mathematics1[v6],135,30,32,White)
			options("Mrs. Carmicheal", 50, 400, 250, 80, Black, user, 30, "wrongs6")
			options("Mr. Pikolon", 525, 500, 250, 80, Black, user, 35, "wrongs6")
			options("Mrs. Evans", 525, 400, 250, 80, Black,user, 35, "Rights6")
			options("Mr.Grey", 50, 500, 250, 80, Black, user, 35, "wrongs6")
		elif v6 == 1:
			message_display(Mathematics1[v6],135,30,32,White)
			options("2", 50, 400, 250, 80, Black, user, 35, "wrongs6")
			options("0", 50, 500, 250, 80, Black, user, 35, "wrongs6")
			options("1", 525, 500, 250, 80, Black,user, 35, "Rights6")
			options("3", 525, 400, 250, 80, Black, user, 35, "wrongs6")
		elif v6 == 2:
			message_display(Mathematics1[v6],90,30,32,White)
			options("Additon", 50, 500, 250, 80, Black, user, 35, "wrongs6")
			options("Exponents", 525, 500, 250, 80, Black, user, 35, "wrongs6")
			options("Brackets", 50, 400, 250, 80, Black,user, 35, "Rights6")
			options("Multipication", 525, 400, 250, 80, Black, user, 35, "wrongs6")
		elif v6 == 3:
			message_display(Mathematics1[v6],40,30,32,White)
			options("18", 50, 400, 250, 80, Black, user, 35, "wrongs6")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrongs6")
			options("14", 525, 400, 250, 80, Black,user, 35, "Rights6")
			options("12", 50, 500, 250, 80, Black, user, 35, "wrongs6")
		elif v6 == 4:
			message_display(Mathematics1[v6],100,30,28,White)
			options("z", 50, 400, 250, 80, Black, user, 35, "wrongs6")
			options("y", 525, 500, 250, 80, Black, user, 35, "wrongs6")
			options("x", 50, 500, 250, 80, Black,user, 35, "Rights6")
			options("a", 525, 400, 250, 80, Black, user, 35, "wrongs6")
		pygame.display.update()
		clock.tick(15)

def a6():
	global juliet4
	global v6
	v6 = randint(0,4)
	juliet4 = True
	while juliet4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1111, (display_width/2 - 182,display_height/2-180))
		if v6 == 0:
			message_display(Mathematics1[v6],135,30,32,White)
			options("Mrs. Carmicheal", 50, 400, 250, 80, Black, user, 30, "wrong6")
			options("Mr. Pikolon", 50, 500, 250, 80, Black, user, 35, "wrong6")
			options("Mrs. Evans", 525, 500, 250, 80, Black,user, 35, "Right6")
			options("Mr.Grey", 525, 400, 250, 80, Black, user, 35, "wrong6")
		elif v6 == 1:
			message_display(Mathematics1[v6],135,30,32,White)
			options("2", 50, 500, 250, 80, Black, user, 35, "wrong6")
			options("0", 525, 500, 250, 80, Black, user, 35, "wrong6")
			options("1", 50, 400, 250, 80, Black,user, 35, "Right6")
			options("3", 525, 400, 250, 80, Black, user, 35, "wrong6")
		elif v6 == 2:
			message_display(Mathematics1[v6],90,30,32,White)
			options("Additon", 50, 500, 250, 80, Black, user, 30, "wrong6")
			options("Exponents", 525, 500, 250, 80, Black, user, 35, "wrong6")
			options("Brackets", 50, 400, 250, 80, Black,user, 35, "Right6")
			options("Multipication", 525, 400, 250, 80, Black, user, 35, "wrong6")
		elif v6 == 3:
			message_display(Mathematics1[v6],40,30,32,White)
			options("18", 50, 400, 250, 80, Black, user, 35, "wrong6")
			options("1", 50, 500, 250, 80, Black, user, 35, "wrong6")
			options("14", 525, 500, 250, 80, Black,user, 35, "Right6")
			options("12", 525, 400, 250, 80, Black, user, 35, "wrong6")
		elif v6 == 4:
			message_display(Mathematics1[v6],100,30,28,White)
			options("z", 50, 400, 250, 80, Black, user, 35, "wrong6")
			options("y", 525, 500, 250, 80, Black, user, 35, "wrong6")
			options("x", 525, 400, 250, 80, Black,user, 35, "Right6")
			options("a", 50, 500, 250, 80, Black, user, 35, "wrong6")
		pygame.display.update()
		clock.tick(15)

def a7():
	global juliet5
	global v7
	v7 = randint(0,4)
	juliet5 = True
	while juliet5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1112, (display_width/2 - 182,display_height/2-180))
		if v7 == 0:
			message_display(Mathematics2[v7],15,30,25,White)
			options("Trigonometric", 50, 400, 250, 80, Black, user, 30, "wrong7")
			options("Logarithmic", 525, 500, 250, 80, Black, user, 35, "wrong7")
			options("Exponential", 525, 400, 250, 80, Black,user, 35, "Right7")
			options("Quadratic", 50, 500, 250, 80, Black, user, 35, "wrong7")
		elif v7 == 1:
			message_display(Mathematics2[v7],67,30,30,White)
			options("5", 50, 400, 250, 80, Black, user, 35, "wrong7")
			options("2", 525, 500, 250, 80, Black, user, 35, "wrong7")
			options("3", 525, 400, 250, 80, Black,user, 35, "Right7")
			options("4", 50, 500, 250, 80, Black, user, 35, "wrong7")
		elif v7 == 2:
			message_display(Mathematics2[v7],135,30,30,White)
			options("0", 50, 500, 250, 80, Black, user, 35, "wrong7")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrong7")
			options("2", 50, 400, 250, 80, Black,user, 35, "Right7")
			options("3", 525, 400, 250, 80, Black, user, 35, "wrong7")
		elif v7 == 3:
			message_display(Mathematics2[v7],152,30,30,White)
			options("3, 9, 18", 50, 400, 250, 80, Black, user, 35, "wrong7")
			options("3, 3, 3", 50, 500, 250, 80, Black, user, 35, "wrong7")
			options("3, 6, 9", 525, 500, 250, 80, Black,user, 35, "Right7")
			options("3, 9, 81", 525, 400, 250, 80, Black, user, 35, "wrong7")
		elif v7 == 4:
			message_display(Mathematics2[v7],250,30,30,White)
			options("1", 50, 400, 250, 80, Black, user, 35, "wrong7")
			options("Infinity", 50, 500, 250, 80, Black, user, 35, "wrong7")
			options("Undefined", 525, 500, 250, 80, Black,user, 35, "Right7")
			options("0", 525, 400, 250, 80, Black, user, 35, "wrong7")

		pygame.display.update()
		clock.tick(15)

def a7s():
	global v7 
	global kilo5
	kilo5 = True
	while kilo5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1112, (display_width/2 - 182,display_height/2-180))
		if v7 == 0:
			message_display(Mathematics2[v7],15,30,25,White)
			options("Trigonometric", 50, 400, 250, 80, Black, user, 30, "wrongs7")
			options("Logarithmic", 525, 500, 250, 80, Black, user, 35, "wrongs7")
			options("Exponential", 525, 400, 250, 80, Black,user, 35, "Rights7")
			options("Quadratic", 50, 500, 250, 80, Black, user, 35, "wrongs7")
		elif v7 == 1:
			message_display(Mathematics2[v7],67,30,30,White)
			options("5", 50, 400, 250, 80, Black, user, 35, "wrongs7")
			options("2", 50, 500, 250, 80, Black, user, 35, "wrongs7")
			options("3", 525, 500, 250, 80, Black,user, 35, "Rights7")
			options("4", 525, 400, 250, 80, Black, user, 35, "wrongs7")
		elif v7 == 2:
			message_display(Mathematics2[v7],135,30,30,White)
			options("0", 50, 500, 250, 80, Black, user, 35, "wrongs7")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrongs7")
			options("2", 50, 400, 250, 80, Black,user, 35, "Rights7")
			options("3", 525, 400, 250, 80, Black, user, 35, "wrongs7")
		elif v7 == 3:
			message_display(Mathematics2[v7],152,30,30,White)
			options("3, 9, 18", 50, 400, 250, 80, Black, user, 35, "wrongs7")
			options("3, 3, 3", 525, 500, 250, 80, Black, user, 35, "wrongs7")
			options("3, 6, 9", 50, 500, 250, 80, Black,user, 35, "Rights7")
			options("3, 9, 81", 525, 400, 250, 80, Black, user, 35, "wrongs7")
		elif v7 == 4:
			message_display(Mathematics2[v7],250,30,30,White)
			options("1", 50, 400, 250, 80, Black, user, 35, "wrongs7")
			options("Infinity", 525, 500, 250, 80, Black, user, 35, "wrongs7")
			options("Undefined", 50, 500, 250, 80, Black,user, 35, "Rights7")
			options("0", 525, 400, 250, 80, Black, user, 35, "wrongs7")
		pygame.display.update()
		clock.tick(15)


def a8s():
	global v8 
	global kilo6
	kilo6 = True
	while kilo6:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1113, (display_width/2 - 182,display_height/2-200))
		if v8 == 0:
			message_display(Mathematics3[v8],58,30,35,White)
			options("Derivative", 50, 400, 250, 80, Black, user, 35, "wrongs8")
			options("Subtraction", 50, 500, 250, 80, Black, user, 35, "wrongs8")
			options("Summation", 525, 500, 250, 80, Black,user, 35, "Rights8")
			options("Integration", 525, 400, 250, 80, Black, user, 35, "wrongs8")
		elif v8 == 1:
			message_display(Mathematics3[v8],15,30,29,White)
			options("Beta", 50, 500, 250, 80, Black, user, 35, "wrongs8")
			options("X", 525, 500, 250, 80, Black, user, 35, "wrongs8")
			options("Theta", 50, 400, 250, 80, Black,user, 35, "Rights8")
			options("Gamma", 525, 400, 250, 80, Black, user, 35, "wrongs8")
		elif v8 == 2:
			message_display(Mathematics3[v8],35,30,32,White)
			options("Vectors", 50, 400, 250, 80, Black, user, 35, "wrongs8")
			options("Logarithms", 525, 500, 250, 80, Black, user, 35, "wrongs8")
			options("Curvation", 525, 400, 250, 80, Black,user, 35, "Rights8")
			options("Diffrention", 50, 500, 250, 80, Black, user, 35, "wrongs8")
		elif v8 == 3:
			message_display(Mathematics3[v8],20,30,25,White)
			options("Simplify", 50, 400, 250, 80, Black, user, 35, "wrongs8")
			options("Add", 525, 500, 250, 80, Black, user, 35, "wrongs8")
			options("Prove", 525, 400, 250, 80, Black,user, 35, "Rights8")
			options("Solve", 50, 500, 250, 80, Black, user, 35, "wrongs8")
		elif v8 == 4:
			message_display(Mathematics3[v8],120,30,35,White)
			options("sin2a", 50, 400, 250, 80, Black, user, 35, "wrongs8")
			options("x+y=z", 50, 500, 250, 80, Black, user, 35, "wrongs8")
			options("sinx^2+cosx^2=1", 525, 500, 250, 80, Black,user, 26, "Rights8")
			options("a^2+b^2=c^2", 525, 400, 250, 80, Black, user, 35, "wrongs8")
		pygame.display.update()
		clock.tick(15)


def a8():
	global juliet6
	global v8
	v8 = randint(0,4)
	juliet6 = True
	while juliet6:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1113, (display_width/2 - 182,display_height/2-200))
		if v8 == 0:
			message_display(Mathematics3[v8],58,30,35,White)
			options("Derivative", 50, 500, 250, 80, Black, user, 35, "wrong8")
			options("Subtraction", 525, 500, 250, 80, Black, user, 35, "wrong8")
			options("Summation", 50, 400, 250, 80, Black,user, 35, "Right8")
			options("Integration", 525, 400, 250, 80, Black, user, 35, "wrong8")
		elif v8 == 1:
			message_display(Mathematics3[v8],15,30,29,White)
			options("Beta", 50, 400, 250, 80, Black, user, 35, "wrong8")
			options("X", 525, 500, 250, 80, Black, user, 35, "wrong8")
			options("Theta", 525, 400, 250, 80, Black,user, 35, "Right8")
			options("Gamma", 50, 500, 250, 80, Black, user, 35, "wrong8")
		elif v8 == 2:
			message_display(Mathematics3[v8],35,30,32,White)
			options("Vectors", 50, 400, 250, 80, Black, user, 35, "wrong8")
			options("Logarithms", 525, 500, 250, 80, Black, user, 35, "wrong8")
			options("Curvation", 50, 500, 250, 80, Black,user, 35, "Right8")
			options("Diffrention", 525, 400, 250, 80, Black, user, 35, "wrong8")
		elif v8 == 3:
			message_display(Mathematics3[v8],20,30,25,White)
			options("Simply", 50, 400, 250, 80, Black, user, 35, "wrong8")
			options("Add", 50, 500, 250, 80, Black, user, 35, "wrong8")
			options("Prove", 525, 500, 250, 80, Black,user, 35, "Right8")
			options("Solve", 525, 400, 250, 80, Black, user, 35, "wrong8")
		elif v8 == 4:
			message_display(Mathematics3[v8],120,30,35,White)
			options("sin2a", 50, 500, 250, 80, Black, user, 35, "wrong8")
			options("x+y=z", 525, 500, 250, 80, Black, user, 35, "wrong8")
			options("sinx^2+cosx^2=1", 50, 400, 250, 80, Black,user, 26, "Right8")
			options("a^2+b^2=c^2", 525, 400, 250, 80, Black, user, 35, "wrong8")
		pygame.display.update()
		clock.tick(15)

def a9s():
	global v9 
	global kilo7
	kilo7 = True
	while kilo7:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1114, (display_width/2 - 182,display_height/2-200))
		if v9 == 0:
			message_display(Mathematics4[v9],12,30,30,White)
			options("Y", 50, 400, 250, 80, Black, user, 35, "wrongs9")
			options("X", 525, 500, 250, 80, Black, user, 35, "wrongs9")
			options("i", 525, 400, 250, 80, Black,user, 35, "Rights9")
			options("iota", 50, 500, 250, 80, Black, user, 35, "wrongs9")
		elif v9 == 1:
			message_display(Mathematics4[v9],150,30,35,White)
			options("Y", 50, 400, 250, 80, Black, user, 35, "wrongs9")
			options("10", 525, 500, 250, 80, Black, user, 35, "wrongs9")
			options("X", 525, 400, 250, 80, Black,user, 35, "Rights9")
			options("0", 50, 500, 250, 80, Black, user, 35, "wrongs9")
		elif v9 == 2:
			message_display(Mathematics4[v9],216,30,35,White)
			options("Maybe", 50, 400, 250, 80, Black, user, 35, "wrongs9")
			options("No", 525, 500, 250, 80, Black, user, 35, "wrongs9")
			options("Yes", 50, 400, 250, 80, Black,user, 35, "Rights9")
			options("IDK", 525, 400, 250, 80, Black, user, 35, "wrongs9")
		elif v9 == 3:
			message_display(Mathematics4[v9],15,30,32,White)
			options("Definite Maximum", 50, 400, 250, 80, Black, user, 26, "wrongs9")
			options("Maxmini", 525, 500, 250, 80, Black, user, 35, "wrongs9")
			options("Minimax", 50, 500, 250, 80, Black,user, 35, "Rights9")
			options("Definite Minimum", 525, 400, 250, 80, Black, user, 26, "wrongs9")
		elif v9 == 4:
			message_display(Mathematics4[v9],105,30,35,White)
			options("NADH", 50, 400, 250, 80, Black, user, 35, "wrongs9")
			options("AROC", 525, 500, 250, 80, Black, user, 35, "wrongs9")
			options("IROC", 525, 400, 250, 80, Black,user, 35, "Rights9")
			options("FADH", 50, 500, 250, 80, Black, user, 35, "wrongs9") 
		pygame.display.update()
		clock.tick(15)

def a9():
	global juliet7
	global v9
	v9 = randint(0,4)
	juliet7 = True
	while juliet7:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1114, (display_width/2 - 182,display_height/2-200))
		if v9 == 0:
			message_display(Mathematics4[v9],12,30,30,White)
			options("Y", 50, 500, 250, 80, Black, user, 35, "wrong9")
			options("X", 525, 500, 250, 80, Black, user, 35, "wrong9")
			options("i", 50, 400, 250, 80, Black,user, 35, "Right9")
			options("iota", 525, 400, 250, 80, Black, user, 35, "wrong9")
		elif v9 == 1:
			message_display(Mathematics4[v9],150,30,35,White)
			options("Y", 50, 400, 250, 80, Black, user, 35, "wrong9")
			options("10", 50, 500, 250, 80, Black, user, 35, "wrong9")
			options("X", 525, 500, 250, 80, Black,user, 35, "Right9")
			options("0", 525, 400, 250, 80, Black, user, 35, "wrong9")
		elif v9 == 2:
			message_display(Mathematics4[v9],216,30,35,White)
			options("Maybe", 50, 400, 250, 80, Black, user, 35, "wrong9")
			options("No", 525, 500, 250, 80, Black, user, 35, "wrong9")
			options("Yes", 525, 400, 250, 80, Black,user, 35, "Right9")
			options("IDK", 50, 500, 250, 80, Black, user, 35, "wrong9")
		elif v9 == 3:
			message_display(Mathematics4[v9],15,30,32,White)
			options("Definite Maximum", 50, 400, 250, 80, Black, user, 26, "wrong9")
			options("Maxmini", 50, 500, 250, 80, Black, user, 35, "wrong9")
			options("Minimax", 525, 500, 250, 80, Black,user, 35, "Right9")
			options("Definite Minimum", 525, 400, 250, 80, Black, user, 26, "wrong9")
		elif v9 == 4:
			message_display(Mathematics4[v9],105,30,35,White)
			options("NADH", 50, 500, 250, 80, Black, user, 35, "wrong9")
			options("AROC", 525, 500, 250, 80, Black, user, 35, "wrong9")
			options("IROC", 50, 400, 250, 80, Black,user, 35, "Right9")
			options("FADH", 525, 400, 250, 80, Black, user, 35, "wrong9")
		pygame.display.update()
		clock.tick(15)

def a10s():
	global v10
	global kilo8
	kilo8 = True
	while kilo8:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1115, (display_width/2 - 182,display_height/2-200))
		if v10 == 0:
			message_display(Mathematics5[v10],55,30,35,White)
			options("Einstien", 50, 400, 250, 80, Black, user, 35, "wrongs10")
			options("Libneez", 525, 500, 250, 80, Black, user, 35, "wrongs10")
			options("Newton", 525, 400, 250, 80, Black,user, 35, "Rights10")
			options("Gotfied", 50, 500, 250, 80, Black, user, 35, "wrongs10")
		elif v10 == 1:
			message_display(Mathematics5[v10],14,30,26,White)
			options("X", 50, 400, 250, 80, Black, user, 35, "wrongs10")
			options("1", 50, 500, 250, 80, Black, user, 35, "wrongs10")
			options("0", 525, 500, 250, 80, Black,user, 35, "Rights10")
			options("Infinity", 525, 400, 250, 80, Black, user, 35, "wrongs10")
		elif v10 == 2:
			message_display(Mathematics5[v10],97,30,35,White)
			options("Even function", 50, 400, 250, 80, Black, user, 35, "wrongs10")
			options("X axis", 50, 500, 250, 80, Black, user, 35, "wrongs10")
			options("Y axis", 525, 500, 250, 80, Black,user, 35, "Rights10")
			options("Odd function", 525, 400, 250, 80, Black, user, 35, "wrongs10")
		elif v10 == 3:
			message_display(Mathematics5[v10],125,30,35,White)
			options("%", 50, 400, 250, 80, Black, user, 35, "wrongs10")
			options("<>", 525, 500, 250, 80, Black, user, 35, "wrongs10")
			options("!", 525, 400, 250, 80, Black,user, 35, "Rights10")
			options("&&", 50, 500, 250, 80, Black, user, 35, "wrongs10")
		elif v10 == 4:
			message_display(Mathematics5[v10],75,30,35,White)
			options("sec(x)", 50, 500, 250, 80, Black, user, 35, "wrongs10")
			options("sin(x)", 525, 500, 250, 80, Black, user, 35, "wrongs10")
			options("tan(x)", 50, 400, 250, 80, Black,user, 35, "Rights10")
			options("csc(x)", 525, 400, 250, 80, Black, user, 35, "wrongs10")
		pygame.display.update()
		clock.tick(15)


def a10():
	global juliet8
	global v10
	v10 = randint(0,4)
	juliet8 = True
	while juliet8:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(testing1115, (display_width/2 - 182,display_height/2-200))
		if v10 == 0:
			message_display(Mathematics5[v10],55,30,35,White)
			options("Einstien", 50, 500, 250, 80, Black, user, 35, "wrong10")
			options("Libneez", 525, 500, 250, 80, Black, user, 35, "wrong10")
			options("Newton", 50, 400, 250, 80, Black,user, 35, "Right10")
			options("Gotfied", 525, 400, 250, 80, Black, user, 35, "wrong10")
		elif v10 == 1:
			message_display(Mathematics5[v10],14,30,26,White)
			options("X", 50, 400, 250, 80, Black, user, 35, "wrong10")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrong10")
			options("0", 525, 400, 250, 80, Black,user, 35, "Right10")
			options("Infinity", 50, 500, 250, 80, Black, user, 35, "wrong10")
		elif v10 == 2:
			message_display(Mathematics5[v10],97,30,35,White)
			options("Even function", 50, 400, 250, 80, Black, user, 35, "wrong10")
			options("X axis", 50, 500, 250, 80, Black, user, 35, "wrong10")
			options("Y axis", 525, 500, 250, 80, Black,user, 35, "Right10")
			options("Odd function", 525, 400, 250, 80, Black, user, 35, "wrong10")
		elif v10 == 3:
			message_display(Mathematics5[v10],125,30,35,White)
			options("%", 50, 400, 250, 80, Black, user, 35, "wrong10")
			options("<>", 50, 500, 250, 80, Black, user, 35, "wrong10")
			options("!", 525, 500, 250, 80, Black,user, 35, "Right10")
			options("&&", 525, 400, 250, 80, Black, user, 35, "wrong10")
		elif v10 == 4:
			message_display(Mathematics5[v10],75,30,35,White)
			options("sec(x)", 50, 400, 250, 80, Black, user, 35, "wrong10")
			options("sin(x)", 525, 500, 250, 80, Black, user, 35, "wrong10")
			options("tan(x)", 525, 400, 250, 80, Black,user, 35, "Right10")
			options("csc(x)", 50, 500, 250, 80, Black, user, 35, "wrong10")
		pygame.display.update()
		clock.tick(15)

def a11s():
	global v11
	global kilo9
	kilo9 = True
	while kilo9:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v11 == 0:
			gameDisplay.blit(testing21, (display_width/2 - 182,display_height/2-190))
			message_display(GK1[v11],21,30,30,Black)
			options("Boeing-777", 50, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Boeing-787", 525, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Airbus A380", 50, 400, 250, 80, Black,user, 35, "Rights11")
			options("Boeing-797", 525, 400, 250, 80, Black, user, 35, "wrongs11")
		elif v11 == 1:
			gameDisplay.blit(testing23, (display_width/2 - 182,display_height/2-200))
			message_display(GK1[v11],115,30,35,Black)
			options("Uranus", 50, 400, 250, 80, Black, user, 35, "wrongs11")
			options("Venus", 50, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Mercury", 525, 500, 250, 80, Black,user, 35, "Rights11")
			options("Mars", 525, 400, 250, 80, Black, user, 35, "wrongs11")
		elif v11 == 2:
			gameDisplay.blit(testing106, (display_width/2 - 182,display_height/2-220))
			message_display(GK1[v11],205,30,35,Black)
			options("Joules", 50, 400, 250, 80, Black, user, 35, "wrongs11")
			options("Kilogram", 525, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Newton", 525, 400, 250, 80, Black,user, 35, "Rights11")
			options("Pounds", 50, 500, 250, 80, Black, user, 35, "wrongs11")
		elif v11 == 3:
			gameDisplay.blit(testing107, (display_width/2 - 182,display_height/2-220))
			message_display(GK1[v11],225,30,35,Black)
			options("Universe", 50, 400, 250, 80, Black, user, 35, "wrongs11")
			options("Andromeda", 50, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Milky Way", 525, 500, 250, 80, Black,user, 35, "Rights11")
			options("Sun", 525, 400, 250, 80, Black, user, 35, "wrongs11")
		elif v11 == 4:
			gameDisplay.blit(testing24, (display_width/2 - 182,display_height/2-200))
			message_display(GK1[v11],110,30,35,Black)
			options("Poppy", 50, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Sunflower", 525, 500, 250, 80, Black, user, 35, "wrongs11")
			options("Trillum", 50, 400, 250, 80, Black,user, 35, "Rights11")
			options("Lavender", 525, 400, 250, 80, Black, user, 35, "wrongs11")
		pygame.display.update()
		clock.tick(15)

def a11():
	global juliet9
	global v11
	v11 = randint(0,4)
	juliet9 = True
	while juliet9:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v11 == 0:
			gameDisplay.blit(testing21, (display_width/2 - 182,display_height/2-190))
			message_display(GK1[v11],21,30,30,Black)
			options("Boeing-777", 50, 400, 250, 80, Black, user, 35, "wrong11")
			options("Boeing-787", 525, 500, 250, 80, Black, user, 35, "wrong11")
			options("Airbus A380", 525, 400, 250, 80, Black,user, 35, "Right11")
			options("Boeing-797", 50, 500, 250, 80, Black, user, 35, "wrong11")
		elif v11 == 1:
			gameDisplay.blit(testing23, (display_width/2 - 182,display_height/2-200))
			message_display(GK1[v11],115,30,35,Black)
			options("Uranus", 50, 400, 250, 80, Black, user, 35, "wrong11")
			options("Venus", 50, 500, 250, 80, Black, user, 35, "wrong11")
			options("Mercury", 525, 500, 250, 80, Black,user, 35, "Right11")
			options("Mars", 525, 400, 250, 80, Black, user, 35, "wrong11")
		elif v11 == 2:
			gameDisplay.blit(testing106, (display_width/2 - 182,display_height/2-220))
			message_display(GK1[v11],205,30,35,Black)
			options("Joules", 50, 500, 250, 80, Black, user, 35, "wrong11")
			options("Kilogram", 525, 500, 250, 80, Black, user, 35, "wrong11")
			options("Newton", 50, 400, 250, 80, Black,user, 35, "Right11")
			options("Pounds", 525, 400, 250, 80, Black, user, 35, "wrong11")
		elif v11 == 3:
			gameDisplay.blit(testing107, (display_width/2 - 182,display_height/2-220))
			message_display(GK1[v11],225,30,35,Black)
			options("Universe", 50, 400, 250, 80, Black, user, 35, "wrong11")
			options("Andromeda", 525, 500, 250, 80, Black, user, 35, "wrong11")
			options("Milky Way", 525, 400, 250, 80, Black,user, 35, "Right11")
			options("Sun", 50, 500, 250, 80, Black, user, 35, "wrong11")
		elif v11 == 4:
			gameDisplay.blit(testing24, (display_width/2 - 182,display_height/2-200))
			message_display(GK1[v11],110,30,35,Black)
			options("Poppy", 50, 400, 250, 80, Black, user, 35, "wrong11")
			options("Sunflower", 50, 500, 250, 80, Black, user, 35, "wrong11")
			options("Trillum", 525, 500, 250, 80, Black,user, 35, "Right11")
			options("Lavender", 525, 400, 250, 80, Black, user, 35, "wrong11")
		pygame.display.update()
		clock.tick(15)

def a12s():
	global v12
	global kilo10
	kilo10 = True
	while kilo10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v12 == 0:
			gameDisplay.blit(testing26, (display_width/2 - 182,display_height/2-230))
			message_display(GK2[v12],95,30,35,Black)
			options("Gravel", 50, 500, 250, 80, Black, user, 35, "wrongs12")
			options("Bitumen", 525, 500, 250, 80, Black, user, 35, "wrongs12")
			options("Tarmac", 50, 400, 250, 80, Black,user, 35, "Rights12")
			options("Aggregate", 525, 400, 250, 80, Black, user, 35, "wrongs12")
		elif v12 == 1:
			gameDisplay.blit(testing27, (display_width/2 - 182,display_height/2-190))
			message_display(GK2[v12],70,30,35,Black)
			options("Octnary", 50, 400, 250, 80, Black, user, 35, "wrongs12")
			options("Decimal", 50, 500, 250, 80, Black, user, 35, "wrongs12")
			options("Binary", 525, 500, 250, 80, Black,user, 35, "Rights12")
			options("Base 10", 525, 400, 250, 80, Black, user, 35, "wrongs12")
		elif v12 == 2:
			gameDisplay.blit(testing28, (display_width/2 - 182,display_height/2-200))
			message_display(GK2[v12],50,30,35,Black)
			options("Ruddur", 50, 400, 250, 80, Black, user, 35, "wrongs12")
			options("Fuselage", 525, 500, 250, 80, Black, user, 35, "wrongs12")
			options("Wing", 525, 400, 250, 80, Black,user, 35, "Rights12")
			options("Flaps", 50, 500, 250, 80, Black, user, 35, "wrongs12")
		elif v12 == 3:
			gameDisplay.blit(testing29, (display_width/2 - 182,display_height/2-220))
			message_display(GK2[v12],35,30,35,Black)
			options("Barlley", 50, 400, 250, 80, Black, user, 35, "wrongs12")
			options("Wheat", 50, 500, 250, 80, Black, user, 35, "wrongs12")
			options("Maize", 525, 500, 250, 80, Black,user, 35, "Rights12")
			options("Oatmeal", 525, 400, 250, 80, Black, user, 35, "wrongs12")
		elif v12 == 4:
			gameDisplay.blit(testing30, (display_width/2 - 182,display_height/2-216))
			message_display(GK2[v12],175,30,35,Black)
			options("Rubbers", 50, 400, 250, 80, Black, user, 35, "wrongs12")
			options("Plastics", 525, 500, 250, 80, Black, user, 35, "wrongs12")
			options("Insulators", 50, 500, 250, 80, Black,user, 35, "Rights12")
			options("Conduator", 525, 400, 250, 80, Black, user, 35, "wrongs12")
		pygame.display.update()
		clock.tick(15)


def a12():
	global juliet10
	global v12
	v12 = randint(0,4)
	juliet10 = True
	while juliet10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v12 == 0:
			gameDisplay.blit(testing26, (display_width/2 - 182,display_height/2-230))
			message_display(GK2[v12],95,30,35,Black)
			options("Gravel", 50, 500, 250, 80, Black, user, 35, "wrong12")
			options("Bitumen", 525, 500, 250, 80, Black, user, 35, "wrong12")
			options("Tarmac", 50, 400, 250, 80, Black,user, 35, "Right12")
			options("Aggregate", 525, 400, 250, 80, Black, user, 35, "wrong12")
		elif v12 == 1:
			gameDisplay.blit(testing27, (display_width/2 - 182,display_height/2-190))
			message_display(GK2[v12],70,30,35,Black)
			options("Octnary", 50, 400, 250, 80, Black, user, 35, "wrong12")
			options("Decimal", 50, 500, 250, 80, Black, user, 35, "wrong12")
			options("Binary", 525, 500, 250, 80, Black,user, 35, "Right12")
			options("Base 10", 525, 400, 250, 80, Black, user, 35, "wrong12")
		elif v12 == 2:
			gameDisplay.blit(testing28, (display_width/2 - 182,display_height/2-200))
			message_display(GK2[v12],50,30,35,Black)
			options("Ruddur", 50, 400, 250, 80, Black, user, 35, "wrong12")
			options("Fuselage", 50, 500, 250, 80, Black, user, 35, "wrong12")
			options("Wing", 525, 500, 250, 80, Black,user, 35, "Right12")
			options("Flaps", 525, 400, 250, 80, Black, user, 35, "wrong12")
		elif v12 == 3:
			gameDisplay.blit(testing29, (display_width/2 - 182,display_height/2-220))
			message_display(GK2[v12],35,30,35,Black)
			options("Barlley", 50, 400, 250, 80, Black, user, 35, "wrong12")
			options("Wheat", 525, 500, 250, 80, Black, user, 35, "wrong12")
			options("Maize", 525, 400, 250, 80, Black,user, 35, "Right12")
			options("Oatmeal", 50, 500, 250, 80, Black, user, 35, "wrong12")
		elif v12 == 4:
			gameDisplay.blit(testing30, (display_width/2 - 182,display_height/2-216))
			message_display(GK2[v12],175,30,35,Black)
			options("Rubbers", 50, 500, 250, 80, Black, user, 35, "wrong12")
			options("Plastics", 525, 500, 250, 80, Black, user, 35, "wrong12")
			options("Insulators", 50, 400, 250, 80, Black,user, 35, "Right12")
			options("Conduator", 525, 400, 250, 80, Black, user, 35, "wrong12")
		pygame.display.update()
		clock.tick(15)

def a13s():
	global v13
	global kilo11
	kilo11 = True
	while kilo11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v13 == 0:
			gameDisplay.blit(testing31, (display_width/2 - 182,display_height/2-200))
			message_display(GK3[v13],270,30,35,Black)
			options("Canadian Brodcasting Cooperation", 50, 400, 250, 80, Black, user, 13, "wrongs13")
			options("Canadian Binding Corporation", 525, 500, 250, 80, Black, user, 15, "wrongs13")
			options("Canadian Brodcasting Corporation", 525, 400, 250, 80, Black,user, 13, "Rights13")
			options("Casting Brodcasting in Canada", 50, 500, 250, 80, Black, user, 15, "wrongs13")
		elif v13 == 1:
			gameDisplay.blit(testing32, (display_width/2 - 182,display_height/2-200))
			message_display(GK3[v13],5,30,32,Black)
			options("Europe", 50, 400, 250, 80, Black, user, 35, "wrongs13")
			options("North America", 50, 500, 250, 80, Black, user, 35, "wrongs13")
			options("Asia", 525, 500, 250, 80, Black,user, 35, "Rights13")
			options("Africa", 525, 400, 250, 80, Black, user, 35, "wrongs13")
		elif v13 == 2:
			gameDisplay.blit(testing109, (display_width/2 - 182,display_height/2-220))
			message_display(GK3[v13],17,26,25,Black)
			options("Ontario", 50, 500, 250, 80, Black, user, 35, "wrongs13")
			options("Quebec", 525, 500, 250, 80, Black, user, 35, "wrongs13")
			options("Nunavut", 50, 400, 250, 80, Black,user, 35, "Rights13")
			options("Alberta", 525, 400, 250, 80, Black, user, 35, "wrongs13")
		elif v13 == 3:
			gameDisplay.blit(testing33, (display_width/2 - 182,display_height/2-200))
			message_display(GK3[v13],25,26,35,Black)
			options("Fungi", 50, 500, 250, 80, Black, user, 35, "wrongs13")
			options("Worms", 525, 500, 250, 80, Black, user, 35, "wrongs13")
			options("Bacteria", 50, 400, 250, 80, Black,user, 35, "Rights13")
			options("Protist", 525, 400, 250, 80, Black, user, 35, "wrongs13")
		elif v13 == 4:
			gameDisplay.blit(testing108, (display_width/2 - 182,display_height/2-220))
			message_display(GK3[v13],95,26,32,Black)
			options("15 Billion", 50, 400, 250, 80, Black, user, 35, "wrongs13")
			options("10 Billion", 525, 500, 250, 80, Black, user, 35, "wrongs13")
			options("11 Billion", 525, 400, 250, 80, Black,user, 35, "Rights13")
			options("14 Billion", 50, 500, 250, 80, Black, user, 35, "wrongs13")
		pygame.display.update()
		clock.tick(15)


def a13():
	global juliet11
	global v13
	v13 = randint(0,4)
	juliet11 = True
	while juliet11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v13 == 0:
			gameDisplay.blit(testing31, (display_width/2 - 182,display_height/2-200))
			message_display(GK3[v13],270,30,35,Black)
			options("Canadian Brodcasting Cooperation", 50, 400, 250, 80, Black, user, 13, "wrong13")
			options("Canadian Binding Corporation", 525, 500, 250, 80, Black, user, 15, "wrong13")
			options("Canadian Brodcasting Corporation", 50, 500, 250, 80, Black,user, 13, "Right13")
			options("Casting Brodcasting in Canada", 525, 400, 250, 80, Black, user, 15, "wrong13")
		elif v13 == 1:
			gameDisplay.blit(testing32, (display_width/2 - 182,display_height/2-200))
			message_display(GK3[v13],5,30,32,Black)
			options("Europe", 50, 400, 250, 80, Black, user, 35, "wrong13")
			options("North America", 525, 500, 250, 80, Black, user, 35, "wrong13")
			options("Asia", 50, 500, 250, 80, Black,user, 35, "Right13")
			options("Africa", 525, 400, 250, 80, Black, user, 35, "wrong13")
		elif v13 == 2:
			gameDisplay.blit(testing109, (display_width/2 - 182,display_height/2-220))
			message_display(GK3[v13],17,26,25,Black)
			options("Ontario", 50, 400, 250, 80, Black, user, 35, "wrong13")
			options("Quebec", 525, 500, 250, 80, Black, user, 35, "wrong13")
			options("Nunavut", 525, 400, 250, 80, Black,user, 35, "Right13")
			options("Alberta", 50, 500, 250, 80, Black, user, 35, "wrong13")
		elif v13 == 3:
			gameDisplay.blit(testing33, (display_width/2 - 182,display_height/2-200))
			message_display(GK3[v13],25,26,35,Black)
			options("Fungi", 50, 500, 250, 80, Black, user, 35, "wrong13")
			options("Worms", 525, 500, 250, 80, Black, user, 35, "wrong13")
			options("Bacteria", 50, 400, 250, 80, Black,user, 35, "Right13")
			options("Protist", 525, 400, 250, 80, Black, user, 35, "wrong13")
		elif v13 == 4:
			gameDisplay.blit(testing108, (display_width/2 - 182,display_height/2-220))
			message_display(GK3[v13],95,26,32,Black)
			options("15 Billion", 50, 400, 250, 80, Black, user, 35, "wrong13")
			options("10 Billion", 50, 500, 250, 80, Black, user, 35, "wrong13")
			options("11 Billion", 525, 500, 250, 80, Black,user, 35, "Right13")
			options("14 Billion", 525, 400, 250, 80, Black, user, 35, "wrong13")

		pygame.display.update()
		clock.tick(15)

def a14s():
	global v14
	global kilo12
	kilo12 = True
	while kilo12:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v14 == 0:
			gameDisplay.blit(testing34, (display_width/2 - 182,display_height/2-200))
			message_display(GK4[v14],5,30,27,Black)
			options("Messier-121", 50, 400, 250, 80, Black, user, 35, "wrongs14")
			options("Whirlpool", 525, 500, 250, 80, Black, user, 35, "wrongs14")
			options("Andromeda", 525, 400, 250, 80, Black,user, 35, "Rights14")
			options("Centarus B", 50, 500, 250, 80, Black, user, 35, "wrongs14")
		elif v14 == 1:
			gameDisplay.blit(testing36, (display_width/2 - 182,display_height/2-200))
			message_display(GK4[v14],125,30,35,Black)
			options("Lines", 50, 500, 250, 80, Black, user, 35, "wrongs14")
			options("Colors", 525, 500, 250, 80, Black, user, 35, "wrongs14")
			options("Pixels", 50, 400, 250, 80, Black,user, 35, "Rights14")
			options("Shapes", 525, 400, 250, 80, Black, user, 35, "wrongs14")
		elif v14 == 2:
			gameDisplay.blit(testing110, (display_width/2 - 182,display_height/2-220))
			message_display(GK4[v14],95,30,35,Black)
			options("Uninturuptted Socket Bus", 50, 400, 250, 80, Black, user, 19, "wrongs14")
			options("United Serial Bus", 50, 500, 250, 80, Black, user, 26, "wrongs14")
			options("Universal Serial Bus", 525, 500, 250, 80, Black,user, 22, "Rights14")
			options("United Shaped Bus", 525, 400, 250, 80, Black, user, 22, "wrongs14")
		elif v14 == 3:
			gameDisplay.blit(testing111, (display_width/2 - 182,display_height/2-220))
			message_display(GK4[v14],190,30,35,Black)
			options("Pi Bonds", 50, 400, 250, 80, Black, user, 35, "wrongs14")
			options("Small Hydrocarbons", 525, 500, 250, 80, Black, user, 22, "wrongs14")
			options("Polymers", 525, 400, 250, 80, Black,user, 35, "Right1s4")
			options("4,2 octene", 50, 500, 250, 80, Black, user, 35, "wrongs14")
		elif v14 == 4:
			gameDisplay.blit(testing37, (display_width/2 - 182,display_height/2-216))
			message_display(GK4[v14],25,30,35,Black)
			options("1541", 50, 400, 250, 80, Black, user, 35, "wrongs14")
			options("2451", 525, 500, 250, 80, Black, user, 35, "wrongs14")
			options("2501", 50, 500, 250, 80, Black,user, 35, "Rights14")
			options("2546", 525, 400, 250, 80, Black, user, 35, "wrongs14")
		pygame.display.update()
		clock.tick(15)

def a14():
	global juliet12
	global v14
	v14 = randint(0,4)
	juliet12 = True
	while juliet12:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v14 == 0:
			gameDisplay.blit(testing34, (display_width/2 - 182,display_height/2-200))
			message_display(GK4[v14],5,30,27,Black)
			options("Messier-121", 50, 400, 250, 80, Black, user, 35, "wrong14")
			options("Whirlpool", 525, 500, 250, 80, Black, user, 35, "wrong14")
			options("Andromeda", 525, 400, 250, 80, Black,user, 35, "Right14")
			options("Centarus B", 50, 500, 250, 80, Black, user, 35, "wrong14")
		elif v14 == 1:
			gameDisplay.blit(testing36, (display_width/2 - 182,display_height/2-200))
			message_display(GK4[v14],125,30,35,Black)
			options("Lines", 50, 400, 250, 80, Black, user, 35, "wrong14")
			options("Colors", 50, 500, 250, 80, Black, user, 35, "wrong14")
			options("Pixels", 525, 500, 250, 80, Black,user, 35, "Right14")
			options("Shapes", 525, 400, 250, 80, Black, user, 35, "wrong14")
		elif v14 == 2:
			gameDisplay.blit(testing110, (display_width/2 - 182,display_height/2-220))
			message_display(GK4[v14],95,30,35,Black)
			options("Uninturuptted Socket Bus", 50, 500, 250, 80, Black, user, 19, "wrong14")
			options("United Serial Bus", 525, 500, 250, 80, Black, user, 26, "wrong14")
			options("Universal Serial Bus", 50, 400, 250, 80, Black,user, 22, "Right14")
			options("United Shaped Bus", 525, 400, 250, 80, Black, user, 22, "wrong14")
		elif v14 == 3:
			gameDisplay.blit(testing111, (display_width/2 - 182,display_height/2-220))
			message_display(GK4[v14],190,30,35,Black)
			options("Pi Bonds", 50, 400, 250, 80, Black, user, 35, "wrong14")
			options("Small Hydrocarbons", 525, 500, 250, 80, Black, user, 22, "wrong14")
			options("Polymers", 525, 400, 250, 80, Black,user, 35, "Right14")
			options("4,2 octene", 50, 500, 250, 80, Black, user, 35, "wrong14")
		elif v14 == 4:
			gameDisplay.blit(testing37, (display_width/2 - 182,display_height/2-216))
			message_display(GK4[v14],25,30,35,Black)
			options("1541", 50, 400, 250, 80, Black, user, 35, "wrong14")
			options("2451", 525, 500, 250, 80, Black, user, 35, "wrong14")
			options("2501", 525, 400, 250, 80, Black,user, 35, "Right14")
			options("2546", 50, 500, 250, 80, Black, user, 35, "wrong14")
		pygame.display.update()
		clock.tick(15)


def a15s():
	global v15
	global kilo13
	kilo13 = True
	while kilo13:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v15 == 0:
			gameDisplay.blit(testing38, (display_width/2 - 182,display_height/2-200))
			message_display(GK5[v15],25,30,25,Black)
			options("AEAAASN", 50, 500, 250, 80, Black, user, 35, "wrongs15")
			options("Continent", 525, 500, 250, 80, Black, user, 35, "wrongs15")
			options("Pangia", 50, 400, 250, 80, Black,user, 35, "Rights15")
			options("United Globe", 525, 400, 250, 80, Black, user, 35, "wrongs15")
		elif v15 == 1:
			gameDisplay.blit(testing39, (display_width/2 - 182,display_height/2-230))
			message_display(GK5[v15],25,30,34,Black)
			options("Pigeons", 50, 400, 250, 80, Black, user, 35, "wrongs15")
			options("Chickens", 525, 500, 250, 80, Black, user, 35, "wrongs15")
			options("Ducks", 525, 400, 250, 80, Black,user, 35, "Rights15")
			options("Hawks", 50, 500, 250, 80, Black, user, 35, "wrongs15")
		elif v15 == 2:
			gameDisplay.blit(testing114, (display_width/2 - 182,display_height/2-220))
			message_display(GK5[v15],267,30,35,Black)
			options("Light Ions", 50, 400, 250, 80, Black, user, 35, "wrongs15")
			options("Laxative Ions", 50, 500, 250, 80, Black, user, 30, "wrongs15")
			options("Lithium Ion", 525, 500, 250, 80, Black,user, 32, "Rights15")
			options("Linked Ions", 525, 400, 250, 80, Black, user, 35, "wrongs15")
		elif v15 == 3:
			gameDisplay.blit(testing40, (display_width/2 - 182,display_height/2-213))
			message_display(GK5[v15],100,30,35,Black)
			options("Green", 50, 400, 250, 80, Black, user, 35, "wrongs15")
			options("Red", 525, 500, 250, 80, Black, user, 35, "wrongs15")
			options("Blue", 525, 400, 250, 80, Black,user, 35, "Rights15")
			options("Pink", 50, 500, 250, 80, Black, user, 35, "wrongs15")
		elif v15 == 4:
			gameDisplay.blit(testing41, (display_width/2 - 182,display_height/2-220))
			message_display(GK5[v15],22,30,30,Black)
			options("D", 50, 500, 250, 80, Black, user, 35, "wrongs15")
			options("K24", 525, 500, 250, 80, Black, user, 35, "wrongs15")
			options("A", 50, 400, 250, 80, Black,user, 35, "Rights15")
			options("B3", 525, 400, 250, 80, Black, user, 35, "wrongs15")
		pygame.display.update()
		clock.tick(15)


def a15():
	global juliet13
	global v15
	v15 = randint(0,4)
	juliet13 = True
	while juliet13:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		if v15 == 0:
			gameDisplay.blit(testing38, (display_width/2 - 182,display_height/2-200))
			message_display(GK5[v15],25,30,25,Black)
			options("AEAAASN", 50, 400, 250, 80, Black, user, 35, "wrong15")
			options("Continent", 525, 500, 250, 80, Black, user, 35, "wrong15")
			options("Pangia", 50, 500, 250, 80, Black,user, 35, "Right15")
			options("United Globe", 525, 400, 250, 80, Black, user, 35, "wrong15")
		elif v15 == 1:
			gameDisplay.blit(testing39, (display_width/2 - 182,display_height/2-230))
			message_display(GK5[v15],25,30,34,Black)
			options("Pigeons", 50, 400, 250, 80, Black, user, 35, "wrong15")
			options("Chickens", 50, 500, 250, 80, Black, user, 35, "wrong15")
			options("Ducks", 525, 500, 250, 80, Black,user, 35, "Right15")
			options("Hawks", 525, 400, 250, 80, Black, user, 35, "wrong15")
		elif v15 == 2:
			gameDisplay.blit(testing114, (display_width/2 - 182,display_height/2-220))
			message_display(GK5[v15],267,30,35,Black)
			options("Light Ions", 50, 400, 250, 80, Black, user, 35, "wrong15")
			options("Laxative Ions", 525, 500, 250, 80, Black, user, 30, "wrong15")
			options("Lithium Ion", 525, 400, 250, 80, Black,user, 32, "Right15")
			options("Linked Ions", 50, 500, 250, 80, Black, user, 35, "wrong15")
		elif v15 == 3:
			gameDisplay.blit(testing40, (display_width/2 - 182,display_height/2-213))
			message_display(GK5[v15],100,30,35,Black)
			options("Green", 50, 400, 250, 80, Black, user, 35, "wrong15")
			options("Red", 525, 500, 250, 80, Black, user, 35, "wrong15")
			options("Blue", 525, 400, 250, 80, Black,user, 35, "Right15")
			options("Pink", 50, 500, 250, 80, Black, user, 35, "wrong15")
		elif v15 == 4:
			gameDisplay.blit(testing41, (display_width/2 - 182,display_height/2-220))
			message_display(GK5[v15],22,30,30,Black)
			options("D", 50, 500, 250, 80, Black, user, 35, "wrong15")
			options("K24", 525, 500, 250, 80, Black, user, 35, "wrong15")
			options("A", 50, 400, 250, 80, Black,user, 35, "Right15")
			options("B3", 525, 400, 250, 80, Black, user, 35, "wrong15")
		pygame.display.update()
		clock.tick(15)

def a16s():
	global v16
	global kilo14
	kilo14 = True
	while kilo14:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v16 == 0:
			gameDisplay.blit(testing42, (display_width/2 - 182,display_height/2-180))
			message_display(Sci1[v16],100,30,35,Black)
			options("Teal", 50, 400, 250, 80, Black, user, 35, "wrongs16")
			options("Blue", 525, 500, 250, 80, Black, user, 35, "wrongs16")
			options("Red", 525, 400, 250, 80, Black,user, 35, "Rights16")
			options("Sky Blue", 50, 500, 250, 80, Black, user, 35, "wrongs16")
		elif v16 == 1:
			gameDisplay.blit(testing43, (display_width/2 - 182,display_height/2-200))
			message_display(Sci1[v16],25,30,30,Black)
			options("Decompositon", 50, 400, 250, 80, Black, user, 31, "wrongs16")
			options("Fisson", 50, 500, 250, 80, Black, user, 35, "wrongs16")
			options("Fusion", 525, 500, 250, 80, Black,user, 35, "Rights16")
			options("Synthesis", 525, 400, 250, 80, Black, user, 35, "wrongs16")
		elif v16 == 2:
			gameDisplay.blit(testing112, (display_width/2 - 182,display_height/2-220))
			message_display(Sci1[v16],15,30,33,Black)
			options("Eldridge", 50, 500, 250, 80, Black, user, 35, "wrongs16")
			options("Lamarck", 525, 500, 250, 80, Black, user, 35, "wrongs16")
			options("Darwin", 50, 400, 250, 80, Black,user, 35, "Rights16")
			options("Rutherford", 525, 400, 250, 80, Black, user, 33, "wrongs16")
		elif v16 == 3:
			gameDisplay.blit(testing44, (display_width/2 - 182,display_height/2-217))
			message_display(Sci1[v16],30,30,26,Black)
			options("2s3p", 50, 400, 250, 80, Black, user, 35, "wrongs16")
			options("2", 525, 500, 250, 80, Black, user, 35, "wrongs16")
			options("8", 50, 500, 250, 80, Black,user, 35, "Rights16")
			options("16", 525, 400, 250, 80, Black, user, 35, "wrongs16")
		elif v16 == 4:
			gameDisplay.blit(testing45, (display_width/2 - 182,display_height/2-200))
			message_display(Sci1[v16],10,30,24,Black)
			options("Tusunami", 50, 400, 250, 80, Black, user, 35, "wrongs16")
			options("Hurricanes", 50, 500, 250, 80, Black, user, 35, "wrongs16")
			options("Earthquakes", 525, 500, 250, 80, Black,user, 33, "Rights16")
			options("Blizzards", 525, 400, 250, 80, Black, user, 35, "wrongs16")
		pygame.display.update()
		clock.tick(15)

def a16():
	global juliet14
	global v16
	v16 = randint(0,4)
	juliet14 = True
	while juliet14:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v16 == 0:
			gameDisplay.blit(testing42, (display_width/2 - 182,display_height/2-180))
			message_display(Sci1[v16],100,30,35,Black)
			options("Teal", 50, 400, 250, 80, Black, user, 35, "wrong16")
			options("Blue", 525, 500, 250, 80, Black, user, 35, "wrong16")
			options("Red", 525, 400, 250, 80, Black,user, 35, "Right16")
			options("Sky Blue", 50, 500, 250, 80, Black, user, 35, "wrong16")
		elif v16 == 1:
			gameDisplay.blit(testing43, (display_width/2 - 182,display_height/2-200))
			message_display(Sci1[v16],25,30,30,Black)
			options("Decompositon", 50, 400, 250, 80, Black, user, 31, "wrong16")
			options("Fisson", 50, 500, 250, 80, Black, user, 35, "wrong16")
			options("Fusion", 525, 500, 250, 80, Black,user, 35, "Right16")
			options("Synthesis", 525, 400, 250, 80, Black, user, 35, "wrong16")
		elif v16 == 2:
			gameDisplay.blit(testing112, (display_width/2 - 182,display_height/2-220))
			message_display(Sci1[v16],15,30,33,Black)
			options("Eldridge", 50, 500, 250, 80, Black, user, 35, "wrong16")
			options("Lamarck", 525, 500, 250, 80, Black, user, 35, "wrong16")
			options("Darwin", 50, 400, 250, 80, Black,user, 35, "Right16")
			options("Rutherford", 525, 400, 250, 80, Black, user, 33, "wrong16")
		elif v16 == 3:
			gameDisplay.blit(testing44, (display_width/2 - 182,display_height/2-217))
			message_display(Sci1[v16],30,30,26,Black)
			options("2s3p", 50, 400, 250, 80, Black, user, 35, "wrong16")
			options("2", 50, 500, 250, 80, Black, user, 35, "wrong16")
			options("8", 525, 500, 250, 80, Black,user, 35, "Right16")
			options("16", 525, 400, 250, 80, Black, user, 35, "wrong16")
		elif v16 == 4:
			gameDisplay.blit(testing45, (display_width/2 - 182,display_height/2-200))
			message_display(Sci1[v16],10,30,24,Black)
			options("Tusunami", 50, 400, 250, 80, Black, user, 35, "wrong16")
			options("Hurricanes", 50, 500, 250, 80, Black, user, 35, "wrong16")
			options("Earthquakes", 525, 500, 250, 80, Black,user, 33, "Right16")
			options("Blizzards", 525, 400, 250, 80, Black, user, 35, "wrong16")
		pygame.display.update()
		clock.tick(15)

def a17s():
	global v17
	global kilo15
	kilo15 = True
	while kilo15:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v17 == 0:
			gameDisplay.blit(testing46, (display_width/2 - 182,display_height/2-220))
			message_display(Sci2[v17],100,30,35,Black)
			options("CO2", 50, 400, 250, 80, Black, user, 35, "wrongs17")
			options("Oxygen", 525, 500, 250, 80, Black, user, 35, "wrongs17")
			options("Nitrogen", 50, 500, 250, 80, Black,user, 35, "Rights17")
			options("Methane", 525, 400, 250, 80, Black, user, 35, "wrongs17")
		elif v17 == 1:
			gameDisplay.blit(testing47, (display_width/2 - 182,display_height/2-167))
			message_display(Sci2[v17],20,30,31,Black)
			options("Air", 50, 400, 250, 80, Black, user, 35, "wrongs17")
			options("Pebbles", 525, 500, 250, 80, Black, user, 35, "wrongs17")
			options("Clay", 50, 500, 250, 80, Black,user, 35, "Rights17")
			options("Nutrients", 525, 400, 250, 80, Black, user, 35, "wrongs17")
		elif v17 == 2:
			gameDisplay.blit(testing48, (display_width/2 - 182,display_height/2-200))
			message_display(Sci2[v17],60,30,35,Black)
			options("Heparin", 50, 500, 250, 80, Black, user, 35, "wrongs17")
			options("Bile", 525, 500, 250, 80, Black, user, 35, "wrongs17")
			options("Insulin", 50, 400, 250, 80, Black,user, 35, "Rights17")
			options("Ether", 525, 400, 250, 80, Black, user, 35, "wrongs17")
		elif v17 == 3:
			gameDisplay.blit(testing49, (display_width/2 - 182,display_height/2-220))
			message_display(Sci2[v17],190,30,35,Black)
			options("Volts", 50, 400, 250, 80, Black, user, 35, "wrongs17")
			options("Watts", 525, 500, 250, 80, Black, user, 35, "wrongs17")
			options("Joules", 525, 400, 250, 80, Black,user, 35, "Rights17")
			options("Ohm's", 50, 500, 250, 80, Black, user, 35, "wrongs17")
		elif v17 == 4:
			gameDisplay.blit(testing50, (display_width/2 - 182,display_height/2-200))
			message_display(Sci2[v17],10,30,32,Black)
			options("Vitamins", 50, 400, 250, 80, Black, user, 35, "wrongs17")
			options("Protiens", 525, 500, 250, 80, Black, user, 35, "wrongs17")
			options("Fats", 50, 500, 250, 80, Black,user, 35, "Rights17")
			options("Polysaccharides", 525, 400, 250, 80, Black, user, 30, "wrongs17")
		pygame.display.update()
		clock.tick(15)

def a17():
	global juliet15
	global v17
	v17 = randint(0,4)
	juliet15 = True
	while juliet15:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v17 == 0:
			gameDisplay.blit(testing46, (display_width/2 - 182,display_height/2-220))
			message_display(Sci2[v17],100,30,35,Black)
			options("CO2", 50, 400, 250, 80, Black, user, 35, "wrong17")
			options("Oxygen", 50, 500, 250, 80, Black, user, 35, "wrong17")
			options("Nitrogen", 525, 500, 250, 80, Black,user, 35, "Right17")
			options("Methane", 525, 400, 250, 80, Black, user, 35, "wrong17")
		elif v17 == 1:
			gameDisplay.blit(testing47, (display_width/2 - 182,display_height/2-167))
			message_display(Sci2[v17],20,30,31,Black)
			options("Air", 50, 400, 250, 80, Black, user, 35, "wrong17")
			options("Pebbles", 525, 500, 250, 80, Black, user, 35, "wrong17")
			options("Clay", 525, 400, 250, 80, Black,user, 35, "Right17")
			options("Nutrients", 50, 500, 250, 80, Black, user, 35, "wrong17")
		elif v17 == 2:
			gameDisplay.blit(testing48, (display_width/2 - 182,display_height/2-200))
			message_display(Sci2[v17],60,30,35,Black)
			options("Heparin", 50, 500, 250, 80, Black, user, 35, "wrong17")
			options("Bile", 525, 500, 250, 80, Black, user, 35, "wrong17")
			options("Insulin", 50, 400, 250, 80, Black,user, 35, "Right17")
			options("Ether", 525, 400, 250, 80, Black, user, 35, "wrong17")
		elif v17 == 3:
			gameDisplay.blit(testing49, (display_width/2 - 182,display_height/2-220))
			message_display(Sci2[v17],190,30,35,Black)
			options("Volts", 50, 400, 250, 80, Black, user, 35, "wrong17")
			options("Watts", 525, 500, 250, 80, Black, user, 35, "wrong17")
			options("Joules", 525, 400, 250, 80, Black,user, 35, "Right17")
			options("Ohm's", 50, 500, 250, 80, Black, user, 35, "wrong17")
		elif v17 == 4:
			gameDisplay.blit(testing50, (display_width/2 - 182,display_height/2-200))
			message_display(Sci2[v17],10,30,32,Black)
			options("Vitamins", 50, 400, 250, 80, Black, user, 35, "wrong17")
			options("Protiens", 50, 500, 250, 80, Black, user, 35, "wrong17")
			options("Fats", 525, 500, 250, 80, Black,user, 35, "Right17")
			options("Polysaccharides", 525, 400, 250, 80, Black, user, 30, "wrong17")
		pygame.display.update()
		clock.tick(15)

def a18s():
	global v18
	global kilo16
	kilo16 = True
	while kilo16:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v18 == 0:
			gameDisplay.blit(testing51, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],160,30,35,Black)
			options("Recurrent", 50, 500, 250, 80, Black, user, 35, "wrongs18")
			options("Enthalpy", 525, 500, 250, 80, Black, user, 35, "wrongs18")
			options("Disorder", 50, 400, 250, 80, Black,user, 35, "Rights18")
			options("Chaoos", 525, 400, 250, 80, Black, user, 35, "wrongs18")
		elif v18 == 1:
			gameDisplay.blit(testing52, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],10,30,29,Black)
			options("6", 50, 400, 250, 80, Black, user, 35, "wrongs18")
			options("24", 525, 500, 250, 80, Black, user, 35, "wrongs18")
			options("12", 525, 400, 250, 80, Black,user, 35, "Rights18")
			options("0.00012", 50, 500, 250, 80, Black, user, 35, "wrongs18")
		elif v18 == 2:
			gameDisplay.blit(testing113, (display_width/2 - 182,display_height/2-220))
			message_display(Sci3[v18],140,30,35,Black)
			options("Lymph", 50, 400, 250, 80, Black, user, 35, "wrongs18")
			options("Cerebral Fluid", 50, 500, 250, 80, Black, user, 33, "wrongs18")
			options("Blood", 525, 500, 250, 80, Black, user, 35, "Rights18")
			options("Synovial Fluid", 525, 400, 250, 80, Black, user, 33, "wrongs18")
		elif v18 == 3:
			gameDisplay.blit(testing53, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],60,30,33,Black)
			options("Molten Crust", 50, 500, 250, 80, Black, user, 33, "wrongs18")
			options("Lava", 525, 500, 250, 80, Black, user, 35, "wrongs18")
			options("Magma", 50, 400, 250, 80, Black,user, 35, "Rights18")
			options("Ground Ash", 525, 400, 250, 80, Black, user, 35, "wrongs18")
		elif v18 == 4:
			gameDisplay.blit(testing54, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],150,30,35,Black)
			options("Free", 50, 400, 250, 80, Black, user, 35, "wrongs18")
			options("Valacnce", 525, 500, 250, 80, Black, user, 35, "wrongs18")
			options("Delocalized", 50, 500, 250, 80, Black,user, 33, "Rights18")
			options("Bounded", 525, 400, 250, 80, Black, user, 35, "wrongs18")
		pygame.display.update()
		clock.tick(15)

def a18():
	global juliet16
	global v18
	v18 = randint(0,4)
	juliet16 = True
	while juliet16:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v18 == 0:
			gameDisplay.blit(testing51, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],160,30,35,Black)
			options("Recurrent", 50, 400, 250, 80, Black, user, 35, "wrong18")
			options("Enthalpy", 525, 500, 250, 80, Black, user, 35, "wrong18")
			options("Disorder", 525, 400, 250, 80, Black,user, 35, "Right18")
			options("Chaoos", 50, 500, 250, 80, Black, user, 35, "wrong18")
		elif v18 == 1:
			gameDisplay.blit(testing52, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],10,30,29,Black)
			options("6", 50, 400, 250, 80, Black, user, 35, "wrong18")
			options("24", 50, 500, 250, 80, Black, user, 35, "wrong18")
			options("12", 525, 500, 250, 80, Black,user, 35, "Right18")
			options("0.00012", 525, 400, 250, 80, Black, user, 35, "wrong18")
		elif v18 == 2:
			gameDisplay.blit(testing113, (display_width/2 - 182,display_height/2-220))
			message_display(Sci3[v18],140,30,35,Black)
			options("Lymph", 50, 500, 250, 80, Black, user, 35, "wrong18")
			options("Cerebral Fluid", 525, 500, 250, 80, Black, user, 33, "wrong18")
			options("Blood", 50, 400, 250, 80, Black, user, 35, "Right18")
			options("Synovial Fluid", 525, 400, 250, 80, Black, user, 33, "wrong18")
		elif v18 == 3:
			gameDisplay.blit(testing53, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],60,30,33,Black)
			options("Molten Crust", 50, 400, 250, 80, Black, user, 33, "wrong18")
			options("Lava", 50, 500, 250, 80, Black, user, 35, "wrong18")
			options("Magma", 525, 500, 250, 80, Black,user, 35, "Right18")
			options("Ground Ash", 525, 400, 250, 80, Black, user, 35, "wrong18")
		elif v18 == 4:
			gameDisplay.blit(testing54, (display_width/2 - 182,display_height/2-200))
			message_display(Sci3[v18],150,30,35,Black)
			options("Free", 50, 400, 250, 80, Black, user, 35, "wrong18")
			options("Valacnce", 525, 500, 250, 80, Black, user, 35, "wrong18")
			options("Delocalized", 525, 400, 250, 80, Black,user, 33, "Right18")
			options("Bounded", 50, 500, 250, 80, Black, user, 35, "wrong18")
		pygame.display.update()
		clock.tick(15)

def a19s():
	global v19
	global kilo17
	kilo17 = True
	while kilo17:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v19 == 0:
			gameDisplay.blit(testing114, (display_width/2 - 182,display_height/2-220))
			message_display(Sci4[v19],35,30,31,Black)
			options("Deuterium", 50, 400, 250, 80, Black, user, 35, "wrongs19")
			options("Hydrogen Peroxide", 525, 500, 250, 80, Black, user, 25, "wrongs19")
			options("Water", 50, 500, 250, 80, Black,user, 35, "Rights19")
			options("Tritium", 525, 400, 250, 80, Black, user, 35, "wrongs19")
		elif v19 == 1:
			gameDisplay.blit(testing115, (display_width/2 - 182,display_height/2-220))
			message_display(Sci4[v19],25,30,30,Black)
			options("CO3", 50, 400, 250, 80, Black, user, 35, "wrongs19")
			options("CO2", 50, 500, 250, 80, Black, user, 35, "wrongs19")
			options("CO", 525, 500, 250, 80, Black,user, 35, "Rights19")
			options("SO3", 525, 400, 250, 80, Black, user, 35, "wrongs19")
		elif v19 == 2:
			gameDisplay.blit(testing56, (display_width/2 - 182,display_height/2-200))
			message_display(Sci4[v19],120,30,35,Black)
			options("Omega 3", 50, 500, 250, 80, Black, user, 35, "wrongs19")
			options("Collagen", 525, 500, 250, 80, Black, user, 35, "wrongs19")
			options("Keratin", 50, 400, 250, 80, Black,user, 35, "Rights19")
			options("Histone", 525, 400, 250, 80, Black, user, 35, "wrongs19")
		elif v19 == 3:
			gameDisplay.blit(testing116, (display_width/2 - 182,display_height/2-220))
			message_display(Sci4[v19],135,30,31,Black)
			options("Polysaccharides", 50, 400, 250, 80, Black, user, 29, "wrongs19")
			options("Triglycerides", 525, 500, 250, 80, Black, user, 31, "wrongs19")
			options("Phospholipids", 525, 400, 250, 80, Black,user, 31, "Rights19")
			options("4,2 Ocetene", 50, 500, 250, 80, Black, user, 35, "wrongs19")
		elif v19 == 4:
			gameDisplay.blit(testing57, (display_width/2 - 182,display_height/2-200))
			message_display(Sci4[v19],10,30,32,Black)
			options("Pepsin", 50, 400, 250, 80, Black, user, 35, "wrongs19")
			options("Amalyse", 50, 500, 250, 80, Black, user, 35, "wrongs19")
			options("Maltase", 525, 500, 250, 80, Black,user, 35, "Rights19")
			options("Cellulase", 525, 400, 250, 80, Black, user, 35, "wrongs19")
		pygame.display.update()
		clock.tick(15)


def a19():
	global juliet17
	global v19
	v19 = randint(0,4)
	juliet17 = True
	while juliet17:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v19 == 0:
			gameDisplay.blit(testing114, (display_width/2 - 182,display_height/2-220))
			message_display(Sci4[v19],35,30,31,Black)
			options("Deuterium", 50, 500, 250, 80, Black, user, 35, "wrong19")
			options("Hydrogen Peroxide", 525, 500, 250, 80, Black, user, 25, "wrong19")
			options("Water", 50, 400, 250, 80, Black,user, 35, "Right19")
			options("Tritium", 525, 400, 250, 80, Black, user, 35, "wrong19")
		elif v19 == 1:
			gameDisplay.blit(testing115, (display_width/2 - 182,display_height/2-220))
			message_display(Sci4[v19],25,30,30,Black)
			options("CO3", 50, 400, 250, 80, Black, user, 35, "wrong19")
			options("CO2", 50, 500, 250, 80, Black, user, 35, "wrong19")
			options("CO", 525, 500, 250, 80, Black,user, 35, "Right19")
			options("SO3", 525, 400, 250, 80, Black, user, 35, "wrong19")
		elif v19 == 2:
			gameDisplay.blit(testing56, (display_width/2 - 182,display_height/2-200))
			message_display(Sci4[v19],120,30,35,Black)
			options("Omega 3", 50, 400, 250, 80, Black, user, 35, "wrong19")
			options("Collagen", 525, 500, 250, 80, Black, user, 35, "wrong19")
			options("Keratin", 525, 400, 250, 80, Black,user, 35, "Right19")
			options("Histone", 50, 500, 250, 80, Black, user, 35, "wrong19")
		elif v19 == 3:
			gameDisplay.blit(testing116, (display_width/2 - 182,display_height/2-220))
			message_display(Sci4[v19],135,30,31,Black)
			options("Polysaccharides", 50, 400, 250, 80, Black, user, 29, "wrong19")
			options("Triglycerides", 525, 500, 250, 80, Black, user, 31, "wrong19")
			options("Phospholipids", 50, 500, 250, 80, Black,user, 31, "Right19")
			options("4,2 Ocetene", 525, 400, 250, 80, Black, user, 35, "wrong19")
		elif v19 == 4:
			gameDisplay.blit(testing57, (display_width/2 - 182,display_height/2-200))
			message_display(Sci4[v19],10,30,32,Black)
			options("Pepsin", 50, 400, 250, 80, Black, user, 35, "wrong19")
			options("Amalyse", 50, 500, 250, 80, Black, user, 35, "wrong19")
			options("Maltase", 525, 500, 250, 80, Black,user, 35, "Right19")
			options("Cellulase", 525, 400, 250, 80, Black, user, 35, "wrong19")
		pygame.display.update()
		clock.tick(15)

def a20s():
	global v20
	global kilo18
	kilo18 = True
	while kilo18:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v20 == 0:
			gameDisplay.blit(testing117, (display_width/2 - 182,display_height/2-220))
			message_display(Sci5[v20],25,30,29,Black)
			options("234", 50, 500, 250, 80, Black, user, 35, "wrongs20")
			options("238", 525, 500, 250, 80, Black, user, 35, "wrongs20")
			options("235", 50, 400, 250, 80, Black,user, 35, "Rights20")
			options("240", 525, 400, 250, 80, Black, user, 35, "wrongs20")
		elif v20 == 1:
			gameDisplay.blit(testing58, (display_width/2 - 182,display_height/2-200))
			message_display(Sci5[v20],15,30,24,Black)
			options("Thallium", 50, 400, 250, 80, Black, user, 35, "wrongs20")
			options("Iridium", 525, 500, 250, 80, Black, user, 35, "wrongs20")
			options("Indium Tin-Oxide", 525, 400, 250, 80, Black,user, 29, "Rights20")
			options("Tungsten Carbide", 50, 500, 250, 80, Black, user, 27, "wrongs20")
		elif v20 == 2:
			gameDisplay.blit(testing59, (display_width/2 - 182,display_height/2-225))
			message_display(Sci5[v20],150,30,35,Black)
			options("Pepsin", 50, 500, 250, 80, Black, user, 35, "wrongs20")
			options("Beta-Kertain", 525, 500, 250, 80, Black, user, 32, "wrongs20")
			options("Collagen", 50, 400, 250, 80, Black,user, 35, "Rights20")
			options("Renin", 525, 400, 250, 80, Black, user, 35, "wrongs20")
		elif v20 == 3:
			gameDisplay.blit(testing60, (display_width/2 - 182,display_height/2-200))
			message_display(Sci5[v20],125,30,35,Black)
			options("Adenine", 50, 400, 250, 80, Black, user, 35, "wrongs20")
			options("Thymine", 50, 500, 250, 80, Black, user, 35, "wrongs20")
			options("Adenosine", 525, 500, 250, 80, Black,user, 33, "Rights20")
			options("Guanine", 525, 400, 250, 80, Black, user, 35, "wrongs20")
		elif v20 == 4:
			gameDisplay.blit(testing61, (display_width/2 - 182,display_height/2-200))
			message_display(Sci5[v20],100,30,35,Black)
			options("Amalyse", 50, 500, 250, 80, Black, user, 35, "wrongs20")
			options("Hemoglobin", 525, 500, 250, 80, Black, user, 35, "wrongs20")
			options("Histone", 50, 400, 250, 80, Black,user, 33, "Rights20")
			options("Keratin", 525, 400, 250, 80, Black, user, 35, "wrongs20")
		pygame.display.update()
		clock.tick(15)

def a20():
	global juliet18
	global v20
	v20 = randint(0,4)
	juliet18 = True
	while juliet18:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background6, (0,0))
		if v20 == 0:
			gameDisplay.blit(testing117, (display_width/2 - 182,display_height/2-220))
			message_display(Sci5[v20],25,30,29,Black)
			options("234", 50, 400, 250, 80, Black, user, 35, "wrong20")
			options("238", 50, 500, 250, 80, Black, user, 35, "wrong20")
			options("235", 525, 500, 250, 80, Black,user, 35, "Right20")
			options("240", 525, 400, 250, 80, Black, user, 35, "wrong20")
		elif v20 == 1:
			gameDisplay.blit(testing58, (display_width/2 - 182,display_height/2-200))
			message_display(Sci5[v20],15,30,24,Black)
			options("Thallium", 50, 400, 250, 80, Black, user, 35, "wrong20")
			options("Iridium", 525, 500, 250, 80, Black, user, 35, "wrong20")
			options("Indium Tin-Oxide", 50, 500, 250, 80, Black,user, 29, "Right20")
			options("Tungsten Carbide", 525, 400, 250, 80, Black, user, 27, "wrong20")
		elif v20 == 2:
			gameDisplay.blit(testing59, (display_width/2 - 182,display_height/2-225))
			message_display(Sci5[v20],150,30,35,Black)
			options("Pepsin", 50, 400, 250, 80, Black, user, 35, "wrong20")
			options("Beta-Kertain", 525, 500, 250, 80, Black, user, 32, "wrong20")
			options("Collagen", 525, 400, 250, 80, Black,user, 35, "Right20")
			options("Renin", 50, 500, 250, 80, Black, user, 35, "wrong20")
		elif v20 == 3:
			gameDisplay.blit(testing60, (display_width/2 - 182,display_height/2-200))
			message_display(Sci5[v20],125,30,35,Black)
			options("Adenine", 50, 400, 250, 80, Black, user, 35, "wrong20")
			options("Thymine", 50, 500, 250, 80, Black, user, 35, "wrong20")
			options("Adenosine", 525, 500, 250, 80, Black,user, 33, "Right20")
			options("Guanine", 525, 400, 250, 80, Black, user, 35, "wrong20")
		elif v20 == 4:
			gameDisplay.blit(testing61, (display_width/2 - 182,display_height/2-200))
			message_display(Sci5[v20],100,30,35,Black)
			options("Amalyse", 50, 400, 250, 80, Black, user, 35, "wrong20")
			options("Hemoglobin", 525, 500, 250, 80, Black, user, 35, "wrong20")
			options("Histone", 50, 500, 250, 80, Black,user, 33, "Right20")
			options("Keratin", 525, 400, 250, 80, Black, user, 35, "wrong20")
		pygame.display.update()
		clock.tick(15)

def a21s():
	global v21
	global kilo19
	kilo19 = True
	while kilo19:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v21 == 0:
			gameDisplay.blit(testing62, (display_width/2 - 182,display_height/2-200))
			message_display(Med1[v21],125,30,35,Black)
			options("Fentanyl", 50, 500, 250, 80, Black, user, 35, "wrongs21")
			options("Cephalexin", 525, 500, 250, 80, Black, user, 33, "wrongs21")
			options("Penicillin", 50, 400, 250, 80, Black,user, 33, "Rights21")
			options("Amoxicillin", 525, 400, 250, 80, Black, user, 30, "wrongs21")
		elif v21 == 1:
			gameDisplay.blit(testing63, (display_width/2 - 182,display_height/2-225))
			message_display(Med1[v21],195,30,35,Black)
			options("Monkey", 50, 400, 250, 80, Black, user, 35, "wrongs21")
			options("Rat", 525, 500, 250, 80, Black, user, 35, "wrongs21")
			options("Human", 525, 400, 250, 80, Black,user, 35, "Rights21")
			options("Toad", 50, 500, 250, 80, Black, user, 35, "wrongs21")
		elif v21 == 2:
			gameDisplay.blit(testing1024, (display_width/2 - 182,display_height/2-200))
			message_display(Med1[v21],50,30,35,Black)
			options("Serous", 50, 400, 250, 80, Black, user, 35, "wrongs21")
			options("Pharynx", 50, 500, 250, 80, Black, user, 35, "wrongs21")
			options("Alveoli", 525, 500, 250, 80, Black,user, 35, "Rights21")
			options("Nares", 525, 400, 250, 80, Black, user, 35, "wrongs21")
		elif v21 == 3:
			gameDisplay.blit(testing64, (display_width/2 - 182,display_height/2-200))
			message_display(Med1[v21],20,30,32,Black)
			options("Ligaments", 50, 400, 250, 80, Black, user, 35, "wrongs21")
			options("Tendons", 525, 500, 250, 80, Black, user, 35, "wrongs21")
			options("Cartilage", 50, 500, 250, 80, Black,user, 35, "Rights21")
			options("Mesentry", 525, 400, 250, 80, Black, user, 35, "wrongs21")
		elif v21 == 4:
			gameDisplay.blit(testing65, (display_width/2 - 182,display_height/2-180))
			message_display(Med1[v21],10,30,29,Black)
			options("Endoconsume", 50, 500, 250, 80, Black, user, 35, "wrongs21")
			options("Endocytosis", 525, 500, 250, 80, Black, user, 35, "wrongs21")
			options("Phagocytosis", 50, 400, 250, 80, Black,user, 32, "Rights21")
			options("Phagoconsume", 525, 400, 250, 80, Black, user, 32, "wrongs21")
		pygame.display.update()
		clock.tick(15)

def a21():
	global juliet19
	global v21
	v21 = randint(0,4)
	juliet19 = True
	while juliet19:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v21 == 0:
			gameDisplay.blit(testing62, (display_width/2 - 182,display_height/2-200))
			message_display(Med1[v21],125,30,35,Black)
			options("Fentanyl", 50, 400, 250, 80, Black, user, 35, "wrong21")
			options("Cephalexin", 50, 500, 250, 80, Black, user, 33, "wrong21")
			options("Penicillin", 525, 500, 250, 80, Black,user, 33, "Right21")
			options("Amoxicillin", 525, 400, 250, 80, Black, user, 32, "wrong21")
		elif v21 == 1:
			gameDisplay.blit(testing63, (display_width/2 - 182,display_height/2-225))
			message_display(Med1[v21],195,30,35,Black)
			options("Monkey", 50, 400, 250, 80, Black, user, 35, "wrong21")
			options("Rat", 50, 500, 250, 80, Black, user, 35, "wrong21")
			options("Human", 525, 500, 250, 80, Black,user, 35, "Right21")
			options("Toad", 525, 400, 250, 80, Black, user, 35, "wrong21")
		elif v21 == 2:
			gameDisplay.blit(testing1024, (display_width/2 - 182,display_height/2-200))
			message_display(Med1[v21],50,30,35,Black)
			options("Serous", 50, 500, 250, 80, Black, user, 35, "wrong21")
			options("Pharynx", 525, 500, 250, 80, Black, user, 35, "wrong21")
			options("Alveoli", 50, 400, 250, 80, Black,user, 35, "Right21")
			options("Nares", 525, 400, 250, 80, Black, user, 35, "wrong21")
		elif v21 == 3:
			gameDisplay.blit(testing64, (display_width/2 - 182,display_height/2-200))
			message_display(Med1[v21],20,30,32,Black)
			options("Ligaments", 50, 400, 250, 80, Black, user, 35, "wrong21")
			options("Tendons", 525, 500, 250, 80, Black, user, 35, "wrong21")
			options("Cartilage", 525, 400, 250, 80, Black,user, 35, "Right21")
			options("Mesentry", 50, 500, 250, 80, Black, user, 35, "wrong21")
		elif v21 == 4:
			gameDisplay.blit(testing65, (display_width/2 - 182,display_height/2-180))
			message_display(Med1[v21],10,30,29,Black)
			options("Endoconsume", 50, 400, 250, 80, Black, user, 35, "wrong21")
			options("Endocytosis", 525, 500, 250, 80, Black, user, 35, "wrong21")
			options("Phagocytosis", 50, 500, 250, 80, Black,user, 32, "Right21")
			options("Phagoconsume", 525, 400, 250, 80, Black, user, 32, "wrong21")
		pygame.display.update()
		clock.tick(15)

def a22s():
	global v22
	global kilo20
	kilo20 = True
	while kilo20:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v22 == 0:
			gameDisplay.blit(testing66, (display_width/2 - 182,display_height/2-227))
			message_display(Med2[v22],170,30,35,Black)
			options("Hemoglobin", 50, 400, 250, 80, Black, user, 35, "wrongs22")
			options("Membrane", 525, 500, 250, 80, Black, user, 35, "wrongs22")
			options("Nucleus", 525, 400, 250, 80, Black,user, 35, "Rights22")
			options("Shape", 50, 500, 250, 80, Black, user, 35, "wrongs22")
		elif v22 == 1:
			gameDisplay.blit(testing67, (display_width/2 - 182,display_height/2-217))
			message_display(Med2[v22],55,30,35,Black)
			options("Amalyse", 50, 500, 250, 80, Black, user, 35, "wrongs22")
			options("Cellulase", 525, 500, 250, 80, Black, user, 35, "wrongs22")
			options("Enzymes", 50, 400, 250, 80, Black,user, 35, "Rights22")
			options("Carboxypepsidase", 525, 400, 250, 80, Black, user, 26, "wrongs22")
		elif v22 == 2:
			gameDisplay.blit(testing68, (display_width/2 - 182,display_height/2-200))
			message_display(Med2[v22],100,30,35,Black)
			options("Salicylic Acid", 50, 400, 250, 80, Black, user, 32, "wrongs22")
			options("Acetaminophen", 50, 500, 250, 80, Black, user, 32, "wrongs22")
			options("Epinephrine", 525, 500, 250, 80, Black,user, 32, "Rights22")
			options("Sevoflurane", 525, 400, 250, 80, Black, user, 32, "wrongs22")
		elif v22 == 3:
			gameDisplay.blit(testing69, (display_width/2 - 182,display_height/2-200))
			message_display(Med2[v22],15,30,28,Black)
			options("Plasma", 50, 500, 250, 80, Black, user, 35, "wrongs22")
			options("Serum", 525, 500, 250, 80, Black, user, 35, "wrongs22")
			options("Platlets", 50, 400, 250, 80, Black,user, 35, "Rights22")
			options("Fibrrinogen", 525, 400, 250, 80, Black, user, 33, "wrongs22")
		elif v22 == 4:
			gameDisplay.blit(testing70, (display_width/2 - 182,display_height/2-160))
			message_display(Med2[v22],15,30,30,Black)
			options("1", 50, 400, 250, 80, Black, user, 35, "wrongs22")
			options("3", 525, 500, 250, 80, Black, user, 35, "wrongs22")
			options("4", 525, 400, 250, 80, Black,user, 35, "Rights22")
			options("5", 50, 500, 250, 80, Black, user, 33, "wrongs22")
		pygame.display.update()
		clock.tick(15)

def a22():
	global juliet20
	global v22
	v22 = randint(0,4)
	juliet20 = True
	while juliet20:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v22 == 0:
			gameDisplay.blit(testing66, (display_width/2 - 182,display_height/2-227))
			message_display(Med2[v22],170,30,35,Black)
			options("Hemoglobin", 50, 500, 250, 80, Black, user, 35, "wrong22")
			options("Membrane", 525, 500, 250, 80, Black, user, 35, "wrong22")
			options("Nucleus", 50, 400, 250, 80, Black,user, 35, "Right22")
			options("Shape", 525, 400, 250, 80, Black, user, 35, "wrong22")
		elif v22 == 1:
			gameDisplay.blit(testing67, (display_width/2 - 182,display_height/2-217))
			message_display(Med2[v22],55,30,35,Black)
			options("Amalyse", 50, 400, 250, 80, Black, user, 35, "wrong22")
			options("Cellulase", 525, 500, 250, 80, Black, user, 35, "wrong22")
			options("Enzymes", 50, 500, 250, 80, Black,user, 35, "Right22")
			options("Carboxypepsidase", 525, 400, 250, 80, Black, user, 26, "wrong22")
		elif v22 == 2:
			gameDisplay.blit(testing68, (display_width/2 - 182,display_height/2-200))
			message_display(Med2[v22],100,30,35,Black)
			options("Salicylic Acid", 50, 400, 250, 80, Black, user, 32, "wrong22")
			options("Acetaminophen", 525, 500, 250, 80, Black, user, 32, "wrong22")
			options("Epinephrine", 525, 400, 250, 80, Black,user, 32, "Right22")
			options("Sevoflurane", 50, 500, 250, 80, Black, user, 32, "wrong22")
		elif v22 == 3:
			gameDisplay.blit(testing69, (display_width/2 - 182,display_height/2-200))
			message_display(Med2[v22],15,30,28,Black)
			options("Plasma", 50, 400, 250, 80, Black, user, 35, "wrong22")
			options("Serum", 50, 500, 250, 80, Black, user, 35, "wrong22")
			options("Platlets", 525, 500, 250, 80, Black,user, 35, "Right22")
			options("Fibrrinogen", 525, 400, 250, 80, Black, user, 33, "wrong22")
		elif v22 == 4:
			gameDisplay.blit(testing70, (display_width/2 - 182,display_height/2-160))
			message_display(Med2[v22],15,30,30,Black)
			options("1", 50, 500, 250, 80, Black, user, 35, "wrong22")
			options("3", 525, 500, 250, 80, Black, user, 35, "wrong22")
			options("4", 50, 400, 250, 80, Black,user, 35, "Right22")
			options("5", 525, 400, 250, 80, Black, user, 33, "wrong22")
		pygame.display.update()
		clock.tick(15)

def a23s():
	global v23
	global kilo21
	kilo21 = True
	while kilo21:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v23 == 0:
			gameDisplay.blit(testing71, (display_width/2 - 182,display_height/2-190))
			message_display(Med3[v23],123,30,35,Black)
			options("Muscle", 50, 400, 250, 80, Black, user, 35, "wrongs23")
			options("Intestines", 50, 500, 250, 80, Black, user, 35, "wrongs23")
			options("Bone", 525, 500, 250, 80, Black,user, 35, "Rights23")
			options("Lungs", 525, 400, 250, 80, Black, user, 35, "wrongs23")
		elif v23 == 1:
			gameDisplay.blit(testing72, (display_width/2 - 182,display_height/2-200))
			message_display(Med3[v23],215,30,35,Black)
			options("Yellow", 50, 500, 250, 80, Black, user, 35, "wrongs23")
			options("Red", 525, 500, 250, 80, Black, user, 35, "wrongs23")
			options("Clear", 50, 400, 250, 80, Black,user, 35, "Rights23")
			options("Green", 525, 400, 250, 80, Black, user, 35, "wrongs23")
		elif v23 == 2:
			gameDisplay.blit(testing73, (display_width/2 - 182,display_height/2-200))
			message_display(Med3[v23],25,30,23,Black)
			options("5", 50, 400, 250, 80, Black, user, 35, "wrongs23")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrongs23")
			options("4", 525, 400, 250, 80, Black,user, 35, "Rights23")
			options("10", 50, 500, 250, 80, Black, user, 35, "wrongs23")
		elif v23 == 3:
			gameDisplay.blit(testing74, (display_width/2 - 182,display_height/2-225))
			message_display(Med3[v23],17,30,35,Black)
			options("Carbs", 50, 500, 250, 80, Black, user, 35, "wrongs23")
			options("Vitamins", 525, 500, 250, 80, Black, user, 35, "wrongs23")
			options("Protiens", 50, 400, 250, 80, Black,user, 35, "Rights23")
			options("Minerals", 525, 400, 250, 80, Black, user, 35, "wrongs23")
		elif v23 == 4:
			gameDisplay.blit(testing75, (display_width/2 - 182,display_height/2-200))
			message_display(Med3[v23],15,30,29,Black)
			options("3", 50, 400, 250, 80, Black, user, 35, "wrongs23")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrongs23")
			options("2", 525, 400, 250, 80, Black,user, 35, "Rights23")
			options("4", 50, 500, 250, 80, Black, user, 35, "wrongs23")
		pygame.display.update()
		clock.tick(15)

def a23():
	global juliet21
	global v23
	v23 = randint(0,4)
	juliet21 = True
	while juliet21:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v23 == 0:
			gameDisplay.blit(testing71, (display_width/2 - 182,display_height/2-190))
			message_display(Med3[v23],123,30,35,Black)
			options("Muscle", 50, 400, 250, 80, Black, user, 35, "wrong23")
			options("Intestines", 525, 500, 250, 80, Black, user, 35, "wrong23")
			options("Bone", 50, 500, 250, 80, Black,user, 35, "Right23")
			options("Lungs", 525, 400, 250, 80, Black, user, 35, "wrong23")
		elif v23 == 1:
			gameDisplay.blit(testing72, (display_width/2 - 182,display_height/2-200))
			message_display(Med3[v23],215,30,35,Black)
			options("Yellow", 50, 400, 250, 80, Black, user, 35, "wrong23")
			options("Red", 50, 500, 250, 80, Black, user, 35, "wrong23")
			options("Clear", 525, 500, 250, 80, Black,user, 35, "Right23")
			options("Green", 525, 400, 250, 80, Black, user, 35, "wrong23")
		elif v23 == 2:
			gameDisplay.blit(testing73, (display_width/2 - 182,display_height/2-200))
			message_display(Med3[v23],25,30,23,Black)
			options("5", 50, 400, 250, 80, Black, user, 35, "wrong23")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrong23")
			options("4", 525, 400, 250, 80, Black,user, 35, "Right23")
			options("10", 50, 500, 250, 80, Black, user, 35, "wrong23")
		elif v23 == 3:
			gameDisplay.blit(testing74, (display_width/2 - 182,display_height/2-225))
			message_display(Med3[v23],17,30,35,Black)
			options("Carbs", 50, 400, 250, 80, Black, user, 35, "wrong23")
			options("Vitamins", 50, 500, 250, 80, Black, user, 35, "wrong23")
			options("Protiens", 525, 500, 250, 80, Black,user, 35, "Right23")
			options("Minerals", 525, 400, 250, 80, Black, user, 35, "wrong23")
		elif v23 == 4:
			gameDisplay.blit(testing75, (display_width/2 - 182,display_height/2-200))
			message_display(Med3[v23],15,30,29,Black)
			options("3", 50, 500, 250, 80, Black, user, 35, "wrong23")
			options("1", 525, 500, 250, 80, Black, user, 35, "wrong23")
			options("2", 50, 400, 250, 80, Black,user, 35, "Right23")
			options("4", 525, 400, 250, 80, Black, user, 35, "wrong23")
		pygame.display.update()
		clock.tick(15)

def a24s():
	global v24
	global kilo22
	kilo22 = True
	while kilo22:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v24 == 0:
			gameDisplay.blit(testing76, (display_width/2 - 182,display_height/2-200))
			message_display(Med4[v24],95,30,35,Black)
			options("Sunflowers", 50, 500, 250, 80, Black, user, 33, "wrongs24")
			options("Mustard", 525, 500, 250, 80, Black, user, 35, "wrongs24")
			options("Poppies", 50, 400, 250, 80, Black,user, 35, "Rights24")
			options("Trillums", 525, 400, 250, 80, Black, user, 35, "wrongs24")
		elif v24 == 1:
			gameDisplay.blit(testing77, (display_width/2 - 182,display_height/2-200))
			message_display(Med4[v24],70,30,35,Black)
			options("Wrist", 50, 400, 250, 80, Black, user, 33, "wrongs24")
			options("Leg", 50, 500, 250, 80, Black, user, 35, "wrongs24")
			options("Arm", 525, 500, 250, 80, Black,user, 35, "Rights24")
			options("Head", 525, 400, 250, 80, Black, user, 35, "wrongs24")
		elif v24 == 2:
			gameDisplay.blit(testing78, (display_width/2 - 182,display_height/2-180))
			message_display(Med4[v24],17,30,29,Black)
			options("Liver", 50, 400, 250, 80, Black, user, 33, "wrongs24")
			options("Spleen", 525, 500, 250, 80, Black, user, 35, "wrongs24")
			options("Intestine", 525, 400, 250, 80, Black,user, 35, "Rights24")
			options("Gall Bladder", 50, 500, 250, 80, Black, user, 33, "wrongs24")
		elif v24 == 3:
			gameDisplay.blit(testing79, (display_width/2 - 182,display_height/2-213))
			message_display(Med4[v24],10,30,35,Black)
			options("Altered", 50, 500, 250, 80, Black, user, 33, "wrongs24")
			options("Broken", 525, 500, 250, 80, Black, user, 35, "wrongs24")
			options("Denatured", 50, 400, 250, 80, Black,user, 35, "Rights24")
			options("Bent", 525, 400, 250, 80, Black, user, 35, "wrongs24")
		elif v24 == 4:
			gameDisplay.blit(testing80, (display_width/2 - 182,display_height/2-200))
			message_display(Med4[v24],25,30,21,Black)
			options("NFDH", 50, 400, 250, 80, Black, user, 33, "wrongs24")
			options("FDAH", 525, 500, 250, 80, Black, user, 35, "wrongs24")
			options("NADH", 50, 500, 250, 80, Black,user, 35, "Rights24")
			options("NKLA", 525, 400, 250, 80, Black, user, 35, "wrongs24")
		pygame.display.update()
		clock.tick(15)

def a24():
	global juliet22
	global v24
	v24 = randint(0,4)
	juliet22 = True
	while juliet22:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v24 == 0:
			gameDisplay.blit(testing76, (display_width/2 - 182,display_height/2-200))
			message_display(Med4[v24],95,30,35,Black)
			options("Sunflowers", 50, 400, 250, 80, Black, user, 33, "wrong24")
			options("Mustard", 525, 500, 250, 80, Black, user, 35, "wrong24")
			options("Poppies", 525, 400, 250, 80, Black,user, 35, "Right24")
			options("Trillums", 50, 500, 250, 80, Black, user, 35, "wrong24")
		elif v24 == 1:
			gameDisplay.blit(testing77, (display_width/2 - 182,display_height/2-200))
			message_display(Med4[v24],70,30,35,Black)
			options("Wrist", 50, 500, 250, 80, Black, user, 33, "wrong24")
			options("Leg", 525, 500, 250, 80, Black, user, 35, "wrong24")
			options("Arm", 50, 400, 250, 80, Black,user, 35, "Right24")
			options("Head", 525, 400, 250, 80, Black, user, 35, "wrong24")
		elif v24 == 2:
			gameDisplay.blit(testing78, (display_width/2 - 182,display_height/2-180))
			message_display(Med4[v24],17,30,29,Black)
			options("Liver", 50, 400, 250, 80, Black, user, 33, "wrong24")
			options("Spleen", 525, 500, 250, 80, Black, user, 35, "wrong24")
			options("Intestine", 525, 400, 250, 80, Black,user, 35, "Right24")
			options("Gall Bladder", 50, 500, 250, 80, Black, user, 33, "wrong24")
		elif v24 == 3:
			gameDisplay.blit(testing79, (display_width/2 - 182,display_height/2-213))
			message_display(Med4[v24],10,30,35,Black)
			options("Altered", 50, 400, 250, 80, Black, user, 33, "wrong24")
			options("Broken", 525, 500, 250, 80, Black, user, 35, "wrong24")
			options("Denatured", 50, 500, 250, 80, Black,user, 35, "Right24")
			options("Bent", 525, 400, 250, 80, Black, user, 35, "wrong24")
		elif v24 == 4:
			gameDisplay.blit(testing80, (display_width/2 - 182,display_height/2-200))
			message_display(Med4[v24],25,30,21,Black)
			options("NFDH", 50, 400, 250, 80, Black, user, 33, "wrong24")
			options("FDAH", 50, 500, 250, 80, Black, user, 35, "wrong24")
			options("NADH", 525, 500, 250, 80, Black,user, 35, "Right24")
			options("NKLA", 525, 400, 250, 80, Black, user, 35, "wrong24")
		pygame.display.update()
		clock.tick(15)

def a25s():
	global v25
	global kilo23
	kilo23 = True
	while kilo23:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v25 == 0:
			gameDisplay.blit(testing81, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],104,30,35,Black)
			options("Salicylic Acid", 50, 500, 250, 80, Black, user, 33, "wrongs25")
			options("Sevoflurane", 525, 500, 250, 80, Black, user, 33, "wrongs25")
			options("Acetaminophen", 50, 400, 250, 80, Black,user, 31, "Rights25")
			options("Pepsin", 525, 400, 250, 80, Black, user, 35, "wrongs25")
		elif v25 == 1:
			gameDisplay.blit(testing82, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],27,30,29,Black)
			options("Starch", 50, 400, 250, 80, Black, user, 35, "wrongs25")
			options("Cellulose", 50, 500, 250, 80, Black, user, 35, "wrongs25")
			options("Glycogen", 525, 500, 250, 80, Black,user, 35, "Rights25")
			options("Myoglobin", 525, 400, 250, 80, Black, user, 35, "wrongs25")
		elif v25 == 2:
			gameDisplay.blit(testing83, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],17,30,27,Black)
			options("Head", 50, 500, 250, 80, Black, user, 35, "wrongs25")
			options("Arm", 525, 500, 250, 80, Black, user, 35, "wrongs25")
			options("Wrist", 50, 400, 250, 80, Black,user, 35, "Rights25")
			options("Leg", 525, 400, 250, 80, Black, user, 35, "wrongs25")
		elif v25 == 3:
			gameDisplay.blit(testing84, (display_width/2 - 182,display_height/2-220))
			message_display(Med5[v25],104,30,35,Black)
			options("Abdomen", 50, 400, 250, 80, Black, user, 35, "wrongs25")
			options("Spinal Cord", 50, 500, 250, 80, Black, user, 35, "wrongs25")
			options("Joints", 525, 500, 250, 80, Black,user, 35, "Rights25")
			options("Cranium", 525, 400, 250, 80, Black, user, 35, "wrongs25")
		elif v25 == 4:
			gameDisplay.blit(testing85, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],17,30,20,Black)
			options("Adenosine", 50, 400, 250, 80, Black, user, 35, "wrongs25")
			options("Adenine", 525, 500, 250, 80, Black, user, 35, "wrongs25")
			options("Uracil", 50, 500, 250, 80, Black,user, 35, "Rights25")
			options("Thymine", 525, 400, 250, 80, Black, user, 35, "wrongs25")
		pygame.display.update()
		clock.tick(15)

def a25():
	global juliet23
	global v25
	v25 = randint(0,4)
	juliet23 = True
	while juliet23:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background7, (0,0))
		if v25 == 0:
			gameDisplay.blit(testing81, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],104,30,35,Black)
			options("Salicylic Acid", 50, 400, 250, 80, Black, user, 33, "wrong25")
			options("Sevoflurane", 50, 500, 250, 80, Black, user, 33, "wrong25")
			options("Acetaminophen", 525, 500, 250, 80, Black,user, 31, "Right25")
			options("Pepsin", 525, 400, 250, 80, Black, user, 35, "wrong25")
		elif v25 == 1:
			gameDisplay.blit(testing82, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],27,30,29,Black)
			options("Starch", 50, 400, 250, 80, Black, user, 35, "wrong25")
			options("Cellulose", 525, 500, 250, 80, Black, user, 35, "wrong25")
			options("Glycogen", 50, 500, 250, 80, Black,user, 35, "Right25")
			options("Myoglobin", 525, 400, 250, 80, Black, user, 35, "wrong25")
		elif v25 == 2:
			gameDisplay.blit(testing83, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],17,30,27,Black)
			options("Head", 50, 400, 250, 80, Black, user, 35, "wrong25")
			options("Arm", 525, 500, 250, 80, Black, user, 35, "wrong25")
			options("Wrist", 525, 400, 250, 80, Black,user, 35, "Right25")
			options("Leg", 50, 500, 250, 80, Black, user, 35, "wrong25")
		elif v25 == 3:
			gameDisplay.blit(testing84, (display_width/2 - 182,display_height/2-220))
			message_display(Med5[v25],104,30,35,Black)
			options("Abdomen", 50, 400, 250, 80, Black, user, 35, "wrong25")
			options("Spinal Cord", 525, 500, 250, 80, Black, user, 35, "wrong25")
			options("Joints", 50, 500, 250, 80, Black,user, 35, "Right25")
			options("Cranium", 525, 400, 250, 80, Black, user, 35, "wrong25")
		elif v25 == 4:
			gameDisplay.blit(testing85, (display_width/2 - 182,display_height/2-200))
			message_display(Med5[v25],17,30,20,Black)
			options("Adenosine", 50, 400, 250, 80, Black, user, 35, "wrong25")
			options("Adenine", 50, 500, 250, 80, Black, user, 35, "wrong25")
			options("Uracil", 525, 500, 250, 80, Black,user, 35, "Right25")
			options("Thymine", 525, 400, 250, 80, Black, user, 35, "wrong25")
		pygame.display.update()
		clock.tick(15)

#This function is used to make the color of the button grey it is a simplified version the levels and options function above in that it is not interactive
def used(inactive, x, y, width, height, message, size):
	pygame.draw.rect(gameDisplay, inactive, (x,y,width,height))
	center(message, size, (x + (width/2)), (y + (height/2)), White)

#This fucntion displays the final points when the game is finished
def finish():
	#To be finished move button and add background make look prity
	global finsihing
	global points_jackk
	global points_Taha
	while finsihing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background5, (0,0))
		center("Final score is", 55, display_width/2, 200 , Black)
		message_display(str(points_Taha),575,500,30, Blue)
		message_display("Taha's points equal:", 450, 450, 30, Blue)
		message_display("Jackk's points equal:",50, 450, 30, Red)
		message_display(str(points_jackk),175, 500, 30, Red)
		starts("Done!", display_width/2-47, display_height/2 + 40, 100, 70, user, Black, 28, "Finish")
		pygame.display.update()
		clock.tick(15)

#This function shows the main menu when the game is started
def game_boot():
	begin = True
	while begin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(White)
		gameDisplay.blit(Background1, (0,0))
		gameDisplay.blit(Text1241, (50,50))
		starts("Quick Play", 550, 100, 175, 70, user, Buttons, 30, "Quick Play")
		starts("Instructions", 550, 225, 175, 70, user, Buttons, 27, "Instructions")
		starts("Help", 550, 350, 175, 70, user, Buttons, 30,"Help")
		starts("Quit", 550, 475, 175, 70, user, Buttons, 30,"Quit")
		pygame.display.update()
		clock.tick(15)

#This function is run when the help button is clicked on
def Help1():
	global tanas
	tanas = True
	while tanas:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		center("Jeopardy 2017 - 2018", 35, display_width/2, 200, White)
		center("All Rights Reserved", 35, display_width/2, 300, White)
		center("Report problems to nadeem.shaheer2@gmail.com", 31, display_width/2, 400, White)
		starts("Back", display_width/2-75, 500, 175,70,user, Buttons,30,"Oks")
		pygame.display.update()
		clock.tick(15)

#This function is run when the instructions button is clicked on
def instructions1():
	global tanas
	tanas = True
	while tanas:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(Background4, (0,0))
		gameDisplay.blit(adgk, (0,75))
		center("Click on Quick Play button. Then pick a nickname", 31, display_width/2, 100, White)
		center("with your partner as well as the assossiated", 31, display_width/2, 150, White)
		center("color. Then choose a question from the categories.", 31, display_width/2, 200, White)
		center("The question number is equal to the points its", 31, display_width/2, 250, White)
		center("worth. If you get the question wrong your partner", 31, display_width/2, 300, White)
		center("get's to steal the question. Play until the end", 31, display_width/2, 350, White)
		center("to see if your good enough to beat you're partner.", 31, display_width/2, 400, White)
		starts("Back", display_width/2-75, 500, 175,70,user, Buttons,30,"Oks")
		pygame.display.update()
		clock.tick(15)

#This function displays the two nicknames allowing the user to pick with his partner the names he likes
def intro_screen():
	global echo
	while echo:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(White)
		center("Please choose a color and the assossiated", 35, display_width/2, 30, Black)
		center("nickname with your partner", 35, display_width/2, 70, Black)
		center("Jakk play's first!", 37, display_width/2, 150, Black)
		message_display("= Jakk",display_width/2+55, display_height/2 -35, 35,Red)
		pygame.draw.rect(gameDisplay, Red, (display_width/2-100,display_height/2-40,120,50))
		message_display("= Taha", display_width/2+55, display_height/2 + 47, 35, Blue)
		pygame.draw.rect(gameDisplay, Blue, (display_width/2-100,display_height/2+40,120,50))
		pygame.display.update()
		sleep(5)
		PlayDisplay()

#This function shows all the buttons for each category and switches the color is they have already been played. Also assgins the ponts for each button
def PlayDisplay():
	global echo 
	echo = False
	jack = True
	controllers()
	while jack:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()	
		gameDisplay.fill(Black)
		gameDisplay.blit(Background2, (0,0))
		catagories("Countries",29, 20, 125, 55, 24)
		if c1 == False and c2 == False and c3 == False and c4 == False and c5 == False and c6 == False and c7 == False and c8 == False and c9 == False and c10 == False and c11 == False and c12 == False and c13 == False and c14 == False and c15 == False and c16 == False and c17 == False and c18 == False and c19 == False and c20 == False and c21 == False and c22 == False and c23 == False and c24 == False and c25 == False:
			finish()
		else: 
			if c1 == True:		
				Levels("100", 33, 100, 115, 50, Buttons, B1, 26,"Run1")
			else: 
				used(user, 33, 100, 115, 50, "100", 26)
			if c2 == True:
				Levels("200", 33, 200, 115, 50, Buttons, B1, 26, "Run2")
			else: 
				used(user, 33, 200, 115, 50, "200", 26)
			if c3 == True:
				Levels("300", 33, 300, 115, 50, Buttons, B1, 26, "Run3")
			else:
				used(user, 33, 300, 115, 50, "300", 26)
			if c4 == True:
				Levels("400", 33, 400, 115, 50, Buttons, B1, 26, "Run4")
			else: 
				used(user, 33, 400, 115, 50, "400", 26)
			if c5 == True:
				Levels("500", 33, 500, 115, 50, Buttons, B1, 26, "Run5")
			else: 
				used(user, 33, 500, 115, 50, "500", 26)

			catagories("Math", 182, 20 , 125, 55, 24)

			if c6 == True:
				Levels("100", 186, 100, 115, 50, Buttons, B1, 26, "Run6")
			else:
				used(user, 186, 100, 115, 50, "100", 26)
			if c7 == True:
				Levels("200", 186, 200, 115, 50, Buttons, B1, 26, "Run7")
			else:
				used(user, 186, 200, 115, 50, "200", 26)
			if c8 == True:
				Levels("300", 186, 300, 115, 50, Buttons, B1, 26, "Run8")
			else:
				used(user, 186, 300, 115, 50, "300", 26)
			if c9 == True:
				Levels("400", 186, 400, 115, 50, Buttons, B1, 26, "Run9")
			else:
				used(user, 186, 400, 115, 50, "400", 26)
			if c10 == True:
				Levels("500", 186, 500, 115, 50, Buttons, B1, 26, "Run10")
			else:
				used(user, 186, 500, 115, 50, "500", 26)

			catagories("Facts", 337, 20, 125, 55, 24)

			if c11 == True:
				Levels("100", 341, 100, 115, 50, Buttons, B1, 26, "Run11")
			else:
				used(user, 341, 100, 115, 50, "100", 26)
			if c12 == True:
				Levels("200", 341, 200, 115, 50, Buttons, B1, 26, "Run12")
			else:
				used(user, 341, 200, 115, 50, "200", 26)
			if c13 == True:
				Levels("300", 341, 300, 115, 50, Buttons, B1, 26, "Run13")
			else:
				used(user, 341, 300, 115, 50, "300", 26)
			if c14 == True:
				Levels("400", 341, 400, 115, 50, Buttons, B1, 26, "Run14")
			else:
				used(user, 341, 400, 115, 50, "400", 26)
			if c15 == True:
				Levels("500", 341, 500, 115, 50, Buttons, B1, 26, "Run15")
			else:
				used(user, 341, 500, 115, 50, "500", 26)

			catagories("Science", 492, 20, 125, 55, 24)

			if c16 == True:
				Levels("100", 496, 100, 115, 50, Buttons, B1, 26, "Run16")
			else:
				used(user, 496, 100, 115, 50, "100", 26)
			if c17 == True:
				Levels("200", 496, 200, 115, 50, Buttons, B1, 26, "Run17")
			else:
				used(user, 496, 200, 115, 50, "200", 26)
			if c18 == True:
				Levels("300", 496, 300, 115, 50, Buttons, B1, 26, "Run18")
			else:
				used(user, 496, 300, 115, 50, "300", 26)
			if c19 == True:
				Levels("400", 496, 400, 115, 50, Buttons, B1, 26, "Run19")
			else:
				used(user, 496, 400, 115, 50, "400", 26)
			if c20 == True:
				Levels("500", 496, 500, 115, 50, Buttons, B1, 26, "Run20")
			else:
				used(user, 496, 500, 115, 50, "500", 26)

			catagories("Medicine", 647, 20, 125, 55, 24)

			if c21 == True:
				Levels("100", 651, 100, 115, 50, Buttons, B1, 26, "Run21")
			else:
				used(user, 651, 100, 115, 50, "100", 26)
			if c22 == True:
				Levels("200", 651, 200, 115, 50, Buttons, B1, 26, "Run22")
			else:
				used(user, 651, 200, 115, 50, "200", 26)
			if c23 == True:
				Levels("300", 651, 300, 115, 50, Buttons, B1, 26, "Run23")
			else:
				used(user, 651, 300, 115, 50, "300", 26)
			if c24 == True:
				Levels("400", 651, 400, 115, 50, Buttons, B1, 26, "Run24")
			else:
				used(user, 651, 400, 115, 50, "400", 26)
			if c25 == True:
				Levels("500", 651, 500, 115, 50, Buttons, B1, 26, "Run25")
			else:
				used(user, 651, 500, 115, 50, "500", 26)
		pygame.display.update()  
		clock.tick(30)
		#print counter

#These functions allow the user to quit if they wish
game_boot()
PlayDisplay()
pygame.quit()
quit()
