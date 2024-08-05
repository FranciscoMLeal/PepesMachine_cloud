import pygame
import random


#####################
#####################
#####################   Padroes aqui passaram a variaveis de outros que são parecidos

def MakesHorizontalLinePatternOnFillete(self):
    x,y,NFsizeX,NFsizeY = self.Filletes[-1]
    rangeX = NFsizeX / (self.largTela/self.divLarg)
    rangeY = NFsizeY / (self.altTela/self.divAlt)
    PatColor = self.CorPattern
    if rangeY % 2 == 0:
        rangeC = (rangeY / 2)
    else:
        rangeC = rangeY / 2 + 1
    for mk in range(int(rangeC)):
        sizeY = NFsizeY/rangeY
        sizeX = NFsizeX
        #print("I m A Square",x,rangeY,mk,rangeC)
        self.DrawLinePatternOnFillete(x,y,sizeX,sizeY,PatColor)
        y += 2
        mk += 2
        
def MakesCirclesOnFillete(self):
    x,y,sizeX,sizeY = self.Filletes[-1]
    center = (x * (self.largTela/self.divLarg)) + (sizeX/2),(y * (self.altTela/self.divAlt))+ (sizeY/2)
    if sizeX > sizeY:
        rad = sizeY/2
    elif sizeY > sizeX:
        rad = sizeX/2
    else:
        rad = sizeY/2
    pygame.draw.circle(self.screen,self.CorPattern,center,rad)
        
        
#####################
#####################
#####################

class PatternStyles:
    def __init__(self,CorFundo,CorPattern,Filletes,patternEssencials,PepeQuad1,PepeQuad2):
        self.CorPattern = CorPattern
        self.CorFundo = CorFundo
        self.Filletes = Filletes
        self.patternEssencials = patternEssencials
        self.divLarg = patternEssencials[0]
        self.divAlt = patternEssencials[1]
        self.largTela = patternEssencials[2]
        self.altTela = patternEssencials[3]
        self.screen = patternEssencials[4]
        self.PepeQuad1 = PepeQuad1
        self.PepeQuad2 = PepeQuad2
        

    def pepesAiSignature(self,FinalPepeColors):
        x,y,sizeX,sizeY = self.Filletes[-1]

        oldX = x
        Xtimes = int(sizeX / (self.largTela/self.divLarg))
        Ytimes = int(sizeY / (self.altTela/self.divAlt))

        for yfuck in range(Ytimes):
            for xfuck in range(Xtimes):
                self.PatColor = random.choice(FinalPepeColors)
                self.imaa = pygame.draw.rect(self.screen,self.PatColor,((self.largTela/self.divLarg)*(x+xfuck) ,((self.altTela/self.divAlt)*(y+yfuck)),self.largTela/self.divLarg,self.altTela/self.divAlt))
                print("x = ",x,"y =",y)
                xfuck+=1
            xfuck=oldX
            yfuck+=1
        print("ITTs working",FinalPepeColors)
      
    

    def MakeSquaresInsideSquares(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        startpoint1 = (x * (self.largTela/self.divLarg)) + (sizeX/4),(y * (self.altTela/self.divAlt))+ (sizeY/4)
        dimensions1 = (sizeX/4) * 2, (sizeY/4) * 2
        
        startpoint2 = startpoint1[0] + dimensions1[0]/4, startpoint1[1] + dimensions1[1]/4
        dimensions2 = dimensions1[0]-((dimensions1[0]/4)*2), dimensions1[1]- ((dimensions1[1]/4)*2)
        
        startpoint0 = (x * (self.largTela/self.divLarg)) + (sizeX/8),(y * (self.altTela/self.divAlt))+ (sizeY/8)
        dimensions0 = dimensions1[0] + ((sizeX/8)*2), dimensions1[1] + ((sizeY/8) * 2)

        pygame.draw.rect(self.screen,self.CorPattern,(startpoint0,dimensions0))
        pygame.draw.rect(self.screen,self.CorFundo,(startpoint1,dimensions1))
        pygame.draw.rect(self.screen,self.CorPattern,(startpoint2,dimensions2))
    

    def MakesCirclesinCirclesOnFillete(self):
        random_variable = random.randint(1,2)
        if random_variable == 1:
            Patcolor = self.CorPattern

            x,y,sizeX,sizeY = self.Filletes[-1]

            center = (x * (self.largTela/self.divLarg)) + (sizeX/2),(y * (self.altTela/self.divAlt))+ (sizeY/2)
            if sizeX > sizeY:
                rad = sizeY/2
            elif sizeY > sizeX:
                rad = sizeX/2
            else:
                rad = sizeY/2
            pygame.draw.circle(self.screen,Patcolor,center,rad)
            pygame.draw.circle(self.screen,self.CorFundo,center,(rad/3)*2)
            pygame.draw.circle(self.screen,Patcolor,center,rad/3)
        elif random_variable == 1:
            MakesCirclesOnFillete(self)
        elif random_variable == 2:
            self.MakesCirclesPatternOnFillete(self.CorPattern)
        


    ### Pattern Shapes --- Not in order sorry

    def MakeSquarePattern(self):
        x = int(input("Start Horizontal: ")) - 1
        y = int(input("Start Vertical: ")) - 1
        PatColor = self.CorPattern
        self.DrawSquarePattern()


    def DrawSquarePattern(self,x,y,PatColor):
        daseX =((self.largTela/self.divLarg)/2)
        daseY =((self.altTela/self.divAlt)/2)
        cubo1 = pygame.draw.rect(self.screen,PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),((self.largTela/self.divLarg)/2),((self.altTela/self.divAlt)/2)))
        cubo2 = pygame.draw.rect(self.screen,PatColor,(((self.largTela/self.divLarg)*x) + daseX,((self.altTela/self.divAlt)*y) + daseY,((self.largTela/self.divLarg)/2),((self.altTela/self.divAlt)/2)))
        #print("made Square Pattern",daseX,daseY)

    def LineSquarePattern(self,x,y):
        x,y = self.PepeQuad2
        x = x - 1
        y = y - 1
        comp,alt = self.PepeQuad1
        PatColor = self.CorPattern
        for y in range(y,y + alt):
            self.LinePattern(x,y,PatColor,comp)

    def LinePattern(self,x,y,PatColor,comp):
        for x in range(x,x+comp):
            self.DrawSquarePattern(x,y,PatColor)
            x += 1


    # Fillete Shapes

    def MakesZigZagPatternFillete(self):   
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        therealX = realX

        PatColor = self.CorPattern

    
        for s in range(ny):
            if s % 2 == 0:
                a = 0
            else:
                a = qx
            #realX = therealX + (s*qx)
            for p in range(nx):
                pos1 = (realX + (qx*p))+a, (realY) + (qy*s)
                pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                pos3 = ((realX + qx) + (qx*p)), (realY + qy) + (qy*s)
                p += 1
                #pygame.draw.rect(self.screen,PatColorHolder[-1],(pos1[0],pos1[1],qx,qy))
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                #print(p,s,pos1,pos2,pos3,PatColorHolder[-1],PatColor,"par")
            s +=1              

    def MakesZigZagArrows(self):   
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        PatColor = self.CorPattern
        for s in range(ny):
            if s % 2 == 0:
                a = 0
            else:
                a = qy
            #realX = therealX + (s*qx)
            for p in range(nx):
                pos1 = (realX + (qx*p)), (realY) + (qy*s)
                pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                pos3 = ((realX + qx) + (qx*p)), (realY + a) + (qy*s)
                p += 1
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
            s +=1         
    
    def MakesZigZagbyMegs(self):  
        random_variable = random.randint(1,2)
        if random_variable == 1: 
            x,y,sizeX,sizeY = self.Filletes[-1]
            nx = int(sizeX/(self.largTela/self.divLarg))
            ny = int(sizeY/(self.altTela/self.divAlt))
            qx = self.largTela/self.divLarg
            qy = self.altTela/self.divAlt
            realX = x * qx
            realY = y * qy
            PatColor = self.CorPattern
            for s in range(ny):
                if s % 2 == 0:
                    a = 0
                    b = 0
                else:
                    a = qy
                    b = qx
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + b + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                    pos3 = ((realX + qx) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                s +=1    
        else:
            self.MakesDistortLosanglesPatternFillete()
    
    
    def Makes_weird_lines(self):   
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        PatColor = self.CorPattern
        random_variable = random.randint(4,4)
        
        if random_variable == 2:
            for s in range(ny):
                if s % 2 == 0:
                    a = 0
                    b = 0
                else:
                    a = qy
                    b = qx
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + (b/2) + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                    pos3 = ((realX + (qx/2)) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                s +=1  
                
        elif random_variable == 3:
            for s in range(ny):
                if s % 2 == 0:
                    a = qy
                    b = qx
                else:
                    a = 0
                    b = 0
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + (b/2) + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                    pos3 = ((realX + (qx/2)) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    if p%2 == 0:                        
                        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                    else:
                        pygame.draw.rect(self.screen, PatColor, (pos1[0],pos1[1],qx,qy+1))
                        pygame.draw.polygon(self.screen,self.CorFundo,(pos1,pos2,pos3))
                s +=1
                
        elif random_variable ==1:
            for s in range(ny):
                if s % 2 == 0:
                    a = qy
                    b = qx
                else:
                    a = 0
                    b = 0
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + (b/2) + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                    pos3 = ((realX + (qx/2)) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    if s%2 == 0:                        
                        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                    else:
                        pygame.draw.rect(self.screen, PatColor, (pos1[0],pos1[1],qx,qy+1))
                        pygame.draw.polygon(self.screen,self.CorFundo,(pos1,pos2,pos3))
                s +=1   
                
        elif random_variable == 4:
            for s in range(ny):
                if s % 2 == 0:
                    a = qy
                    b = qx
                else:
                    a = 0
                    b = 0
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + (b/2) + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                    pos3 = ((realX + (qx/2)) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    if p%2 == 0:
                        if s%2 == 0:                        
                            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                        else:
                            pygame.draw.rect(self.screen, PatColor, (pos1[0],pos1[1],qx,qy+1))
                            pygame.draw.polygon(self.screen,self.CorFundo,(pos1,pos2,pos3))
                    else:
                        if s%2 == 0:                        
                            pygame.draw.rect(self.screen, PatColor, (pos1[0],pos1[1],qx,qy+1))
                            pygame.draw.polygon(self.screen,self.CorFundo,(pos1,pos2,pos3))
                        else:
                            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                s +=1   
                    
    def Makes_triangle_combinations(self):   
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        PatColor = self.CorPattern
        
        random_variant = random.randint(1,3)
        if random_variant == 1:
            for s in range(ny):
                if s % 2 == 0:
                    a = 0
                    b = 0
                    c = qx
                else:
                    a = qy
                    b = qx
                    c = 0
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + (b/2) + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p))+ (c/2), (realY + qy) + (qy*s)
                    pos3 = ((realX + qx) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                s +=1    
        elif random_variant == 2:
            for s in range(ny):
                
                a = qy
                b = qx
                c = qx
                #realX = therealX + (s*qx)
                for p in range(nx):
                    pos1 = (realX + (b/2) + (qx*p)), (realY) + (qy*s)
                    pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                    pos3 = ((realX + qx) + (qx*p)), (realY + a) + (qy*s)
                    p += 1
                    pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                s +=1 
        elif random_variant == 3:
            self.MakesTriangleGridPatternFillete()   
        elif random_variant == 4:
            self.MakeSetas()
            
    def draw_small_square(self):
        random_variable = random.randint(2,2)
        
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    #get centers

                    # Draw top-left semi-circle
                    pygame.draw.rect(self.screen, color1, (cell_x + (qx/4), cell_y + (qy/4),qx/2,qy/2))
                    #pygame.draw.rect(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)))  
        elif random_variable == 2:
            self.draw_all_squares_with_inner()
        elif random_variable == 3:
            self.MakeSquaresInsideSquares()

    def Makes45gLinesPatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        therealX = realX

        PatColor = self.CorPattern

        realPatColor = PatColor
        realFilletesCor = self.CorFundo

        realrealPatColor = PatColor
        realrealFilletesCor = self.CorFundo

    
        for s in range(ny):
            if s % 2 != 0:
                realPatColor = realrealPatColor
                realFilletesCor = realrealFilletesCor 
            else:
                realFilletesCor = realrealPatColor 
                realPatColor = realrealFilletesCor
            #realX = therealX + (s*qx)
            for p in range(nx):
                if p % 2 != 0:
                    PatColor = realFilletesCor
                    self.CorPattern = realPatColor
                else:
                    PatColor = realPatColor
                    self.CorPattern = realFilletesCor
                pos1 = realX + (qx*p), (realY) + (qy*s)
                pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                p += 1
                pygame.draw.rect(self.screen,self.CorPattern,(pos1[0],pos1[1],qx,qy))
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                #print(p,s,pos1,pos2,pos3,PatColorHolder[-1],PatColor,"par")
            s +=1

    def MakesDistortLosanglesPatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy

        PatColor = self.CorPattern


        for s in range(ny):
            for p in range(nx):
                if p % 2 == 0:
                    pos1 = realX + (qx*p), (realY) + (qy*s)
                    pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                    pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                    p += 1
                    pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                else:
                    pos1 = realX + (qx*p), (realY) + (qy*s)
                    pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                    pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                    p += 1
                    pygame.draw.rect(self.screen,PatColor,(pos1[0],pos1[1],qx,qy))
                    pygame.draw.polygon(self.screen,self.CorFundo,(pos1,pos2,pos3))
            s +=1

    def MakesTriangleGridPatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy

        PatColor = self.CorPattern
        for s in range(ny):
            for p in range(nx):
                pos1 = realX + (qx*p), (realY) + (qy*s)
                pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                p += 1
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
            s +=1


    def MakesLosanglePatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        therealY = realY
        PatColor = self.CorPattern

        p = 1


        for s in range(ny):
            realY = therealY
            realY = realY + (qy*s)
            s += 1
            for p in range(nx):

                pos1 = (realX +(qx*p)) + (qx/2), realY
                pos2 = (realX +(qx*p)), realY + (qy/2)
                pos3 = (realX +(qx*p)) + (qx/2), realY + qy
                pos4 = (realX +(qx*p)) + qx, realY + (qy/2)
                p+=1
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3,pos4))


    def MakesLosangleInsideLosangle(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        x = x*(self.largTela/self.divLarg)
        y = y*(self.altTela/self.divAlt)

        pos1 = x + (sizeX/2), y
        pos2 = x , y + (sizeY/2)
        pos3 = x + (sizeX/2) , y + sizeY
        pos4 = x + sizeX , y + (sizeY/2)
        PatColor = self.CorPattern

        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3,pos4))

        pos5 = x + (sizeX/2), y + (sizeY/4)
        pos6 = x + (sizeX/4), y + (sizeY/2)
        pos7 = x + (sizeX/2), y + ((sizeY/4)*3)
        pos8 = x + ((sizeX/4)*3), y + (sizeY/2)

        pygame.draw.polygon(self.screen,self.CorFundo,(pos5,pos6,pos7,pos8))





    def MakesLosangleFillete(self):
        random_variable = random.randint(1,3)
        if random_variable == 1:
            x,y,sizeX,sizeY = self.Filletes[-1]

            x = x*(self.largTela/self.divLarg)
            y = y*(self.altTela/self.divAlt)

            pos1 = x + (sizeX/2), y
            pos2 = x , y + (sizeY/2)
            pos3 = x + (sizeX/2) , y + sizeY
            pos4 = x + sizeX , y + (sizeY/2)
            PatColor = self.CorPattern
            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3,pos4))
        elif random_variable == 2 :
            self.MakesLosangleInsideLosangle()
        elif random_variable == 3:
            self.MakesTriangleOnFillete(self.CorPattern)


    def MakeSetas(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        yLevel = int(sizeY / (self.altTela/self.divAlt))

        x = x*(self.largTela/self.divLarg)
        y = y*(self.altTela/self.divAlt)
        Patcolor = self.CorPattern

        t = x + (sizeX/2), y
        e = x, y + sizeY
        d = x + sizeX, y + sizeY

        CorP = 2

        for f in range(yLevel-1):
            if CorP == 2:
                t = x + (sizeX/2), y + (f * (self.altTela/self.divAlt))
                e = x, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))
                d = x + sizeX, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))
                r = sizeX, (sizeY - (f * (self.altTela/self.divAlt)))- ((self.altTela/self.divAlt)*2)
                pygame.draw.polygon(self.screen,Patcolor,(t,e,d))
                pygame.draw.rect(self.screen,Patcolor,(e,r))
                #print("par",r)
                f +=1
                CorP = 3
            elif CorP == 3:
                t = x + (sizeX/2), y + (f * (self.altTela/self.divAlt))
                e = x, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))
                d = x + sizeX, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))

                r = sizeX, (sizeY - (f * (self.altTela/self.divAlt)))- ((self.altTela/self.divAlt)*2)

                pygame.draw.polygon(self.screen,self.CorFundo,(t,e,d))
                pygame.draw.rect(self.screen,self.CorFundo,(e,r))
                    #print("impar",r)

                f +=1
                CorP = 2


    def MakesCirclesPatternOnFillete(self,CorPattern):
        x,y,sizeX,sizeY = self.Filletes[-1]
        px = x + 1
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        PatColor = CorPattern

        for s in range(0,ny):
            for u in range(0,nx,2):
                if s % 2 == 0:
                    self.MakesCirclesPosforPattern(x+u,y+s,PatColor)
                    #print("CIRCLE ",x+u,y+s," is on",nx+x)
                elif s % 2 != 0 and (px+u)>=(nx+x) and (px+u) != (self.altTela/self.divAlt):
                    print()
                #elif s % 2 != 0 and (px+u) == (self.altTela/self.divAlt):
                #    MakesCirclesPosforPattern(px+u,y+s,PatColor)
                #    print("CIRCLE ",px+u,y+s," is special",nx+x)
                elif s % 2 != 0:
                    self.MakesCirclesPosforPattern(px+u,y+s,PatColor)
                    #print("CIRCLE ",px+u,y+s," is on",nx+x)

    def MakesCirclesPosforPattern(self,NewX,NewY,PatColor):
        center = ((self.largTela/self.divLarg)* NewX) + ((self.largTela/self.divLarg)/2), ((self.altTela/self.divAlt) * NewY) + ((self.altTela/self.divAlt)/2)
        if self.altTela/self.divAlt <= self.largTela/self.divLarg:
            rad = (self.altTela/self.divAlt)/2
        else:
            rad = (self.largTela/self.divLarg)/2
        self.MakesCirclePat(center,rad,PatColor)

    def MakesCirclePat(self,center,rad,PatColor):
        pygame.draw.circle(self.screen,PatColor,center,rad)
        
        #print("IT MAKES CIRCLES")



    def MakesTriangleOnFillete(self,CorPattern):
        random_variable = random.randint(1,2)
        x,y,sizeX,sizeY = self.Filletes[-1]
        
        if random_variable == 1:
            a = sizeX
        else:
            a = 0

        pos1 = x * (self.largTela/self.divLarg) + a, y * (self.altTela/self.divAlt)
        pos2 = x * (self.largTela/self.divLarg), (y * (self.altTela/self.divAlt)) + sizeY
        pos3 = x * (self.largTela/self.divLarg) + sizeX, (y * (self.altTela/self.divAlt)) + sizeY
        self.MakesTriangles(pos1,pos2,pos3,CorPattern)

    def MakesTrianglePatternOnFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        rangeX = int(sizeX / (self.largTela/self.divLarg))
        rangeY = int(sizeY / (self.altTela/self.divAlt))
        mk = 1
        PatColor = self.CorPattern


        if rangeX >= rangeY:
            for mk in range(rangeX):
                pos1 = x * (self.largTela/self.divLarg) + (self.largTela/self.divLarg)*mk, y * (self.altTela/self.divAlt)
                pos2 = x * (self.largTela/self.divLarg) + (self.largTela/self.divLarg)*mk, (y * (self.altTela/self.divAlt)) + sizeY
                pos3 = x * (self.largTela/self.divLarg) + ((self.largTela/self.divLarg)*(mk+1)), (y * (self.altTela/self.divAlt)) + sizeY
                self.MakesTrianglesPattern(pos1,pos2,pos3,PatColor)
                mk += 1
        else:
            for mk in range(rangeY):
                pos1 =  x * (self.largTela/self.divLarg), (y * (self.altTela/self.divAlt)) + ((self.altTela/self.divAlt)*mk)
                pos2 = (x * (self.largTela/self.divLarg))+sizeX, (y * (self.altTela/self.divAlt)) + ((self.altTela/self.divAlt)*mk)
                pos3 = (x * (self.largTela/self.divLarg))+sizeX, (y * (self.altTela/self.divAlt)) + ((self.altTela/self.divAlt)*(mk + 1))
                self.MakesTrianglesPattern(pos1,pos2,pos3,PatColor)
                mk += 1




    def MakesVerticalLinePatternOnFillete(self):
        random_variable = random.randint(0,1)
        if random_variable == 1:
            x,y,NFsizeX,NFsizeY = self.Filletes[-1]
            rangeX = NFsizeX / (self.largTela/self.divLarg)
            rangeY = int(NFsizeY / (self.altTela/self.divAlt))
            PatColor = self.CorPattern
            if rangeX % 2 == 0:
                rangeC = (rangeX / 2)
            else:
                rangeC = rangeX / 2 + 1
            for mk in range(int(rangeC)):
                sizeY = NFsizeY
                sizeX = (NFsizeX/rangeX)
                #print("I m A Square",x,rangeX,mk,rangeC)
                self.DrawLinePatternOnFillete(x,y,sizeX,sizeY,PatColor)
                x += 2
                mk += 2
        else :
            MakesHorizontalLinePatternOnFillete(self)
            
    def MakesGridonFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        lineStroke = 5
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy

        PatColor = self.CorPattern
    
            #draw Horizontal Lines
        for s in range(nx-1):
            s += 1
            pos1 = realX + (qx*s) - (lineStroke/2) , realY
            pos2 = realX + (qx*s) + (lineStroke/2), realY
            pos3 = realX + (qx*s) - (lineStroke/2) , realY + sizeY
            pos4 = realX + (qx*s) + (lineStroke/2) , realY + sizeY

            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos4,pos3))
        #draw Vertical Lines
        for t in range(ny-1):
            t += 1
            pos1 = realX , realY + (qy*t) - (lineStroke/2)
            pos2 = realX , realY + (qy*t) + (lineStroke/2)
            pos3 = realX + sizeX, realY + (qy*t) - (lineStroke/2)
            pos4 = realX + sizeX, realY + (qy*t) + (lineStroke/2)

            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos4,pos3))
            
    def draw_overlapping_circles_pattern(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
    
        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                width = height = qx
    
                # Alternate colors
                color = color1 if (row + col) % 2 == 0 else color2
    
                # Draw two overlapping circles in each cell
                pygame.draw.circle(self.screen, color, (int(cell_x), int(cell_y)), int(width // 2))
                pygame.draw.circle(self.screen, color, (int(cell_x + width // 2), int(cell_y + height // 2)), int(width // 2))


    def draw_quarter_shell_circles_pattern(self):
        
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        # Random Invert
        random_invert = random.randint(1, 4)

        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                # Draw top-left semi-circle
                if random_invert == 1:
                    pygame.draw.circle(self.screen, color1, (cell_x, cell_y), qx,draw_bottom_right=True)
                elif random_invert == 2:
                    pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y+qy), qx,draw_top_left=True) 
                elif random_invert == 3:
                    pygame.draw.circle(self.screen, color1, (cell_x, cell_y+qy), qx,draw_top_right=True)
                elif random_invert == 4:
                    pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y), qx,draw_bottom_left=True)
                    
    def draw_quarter_shell_random(self):
        
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        # Random Invert
        

        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                random_invert = random.randint(1, 4)
                # Draw top-left semi-circle
                if random_invert == 1:
                    pygame.draw.circle(self.screen, color1, (cell_x, cell_y), qx,draw_bottom_right=True)
                elif random_invert == 2:
                    pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y+qy), qx,draw_top_left=True) 
                elif random_invert == 3:
                    pygame.draw.circle(self.screen, color1, (cell_x, cell_y+qy), qx,draw_top_right=True)
                elif random_invert == 4:
                    pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y), qx,draw_bottom_left=True)



    def draw_dir_squares_pattern(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo 
        random_variable = random.randint(1,3)
        
        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                width = height = qx
                if random_variable == 1:
                    if col % 2 == 0:
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                        pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                        pygame.draw.rect(self.screen, color2, (cell_x, cell_y,(qx/5),(qy/5)))
                    else : 
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y,qx,qy+1))
                        pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                        pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y,(qx/5),(qy/5)))
                        
                elif random_variable == 2:
                    pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                    pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                    pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                    pygame.draw.rect(self.screen, color2, (cell_x, cell_y,(qx/5),(qy/5)))
                    
                elif random_variable == 3:
                    if row % 2 == 0:
                        if col % 2 == 0:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y,(qx/5),(qy/5)))
                        else : 
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y,qx,qy+1))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y,(qx/5),(qy/5)))
                    else:
                        if col % 2 == 0:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y,qx,qy+1))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y,(qx/5),(qy/5)))
                        else : 
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 4 * (qx/5), 4 * (qy/5)))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, 3 * (qx/5), 3 * (qy/5)))
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, 2 * (qx/5), 2 * (qy/5)))
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y,(qx/5),(qy/5)))
                



    
    def draw_lofi_circles_pattern(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        random_invert = random.randint(1,3)
        if random_invert == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw right semi-circle
                    pygame.draw.rect(self.screen, color1, (cell_x, cell_y, (qx/2), qy+1))
                    pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                    pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)
        
        elif random_invert == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw right semi-circle
                    if col %2 == 0:
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, (qx/2), qy+1))
                        pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                        pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)
                    else :
                        pygame.draw.rect(self.screen, color2, (cell_x, cell_y, (qx/2), qy+1))
                        pygame.draw.rect(self.screen, color1, (cell_x+ qx/2 + 1, cell_y, (qx/2), qy+1))
                        pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                        pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)

        elif random_invert == 3:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw right semi-circle
                    if row % 2 == 0:
                        if col %2 == 0:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, (qx/2), qy+1))
                            pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                            pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)
                        else :
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, (qx/2), qy+1))
                            pygame.draw.rect(self.screen, color1, (cell_x+ qx/2 + 1, cell_y, (qx/2), qy+1))
                            pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                            pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)
                    else:
                        if col %2 == 0:
                            pygame.draw.rect(self.screen, color2, (cell_x, cell_y, (qx/2), qy+1))
                            pygame.draw.rect(self.screen, color1, (cell_x+ qx/2 + 1, cell_y, (qx/2), qy+1))
                            pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                            pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)
                        else :
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, (qx/2), qy+1))
                            pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_left=True,draw_bottom_left=True)
                            pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/3,draw_top_right=True,draw_bottom_right=True)


    def draw_meggie_triangles(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        random_variable = random.randint(1,4)

        if random_variable == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy            
                    pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx/2, qy+1))
                    pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x, cell_y + (qy/2))])
                    pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x + qx, cell_y + (qy/2))])
        
        elif random_variable == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if col%2 == 0:            
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx/2, qy+1))
                        pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x, cell_y + (qy/2))])
                        pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x + qx, cell_y + (qy/2))])
                    else:
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y + qy/2, qx, qy/2))
                        pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y+qy),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                        pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])

        elif random_variable == 3:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if row % 2 == 0:
                        if col% 2 == 0:            
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx/2, qy+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x + qx, cell_y + (qy/2))])
                        else:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y + qy/2, qx, (qy/2)+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y+qy),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                    else:
                        if col% 2 == 0:            
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y + qy/2, qx, (qy/2)+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y+qy),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                        else:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx/2, qy+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x + qx, cell_y + (qy/2))])
        
        
        elif random_variable == 4:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if row % 2 == 0:
                        if col% 2 == 0:            
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx/2, qy+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x + qx, cell_y + (qy/2))])
                        else:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y + qy/2, qx, (qy/2)+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y+qy),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                    else:
                        if col% 2 == 0:            
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y + qy/2, qx, (qy/2)+1))
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y+qy),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ qx, cell_y+ (qy/2)),(cell_x, cell_y + (qy/2))])
                        else:
                            pygame.draw.rect(self.screen, color1, (cell_x + (qx/2)+1, cell_y, qx/2, qy+1))
                            pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x, cell_y + (qy/2))])
                            pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y),(cell_x+ (qx/2), cell_y+qy),(cell_x + qx, cell_y + (qy/2))])





    def draw_interlocking_triangles(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        random_variable = random.randint(2,3)

        if random_variable == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if col%2==0:
                        pygame.draw.polygon(self.screen, color1, [(cell_x + qx, cell_y),(cell_x+ qx, cell_y+qy),(cell_x, cell_y + (qy/2))])
                    else:
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy+1))
                        pygame.draw.polygon(self.screen, color2, [(cell_x + qx, cell_y),(cell_x+ qx, cell_y+qy),(cell_x, cell_y + (qy/2))])

        elif random_variable == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if col%2==0:
                        pygame.draw.polygon(self.screen, color1, [(cell_x + qx, cell_y),(cell_x+ qx, cell_y+qy),(cell_x, cell_y + (qy/2))])
                    else:
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy+1))
                        pygame.draw.polygon(self.screen, color2, [(cell_x, cell_y),(cell_x, cell_y+qy),(cell_x +qx, cell_y + (qy/2))])
        
        if random_variable == 3:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    pygame.draw.polygon(self.screen, color1, [(cell_x + (qx/2), cell_y),(cell_x+ qx, cell_y+(qy/2)),(cell_x+ qx, cell_y+qy),(cell_x, cell_y + qy),(cell_x, cell_y + (qy/2))])
                    pygame.draw.polygon(self.screen, color2, [(cell_x + (qx/2), cell_y+(qy/2)),(cell_x+ qx, cell_y+qy),(cell_x, cell_y + qy)])
                    


       
    

    def draw_interlocking_circles_pattern(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        random_variable = random.randint(1,5)

        if random_variable == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2

                    # Draw top-left semi-circle
                    pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                    # Draw bottom-right semi-circle
                    pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                    
        elif random_variable == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    # Draw top-left semi-circle
                    pygame.draw.circle(self.screen, color, (cell_x + qx, cell_y), qx/2,draw_bottom_left=True)
                    # Draw bottom-right semi-circle
                    pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    
        elif random_variable == 3:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    # Draw top-left semi-circle
                    if col%2 == 0:
                        pygame.draw.rect(self.screen, color, (cell_x, cell_y, qx, qy +1))
                        pygame.draw.circle(self.screen, color2, (cell_x + qx, cell_y + 1), qx/2,draw_bottom_left=True)
                        # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else:
                        pygame.draw.circle(self.screen, color, (cell_x + qx, cell_y + 1), qx/2,draw_bottom_left=True)
                        # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    
        elif random_variable == 4:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    if col%2 == 0:
                        # Draw top-left semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x + qx, cell_y), qx/2,draw_bottom_left=True)
                        # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else :
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                        
                        
        elif random_variable == 5:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    if col%2 == 0:
                        # Draw top-left semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x + qx, cell_y), qx/2,draw_bottom_left=True)
                        # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else :
                        pygame.draw.rect(self.screen, color, (cell_x, cell_y, qx, qy))
                        pygame.draw.circle(self.screen, color2, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color2, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
    
    def draw_circles_and_stars(self):
        
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        random_variant = random.randint(1,3)
        
        if random_variant == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    
                # Draw top-left semi-circle
                    pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                    pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                # Draw bottom-right semi-circle
                    pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                    pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)


        
        elif random_variant == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    
                    if col%2 == 0:
                    # Draw top-left semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                    # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else :
                    # Faz fundo
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy))
                        pygame.draw.circle(self.screen, color2, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        pygame.draw.circle(self.screen, color2, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                        pygame.draw.circle(self.screen, color2, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                        pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
        
        elif random_variant == 3:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    if row%2 == 0:
                        if col%2 == 0:
                        # Draw top-left semi-circle
                            pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                            pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                        # Draw bottom-right semi-circle
                            pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                            pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                        else :
                        # Faz fundo
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy))

                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                            pygame.draw.circle(self.screen, color2, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                            pygame.draw.circle(self.screen, color2, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else:
                        if col%2 == 0:
                            pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy))

                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                            pygame.draw.circle(self.screen, color2, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                            pygame.draw.circle(self.screen, color2, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qx/2,draw_top_right=True)

                        else :
                        # Draw top-left semi-circle
                            pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                            pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                        # Draw bottom-right semi-circle
                            pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                            pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)

    
    def draw_circles_and_stars_lvl2(self):
        
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        
        random_variant = random.randint(1,3)
        
        if random_variant == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    
                    if col%2 == 0:
                    # Draw top-left semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                    # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else :
                    # Faz fundo
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy+1))
                        pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/2)


        
        elif random_variant == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    
                    if col%2 == 0:
                    # Draw top-left semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                    # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else :
                    # Faz fundo
                        pygame.draw.rect(self.screen, color1, (cell_x, cell_y, qx, qy+1))
                        pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/2)
                        pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/4)
                        
                        
        elif random_variant == 3:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    # Alternate colors
                    color = color1 #if (row + col) % 2 == 0 else color2
                    
                    if col%2 == 0:
                    # Draw top-left semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y), qx/2,draw_bottom_right=True)
                        pygame.draw.circle(self.screen, color, (cell_x +qx, cell_y), qx/2,draw_bottom_left=True)
                    # Draw bottom-right semi-circle
                        pygame.draw.circle(self.screen, color, (cell_x+qx, cell_y+qy), qx/2,draw_top_left=True)
                        pygame.draw.circle(self.screen, color, (cell_x, cell_y+qy), qx/2,draw_top_right=True)
                    else :
                    # Faz fundo
                        pygame.draw.rect(self.screen, color2, (cell_x, cell_y, qx, qy+1))
                        pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/2)

    
                
                
                
    def draw_ropes_pattern(self):

        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        random_variable = random.randint(1,2)
        if random_variable == 1:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    if row%2 == 0:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y), qx,draw_bottom_right=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y+qy), qx,draw_top_left=True)
                    else:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y+qy), qx,draw_top_left=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y), qx,draw_bottom_right=True)
        elif random_variable == 2:
            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx

                    if row%2 == 0:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y), qx,draw_bottom_left=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y+qy), qx,draw_top_right=True)
                    else:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y+qy), qx,draw_top_right=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y), qx,draw_bottom_left=True) 
                
                
    def draw_estrelas(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color

        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                width = height = qx
                
                if row%2 == 0:
                    if col%2 == 0:
                        pygame.draw.circle(self.screen, color1, (cell_x, cell_y), qx,draw_bottom_right=True)
                    else:
                        pygame.draw.circle(self.screen, color1, (cell_x +qx, cell_y), qx,draw_bottom_left=True)
                else:
                    if col%2 == 0:
                        pygame.draw.circle(self.screen, color1, (cell_x, cell_y + qy), qx,draw_top_right=True)
                    else:
                        pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + qy), qx,draw_top_left=True)
    
    def draw_pills_pattern(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color
        random_variable = random.randint(1,3)
        if random_variable == 1:
            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy

                    if col%2 == 0:
                        pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + (qy/2)), qy/2,draw_bottom_left=True, draw_top_left=True)
                        if row%2 == 0:
                            pygame.draw.polygon(self.screen,color1,[(cell_x, cell_y + qy),(cell_x + (qx/2), cell_y + qy),(cell_x, cell_y)])
                        else :
                            pygame.draw.polygon(self.screen,color1,[(cell_x, cell_y),(cell_x + (qx/2), cell_y),(cell_x, cell_y + qy)])
                    else:
                        pygame.draw.circle(self.screen, color1, (cell_x, cell_y + (qy/2)), qy/2,draw_bottom_right=True, draw_top_right=True)
                        if row%2 == 0:
                            pygame.draw.polygon(self.screen,color1,[(cell_x +qx, cell_y + qy),(cell_x + (qx/2), cell_y + qy),(cell_x +qx, cell_y)])
                        else :
                            pygame.draw.polygon(self.screen,color1,[(cell_x +qx, cell_y),(cell_x + (qx/2), cell_y),(cell_x +qx, cell_y + qy)])
        
        elif random_variable == 2:
            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    
                    if col%2 == 0:
                        pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + (qy/2)), qy/2,draw_bottom_left=True, draw_top_left=True)
                        if row%2 == 0:
                            pygame.draw.polygon(self.screen,color1,[(cell_x, cell_y + qy),(cell_x + (qx/2), cell_y + qy),(cell_x, cell_y)])
                        else :
                            pygame.draw.polygon(self.screen,color1,[(cell_x, cell_y),(cell_x + (qx/2), cell_y),(cell_x, cell_y + qy)])
                    else:
                        pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy+1))
                        pygame.draw.circle(self.screen, color2, (cell_x, cell_y + (qy/2)), qy/2,draw_bottom_right=True, draw_top_right=True)
                        if row%2 == 0:
                            pygame.draw.polygon(self.screen,color2,[(cell_x +qx, cell_y + qy),(cell_x + (qx/2), cell_y + qy),(cell_x +qx, cell_y)])
                        else :
                            pygame.draw.polygon(self.screen,color2,[(cell_x +qx, cell_y),(cell_x + (qx/2), cell_y),(cell_x +qx, cell_y + qy)])
        
        elif random_variable == 3:
            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    
                    if col%2 == 0:
                        if row%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + (qy/2)), qy/2,draw_bottom_left=True, draw_top_left=True)
                            pygame.draw.polygon(self.screen,color1,[(cell_x, cell_y + qy),(cell_x + (qx/2), cell_y + qy),(cell_x, cell_y)])
                        else :
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy+1))
                            pygame.draw.circle(self.screen, color2, (cell_x + qx, cell_y + (qy/2)), qy/2,draw_bottom_left=True, draw_top_left=True)
                            pygame.draw.polygon(self.screen,color2 ,[(cell_x, cell_y),(cell_x + (qx/2), cell_y),(cell_x, cell_y + qy)])
                    else:
                        if row%2 == 0:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy+1))
                            pygame.draw.polygon(self.screen,color2,[(cell_x +qx, cell_y + qy),(cell_x + (qx/2), cell_y + qy),(cell_x +qx, cell_y)])
                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y + (qy/2)), qy/2,draw_bottom_right=True, draw_top_right=True)
                        else :
                            pygame.draw.polygon(self.screen,color1,[(cell_x +qx, cell_y),(cell_x + (qx/2), cell_y),(cell_x +qx, cell_y + qy)])
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y + (qy/2)), qy/2,draw_bottom_right=True, draw_top_right=True)


    def draw_eyes(self):
        random_variable = random.randint(1,1)
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if col%2 == 0:
                        pygame.draw.polygon(self.screen,color1,((cell_x,cell_y+(qy/2)),(cell_x +qx,cell_y),(cell_x +qx,cell_y +qy)))
                        pygame.draw.circle(self.screen, color2, (cell_x+qx, cell_y + (qy/2)), qy/2.5,draw_bottom_left=True, draw_top_left=True)
                        pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y + (qy/2)), qy/4.5,draw_bottom_left=True, draw_top_left=True)
                    elif col%2 == 1:
                        pygame.draw.polygon(self.screen,color1,((cell_x + qx,cell_y+(qy/2)),(cell_x,cell_y),(cell_x,cell_y +qy)))
                        pygame.draw.circle(self.screen, color2, (cell_x, cell_y + (qy/2)), qy/2.5,draw_bottom_right=True, draw_top_right=True)
                        pygame.draw.circle(self.screen, color1, (cell_x, cell_y + (qy/2)), qy/4.5,draw_bottom_right=True, draw_top_right=True)
            
    def draw_meggie_setes(self):
        random_variable = random.randint(1,2)
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if col%2 == 0:
                        pygame.draw.polygon(self.screen,color1,((cell_x,cell_y+(qy/2)),(cell_x +qx,cell_y),(cell_x +qx,cell_y +qy)))
                    elif col%2 == 1:
                        pygame.draw.rect(self.screen,color1,(cell_x,cell_y+(qy/4),qx,qy/2))
                        
        elif random_variable == 2:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if row%2 == 0:
                        pygame.draw.polygon(self.screen,color1,((cell_x,cell_y+qy),(cell_x +qx,cell_y + qy),(cell_x +(qx/2),cell_y)))
                    elif row%2 == 1:
                        pygame.draw.rect(self.screen,color1,(cell_x+(qy/4),cell_y,qx/2,qy))
                            
                            
    def draw_clouds(self):
        random_variable = random.randint(1,1)
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color
            random_starter = random.randint(0,3)

            for row in range(ny):
                for col in range(nx):
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    if random_starter % 4 == 0:
                        if col%4 == 0:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx,cell_y+qy),qy/2,draw_top_left=True)
                        elif col%4 == 1:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx/2,cell_y+(qy/2)),qx/2,draw_top_left=True,draw_top_right=True)
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y+(qy/2),qx,qy/2+1))
                        elif col%4 == 2:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx/2,cell_y+(qy/2)),qx/2,draw_top_left=True,draw_top_right=True)
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y+(qy/2),qx,qy/2+1))
                        elif col%4 == 3:
                            pygame.draw.circle(self.screen,color1,(cell_x,cell_y+qy),qy/2,draw_top_right=True)
                            
                    elif random_starter % 4 == 1:
                        if col%4 == 0:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx,cell_y),qy/2,draw_bottom_left=True)
                        elif col%4 == 1:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy/2))
                        elif col%4 == 2:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy/2))
                        elif col%4 == 3:
                            pygame.draw.circle(self.screen,color1,(cell_x,cell_y),qy/2,draw_bottom_right=True)
                            
                    elif random_starter % 4 == 2:
                        if col%4 == 2:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx,cell_y+qy),qy/2,draw_top_left=True)
                        elif col%4 == 3:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx/2,cell_y+(qy/2)),qx/2,draw_top_left=True,draw_top_right=True)
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y+(qy/2),qx,qy/2+1))
                        elif col%4 == 0:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx/2,cell_y+(qy/2)),qx/2,draw_top_left=True,draw_top_right=True)
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y+(qy/2),qx,qy/2+1))
                        elif col%4 == 1:
                            pygame.draw.circle(self.screen,color1,(cell_x,cell_y+qy),qy/2,draw_top_right=True)
                    
                    elif random_starter % 4 == 3:
                        if col%4 == 2:
                            pygame.draw.circle(self.screen,color1,(cell_x+qx,cell_y),qy/2,draw_bottom_left=True)
                        elif col%4 == 3:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy/2))
                        elif col%4 == 0:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy/2))
                        elif col%4 == 1:
                            pygame.draw.circle(self.screen,color1,(cell_x,cell_y),qy/2,draw_bottom_right=True)
                random_starter = random_starter + 1
                    

    
    
    def draw_lisbonflag(self):
        random_variable = random.randint(1,1)
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw top-left semi-circle
                    if row % 2 == 0:
                        if col%2 == 0:
                            pygame.draw.polygon(self.screen, color1, ((cell_x, cell_y),(cell_x+qx, cell_y+qy),(cell_x, cell_y+qy)))
                        elif col%2 == 1:
                            pygame.draw.polygon(self.screen, color1, ((cell_x, cell_y),(cell_x+qx, cell_y),(cell_x, cell_y+qy)))
                    else:
                        if col%2 == 0:
                            pygame.draw.polygon(self.screen, color1, ((cell_x+qx, cell_y),(cell_x+qx, cell_y+qy),(cell_x, cell_y+qy)))
                        elif col%2 == 1:
                            pygame.draw.polygon(self.screen, color1, ((cell_x, cell_y),(cell_x+qx, cell_y),(cell_x+qx, cell_y+qy)))
    
    def draw_flower_pattern(self):
        random_variable = random.randint(1,1)
        
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw top-left semi-circle
                    if row % 2 == 0:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + qy), qy/2,draw_top_left=True,draw_top_right=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y+(qy/2)), qy/2,draw_top_right=True,draw_bottom_right=True)
                    else:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x+qx, cell_y+(qy/2)), qy/2,draw_top_left=True,draw_bottom_left=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y), qy/2,draw_bottom_left=True,draw_bottom_right=True)
        
    
    
    
    
    def draw_convex_circle_pattern(self):
        random_variable = random.randint(1,2)
        
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw top-left semi-circle
                    if row % 2 == 0:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + qy), qy,draw_top_left=True)
                        else:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy))
                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qy,draw_top_right=True)
                    else:
                        if col%2 == 0:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy))
                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qy,draw_top_right=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + qy), qy,draw_top_left=True)
        
        
        elif random_variable == 2:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw top-left semi-circle
                    if row % 2 == 0:
                        if col%2 == 0:
                            pygame.draw.circle(self.screen, color1, (cell_x + qx, cell_y + qy), qx,draw_top_left=True)
                        else:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy))
                            pygame.draw.circle(self.screen, color2, (cell_x, cell_y+qy), qx,draw_top_right=True)
                    else:
                        if col%2 == 0:
                            pygame.draw.rect(self.screen,color1,(cell_x,cell_y,qx,qy))
                            pygame.draw.circle(self.screen, color2, (cell_x + qx, cell_y + qy), qx,draw_top_left=True)
                        else:
                            pygame.draw.circle(self.screen, color1, (cell_x, cell_y+qy), qx,draw_top_right=True)
                            
                            
                        
    def draw_all_circles_pattern(self):
        random_variable = random.randint(1,2)
        if random_variable == 1:
            x, y, sizeX, sizeY = self.Filletes[-1]
            nx = int(sizeX / (self.largTela / self.divLarg))
            ny = int(sizeY / (self.altTela / self.divAlt))
            qx = self.largTela / self.divLarg
            qy = self.altTela / self.divAlt
            color1 = self.CorPattern
            color2 = self.CorFundo  # Replace with your second color

            for row in range(ny):
                for col in range(nx):
                    # Determine the position and size of the cell
                    cell_x = x * qx + col * qx
                    cell_y = y * qy + row * qy
                    width = height = qx
                    # Draw top-left semi-circle
                    pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/2)
        else :
            self.draw_all_circles_with_innercircles_pattern()
    
    def draw_all_circles_with_innercircles_pattern(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color

        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                width = height = qx
                # Draw top-left semi-circle
                pygame.draw.circle(self.screen, color1, (cell_x + (qx/2), cell_y + (qy/2)), qx/2)
                pygame.draw.circle(self.screen, color2, (cell_x + (qx/2), cell_y + (qy/2)), qx/4)
                
    def draw_all_squares_with_inner(self):
        x, y, sizeX, sizeY = self.Filletes[-1]
        nx = int(sizeX / (self.largTela / self.divLarg))
        ny = int(sizeY / (self.altTela / self.divAlt))
        qx = self.largTela / self.divLarg
        qy = self.altTela / self.divAlt
        color1 = self.CorPattern
        color2 = self.CorFundo  # Replace with your second color

        for row in range(ny):
            for col in range(nx):
                # Determine the position and size of the cell
                cell_x = x * qx + col * qx
                cell_y = y * qy + row * qy
                #get centers
                
                # Draw top-left semi-circle
                if row%2 == 0:
                    if col%2 == 0:
                        pygame.draw.rect(self.screen, color1, (cell_x + (qx/4), cell_y + (qy/4),qx/2,qy/2))
                    else:
                        pygame.draw.rect(self.screen, color1, (cell_x , cell_y,qx,qy))
                        pygame.draw.rect(self.screen, color2, (cell_x + (qx/4), cell_y + (qy/4),qx/2,qy/2))
                else:
                    if col%2 == 0:
                        pygame.draw.rect(self.screen, color1, (cell_x , cell_y,qx,qy))
                        pygame.draw.rect(self.screen, color2, (cell_x + (qx/4), cell_y + (qy/4),qx/2,qy/2))
                    else:
                        pygame.draw.rect(self.screen, color1, (cell_x + (qx/4), cell_y + (qy/4),qx/2,qy/2))
      
    def DrawLinePatternOnFillete(self,x,y,sizeX,sizeY,PatColor):
        pygame.draw.rect(self.screen,PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),sizeX,sizeY))

    def MakesStairsonFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        PatColor = self.CorPattern
        yNumber = int(sizeY / (self.altTela/self.divAlt))
        xNumber = int(sizeX / (self.largTela/self.divLarg))
        a = 0
        e = 0

        if yNumber >= xNumber:
            for a in range(yNumber):
                #print("CARRRRALHO",y+a)
                d = e
                e += 1
                for n in range(xNumber-d):
                    self.QuadradosPatcolor(x+n,y+a,PatColor)
                    #print("merda",x+n,y+a)
                    n += 1        
                    a += 1
                    d += 1 
        else:
            for a in range(xNumber):
                #print("CARRRRALHO",y+a)
                d = e
                e += 1
                for n in range(yNumber-d):
                    self.QuadradosPatcolor(x+n,y+a,PatColor)
                    #print("merda",x+n,y+a)
                    n += 1        
                    a += 1
                    d += 1 
    
    def QuadradosPatcolor(self,x,y,PatColor):
        cubo = pygame.draw.rect(self.screen,PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),self.largTela/self.divLarg,self.altTela/self.divAlt))

    def MakesPatternQuadradosOnFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        px = x + 1
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        PatColor = self.CorPattern

        for s in range(0,ny):
            for u in range(0,nx,2):
                if s % 2 == 0:
                    self.QuadradosPatcolor(x+u,y+s,PatColor)
                    #print("SQUARE ",x+u,y+s," is on",nx+x)
                elif s % 2 != 0 and (px+u)>=(nx+x) and (px+u) != (self.altTela/self.divAlt):
                    print()
                elif s % 2 != 0:
                    self.QuadradosPatcolor(px+u,y+s,PatColor)
                    #print("SQUARE ",px+u,y+s," is on",nx+x)
                    
                    
    




    def MakesCircle(self,center,rad,Patcolor):
        pygame.draw.circle(self.screen,Patcolor,center,rad)
        
        #print("IT MAKES CIRCLES")


    def Line(self,LineX,LineY,RealDirectionX,RealDirectionY,PepeCor):
        cubo = pygame.draw.rect(self.screen,PepeCor,((self.largTela/self.divLarg)*LineX,((self.altTela/self.divAlt)*LineY),RealDirectionX,RealDirectionY))
        


    def MakesTriangles(self,pos1,pos2,pos3,CorPattern):
        Patcolor = CorPattern

        pygame.draw.polygon(self.screen,Patcolor,(pos1,pos2,pos3))
        
        #print("IT MAKES TRIANGLES")

    def MakesTrianglesPattern(self,pos1,pos2,pos3,PatColor):
        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
        
        #print("IT MAKES TRIANGLES")


