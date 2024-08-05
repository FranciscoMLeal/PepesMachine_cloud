# from os import write, replace
# from typing import Pattern, Text
import pygame
import random
from PepePatterns import PatternStyles
import ecra

# import importlib


def get_canvas_dimensions(canvas_dividend=100):
    # with open("twin_text.txt", "r") as f:
    #     lines = f.readlines()
    # for line in lines:
    #     if "height" in line:
    #         altTela = int(line.split("=")[1])
    #     if "width" in line:
    #         largTela = int(line.split("=")[1])
    #     if "canvas_dividend" in line:
    #         canvas_dividend = int(line.split("=")[1])

    pygame.init()
    infoObject = pygame.display.Info()
    largTela = int(1241 * 1.7) #infoObject.current_w
    altTela = int(1128 * 1.7) #infoObject.current_h
    #Programar aqui self.DivLarg
    divLarg = int((largTela/canvas_dividend)/2)    #int(input("Numero de lados:"))
    # if divLarg <= 5:
    #     divLarg = 6
    divAlt = int((altTela/canvas_dividend)/2)
    screen = pygame.display.set_mode((largTela, altTela), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("PEPESMACHINE_CLOUDFLARE")
    #screen.fill((255,255,255))
    return altTela,largTela,divAlt,divLarg,screen


    ##### MAKE THE WEATHER COLORS ######



# def get_final_pepecolors(number_of_colors):
#     FinalPepeColors = {}
#     with open("twin_text.txt", "r") as f:
#         lines = f.readlines()
#     for line in lines:
#         if "FinalPepeColors" in line:
#             All_Colors = eval(line.split("=")[1])
#             print(f"ALLLL COLORS = {All_Colors}")
#             break
#     x = 0
#     breakinfiniteloop = 0
#     while x <= number_of_colors - 1:
#         y = random.randrange(0,len(All_Colors))
#         FinalPepeColors[x] = All_Colors[y]
#         print(f"FINALPEPECOLORS = {FinalPepeColors[x]}")
#         z = 0
#         while z < x:
#             if FinalPepeColors[x] == FinalPepeColors[z] and breakinfiniteloop < 1500:
#                 x = x - 1
#                 breakinfiniteloop = breakinfiniteloop + 1
#                 print(f"breakinfiniteloop={breakinfiniteloop}")
#                 break
#             z = z + 1
#         x = x + 1
#     return(All_Colors)




canIgoback = False
canIgobackintoFuture = False
gofoward = True
isdrawn = 0



altTela,largTela,divAlt,divLarg,screen = get_canvas_dimensions()
x = 0
y = 0
steps = 0
cc = 1
cr = 1
PepeQuad = [(0,0),(1,1),(2,2)]
Filletes = []
FilletesCor = []
PatColorHolder = []
CorFundoHolder = ["#000000","#000000"]
CorPatternHolder = ["#000000","#000000"]
ShapeComandHolder = ["tt"]
ShapeComandList = ["pq","lp","tp","zz","45","intc","allint","lofi","dirsq","qsh","zza","meg","smlq","dr","de","cas","casl2","wl","tcc","it","dpp","megt","qshr","dcf","lisb"]#,"pepes","flow","ocp","st","cic","hlp","cp","lil","t","ssi","sqi","cicin","s","tgp","dl",,"clds","mst","eye","l","gr","vlp","lisb"]  nicecombination["dirsq","qsh","zza","meg","smlq","dr","de","cas"]

ShapeSquares = ["pq","lp","tp","zz","45","dirsq","zza","meg","smlq","wl","tcc","it","megt","lisb"]
ShapeCircles =["intc","allint","lofi","qsh","dr","de","cas","casl2","dpp","qshr","dcf"]
SquareCombo = [ShapeComandList,ShapeSquares]
CircleCombo = [ShapeComandList,ShapeCircles]

Ypoints = []
points = []

#SavePepes = []
choosePat = False

#screen = pygame.display.set_mode((largTela, altTela), pygame.HWSURFACE | pygame.DOUBLEBUF)
RandomNum = [2,3,4,5]

ADN = []

patternEssencials = [divLarg,divAlt,largTela,altTela,screen]


# FinalPepeColors = get_final_pepecolors(5)

# def set_new_colors(number_of_colors = 5):
#     global FinalPepeColors
#     FinalPepeColors = get_final_pepecolors(number_of_colors)

# AdnRegistry  = open("babypepes.py", "a+")
# CanvasRegistry  = open("babypepesCanvassize.py", "a+")

SavedPepe = []

def set_ADN_to_nothing():
    global ADN
    ADN = []

# class GridGenerator:
#     def __init__(self):
#         self.background_colour = (255,255,255)
#         self.screen = pygame.display.set_mode((largTela, altTela))

#         self.name = pygame.display.set_caption('RLBB')
#         self.screen.fill(self.background_colour)


#     def draw(self):
#         self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions()
#         for y in range(self.divAlt):
#             for x in range(self.divLarg):
#                 self.PatColor = random.choice(FinalPepeColors)
#                 self.imaa = pygame.draw.rect(self.screen,self.PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),self.largTela/self.divLarg,self.altTela/self.divAlt))
#                 x+=1
#             x=0
#             y+=1
#         #pygame.display.flip()

class PepeAI:
    def __init__(self,cores,pattern_geo):
        self.GetColors(cores)
        self.GetPatternShape(pattern_geo)

    def GetColors(self,cores):
        self.pepeCores = cores
        self.colorFundo = random.choice(self.pepeCores)
        self.colorPattern = random.choice(self.pepeCores)

        #print("FUNDO COLOR HOLDER =", CorFundoHolder[-1],"NEW FUNDO COLOR =",self.colorFundo,"OLD PATTERN COLOR =",CorPatternHolder[-1],"NEW PATTERN COLOR",self.colorPattern )

        while self.colorPattern == self.colorFundo: # or self.colorPattern == CorPatternHolder[-1]:# or self.colorFundo == CorFundoHolder[-1] or self.colorFundo == CorPatternHolder[-1] or self.colorPattern == CorFundoHolder[-1]:
            self.colorPattern = random.choice(self.pepeCores)
            self.colorFundo = random.choice(self.pepeCores)
        #    #print("REPEAT MODE ACTIVATED : FUNDO COLOR HOLDER =", CorFundoHolder[-1],"NEW FUNDO COLOR =",self.colorFundo,"OLD PATTERN COLOR =",CorPatternHolder[-1],"NEW PATTERN COLOR",self.colorPattern )
        #
        #CorFundoHolder.append(self.colorFundo)
        #CorPatternHolder.append(self.colorPattern)

    def GetPatternShape(self,pattern_geo):
        if pattern_geo <=2:
            self.ShapeComand = random.choice(ShapeSquares)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(ShapeSquares)
        elif pattern_geo <= 4:
            color_list = random.choice(SquareCombo)
            self.ShapeComand = random.choice(color_list)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(color_list)
                
        elif pattern_geo <= 6:
            self.ShapeComand = random.choice(ShapeComandList)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(ShapeComandList)
                
        elif pattern_geo <= 8:
            color_list = random.choice(CircleCombo)
            self.ShapeComand = random.choice(color_list)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(color_list)                
        else:
            self.ShapeComand = random.choice(ShapeCircles)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(ShapeCircles)            




class PepeDrawer:
    def __init__(self,CorFundo,CorPattern,PepeQuad1,PepeQuad2,ShapeComand,canvas_dividend):
        self.CorFundo = CorFundo
        self.CorPattern = CorPattern
        self.FirstX,self.FirstY = PepeQuad1
        self.SecX,self.SecY = PepeQuad2
        self.ShapeComand = ShapeComand

        ###################

        self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions(canvas_dividend)

    #### DRAWS FUNDOS
    def startbyFilette(self):
        if self.SecX < self.FirstX:
            self.SizeX = (self.FirstX - self.SecX)
            self.FirstX = self.SecX

        else:
            self.SizeX = (self.SecX - self.FirstX)

        if self.SecY < self.FirstY:
            self.SizeY = (self.FirstY - self.SecY)
            self.FirstY = self.SecY

        else:
            self.SizeY = (self.SecY - self.FirstY)

        self.RealDirectionX = self.SizeX * (self.largTela/self.divLarg)
        self.RealDirectionY = self.SizeY * (self.altTela/self.divAlt)

        ### Transforms Square Fillettes Patterns in circles and Stairs
        #if self.SizeX == self.SizeY and choosePat == False:
        #    self.ShapeComand = random.choice(ShapeComandSquaresList)
        #    while self.ShapeComand == ShapeComandHolder[-1]:
        #        self.ShapeComand = random.choice(ShapeComandSquaresList)
        Filletes.append((self.FirstX,self.FirstY,self.RealDirectionX,self.RealDirectionY))
        print("TA AQUI O ERRO, self.Corfundo =",self.CorFundo)
        novopadrao = pygame.draw.rect(screen,self.CorFundo,((self.largTela/self.divLarg)*self.FirstX,((self.altTela/self.divAlt)*self.FirstY),self.RealDirectionX,self.RealDirectionY))
        self.DrawPattern()
        #pygame.display.flip() # mac solution
        pygame.display.update(novopadrao) # debian solution



    ####READS SHAPECOMAND AND DRAWS PATTERNS

    def DrawPattern(self):
        patternEssencials = []
        patternEssencials = [self.divLarg,self.divAlt,self.largTela,self.altTela,screen]
        patrao = PatternStyles(self.CorFundo,self.CorPattern,Filletes,patternEssencials,(self.FirstX,self.FirstY),(self.SecX,self.SecY))
        # if self.ShapeComand == "c":
        #     patrao.MakesCirclesOnFillete()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        #elif self.ShapeComand == "pepes":
        #    patrao.pepesAiSignature(FinalPepeColors)
        #    #pygame.display.flip()
        #    ShapeComandHolder.append(self.ShapeComand)
        if self.ShapeComand == "cic":
            patrao.MakesCirclesinCirclesOnFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)

        # elif self.ShapeComand == "cp":
        #     patrao.MakesCirclesPatternOnFillete(self.CorPattern)
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "t":
        #     patrao.MakesTriangleOnFillete(self.CorPattern)
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "tp":
            patrao.MakesTrianglePatternOnFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "clds":
            patrao.draw_clouds()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "flow":
            patrao.draw_flower_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "eye":
            patrao.draw_eyes()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "megt":
            patrao.draw_meggie_triangles()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "vlp":
            patrao.MakesVerticalLinePatternOnFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "hlp":
        #     patrao.MakesHorizontalLinePatternOnFillete()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "pq":
            patrao.MakesPatternQuadradosOnFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "mst":
            patrao.draw_meggie_setes()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "st":
            patrao.MakesStairsonFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "gr":
            patrao.MakesGridonFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "sqi":
        #     patrao.MakeSquaresInsideSquares()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "lil":
        #     patrao.MakesLosangleInsideLosangle()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "l":
            patrao.MakesLosangleFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lp":
            patrao.MakesLosanglePatternFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "dcf":
            patrao.draw_convex_circle_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "s":
        #     patrao.MakeSetas()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "tgp":
        #     patrao.MakesTriangleGridPatternFillete()
        #     #pygame.display.flip()
        #    ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "dl":
        #     patrao.MakesDistortLosanglesPatternFillete()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "45":
            patrao.Makes45gLinesPatternFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "intc":
            patrao.draw_interlocking_circles_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "ocp":
            patrao.draw_overlapping_circles_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "wl":
            patrao.Makes_weird_lines()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lisb":
            patrao.draw_lisbonflag()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "tcc":
            patrao.Makes_triangle_combinations()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "casl2":
            patrao.draw_circles_and_stars_lvl2()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "dpp":
            patrao.draw_pills_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "de":
            patrao.draw_estrelas()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "dr":
            patrao.draw_ropes_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "cas":
            patrao.draw_circles_and_stars()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "zza":
            patrao.MakesZigZagArrows()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "ssi":
        #     patrao.draw_all_squares_with_inner()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "meg":
            patrao.MakesZigZagbyMegs()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "smlq":
            patrao.draw_small_square()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "qsh":
            patrao.draw_quarter_shell_circles_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "qshr":
            patrao.draw_quarter_shell_random()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lofi":
            patrao.draw_lofi_circles_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "dirsq":
            patrao.draw_dir_squares_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "it":
            patrao.draw_interlocking_triangles()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        # elif self.ShapeComand == "cicin":
        #     patrao.draw_all_circles_with_innercircles_pattern()
        #     #pygame.display.flip()
        #     ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "allint":
            patrao.draw_all_circles_pattern()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "zz":
            patrao.MakesZigZagPatternFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        else:
            print("You did nothing BITCH")

class StartPepeFunction:
    def __init__(self,colors,canvas_dividend,pattern_geo):
        self.Xpoints = []
        set_ADN_to_nothing()

        self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions(canvas_dividend)

        self.start(colors,canvas_dividend,pattern_geo)

    def start(self,colors,canvas_dividend,pattern_geo):
        x = 0
        while x < self.divLarg:
            self.Xpoints.append(x)
            NewNum = random.choice(RandomNum) ### PEPESAI COULD MESS AROUND HERE
            x = x + NewNum
        self.Xpoints.append(self.divLarg) # adds last point of grid
        self.rowNumber = len(self.Xpoints)

        a = 0
        while a < self.rowNumber-1:
            a = a + 1
            self.Ypoints = []
            y = 0
            while y < self.divAlt:
                self.Ypoints.append(y)
                #pygame.display.flip
                NewNum = random.choice(RandomNum) ### PEPESAI COULD MESS AROUND HERE
                if y + NewNum > self.divAlt:   ### condition for not going out of the canvas in y direction
                    NewNum = self.divAlt - y
                NewPepe = PepeAI(colors,pattern_geo)
                #NewPepe = check_for_touching_colors(self,ADN,NewPepe,a,y,NewNum)    ### MAKES PEPERULES NOT WORKING DUE TO SPEED

                newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),NewPepe.ShapeComand,canvas_dividend)
                newPepitos.startbyFilette()
                # ecra.write_to_fast_terminal("BackgroundColor = " + NewPepe.colorFundo)
                # ecra.write_to_fast_terminal("PatternColor = " + NewPepe.colorPattern)
                ADN.append((NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),newPepitos.ShapeComand))
                ### Save Here The Pepe Reference Coordinates
                ###
                y = y + NewNum
            # ecra.write_to_fast_terminal(str(self.Xpoints) + str(self.Ypoints))
    def get_screen(self):
        return self.screen