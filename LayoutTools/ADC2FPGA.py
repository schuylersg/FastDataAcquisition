#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     07/08/2013
# Copyright:   (c) Owner 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
from os import listdir
from os import path
import math

fileDirN = "C:\Program Files (x86)\EAGLE-6.5.0\scr\\fda_routeb"
fileDir = ""

MIL2MM = 0.0254 #multiply mil by this to get mm
MM2MIL = 39.3700787 #multuply mm by this to get mil

Tpd = 6.5 #LVDS signal propagation speed in ps/mm

MAX_SIGNAL_SKEW = 50 #time in picoseconds
MAX_DIST_SKEW = MAX_SIGNAL_SKEW/Tpd

adcLoc = [20, 50]
fpgaLoc = [60, 50]

adcPinLoc = []
fpgaPinLoc = []

tW = 6 *MIL2MM #Track width
tD = 5*MIL2MM #Differential track distance
tS = 3*tW #Track spacing between different differential pairs
tB = 5*tW #Track spacing between the same differential pair in bends, etc.  !!!! 5 tW is the minimum that allows for a radius of curvature of Rin 3x tW

padExit = 40*MIL2MM #the length out of the pad to extend before moving to tD with differential pair
postPar = 10*MIL2MM #the length after the two tracks are brought together before bends/etc.

Rin = (tB + tW)/2
Rout = Rin + tD + tW
CycleLength = 2*(Rin + Rout)
CyclePathLength = math.pi *(Rin + Rout)

TotalL = 50 #target length for traces
dX23 = 4
dX10 = 4

#[adcPin Further Or Top, adcPinCloser Or Botton, fpgaPin 1, fpgaPin 2]
pairs = [
    [36, 37, 30, 29],    [38, 39, 27, 26],   [43, 44, 24, 23],   [45, 46, 22, 21],     [47, 48, 17, 16],
    [49, 50, 15, 14],    [54, 55, 12, 1],    [56, 57, 10, 9],   [  58, 59, 8, 7],       [60, 61, 6, 5],
  [65, 66, 2, 1],  [68, 67, 141, 142], [70, 69, 139, 140], [72, 71, 137, 138],   [76, 75, 133, 134],
  [78, 77, 131, 132],  [80, 79, 131, 132], [82, 81, 126, 127], [84, 83, 123, 124],   [86, 85, 120, 121],
  [90, 89, 118, 119],  [92, 91, 116, 117], [94, 93, 114, 115], [96, 95, 111, 112], [101, 100, 104, 105],
[103, 102, 101, 102], [105, 104, 99, 100], [107, 106, 97, 98], [112, 111, 94, 95],   [114, 113, 92, 93],
  [116, 115, 87, 88],  [118, 117, 84, 85], [123, 122, 82, 83], [125, 124, 80, 81]]

#changes in initial x and y
#              1           2           3           4           5           6           7           8           9          10
dY = [000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,  210*MIL2MM,
      270*MIL2MM, 330*MIL2MM, 380*MIL2MM, 430*MIL2MM, 000*MIL2MM, 100*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM]
#              1           2           3           4           5           6           7           8           9          10
dX = [000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, (Rout-Rin+tS+tW)*9, (Rout-Rin+tS+tW)*8, (Rout-Rin+tS+tW)*7,
      (Rout-Rin+tS+tW)*6, (Rout-Rin+tS+tW)*5, (Rout-Rin+tS+tW) *4, (Rout-Rin+tS+tW)*3, 0, 0, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM]

#
#Curve Heioght 1           2           3           4           5           6           7           8           9          10
cH = [000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,  93*MIL2MM,  93*MIL2MM, 74.7*MIL2MM,
       62*MIL2MM,  53*MIL2MM,  35*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM]

maxY=[000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM,
      000*MIL2MM, 000*MIL2MM, 000*MIL2MM, 000*MIL2MM]

cDir = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        -1, -1, -1, -1, -1, -1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1]

def PlaceComponents():
    with open(fileDir,'w') as fout:
        fout.write("Move U$1 (" + str(adcLoc[0]) + ' ' + str(adcLoc[1]) +');\n')
        fout.write("Move U$2 (" + str(fpgaLoc[0]) + ' ' + str(fpgaLoc[1]) +');\n')
        fout.flush()

def GeneratePinLocs():
    global adcPinLoc, fpgaPinLoc
    adcPinLoc = []
    fpgaPinLoc = []
#Generate the locations of the pins on the ADC
    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] - 10.6, adcLoc[1] + 7.75 - i*0.5])

    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] - 7.75 + i*0.5, adcLoc[1] - 10.6])

    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] + 10.6, adcLoc[1] - 7.75 + i*0.5])

    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] + 7.75 - i*0.5, adcLoc[1] + 10.6])

#Generate the locations of the pins on the FPGA
    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] - 8.75 + i*0.5, fpgaLoc[1] - 10.7])

    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] + 10.7, fpgaLoc[1] - 8.75 + i*0.5])

    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] + 8.75 - i*0.5, fpgaLoc[1] + 10.7])

    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] - 10.7, fpgaLoc[1] + 8.75 - i*0.5])

def locs2Str(locs):
    strOut = ""
    for l in locs:
        strOut = strOut + " (" + str(l[0]) + " " + str(l[1]) +")"
    return strOut

def locsA2Str(locs, angles):
    strOut = ""
    i = 0
    for l in locs:
        strOut = strOut + " (" + str(l[0]) + " " + str(l[1]) +")"
        if(i < len(angles)):
            strOut = strOut + " "
            if(angles[i] >= 0):
                strOut = strOut + "+"
            strOut = strOut + str(angles[i])
            i = i + 1
    return strOut

def prev(li):
    return li[len(li)-1]

def offset(l, x, y):
    p = prev(l)
    return [p[0] + x, p[1]+y]

def LineLength(a, b):
    deltaX = a[0] - b[0]
    deltaY = a[1] - b[1]
    return math.sqrt(deltaX**2 + deltaY**2)

def LocsLength(p):
    if(len(p)<2):
        return 0
    l = LineLength(p[len(p)-1], p[len(p)-2])
    return l

def Swap(li):
    a = li[0]
    li[0] = li[1]
    li[1] = a

class Direction:
    Up, Left, Down, Right = range(4)

#Generate an arbitrary meander of two lines given starting points, travel direction,
#and meander direction
#yStretch and xStretch are both positive regardless of direction
def ReturnMeander(insideP, outsideP, travelDir, meanderDir, xStretch, yStretch):
    iLocs = list()
    oLocs = list()
    iAngle = list()
    oAngle = list()
    xS = list()
    yS = list()

    signX = 1
    signY = 1
    signAngle = 1

    iLocs.append(insideP)
    oLocs.append(outsideP)

    if(travelDir == Direction.Up):
        yS = [yStretch, 0]
        xS = [0, xStretch]
        if(meanderDir == Direction.Right):
            signX = 1
            signY = 1
            signAngle = -1
        else: #meander to the left
            signX = -1
            signY = 1
            signAngle = 1
    elif(travelDir == Direction.Down):
        yS = [yStretch, 0]
        xS = [0, xStretch]
        if(meanderDir == Direction.Right):
            signX = 1
            signY = -1
            signAngle = 1
        else:
            signX = -1
            signY = -1
            signAngle = -1
    elif(travelDir == Direction.Right):
        yS = [0, yStretch]
        xS = [xStretch, 0]
        if(meanderDir == Direction.Up):
            signX = 1
            signY = 1
            signAngle = 1
        else: #meander down
            signX = 1
            signY = -1
            signAngle = -1
    elif(travelDir == Direction.Left):
        yS = [0, yStretch]
        xS = [xStretch, 0]
        if(meanderDir == Direction.Up):
            signX = -1
            signY = 1
            signAngle = -1
        else: #meander down
            signX = -1
            signY = -1
            signAngle = 1

    if(xS[0] > 0 or yS[0] > 0):
        iLocs.append(offset(iLocs, xS[0]/2*signX, yS[0]/2*signY))
        oLocs.append(offset(oLocs, xS[0]/2*signX, yS[0]/2*signY))
        iAngle.append(0)
        oAngle.append(0)
    Swap(xS)
    Swap(xY)

    for i in range(0, 2):
        for j in range(0,2):
            iLocs.append(offset(iLocs, Rin*signX, Rin*signY))
            oLocs.append(offset(oLocs, Rout*signX, Rout*signY))
            iAngle.append(90*signAngle)
            oAngle.append(90*signAngle)

            d = 2 if (i==1 and j == 1) else 1
            iLocs.append(offset(iLocs, xS[0]*signX/d, yS[0]*signY/d))
            oLocs.append(offset(oLocs, xS[0]*signX/d, yS[0]*signY/d))
            iAngle.append(0)
            oAngle.append(0)

            Swap(xS)
            Swap(xY)
            signAngle *= -1
        if(travelDir == Direction.Up or travelDir == Direction.Down):
            signX *= -1
        else
            signY *= -1
        signAngle *= -1

    iLocs.remove(iLocs[0])
    oLocs.remove(oLocs[0])

    return [iLocs, oLocs, iAngle, oAngle]

def GenerateSideTracksBottom(sIndex, eIndex, indexStep):
    with open(fileDir,'a') as fout:
        for i in range(sIndex, eIndex, indexStep):
            adc1 = adcPinLoc[pairs[i][0]-1]
            adc2 = adcPinLoc[pairs[i][1]-1]
            fpga1 = fpgaPinLoc[pairs[i][2]-1]
            fpga2 = fpgaPinLoc[pairs[i][3]-1]
            locs1 = []
            locs2 = []
            locs3 = []
            locs4 = []

            locs1.append(adc1)
            locs2.append(adc2)
            locs3.append(fpga1)
            locs4.append(fpga2)

            #Calculate the in/outs from the pads
            dT = ((adc1[1] - adc2[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
            locs1.append([adc1[0]+padExit, adc1[1]])    #move out of pad
            locs2.append([adc2[0]+padExit, adc2[1]])

            locs1.append([adc1[0]+padExit+dT, adc1[1]-dT])  #45 degree bend to parallel point
            locs2.append([adc2[0]+padExit+dT, adc2[1]+dT])

            locs1.append([locs1[2][0] + postPar + dX[i], locs1[2][1]])  #extend out before starting bends locs[3]
            locs2.append([locs2[2][0] + postPar + dX[i], locs2[2][1]])

            dT = ((fpga1[1] - fpga2[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
            locs3.append([fpga1[0]-padExit, fpga1[1]])    #move out of pad
            locs4.append([fpga2[0]-padExit, fpga2[1]])


            locs3.append([fpga1[0]-padExit-dT, fpga1[1]-dT])  #45 degree bend to parallel point
            locs4.append([fpga2[0]-padExit-dT, fpga2[1]+dT])

            locs3.append([locs3[2][0] - postPar - dX[i], locs3[2][1]])  #extend out before starting bends locs[3]
            locs4.append([locs4[2][0] - postPar - dX[i], locs4[2][1]])

            dTL = math.sqrt(2*dT**2)  #the length of the dT lines

            #Calculate any wire bends/locations
            numCycles = int((locs3[len(locs3)-1][0] - locs1[len(locs1)-1][0])//CycleLength) #set the maximum number of full curves given geometry available
            xSlack = ((locs3[3][0] - locs1[3][0]) - CycleLength*numCycles) #xSlack helps center the cycles over the full width
            yOffset = (locs1[3][1] - locs3[3][1])

            if(i ==  15):
                dY[i] = 0
            else:
                dY[i] = prev(locs1)[1] - maxY[i+1] + tS + tW   #this is really MIN_Y in this context
                if(yOffset > 0 ):
                    dY[i] -= yOffset

            fixedL = 2*padExit + 2* dTL + 2*postPar

            if(numCycles == 0):
                #print "ERROR: numCycles is zero can't route"
                return 1
            else:
                if(i!=15):
                    cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack - abs(yOffset) - fixedL) / (2*numCycles); #calculate the amount of length that needs to be "made up"
                else:
                    cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack + abs(yOffset) - fixedL) / (2*numCycles);

            while(cH[i] < 0 and numCycles > 1):
                numCycles -= 1
                xSlack = ((locs3[3][0] - locs1[3][0]) - CycleLength*numCycles)
                cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack - abs(yOffset) - fixedL) / (2*numCycles);

            if(numCycles == 1):
                if(yOffset>0):
                    dY[i] -= yOffset
                xSlack = ((locs3[3][0] - locs1[3][0]) - CycleLength*numCycles)
                cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack - abs(yOffset) - fixedL) / (2*numCycles);

            if (cH[i] < 0):
                #print "Error: Trace exceeds length", i
                cH[i] = 0
            xSlack = xSlack/(2*numCycles - 1)

            maxY[i] = prev(locs2)[1] - Rin - Rout - dY[i] - cH[i]

            if(yOffset > 0 and i!=15):
                maxY[i] -= yOffset

            angle = []
            #start at index 3
            for j in range(0, numCycles):
                #first point
                angle.append(90)
                locs1.append(offset(locs1, Rin, Rin))
                locs2.append(offset(locs2, Rout, Rout))

                #second point
                if(j==0 and yOffset<0 and i!=15):
                    deltaY = cH[i] + dY[i] - yOffset
                elif(j==0 and yOffset>0 and i==15):
                    deltaY = cH[i] + dY[i] - yOffset
                elif(j==0):
                    deltaY =  cH[i] + dY[i]
                else:
                    deltaY =  cH[i]
                #only append point if it's different from last point - otherwise you get errors
                if(deltaY != 0):
                    angle.append(0)
                    locs1.append(offset(locs1, 0, deltaY))
                    locs2.append(offset(locs2, 0 ,deltaY))

                #third point
                angle.append(-90)
                locs1.append(offset(locs1, Rout, Rout))
                locs2.append(offset(locs2, Rin, Rin))

                #fourth optional point
                if(xSlack > 0):
                    angle.append(0)
                    locs1.append(offset(locs1, xSlack, 0))
                    locs2.append(offset(locs2, xSlack, 0))

                #fifth point
                angle.append(-90)
                locs1.append(offset(locs1, Rout, -Rout))
                locs2.append(offset(locs2, Rin, - Rin))

                #sixth point
                if(j==numCycles-1 and yOffset>0 and i!=15):
                    deltaY = -cH[i] - dY[i] - yOffset
                elif(j==numCycles-1 and yOffset>0 and i==15):
                    deltaY = -cH[i] - dY[i]
                elif(j==numCycles-1):
                    deltaY = -cH[i] - dY[i]
                else:
                    deltaY = -cH[i]
                #only append point if it's different from last point - otherwise you get errors
                if(deltaY != 0):
                    angle.append(0)
                    locs1.append(offset(locs1, 0, deltaY))
                    locs2.append(offset(locs2, 0, deltaY))

                #seventh point
                angle.append(90)
                locs1.append(offset(locs1, Rin, -Rin))
                locs2.append(offset(locs2, Rout, -Rout))

                if(j!=numCycles-1 and xSlack > 0):
                    angle.append(0)
                    locs1.append(offset(locs1, xSlack, 0))
                    locs2.append(offset(locs2, xSlack, 0))


            angle.append(0)
            locs1.append(locs3[3])
            locs2.append(locs4[3])

            #code to rotate tracks 180 degrees for lower half
            if(cDir[i] == -1):

                centerX = ((locs1[3][0]+locs2[3][0])/2 + (locs1[len(locs1)-1][0]+locs2[len(locs2)-1][0])/2)/2
                centerY = ((locs1[3][1]+locs2[3][1])/2 + (locs1[len(locs1)-1][1]+locs2[len(locs2)-1][1])/2)/2
                for p in range(4,len(locs1)):
                    locs1[p] = [locs1[p][0]-centerX, locs1[p][1]-centerY]
                    locs1[p] = [locs1[p][0]*-1, locs1[p][1]*-1]
                    locs1[p] = [locs1[p][0]+centerX, locs1[p][1]+centerY]
                for p in range(4,len(locs2)):
                    locs2[p] = [locs2[p][0]-centerX, locs2[p][1]-centerY]
                    locs2[p] = [locs2[p][0]*-1, locs2[p][1]*-1]
                    locs2[p] = [locs2[p][0]+centerX, locs2[p][1]+centerY]

                for a in angle:
                    a = a*-1

                temp1 = locs2[0:4]
                temp2 = locs1[0:4]
                locs1[0:4] = locs4[0:4]
                locs2[0:4]= locs3[0:4]
                locs3 = temp1
                locs4 = temp2

            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs1[0:4]) + ";\n")
            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs1[3:len(locs1)], angle) + ";\n")
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs3) + ";\n")


            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs2[0:4]) + ";\n")
            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs2[3:len(locs2)], angle) + ";\n")
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs4) + ";\n")
            fout.flush()

    return 0
    #print "Generated Side Bottom Tracks"



def GenerateSideTracksTop(sIndex, eIndex, indexStep):
    with open(fileDir,'a') as fout:
        for i in range(sIndex, eIndex, indexStep):
            adc1 = adcPinLoc[pairs[i][0]-1]
            adc2 = adcPinLoc[pairs[i][1]-1]
            fpga1 = fpgaPinLoc[pairs[i][2]-1]
            fpga2 = fpgaPinLoc[pairs[i][3]-1]
            locs1 = []
            locs2 = []
            locs3 = []
            locs4 = []

            locs1.append(adc1)
            locs2.append(adc2)
            locs3.append(fpga1)
            locs4.append(fpga2)

            #Calculate the in/outs from the pads
            dT = ((adc1[1] - adc2[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
            locs1.append([adc1[0]+padExit, adc1[1]])    #move out of pad
            locs2.append([adc2[0]+padExit, adc2[1]])

            locs1.append([adc1[0]+padExit+dT, adc1[1]-dT])  #45 degree bend to parallel point
            locs2.append([adc2[0]+padExit+dT, adc2[1]+dT])

            locs1.append([locs1[2][0] + postPar + dX[i], locs1[2][1]])  #extend out before starting bends locs[3]
            locs2.append([locs2[2][0] + postPar + dX[i], locs2[2][1]])

            dT = ((fpga1[1] - fpga2[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
            locs3.append([fpga1[0]-padExit, fpga1[1]])    #move out of pad
            locs4.append([fpga2[0]-padExit, fpga2[1]])

            locs3.append([fpga1[0]-padExit-dT, fpga1[1]-dT])  #45 degree bend to parallel point
            locs4.append([fpga2[0]-padExit-dT, fpga2[1]+dT])

            locs3.append([locs3[2][0] - postPar - dX[i], locs3[2][1]])  #extend out before starting bends locs[3]
            locs4.append([locs4[2][0] - postPar - dX[i], locs4[2][1]])

            dTL = math.sqrt(2*dT**2)  #the length of the dT lines
            fixedL = 2*(dTL + padExit + postPar)

            #Calculate any wire bends/locations
            numCycles = int((locs3[len(locs3)-1][0] - locs1[len(locs1)-1][0])//CycleLength) #set the maximum number of full curves given geometry available
            xSlack = ((locs3[3][0] - locs1[3][0]) - CycleLength*numCycles) #xSlack helps center the cycles over the full width
            yOffset = (locs1[3][1] - locs3[3][1])

            if(i==18 or i ==  15):
                dY[i] = 0
            else:
                dY[i] = maxY[i-1] - prev(locs2)[1] + tS + tW
                if(yOffset < 0 ):
                    dY[i] += yOffset
            if(numCycles == 0):
                #print "ERROR: numCycles is zero can't route"
                return 1
            else:
                cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack - abs(yOffset) - fixedL) / (2*numCycles); #calculate the amount of length that needs to be "made up"

            while(cH[i] < 0 and numCycles > 1):
                numCycles -= 1
                xSlack = ((locs3[3][0] - locs1[3][0]) - CycleLength*numCycles)
                cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack - abs(yOffset) - fixedL) / (2*numCycles);

            if(numCycles == 1):
   #             dY[i] = 0.0001 #maxY[i-1] - prev(locs2)[1]
                if(yOffset<0):
                    dY[i] -= yOffset
                xSlack = ((locs3[3][0] - locs1[3][0]) - CycleLength*numCycles)
                cH[i] = (TotalL - CyclePathLength*numCycles - 2*dY[i] - 2*dX[i] - xSlack - abs(yOffset) - fixedL) / (2*numCycles);

            if (cH[i] < 0):
                #print "Error: Trace exceeds length", i
                cH[i] = 0
            xSlack = xSlack/(2*numCycles - 1)

            maxY[i] = prev(locs1)[1] + Rin + Rout + dY[i] +cH[i]
            if(yOffset < 0):
                maxY[i] -= yOffset

            angle = []
            #start at index 3
            for j in range(0, numCycles):
                #first point
                angle.append(90)
                locs1.append(offset(locs1, Rin, Rin))
                locs2.append(offset(locs2, Rout, Rout))

                #second point
                if(j==0 and yOffset<0):
                    deltaY = cH[i] + dY[i] - yOffset
                elif(j==0):
                    deltaY =  cH[i] + dY[i]
                else:
                    deltaY =  cH[i]
                #only append point if it's different from last point - otherwise you get errors
                if(deltaY != 0):
                    angle.append(0)
                    locs1.append(offset(locs1, 0, deltaY))
                    locs2.append(offset(locs2, 0 ,deltaY))

                #third point
                angle.append(-90)
                locs1.append(offset(locs1, Rout, Rout))
                locs2.append(offset(locs2, Rin, Rin))

                #fourth optional point
                if(xSlack > 0):
                    angle.append(0)
                    locs1.append(offset(locs1, xSlack, 0))
                    locs2.append(offset(locs2, xSlack, 0))

                #fifth point
                angle.append(-90)
                locs1.append(offset(locs1, Rout, -Rout))
                locs2.append(offset(locs2, Rin, - Rin))

                #sixth point
                if(j==numCycles-1 and yOffset>0):
                    deltaY = -cH[i] - dY[i] - yOffset
                elif(j==numCycles-1):
                    deltaY = -cH[i] - dY[i]
                else:
                    deltaY = -cH[i]
                #only append point if it's different from last point - otherwise you get errors
                if(deltaY != 0):
                    angle.append(0)
                    locs1.append(offset(locs1, 0, deltaY))
                    locs2.append(offset(locs2, 0, deltaY))

                #seventh point
                angle.append(90)
                locs1.append(offset(locs1, Rin, -Rin))
                locs2.append(offset(locs2, Rout, -Rout))

                if(j!=numCycles-1 and xSlack > 0):
                    angle.append(0)
                    locs1.append(offset(locs1, xSlack, 0))
                    locs2.append(offset(locs2, xSlack, 0))


            angle.append(0)
            locs1.append(locs3[3])
            locs2.append(locs4[3])

            #code to rotate tracks 180 degrees for lower half
            if(cDir[i] == -1):

                centerX = ((locs1[3][0]+locs2[3][0])/2 + (locs1[len(locs1)-1][0]+locs2[len(locs2)-1][0])/2)/2
                centerY = ((locs1[3][1]+locs2[3][1])/2 + (locs1[len(locs1)-1][1]+locs2[len(locs2)-1][1])/2)/2
                for p in range(4,len(locs1)):
                    locs1[p] = [locs1[p][0]-centerX, locs1[p][1]-centerY]
                    locs1[p] = [locs1[p][0]*-1, locs1[p][1]*-1]
                    locs1[p] = [locs1[p][0]+centerX, locs1[p][1]+centerY]
                for p in range(4,len(locs2)):
                    locs2[p] = [locs2[p][0]-centerX, locs2[p][1]-centerY]
                    locs2[p] = [locs2[p][0]*-1, locs2[p][1]*-1]
                    locs2[p] = [locs2[p][0]+centerX, locs2[p][1]+centerY]

                for a in angle:
                    a = a*-1

                temp1 = locs2[0:4]
                temp2 = locs1[0:4]
                locs1[0:4] = locs4[0:4]
                locs2[0:4]= locs3[0:4]
                locs3 = temp1
                locs4 = temp2

            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs1[0:4]) + ";\n")
            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs1[3:len(locs1)], angle) + ";\n")
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs3) + ";\n")


            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs2[0:4]) + ";\n")
            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs2[3:len(locs2)], angle) + ";\n")
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs4) + ";\n")
            fout.flush()

    return 0
    #print "Generated Side Top Tracks"

def GenerateTopTracks():
    tError = 0
    with open(fileDir,'a') as fout:
        for i in range(24, 34, 1):
            dY[24] = 0
            adc1 = adcPinLoc[pairs[i][0]-1]
            adc2 = adcPinLoc[pairs[i][1]-1]
            fpga2 = fpgaPinLoc[pairs[i][2]-1]
            fpga1 = fpgaPinLoc[pairs[i][3]-1]
            locs1 = []
            locs2 = []
            locs3 = []
            locs4 = []

            locs1.append(adc1)
            locs2.append(adc2)
            locs3.append(fpga1)
            locs4.append(fpga2)
            calcLength = 0

            #Calculate the in/outs from the pads
            dT = ((adc2[0] - adc1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs1.append([adc1[0], adc1[1]+padExit])    #move out of pad
            locs2.append([adc2[0], adc2[1]+padExit])
            calcLength += LocsLength(locs1)

            locs1.append(offset(locs1, 0, dT))  #45 degree bend to parallel point
            locs2.append(offset(locs2, -dT, dT))
            calcLength += LocsLength(locs1)

            locs1.append([locs1[2][0], locs1[2][1] + postPar])  #extend out before starting bends locs[3]
            locs2.append([locs2[2][0], locs2[2][1] + postPar])
            calcLength += LocsLength(locs1)

            dT = ((fpga2[0] - fpga1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs3.append([fpga1[0], fpga1[1]+padExit])    #move out of pad
            locs4.append([fpga2[0], fpga2[1]+padExit])
            calcLength += LocsLength(locs4)

            locs3.append(offset(locs3, dT, dT))  #45 degree bend to parallel point
            locs4.append(offset(locs4, 0, dT))
            calcLength += LocsLength(locs4)

            locs3.append([locs3[2][0], locs3[2][1] + postPar])  #extend out before starting bends locs[3]
            locs4.append([locs4[2][0], locs4[2][1] + postPar])
            calcLength += LocsLength(locs4)

            #dY is how high up from the pin the track must go before starting meander
            #cH is any extra that's added to the cycles but try to keep to 0
            #heightY is the location of the horizontal wire
            #leftX and rightX are the corresponding x dimensions to the top wire
            #Calculate any wire bends/locations
            if(i == 24):
                prevLoc = adcPinLoc[pairs[23][0]-1]
                heightY = prevLoc[1] + dY[i-1] + cH[i-1] + Rin + Rout + tS #i think this is correct
                rightX = fpgaLoc[0] - 12 - dX[i-1]
                leftX = adcLoc[0] + 12 + dX[i-1]    #kind of made up...

            cycleInsertionPoints = [0, 0]
            angleInsertionPoints = [0, 0]
            angle1 = []
            angle2 = []

            #check for geometry errors
            if(i<33):
                if((prev(locs2)[0] > leftX - 2*Rin - Rout) or (rightX + 2*Rin + Rout > prev(locs3)[0])):
                   # print "Top geometry error", i
                    return 1
            else:
                if((prev(locs2)[0] > leftX - Rin) or (rightX + Rin > prev(locs3)[0])):
                   # print "Top geometry error", i
                    return 1

            if(i < len(pairs) - 1):
                #first point A
                if(dY[i] > 0):
                    locs2.append(offset(locs2, 0, dY[i]))
                    locs1.append(offset(locs1, 0, dY[i]))
                    angle1.append(0)
                    angle2.append(0)
                    calcLength += LocsLength(locs1)

                #first point B
                locs2.append(offset(locs2, Rin, Rin))
                locs1.append(offset(locs1, Rout, Rout))
                angle2.append(-90)
                angle1.append(-90)
                calcLength += math.pi*Rout/2

                #second point
                angle1.append(0)
                angle2.append(0)
                locs2.append([(leftX - Rin - Rout), prev(locs2)[1]])
                locs1.append([(leftX - Rin - Rout), prev(locs1)[1]])
                calcLength += LocsLength(locs1)
                if(i<len(dY)-1):
                    dY[i+1] = dY[i] + Rout - Rin + tS + tW

                #third point
                angle1.append(90)
                angle2.append(90)
                locs2.append(offset(locs2, Rout, Rout))
                calcLength += math.pi*Rin/2
                locs1.append(offset(locs1, Rin, Rin))

                cycleInsertionPoints[0] = len(locs2)
                angleInsertionPoints[0] = len(angle1)

                #fourth point
                angle1.append(0)
                angle2.append(0)
                locs2.append([prev(locs2)[0], heightY - Rin])
                locs1.append([prev(locs1)[0], heightY - Rin])
                calcLength += LocsLength(locs1)
                leftX = prev(locs2)[0] - tS - tW

            else:
                angle1.append(0)
                angle2.append(0)
                locs2.append([prev(locs2)[0], heightY - Rin])
                locs1.append([prev(locs1)[0], heightY - Rin])
                calcLength += LocsLength(locs1)

            #fifth point
            angle1.append(-90)
            angle2.append(-90)
            locs2.append(offset(locs2, Rin, Rin))
            calcLength += math.pi*Rout/2
            locs1.append(offset(locs1, Rout, Rout))
            #save heightYfor next run
            heightY = prev(locs1)[1] + tS + tW;

##            #fifth A - length equalizing jog
##            Req = ((Rout-Rin)*math.pi)/(4*math.pi - 8)
##            angle1.append(0)
##            angle2.append(-90)
##            locs2.append(offset(locs2, Req, -Req))
##            locs1.append(offset(locs1, Req, 0))
##            calcLength += LocsLength(locs1)
##
##            #fifth B - length equalizing jog
##            angle1.append(0)
##            angle2.append(90)
##            locs2.append(offset(locs2, Req, -Req))
##            locs1.append(offset(locs1, Req, 0))
##            calcLength += LocsLength(locs1)
##
##            #fifth C - length equalizing jog
##            angle1.append(0)
##            angle2.append(0)
##            locs2.append(offset(locs2, tB, 0))
##            locs1.append(offset(locs1, tB, 0))
##            calcLength += LocsLength(locs1)
##
##            #fifth D - length equalizing jog
##            angle1.append(0)
##            angle2.append(90)
##            locs2.append(offset(locs2, Req, Req))
##            locs1.append(offset(locs1, Req, 0))
##            calcLength += LocsLength(locs1)
##
##            #fifth E - length equalizing jog
##            angle1.append(0)
##            angle2.append(-90)
##            locs2.append(offset(locs2, Req, Req))
##            locs1.append(offset(locs1, Req, 0))
##            calcLength += LocsLength(locs1)


            if(i < len(pairs) - 1):
                #sixth point
                angle1.append(0)
                angle2.append(0)
                locs2.append([rightX, prev(locs2)[1]])
                locs1.append([rightX, prev(locs1)[1]])
                calcLength += LocsLength(locs1)

                #seventh point
                angle1.append(-90)
                angle2.append(-90)
                calcLength += math.pi*Rout/2
                locs2.append(offset(locs2, Rin, -Rin))
                locs1.append(offset(locs1, Rout, -Rout))
                rightX = prev(locs2)[0] + tS + tW

                #eighth point
                angle1.append(0)
                angle2.append(0)
                locs2.append([prev(locs2)[0],  locs3[3][1]+Rin+Rout+dY[i]])
                locs1.append([prev(locs1)[0], locs4[3][1]+Rin+Rout+dY[i]])
                cycleInsertionPoints[1] = len(locs2)
                angleInsertionPoints[1] = len(angle1)
                calcLength += LocsLength(locs1)

                #ninth point
                angle1.append(90)
                angle2.append(90)
                calcLength+= math.pi*Rin/2
                locs2.append(offset(locs2, Rout, -Rout))
                locs1.append(offset(locs1, Rin, -Rin))

                #tenth point
                angle1.append(0)
                angle2.append(0)
                locs2.append([locs3[3][0]-Rin, prev(locs2)[1]])
                locs1.append([locs4[3][0]-Rout, prev(locs1)[1]])
                calcLength += LocsLength(locs1)

                #eleventh point
                angle1.append(-90)
                angle2.append(-90)
                calcLength += math.pi*Rout/2
                locs2.append(offset(locs2, Rin, -Rin))
                locs1.append(offset(locs1, Rout, -Rout))

            else:
                #sixth point
                angle1.append(0)
                angle2.append(0)
                locs2.append([locs3[3][0] - Rin, prev(locs2)[1]])
                locs1.append([locs4[3][0] - Rout, prev(locs1)[1]])
                calcLength += LocsLength(locs1)

                #seventh point
                angle1.append(-90)
                angle2.append(-90)
                calcLength += math.pi*Rout/2
                locs2.append(offset(locs2, Rin, -Rin))
                locs1.append(offset(locs1, Rout, -Rout))
                rightX = prev(locs2)[0] + tS + tW

            #twelth point
            if(dY[i] > 0):
                angle1.append(0)
                angle2.append(0)
                locs2.append(locs3[3])
                locs1.append(locs4[3])
                calcLength += LocsLength(locs1)

            #Check to add cycles
            neededLength = TotalL - calcLength
            maxCycles = int((((locs2[cycleInsertionPoints[0]][1]) - locs2[cycleInsertionPoints[0]-1][1]))//CycleLength)*2

            if(neededLength < 0):
                tError = 2
                #print "Error: Trace exceeds length", i


            if(neededLength > 0):
                numCycles = min(int(neededLength//(CyclePathLength - 2*(Rin+Rout))), maxCycles)    #calculate the number of cycles required
                if(numCycles%2 == 1):
                    numCycles-=1
                if(numCycles >0):
                    xExtend = (neededLength - (CyclePathLength - 2*(Rin+Rout))*numCycles)/numCycles/2
                else:
                    xExtend = 0
            else:
                numCycles = 0
                xExtend = 0

            for c in range(0,numCycles/2, 1):
                #add cycle to left side
                k=cycleInsertionPoints[0]
                a=angleInsertionPoints[0]
                inserts = 0
                locs2.insert(k, [locs2[k-1][0]-Rout, locs2[k-1][1]+Rout])
                locs1.insert(k, [locs1[k-1][0]-Rin, locs1[k-1][1]+Rin])
                angle1.insert(a, 90)
                angle2.insert(a, 90)

                if(xExtend > 0):
                    k= k + 1
                    a = a + 1
                    locs2.insert(k, [locs2[k-1][0]-xExtend, locs2[k-1][1]])
                    locs1.insert(k, [locs1[k-1][0]-xExtend, locs1[k-1][1]])
                    angle2.insert(a, 0)
                    angle1.insert(a, 0)
                    inserts+=1

                k= k + 1
                a = a + 1
                locs2.insert(k, [locs2[k-1][0]-Rin, locs2[k-1][1]+Rin])
                tVal =locs1[k-1][0]-Rout
                locs1.insert(k, [tVal, locs1[k-1][1]+Rout])
                angle2.insert(a, -90)
                angle1.insert(a, -90)
                inserts+=1

                k= k + 1
                a = a + 1
                locs2.insert(k, [locs2[k-1][0]+Rin, locs2[k-1][1]+Rin])
                locs1.insert(k, [locs1[k-1][0]+Rout, locs1[k-1][1]+Rout])
                angle2.insert(a, -90)
                angle1.insert(a, -90)
                inserts+=1

                if(xExtend > 0):
                    k= k + 1
                    a = a + 1
                    locs2.insert(k, [locs2[k-1][0]+xExtend, locs2[k-1][1]])
                    locs1.insert(k, [locs1[k-1][0]+xExtend, locs1[k-1][1]])
                    angle2.insert(a, 0)
                    angle1.insert(a, 0)
                    inserts+=1

                k= k + 1
                a = a + 1
                locs2.insert(k, [locs2[k-1][0]+Rout, locs2[k-1][1]+Rout])
                locs1.insert(k, [locs1[k-1][0]+Rin, locs1[k-1][1]+Rin])
                angle2.insert(a, 90)
                angle1.insert(a, 90)
                inserts+=1

                cycleInsertionPoints[0] = k+1
                angleInsertionPoints[0] = a+1

                #add cycle to right side
                cycleInsertionPoints[1] += inserts
                angleInsertionPoints[1] += inserts + 1
                k = cycleInsertionPoints[1]
                a = angleInsertionPoints[1]
                locs2.insert(k, [locs2[k][0]+Rout, locs2[k][1]+Rout])
                locs1.insert(k, [locs1[k][0]+Rin, locs1[k][1]+Rin])
                angle2.insert(a, 90)
                angle1.insert(a, 90)

                if(xExtend > 0):
                    locs2.insert(k, [locs2[k][0]+xExtend, locs2[k][1]])
                    locs1.insert(k, [locs1[k][0]+xExtend, locs1[k][1]])
                    angle2.insert(a, 0)
                    angle1.insert(a, 0)

                locs2.insert(k, [locs2[k][0]+Rin, locs2[k][1]+Rin])
                tVal =locs1[k][0]+Rout
                locs1.insert(k, [tVal, locs1[k][1]+Rout])
                angle2.insert(a, -90)
                angle1.insert(a, -90)

                locs2.insert(k, [locs2[k][0]-Rin, locs2[k][1]+Rin])
                locs1.insert(k, [locs1[k][0]-Rout, locs1[k][1]+Rout])
                angle2.insert(a, -90)
                angle1.insert(a, -90)

                if(xExtend > 0):
                    locs2.insert(k, [locs2[k][0]-xExtend, locs2[k][1]])
                    locs1.insert(k, [locs1[k][0]-xExtend, locs1[k][1]])
                    angle2.insert(a, 0)
                    angle1.insert(a, 0)

                locs2.insert(k, [locs2[k][0]-Rout, locs2[k][1]+Rout])
                locs1.insert(k, [locs1[k][0]-Rin, locs1[k][1]+Rin])
                angle2.insert(a, 90)
                angle1.insert(a, 90)
                cycleInsertionPoints[1] +=1
                angleInsertionPoints[1] +=0

            if(numCycles > 0):
                leftX -= Rin + Rout + xExtend
                rightX += Rin + Rout + xExtend

            #write inner wire
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs2[0:4]) + ";\n")

            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs2[3:len(locs2)], angle2) + ";\n")

            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs3) + ";\n")

            #write outer wire
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs1[0:4]) + ";\n")

            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs1[3:len(locs1)], angle1) + ";\n")

            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs4) + ";\n")

        fout.flush()
    return tError
    #print "Generated Top Tracks"

def GenerateBottomTracks():
    tError = 0
    with open(fileDir,'a') as fout:
        for i in range(9, -1, -1):
            dY[9] = 0
            calcLength = 0
            adc1 = adcPinLoc[pairs[i][0]-1]
            adc2 = adcPinLoc[pairs[i][1]-1]
            fpga1 = fpgaPinLoc[pairs[i][3]-1]
            fpga2 = fpgaPinLoc[pairs[i][2]-1]
            locs1 = []
            locs2 = []
            locs3 = []
            locs4 = []

            locs1.append(adc1)
            locs2.append(adc2)
            locs3.append(fpga1)
            locs4.append(fpga2)

            #Calculate the in/outs from the pads
            dT = ((adc2[0] - adc1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs1.append([adc1[0], adc1[1]-padExit])    #move out of pad
            locs2.append([adc2[0], adc2[1]-padExit])
            calcLength += LocsLength(locs1)

            locs1.append(offset(locs1, 0, -dT))  #45 degree bend to parallel point
            locs2.append(offset(locs2, -dT, -dT))
            calcLength += LocsLength(locs1)

            locs1.append([locs1[2][0], locs1[2][1] - postPar])  #extend out before starting bends locs[3]
            locs2.append([locs2[2][0], locs2[2][1] - postPar])
            calcLength += LocsLength(locs1)

            dT = ((fpga2[0] - fpga1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs3.append(offset(locs3, 0, -padExit))    #move out of pad
            locs4.append(offset(locs4, 0, -padExit))
            calcLength += LocsLength(locs4)

            locs3.append(offset(locs3, dT, -dT))  #45 degree bend to parallel point
            locs4.append(offset(locs4, 0, -dT))
            calcLength += LocsLength(locs4)

            locs3.append([locs3[2][0], locs3[2][1] - postPar])  #extend out before starting bends locs[3]
            locs4.append([locs4[2][0], locs4[2][1] - postPar])
            calcLength += LocsLength(locs4)

            #dY is how high up from the pin the track must go before starting meander
            #cH is any extra that's added to the cycles but try to keep to 0
            #heightY is the location of the horizontal wire
            #leftX and rightX are the corresponding x dimensions to the top wire
            #Calculate any wire bends/locations
            if(i == 9):
                prevLoc = fpgaPinLoc[pairs[10][3]-1]
                heightY = prevLoc[1] - dY[i+1]  - cH[i+1]  - Rin  - Rout - tS #i think this is correct
                rightX = fpgaLoc[0] - 12 - dX[i+1]
                leftX = adcLoc[0] + 12 + dX[i+1]    #kind of made up...

            cycleInsertionPoints = [0, 0]
            angleInsertionPoints = [0, 0]
            angle = []

            #check for geometry errors
            if(i > 0):
                if((prev(locs2)[0] > leftX - 2*Rin - Rout) or (rightX + 2*Rin + Rout > prev(locs3)[0])):
                    #print "Bottom geometry error", i
                    return 1
            else:
                if((prev(locs2)[0] > leftX - Rin) or (rightX + Rin > prev(locs3)[0])):
                    #print "Bottom geometry error", i
                    return 1

            if(i > 0):
                #first point A
                if(dY[i] < 0):
                    locs2.append(offset(locs2, 0, dY[i]))
                    locs1.append(offset(locs1, 0, dY[i]))
                    angle.append(0)
                    calcLength += LocsLength(locs1)

                #first point B
                locs2.append(offset(locs2, Rin, -Rin))
                locs1.append(offset(locs1, Rout, -Rout))
                angle.append(90)
                calcLength += math.pi*Rout/2

                #second point
                angle.append(0)
                locs2.append([(leftX - Rin - Rout), prev(locs2)[1]])
                locs1.append([(leftX - Rin - Rout), prev(locs1)[1]])
                calcLength += LocsLength(locs1)
                if(i>0):
                    dY[i-1] = dY[i] - Rout + Rin - tS - tW      #inverted all signs....

                #third point
                angle.append(-90)
                locs2.append(offset(locs2, Rout, -Rout))
                calcLength += math.pi*Rin/2
                locs1.append(offset(locs1, Rin, -Rin))

                cycleInsertionPoints[0] = len(locs2)
                angleInsertionPoints[0] = len(angle)

                #fourth point
                angle.append(0)
                locs2.append([prev(locs2)[0], heightY + Rin])
                locs1.append([prev(locs1)[0], heightY + Rin])
                leftX = prev(locs2)[0] - tS - tW
                calcLength += LocsLength(locs1)

            else:
                angle.append(0)
                locs2.append([prev(locs2)[0], heightY + Rin])
                locs1.append([prev(locs1)[0], heightY + Rin])
                calcLength += LocsLength(locs1)

            #fifth point
            angle.append(90)
            locs2.append(offset(locs2, Rin, -Rin))
            calcLength += math.pi*Rout/2
            locs1.append(offset(locs1, Rout, -Rout))
            #save heightYfor next run
            heightY = prev(locs1)[1] - tS - tW;

            if(i > 0):
                #sixth point
                angle.append(0)
                locs2.append([rightX, prev(locs2)[1]])
                locs1.append([rightX, prev(locs1)[1]])
                calcLength += LocsLength(locs1)

                #seventh point
                angle.append(90)
                locs2.append(offset(locs2, Rin, Rin))
                locs1.append(offset(locs1, Rout, Rout))
                rightX = prev(locs2)[0] + tS + tW
                calcLength += math.pi*Rout/2

                #eighth point
                angle.append(0)
                locs2.append([prev(locs2)[0],  locs3[3][1]-Rin-Rout+dY[i]])
                locs1.append([prev(locs1)[0], locs4[3][1]-Rin-Rout+dY[i]])
                cycleInsertionPoints[1] = len(locs2)
                angleInsertionPoints[1] = len(angle)
                calcLength += LocsLength(locs1)

                #ninth point
                angle.append(-90)
                locs2.append(offset(locs2, Rout, Rout))
                locs1.append(offset(locs1, Rin, Rin))
                calcLength+= math.pi*Rin/2

                #tenth point
                angle.append(0)
                locs2.append([locs3[3][0]-Rin, prev(locs2)[1]])
                locs1.append([locs4[3][0]-Rout, prev(locs1)[1]])
                calcLength += LocsLength(locs1)

                #eleventh point
                angle.append(90)
                locs2.append(offset(locs2, Rin, Rin))
                locs1.append(offset(locs1, Rout, Rout))
                calcLength += math.pi*Rout/2

            else:       #outside line
                #sixth point
                angle.append(0)
                locs2.append([locs3[3][0]- Rin, prev(locs2)[1]])
                locs1.append([locs4[3][0]-Rout, prev(locs1)[1]])
                calcLength += LocsLength(locs1)

                #seventh point
                angle.append(90)
                locs2.append(offset(locs2, Rin, Rin))
                locs1.append(offset(locs1, Rout, Rout))
                rightX = prev(locs2)[0] + tS + tW
                calcLength += math.pi*Rout/2

            #twelth point
            if(dY[i] < 0):
                angle.append(0)
                locs2.append(locs3[3])
                locs1.append(locs4[3])
                calcLength += LocsLength(locs1)

            #Check to add cycles
            neededLength = TotalL - calcLength
            maxCycles = int((((locs2[cycleInsertionPoints[0]-1][1]) - locs2[cycleInsertionPoints[0]][1]))//CycleLength)*2


            if(neededLength < 0):
                tError = 2
                #print "Error: Trace exceeds length", i

            if(neededLength > 0):
                numCycles = min(int(neededLength//(CyclePathLength - 2*(Rin+Rout))), maxCycles)    #calculate the number of cycles required
                if(numCycles%2 == 1):
                    numCycles-=1
                if(numCycles >0):
                    xExtend = (neededLength - (CyclePathLength - 2*(Rin+Rout))*numCycles)/numCycles/2
                else:
                    xExtend = 0
            else:
                numCycles = 0
                xExtend = 0

            for c in range(0,numCycles/2, 1):
                #add cycle to left side
                k=cycleInsertionPoints[0]
                a=angleInsertionPoints[0]
                inserts = 0
                locs2.insert(k, [locs2[k-1][0]-Rout, locs2[k-1][1]-Rout])
                locs1.insert(k, [locs1[k-1][0]-Rin, locs1[k-1][1]-Rin])
                angle.insert(a, -90)

                if(xExtend > 0):
                    k= k + 1
                    a = a + 1
                    locs2.insert(k, [locs2[k-1][0]-xExtend, locs2[k-1][1]])
                    locs1.insert(k, [locs1[k-1][0]-xExtend, locs1[k-1][1]])
                    angle.insert(a, 0)
                    inserts+=1

                k= k + 1
                a = a + 1
                locs2.insert(k, [locs2[k-1][0]-Rin, locs2[k-1][1]-Rin])
                tVal =locs1[k-1][0]-Rout
                locs1.insert(k, [tVal, locs1[k-1][1]-Rout])
                angle.insert(a, 90)
                inserts+=1

                k= k + 1
                a = a + 1
                locs2.insert(k, [locs2[k-1][0]+Rin, locs2[k-1][1]-Rin])
                locs1.insert(k, [locs1[k-1][0]+Rout, locs1[k-1][1]-Rout])
                angle.insert(a, 90)
                inserts+=1

                if(xExtend > 0):
                    k= k + 1
                    a = a + 1
                    locs2.insert(k, [locs2[k-1][0]+xExtend, locs2[k-1][1]])
                    locs1.insert(k, [locs1[k-1][0]+xExtend, locs1[k-1][1]])
                    angle.insert(a, 0)
                    inserts+=1

                k= k + 1
                a = a + 1
                locs2.insert(k, [locs2[k-1][0]+Rout, locs2[k-1][1]-Rout])
                locs1.insert(k, [locs1[k-1][0]+Rin, locs1[k-1][1]-Rin])
                angle.insert(a, -90)
                inserts+=1

                cycleInsertionPoints[0] = k+1
                angleInsertionPoints[0] = a+1

                #add cycle to right side
                cycleInsertionPoints[1] += inserts
                angleInsertionPoints[1] += inserts + 1
                k = cycleInsertionPoints[1]
                a = angleInsertionPoints[1]
                locs2.insert(k, [locs2[k][0]+Rout, locs2[k][1]-Rout])
                locs1.insert(k, [locs1[k][0]+Rin, locs1[k][1] - Rin])
                angle.insert(a, -90)

                if(xExtend > 0):
                    locs2.insert(k, [locs2[k][0]+xExtend, locs2[k][1]])
                    locs1.insert(k, [locs1[k][0]+xExtend, locs1[k][1]])
                    angle.insert(a, 0)

                locs2.insert(k, [locs2[k][0]+Rin, locs2[k][1] -Rin])
                tVal =locs1[k][0]+Rout
                locs1.insert(k, [tVal, locs1[k][1] - Rout])
                angle.insert(a, 90)

                locs2.insert(k, [locs2[k][0]-Rin, locs2[k][1] -Rin])
                locs1.insert(k, [locs1[k][0]-Rout, locs1[k][1] -Rout])
                angle.insert(a, 90)

                if(xExtend > 0):
                    locs2.insert(k, [locs2[k][0]-xExtend, locs2[k][1]])
                    locs1.insert(k, [locs1[k][0]-xExtend, locs1[k][1]])
                    angle.insert(a, 0)

                locs2.insert(k, [locs2[k][0]-Rout, locs2[k][1] -Rout])
                locs1.insert(k, [locs1[k][0]-Rin, locs1[k][1] -Rin])
                angle.insert(a, -90)
                cycleInsertionPoints[1] +=1
                angleInsertionPoints[1] +=0

            if(numCycles > 0):
                leftX -= Rin + Rout + xExtend
                rightX += Rin + Rout + xExtend

            #write inner wire
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs2[0:4]) + ";\n")

            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs2[3:len(locs2)], angle) + ";\n")

            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs3) + ";\n")

            #write outer wire
            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs1[0:4]) + ";\n")

            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Route " + str(tW) + " " + locsA2Str(locs1[3:len(locs1)], angle) + ";\n")

            fout.write("SET WIRE_BEND 2;\n")
            fout.write("Route " + str(tW) + " " + locs2Str(locs4) + ";\n")

        fout.flush()
    return tError
    #print "Generated Bottom Tracks"

def RouteClockTracks():
    with open(fileDir,'a') as fout:
        i = 17
        adc1 = adcPinLoc[pairs[i][0]-1]
        adc2 = adcPinLoc[pairs[i][1]-1]
        fpga1 = fpgaPinLoc[pairs[i][2]-1]
        fpga2 = fpgaPinLoc[pairs[i][3]-1]
        locs1 = []
        locs2 = []
        locs3 = []
        locs4 = []

        locs1.append(adc1)
        locs2.append(adc2)
        locs3.append(fpga1)
        locs4.append(fpga2)

        #Calculate the in/outs from the pads
        dT = ((adc1[1] - adc2[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
        locs1.append([adc1[0]+padExit, adc1[1]])    #move out of pad
        locs2.append([adc2[0]+padExit, adc2[1]])

        locs1.append([adc1[0]+padExit+dT, adc1[1]-dT])  #45 degree bend to parallel point
        locs2.append([adc2[0]+padExit+dT, adc2[1]+dT])

        dX[i] = 100*MIL2MM   #picked this randomly
        locs1.append([locs1[2][0] + postPar + dX[i], locs1[2][1]])  #extend out before starting bends locs[3]
        locs2.append([locs2[2][0] + postPar + dX[i], locs2[2][1]])

        dT = ((fpga1[1] - fpga2[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
        locs3.append([fpga1[0]-padExit, fpga1[1]])    #move out of pad
        locs4.append([fpga2[0]-padExit, fpga2[1]])

        locs3.append([fpga1[0]-padExit-dT, fpga1[1]-dT])  #45 degree bend to parallel point
        locs4.append([fpga2[0]-padExit-dT, fpga2[1]+dT])

        ddx = 200*MIL2MM

        locs3.append([prev(locs1)[0]+ddx, locs3[2][1]])  #extend out before starting bends locs[3]
        locs4.append([prev(locs2)[0]+ddx, locs4[2][1]])

        bend2 = []
        bend2.append(prev(locs2))
        mX = (prev(locs4)[0] + prev(locs2)[0])/2
        mY = (prev(locs4)[1] + prev(locs2)[1])/2
        bend2.append([mX, mY])
        bend2.append(prev(locs4))

        bend1 = []
        bend1.append(prev(locs1))
        mX = (prev(locs3)[0] + prev(locs1)[0])/2
        mY = (prev(locs3)[1] + prev(locs1)[1])/2
        bend1.append([mX, mY])
        bend1.append(prev(locs3))

        #write inner wire
        fout.write("SET WIRE_BEND 2;\n")
        fout.write("Route " + str(tW) + " " + locs2Str(locs2) + ";\n")
        fout.write("Route " + str(tW) + " " + locs2Str(locs4) + ";\n")
        fout.write("SET WIRE_BEND 7;\n")
        fout.write("Route " + str(tW) + " " + locs2Str(bend2) + ";\n")


        fout.write("SET WIRE_BEND 2;\n")
        fout.write("Route " + str(tW) + " " + locs2Str(locs1) + ";\n")
        fout.write("Route " + str(tW) + " " + locs2Str(locs3) + ";\n")
        fout.write("SET WIRE_BEND 7;\n")
        fout.write("Route " + str(tW) + " " + locs2Str(bend1) + ";\n")

def WriteScript(ddx, ttl):
    global fpgaLoc, TotalL, dX, fileDir, dY, adcPinLoc, fpgaPinLoc
    TotalL = ttl
    dX[23] = ddx
    dX[10] = ddx
    PlaceComponents()
    #set the X direction offset for the side tracks
    for i in range(22, 16, -1):
        dX[i] = dX[i+1] + (Rout-Rin+tS+tW)
    for i in range(11, 16, 1):
        dX[i] = dX[i-1] + (Rout-Rin+tS+tW)

    r1 = GenerateSideTracksTop(18, 24, 1)
    RouteClockTracks()
    r2 = GenerateSideTracksBottom(15, 9, -1)
    r3 = GenerateTopTracks()
    r4 = GenerateBottomTracks()


def main():
    print "Starting optimization"
    global fpgaLoc, TotalL, dX, fileDir, dY, adcPinLoc, fpgaPinLoc
    minDxChange = 0.1
    minLengthChange = 0.25
    #run optimization
    for partSpacing in range (81, 82, 1):      #cycle through widths
        print "Searching with partSpacing = " + str(partSpacing)
        fpgaLoc[0] = adcLoc[0] + partSpacing
        GeneratePinLocs()
        traceLengths = [0, 0, 0]
        traceLengths[0] = fpgaPinLoc[pairs[31][3]-1][0] - adcPinLoc[pairs[31][2]-1][0] + 9 *(Rout + tS + tD + 2*tW) #theoretical minimum total length
        traceLengths[2] = partSpacing + (2 * 40) + 20    #kind of made this up
        searchLength = True
        fileDir =  fileDirN + str(partSpacing) + ".scr"
        solutionTraceLength = 0
        solutionDX = 0
        # for just writing a file with known params
        #WriteScript(11.6585390625-0.2, 135.84675625)
        #searchLength = False
        while(searchLength):
            traceLengths[1] = (traceLengths[0]+traceLengths[2])/2
            TotalL = traceLengths[1]
            #print "Searchin with length = " + str(traceLengths)
            dXrange = [0, 0, (partSpacing - 20)/2  - (6 * (2*tW + tS + tD))]
            searchDx = True
            r1 = 0
            r2 = 0
            r3 = 0
            r4 = 0
            newSolution = False
            while(searchDx):
                dXrange[1] = (dXrange[0] + dXrange[2])/2
                dX[23] = dXrange[1]
                dX[10] = dXrange[1]
                PlaceComponents()
                #set the X direction offset for the side tracks
                for i in range(22, 16, -1):
                    dX[i] = dX[i+1] + (Rout-Rin+tS+tW)
                for i in range(11, 16, 1):
                    dX[i] = dX[i-1] + (Rout-Rin+tS+tW)

                r1 = GenerateSideTracksTop(18, 24, 1)
                RouteClockTracks()
                r2 = GenerateSideTracksBottom(15, 9, -1)
                r3 = GenerateTopTracks()
                r4 = GenerateBottomTracks()
                if((r1==1) or (r2==1)):    #dX makes tracks too cramped
                    dXrange[2] = dXrange[1]
                elif((r3 == 1) or (r4 == 1)): #if there are geometry errors on the top or bottom tracks, increase dX
                    dXrange[0] = dXrange [1]
                elif((r3 == 2) or (r4 == 2)): #if there is a length error, decrement dX ###increment length
                    dXrange[2] = dXrange[1]
                else:   #no errors - all things being equal, try a smaller dX
                    newSolution = True
                    solutionDX = dXrange [1]
                    solutionTraceLength = traceLengths[1]
                    dXrange[2] = dXrange[1]
                #check if we are done searching for dX
                if((dXrange[2]-dXrange[0]) < minDxChange):
                    searchDx = False
                    if(newSolution):
                       # print "Found minimum dX at", partSpacing, solutionTraceLength, solutionDX
                        traceLengths[2] = traceLengths[1]
                    else:
                       # print "Unable to find dX at", partSpacing, solutionTraceLength
                        traceLengths[0] = traceLengths[1]
                #end of dX while loop

            if(traceLengths[2] - traceLengths[0] < minLengthChange):
                searchLength = False
                if(solutionDX > 0):
                    print "Found minimum solution at", partSpacing, solutionTraceLength, solutionDX
                    TotalL = solutionTraceLength
                    dX[23] = solutionDX
                    dX[10] = solutionDX
                    PlaceComponents()
                    #set the X direction offset for the side tracks
                    for i in range(22, 16, -1):
                        dX[i] = dX[i+1] + (Rout-Rin+tS+tW)
                    for i in range(11, 16, 1):
                        dX[i] = dX[i-1] + (Rout-Rin+tS+tW)

                    r1 = GenerateSideTracksTop(18, 24, 1)
                    RouteClockTracks()
                    r2 = GenerateSideTracksBottom(15, 9, -1)
                    r3 = GenerateTopTracks()
                    r4 = GenerateBottomTracks()

                else:
                    #os.remove(fileDir)
                    print "Unable to find solution at", partSpacing

if __name__ == '__main__':
    main()
