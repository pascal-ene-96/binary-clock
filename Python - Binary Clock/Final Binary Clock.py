import pygame, sys, time
from datetime import datetime

now = datetime.now() #grabbing 'now' method from datetime module

class BinaryTime():
    def __init__(self):
        self.nt = datetime.now()
        #secondones
        self.secsones1 = [376,305]
        self.secsones2 = [376,245]
        self.secsones4 = [376,183]
        self.secsones8 = [376,117]
        #secondtens
        self.secstens1 = [310,305]
        self.secstens2 = [310,245]
        self.secstens4 = [310,182]  
        #minuteones
        self.minsones1 = [248,305]
        self.minsones2 = [248,245]
        self.minsones4 = [248,182]
        self.minsones8 = [248,117]
        #minutetens
        self.minstens1 = [183,305]
        self.minstens2 = [183,245]
        self.minstens4 = [183,182]     
        #hourones
        self.hoursones1 = [120,305]
        self.hoursones2 = [120,245]
        self.hoursones4 = [120,182]
        self.hoursones8 = [120,117]        
        #hourtens
        self.hourstens1 = [55,305]
        self.hourstens2 = [55,245]
        #lists
        self.sec1s = [self.secsones1,self.secsones2,self.secsones4,self.secsones8]
        self.sec10s = [self.secstens1,self.secstens2,self.secstens4]
        self.min1s = [self.minsones1,self.minsones2,self.minsones4,self.minsones8]
        self.min10s = [self.minstens1,self.minstens2,self.minstens4]
        self.hour1s = [self.hoursones1,self.hoursones2,self.hoursones4,self.hoursones8]
        self.hour10s = [self.hourstens1,self.hourstens2]

    def currentreturn(self):
        while True:
            self.nt = datetime.now()
            mytime = [self.nt.hour,self.nt.minute,self.nt.second]
            time.sleep(1)
            return mytime #returns current GMT time

    def onestime(self, currone, onescoords):
        # coords are added to the empty list 'tempone' depending on the time number (ones column)
        tempone = []

        if currone == 1:
            tempone.append(onescoords[0])
        elif currone == 2:
            tempone.append(onescoords[1])
        elif currone == 3:
            tempone.append(onescoords[0])
            tempone.append(onescoords[1])
        elif currone == 4:
            tempone.append(onescoords[2])
        elif currone == 5:
            tempone.append(onescoords[0])
            tempone.append(onescoords[2])
        elif currone == 6:
            tempone.append(onescoords[1])
            tempone.append(onescoords[2])
        elif currone == 7:
            tempone.append(onescoords[0])
            tempone.append(onescoords[1])
            tempone.append(onescoords[2])
        elif currone == 8:
            tempone.append(onescoords[3])
        elif currone == 9:
            tempone.append(onescoords[0])
            tempone.append(onescoords[3])
        else:
            pass
        return tempone

    def tenstime(self, currten, tenscoords):
        # coords are added to the empty list 'tempone' depending on the time number (tens column)
        self.str10 = str(currten)
        tempten = []

        if self.str10[0] == "1":
            tempten.append(tenscoords[0])
        elif self.str10[0] == "2":
            tempten.append(tenscoords[1])
        elif self.str10[0] == "3":
            tempten.append(tenscoords[0])
            tempten.append(tenscoords[1])
        elif self.str10[0] == "4":
            tempten.append(tenscoords[2])
        elif self.str10[0] == "5":
            tempten.append(tenscoords[0])
            tempten.append(tenscoords[2])
        else:
            pass
        return tempten      
        
    def timereturn(self):
        self.nt = datetime.now()
        mytime = [self.nt.hour,self.nt.minute,self.nt.second]
        tpos = "temp"
        templist = []
        templist2 = []
        finalcoords = []
        currh = self.nt.hour
        currm = self.nt.minute
        currs = self.nt.second
        numget = [currh,currm,currs]
        
        # for loop checks for index range in numget (hours, mins or secs)
        # \and then 'if' statements check for number range to determine
        # \what list of coords will be used
        for n in range(len(numget)):
            if n == 0:
                tpos = "hour"
            elif n == 1:
                tpos = "min"
            else:
                tpos = "sec"

            if tpos == "hour":
                if numget[n] < 10:
                    templist = self.hour1s
                else:
                    templist = self.hour10s
                    templist2 = self.hour1s

            elif tpos == "min":
                if numget[n] < 10:
                    templist = self.min1s
                else:
                    templist = self.min10s
                    templist2 = self.min1s

            elif tpos == "sec":
                if numget[n] < 10:
                    templist = self.sec1s
                else:
                    templist = self.sec10s
                    templist2 = self.sec1s
            else:
                print("timepos function's templist can't be filled")

            finalcoords.append(self.coords(numget[n], templist, templist2))
        return finalcoords

    def coords(self, mynum, list1, list2):
        strnum = str(mynum)
        resultscoords = []
        onestemp = []

        if mynum > 9 and mynum < 60:
            resultscoords = self.tenstime(strnum[0],list1)
            onestemp = self.onestime(int(strnum[1]),list2)
            for i in range(0, len(onestemp)):
                resultscoords.append(onestemp[i])
                print (str(resultscoords)) #onestemp added to resultcoords
        elif mynum < 10:
            resultscoords = self.onestime(mynum, list1)
        else:
            print ("The number provided is greater than 59 so it cannot be used in this time")
        return resultscoords
                
  
def main():
    pygame.init()
    white = (255,255,255)
    width = 432
    height = 407
    black = (0,0,0)
    bintime = []
    background = pygame.image.load('binaryclock3.BMP')
    screen = pygame.display.set_mode((width,height))

    meclock = BinaryTime()
    
    while True:
        # prints current time to shell to show what is returned by the currenttime method in
        # \the BinaryTime class. This can used later to check the binary coded display
        
        screen.fill(black)
        screen.blit(background, (0,0))
        print(meclock.currentreturn())
        bintime = meclock.timereturn()
        print (meclock.timereturn())

        if len(bintime) > 0:
            for p in range(len(bintime)):
                for i in range(len(bintime[p])):
                    pygame.draw.circle(screen, white, (bintime[p][i][0],bintime[p][i][1]), 18)
        else:
            pass

        
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def startscreen():
    startscreen = 1
    
    background = pygame.image.load('Menu.BMP')
    icon = pygame.image.load('binaryclock3.BMP')
    pygame.display.set_icon(icon)
    width = 432
    height = 407
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Binary Clock')
    meclock = BinaryTime()
    
    while startscreen == 1:
        screen.blit(background, (0,0))
            
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startscreen = 0
                    main()
                elif event.type == pygame.K_ESCAPE:
                    startscreen = 0
                    pygame.quit()
                    sys.quit()
    
# Run main routine
if __name__ == '__main__' :
    startscreen()
