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
MM2MIL = 1/MIL2MM #multuply mm by this to get mil

def RoundMIL(num):
    remainder = (num/10.0)%1 #get the part to round
    num = int(math.floor((num/10))*10)
    if(remainder < .25):
        return num
    elif (remainder <0.75):
        return num + 5
    else:
        return num + 10

Tpd =   6.5 #LVDS signal propagation speed in ps/mm

MAX_SIGNAL_SKEW = 50 #time in picoseconds
MAX_DIST_SKEW = MAX_SIGNAL_SKEW/Tpd

adcLoc = [1180, 1970]
fpgaLoc = [60, RoundMIL(adcLoc[1]+1*MM2MIL)]

adcPinLoc = []
fpgaPinLoc = []

tW = 6 #Track width
tD = 4 #Differential track distance
tS = 16 #Track spacing between different differential pairs
tB = 16 #5*tW #Track spacing between the same differential pair in bends, etc.  !!!! 5 tW is the minimum that allows for a radius of curvature of Rin 3x tW

padExit = 40 #the length out of the pad to extend before moving to tD with differential pair
postPar = 10 #the length after the two tracks are brought together before bends/etc.

Rin = (tB + tW)/2   #inside radius
Rout = Rin + tD + tW    #outside radius
CycleLength = 2*(Rin + Rout)
CyclePathLength = math.pi *(Rin + Rout)

dX23 = 4
dX10 = 4

#[adcPin Further Or Top, adcPinCloser Or Botton, fpgaPin 1, fpgaPin 2]
pairs = [
    [36, 37, 30, 29],     [38, 39, 27, 26],    [43, 44, 24, 23],   [45, 46, 22, 21],     [47, 48, 17, 16],
    [49, 50, 15, 14],     [54, 55, 12, 11],     [56, 57, 10, 9],    [58, 59, 8, 7],       [60, 61, 6, 5],
    [65, 66, 2, 1],       [68, 67, 141, 142],  [70, 69, 139, 140], [72, 71, 137, 138],   [76, 75, 133, 134],
    [78, 77, 131, 132],   [80, 79, 131, 132],  [82, 81, 126, 127], [84, 83, 123, 124],   [86, 85, 120, 121],
    [90, 89, 118, 119],   [92, 91, 116, 117],  [94, 93, 114, 115], [96, 95, 111, 112],   [101, 100, 104, 105],
    [103, 102, 101, 102], [105, 104, 99, 100], [107, 106, 97, 98], [112, 111, 94, 95],   [114, 113, 92, 93],
    [116, 115, 87, 88],   [118, 117, 84, 85],  [123, 122, 82, 83], [125, 124, 80, 81]]

sigNames = [ "DQD0+", "DQD0-", "DQD1+", "DQD1-", "DQD2+", "DQD2-", "DQD3+", "DQD3-", "DQD4+", "DQD4-", "DQD5+", "DQD5-", "DQD6+", "DQD6-", "DQD7+", "DQD7-",
             "DQ0+", "DQ0-", "DQ1+", "DQ1-", "DQ2+", "DQ2-", "DQ3+", "DQ3-", "DQ4+", "DQ4-", "DQ5+", "DQ5-", "DQ6+", "DQ6-", "DQ7+", "DQ7-",
             "OR-", "OR+", "ADC_DCLK-", "ADC_DCLK+",
             "DI7-", "DI7+", "DI6-", "DI6+", "DI5-", "DI5+", "DI4-", "DI4+", "DI3-", "DI3+", "DI2-", "DI2+", "DI1-", "DI1+", "DI0-", "DI0+",
             "DID7-", "DID7+", "DID6-", "DID6+", "DID5-", "DID5+", "DID4-", "DID4+", "DID3-", "DID3+", "DID2-", "DID2+", "DID1-", "DID1+", "DID0-", "DID0+"]

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
        fout.write("Grid MIL;\n")
        fout.write("Move U$1 (" + str(adcLoc[0]) + ' ' + str(adcLoc[1]) +');\n')
        fout.write("Move U$2 (" + str(fpgaLoc[0]) + ' ' + str(fpgaLoc[1]) +');\n')
        fout.flush()

def GeneratePinLocs():
    global adcPinLoc, fpgaPinLoc
    adcPinLoc = []
    fpgaPinLoc = []
#Generate the locations of the pins on the ADC
    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] - 10.6*MM2MIL, adcLoc[1] + 7.75*MM2MIL - i*0.5*MM2MIL])

    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] - 7.75*MM2MIL + i*0.5*MM2MIL, adcLoc[1] - 10.6*MM2MIL])

    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] + 10.6*MM2MIL, adcLoc[1] - 7.75*MM2MIL + i*0.5*MM2MIL])

    for i in range(0,32):
        adcPinLoc.append([adcLoc[0] + 7.75*MM2MIL - i*0.5*MM2MIL, adcLoc[1] + 10.6*MM2MIL])

#Generate the locations of the pins on the FPGA
    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] - 8.75*MM2MIL + i*0.5*MM2MIL, fpgaLoc[1] - 10.7*MM2MIL])

    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] + 10.7*MM2MIL, fpgaLoc[1] - 8.75*MM2MIL + i*0.5*MM2MIL])

    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] + 8.75*MM2MIL - i*0.5*MM2MIL, fpgaLoc[1] + 10.7*MM2MIL])

    for i in range(0,36):
        fpgaPinLoc.append([fpgaLoc[0] - 10.7*MM2MIL, fpgaLoc[1] + 8.75*MM2MIL - i*0.5*MM2MIL])

def locs2Str(locs, add0):
    strOut = ""
    for i in range (0, len(locs)):
        strOut = strOut + "(" + str(locs[i][0]) + " " + str(locs[i][1]) +")"
        if (add0 and i<len(locs)-1):
            strOut = strOut + " +0 "

    return strOut

def locsA2Str(locs, angles):
    strOut = ""
    i = 0
    for l in locs:
        if(i < len(angles)):
            strOut = strOut + " "
            if(angles[i] >= 0):
                strOut = strOut + "+"
            strOut = strOut + str(angles[i])
            i = i + 1
        strOut = strOut + " (" + str(l[0]) + " " + str(l[1]) +")"
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

def RoundPoints(li, digits):
    for i in range (0, len(li)):
        for j in range (0, len(li[i])):
            li[i][j] = round(li[i][j], digits)

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
    Swap(yS)

    R = [Rout, Rin]
    for i in range(0, 2):
        Swap(R)
        for j in range(0,2):
            iLocs.append(offset(iLocs, R[0]*signX, R[0]*signY))
            oLocs.append(offset(oLocs, R[1]*signX, R[1]*signY))
            iAngle.append(90*signAngle)
            oAngle.append(90*signAngle)

            if(xS[0] > 0 or yS[0] > 0):
                d = 2 if (i==1 and j == 1) else 1
                iLocs.append(offset(iLocs, xS[0]*signX/d, yS[0]*signY/d))
                oLocs.append(offset(oLocs, xS[0]*signX/d, yS[0]*signY/d))
                iAngle.append(0)
                oAngle.append(0)

            Swap(R)
            Swap(xS)
            Swap(yS)
            signAngle *= -1
        if(travelDir == Direction.Up or travelDir == Direction.Down):
            signX *= -1
        else:
            signY *= -1
        signAngle *= -1

    iLocs.remove(iLocs[0])
    oLocs.remove(oLocs[0])
    return [iLocs, oLocs, iAngle, oAngle]

def RouteSideTracks(sIndex, eIndex, indexStep):
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
            dX[i] = 0;

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

            bend2 = []
            bend2.append(prev(locs2))
            mX = (prev(locs4)[0] + prev(locs2)[0])/2
            mY = (prev(locs4)[1] + prev(locs2)[1])/2
            bend2.append([mX, mY])
            bend2.remove(bend2[0])

            bend1 = []
            bend1.append(prev(locs1))
            mX = (prev(locs3)[0] + prev(locs1)[0])/2
            mY = (prev(locs3)[1] + prev(locs1)[1])/2
            bend1.append([mX, mY])
            bend1.remove(bend1[0])

            #write inner wire
            fout.write("SET WIRE_BEND 7;\n")
            locs4.reverse()
            locs3.reverse()
            fout.write("Wire '" + sigNames[i*2] + "' " + str(tW) + " " + locs2Str(locs2, True)
                        + locs2Str(bend2, False) + locs2Str(locs4,True) + ";\n")
            fout.write("Wire '" + sigNames[i*2+1] + "' " + str(tW) + " " + locs2Str(locs1, True)
                        + locs2Str(bend1, False) + locs2Str(locs3,True) + ";\n")
        fout.flush()

def GenerateTopTracks(targetL, maxDiff):
    tError = 0
    with open(fileDir,'a') as fout:
        for i in range(24, 34, 1):
            #targetL += maxDiff/10
            if (i == 33):
                targetL = targetL + maxDiff
            adc1 = adcPinLoc[pairs[i][0]-1]
            adc2 = adcPinLoc[pairs[i][1]-1]
            fpga2 = fpgaPinLoc[pairs[i][2]-1]
            fpga1 = fpgaPinLoc[pairs[i][3]-1]
            locs1 = []
            locs2 = []
            locs3 = []
            locs4 = []
            angle1 = []
            angle2 = []

            locs1.append(adc1)
            locs2.append(adc2)
            locs3.append(fpga1)
            locs4.append(fpga2)
            calcLength = 0

            #Calculate the in/outs from the pads
            dT = ((adc2[0] - adc1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs1.append(offset(locs1, 0, padExit))
            locs2.append(offset(locs2, 0, padExit))
            calcLength += LocsLength(locs1)

            locs1.append(offset(locs1, 0, dT))  #45 degree bend to parallel point
            locs2.append(offset(locs2, -dT, dT))
            calcLength += LocsLength(locs1)

            if(i==24):
                maxY[i] = locs1[2][1]+postPar
            if(i==33):
                maxY[i] -= (Rin + Rout)

            locs1.append([locs1[2][0], maxY[i]])  #extend out before starting bends locs[3]
            locs2.append([locs2[2][0], maxY[i]])
            calcLength += LocsLength(locs1)

            dT = ((fpga2[0] - fpga1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs3.append(offset(locs3, 0, padExit))    #move out of pad
            locs4.append(offset(locs4, 0, padExit))
            calcLength += LocsLength(locs3)

            locs3.append(offset(locs3, dT, dT))  #45 degree bend to parallel point
            locs4.append(offset(locs4, 0, dT))
            calcLength += LocsLength(locs3)

            locs3.append([locs3[2][0], maxY[i]])  #extend out before starting bends locs[3]
            locs4.append([locs4[2][0], maxY[i]])
            calcLength += LocsLength(locs3)

            farX = locs3[len(locs3)-1][0]
            deltaX = farX - locs2[3][0] - 2*Rin
            maxCycles = int(deltaX // CycleLength)

            neededLength = targetL - calcLength - math.pi * Rin

            numCycles = min(int((neededLength-deltaX)//(CyclePathLength-CycleLength)), maxCycles);

            if(numCycles > 0):
                xStretch = (deltaX - numCycles*CycleLength)/(2*numCycles+1)
                yStretch = (neededLength - numCycles*CyclePathLength - numCycles*xStretch*2 - xStretch)/(2*numCycles +2)
            else:
                numCycles = 0
                xStretch = deltaX
                yStretch = 0

            if(i < 33 and numCycles == 0):
                tError = 1
                i == 35
                #return tError

            if(i == 33 and numCycles > 0):
                tError = 2
                #return tError

            if(yStretch > 0):
                locs2.append(offset(locs2, 0, yStretch))
                locs1.append(offset(locs1, 0, yStretch))

            locs2.append(offset(locs2, Rin, Rin))
            locs1.append(offset(locs1, Rout, Rout))

            if(xStretch > 0):
                locs2.append(offset(locs2, xStretch/2, 0))
                locs1.append(offset(locs1, xStretch/2, 0))


            if(i<33):
                maxY[i+1] = locs2[len(locs2)-1][1] + tS + Rout + Rin

            for j in range(0, numCycles):
                iLocs = []
                oLocs =[]
                iAngle = []
                oAngle = []
                [iLocs, oLocs, iAngle, oAngle] = ReturnMeander(locs2[len(locs2)-1], locs1[len(locs1)-1], Direction.Right, Direction.Down, xStretch, yStretch)
                for k in range(0, len(iLocs)):
                    locs2.append(iLocs[k])
                    locs1.append(oLocs[k])
                    angle1.append(oAngle[k])
                    angle2.append(iAngle[k])

            if(xStretch > 0):
                locs2.append(offset(locs2, xStretch/2, 0))
                locs1.append(offset(locs1, xStretch/2, 0))

            if(numCycles > 0):
                locs2.append(offset(locs2, Rin, -Rin))
                locs1.append(offset(locs1, Rout, -Rout))
            #write inner wire
            locs3.reverse()
            locs4.reverse()
##            RoundPoints(locs1, 3)
##            RoundPoints(locs2, 3)
##            RoundPoints(locs3, 3)
##            RoundPoints(locs4, 3)
            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Wire '" + sigNames[i*2] + "' " + str(tW) + " " + locs2Str(locs2[0:4], True) +
                        locs2Str(locs2[4:len(locs2)], False) + " " + locs2Str(locs3, True) + ";\n")
            fout.write("Wire '" + sigNames[i*2+1] + "' " + str(tW) + " " + locs2Str(locs1[0:4], True) +
                        locs2Str(locs1[4:len(locs1)], False) + " " + locs2Str(locs4, True) + ";\n")

        fout.flush()
    return tError
    #print "Generated Top Tracks"

def GenerateDQ2Tracks(targetL):
    tError = 0
    with open(fileDir,'a') as fout:
        i = 10;
        adc1 = adcPinLoc[pairs[i][0]-1]
        adc2 = adcPinLoc[pairs[i][1]-1]
        fpga1 = fpgaPinLoc[pairs[i][2]-1]
        fpga2 = fpgaPinLoc[pairs[i][3]-1]
        locs1 = []
        locs2 = []
        locs3 = []
        locs4 = []
        calcLength = 0

        #locs2 is top
        locs1.append(adc1)
        locs2.append(adc2)
        locs3.append(fpga1)
        locs4.append(fpga2)
        dX[i] = 0;

        #Calculate the in/outs from the pads
        dT = ((adc2[1] - adc1[1])-tD-tW)/2          #calculate the required change in path to get the two tracks to the correct distance
        locs1.append(offset(locs1, padExit, 0))
        locs2.append(offset(locs2, padExit, 0))
        calcLength += LocsLength(locs2)

        locs1.append(offset(locs1, dT, dT))
        locs2.append(offset(locs2, dT, -dT))
        calcLength += LocsLength(locs2)

        locs1.append(offset(locs1, postPar, 0))
        locs2.append(offset(locs2, postPar,0))
        calcLength += LocsLength(locs2)

        dT = ((fpga1[0] - fpga2[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
        locs3.append(offset(locs3, 0, -padExit))    #move out of pad
        locs4.append(offset(locs4, 0, -padExit))
        calcLength += LocsLength(locs4)

        locs3.append(offset(locs3, 0, -dT))  #45 degree bend to parallel point
        locs4.append(offset(locs4, dT, -dT))
        calcLength += LocsLength(locs4)

        locs3.append(offset(locs3, 0, -postPar))  #extend out before starting bends locs[3]
        locs4.append(offset(locs4, 0, -postPar))
        calcLength += LocsLength(locs4)

        locs4.append(offset(locs4, -Rin, -Rin))
        locs3.append(offset(locs3, -Rout, -Rout))
        calcLength += math.pi*Rin/2

        maxY[i-1] = locs3[len(locs3)-1][1] - tS - Rout - Rin

        locs3.append(offset(locs3, -3*MM2MIL, 0)) #3 made up
        locs4.append(offset(locs4, -3*MM2MIL, 0))
        calcLength += LocsLength(locs4)

        locs4.append(offset(locs4, -Rin, Rin))
        locs3.append(offset(locs3, -Rout, Rout))
        calcLength += math.pi*Rin/2

        locs4.append([locs4[len(locs4)-1][0], locs2[len(locs2)-1][1]-Rout])
        locs3.append([locs3[len(locs3)-1][0], locs1[len(locs1)-1][1]-Rin])
        calcLength += LocsLength(locs4)

        locs4.append(offset(locs4, -Rout, Rout))
        locs3.append(offset(locs3, -Rin, Rin))
        calcLength += math.pi*Rout/2


        farX = locs4[len(locs4)-1][0]
        deltaX = farX - locs2[len(locs2)-1][0]
        maxCycles = int(deltaX // CycleLength)

        neededLength = targetL - calcLength

        numCycles = min(int((neededLength-deltaX)//(CyclePathLength-CycleLength)), maxCycles);

        if(numCycles > 0):
            xStretch = (deltaX - numCycles*CycleLength)/(2*numCycles)
            yStretch = (neededLength - numCycles*CyclePathLength - numCycles*xStretch*2)/(2*numCycles)
        else:
            numCycles = 0
            xStretch = deltaX
            yStretch = 0

        currentY =locs4[len(locs4)-1][1]
        maxY[i-1] = min(maxY[i-1], currentY - Rout - yStretch - Rout - tS - Rout - Rin)

        for j in range(0, numCycles):
            iLocs = []
            oLocs =[]
            iAngle = []
            oAngle = []
            [iLocs, oLocs, iAngle, oAngle] = ReturnMeander(locs3[len(locs3)-1], locs4[len(locs4)-1], Direction.Left, Direction.Down, xStretch, yStretch)
            for k in range(0, len(iLocs)):
                locs4.append(oLocs[k])
                locs3.append(iLocs[k])
 #               angle1.append(oAngle[k])
 #               angle2.append(iAngle[k])


        #write inner wire
        locs2.reverse()
        locs1.reverse()
        RoundPoints(locs1, 3)
        RoundPoints(locs2, 3)
        RoundPoints(locs3, 3)
        RoundPoints(locs4, 3)
        fout.write("SET WIRE_BEND 7;\n")
        fout.write("Wire '" + sigNames[i*2+1] + "' " + str(tW) + " " + locs2Str(locs4[0:4], True) +
                    locs2Str(locs4[4:len(locs4)-1], False) + " " + locs2Str(locs2, True) + ";\n")
        fout.write("Wire '" + sigNames[i*2] + "' " + str(tW) + " " + locs2Str(locs3[0:4], True) +
                    locs2Str(locs3[4:len(locs3)-1], False) + " " + locs2Str(locs1, True) + ";\n")

        fout.flush()
    return tError

def GenerateBottomTracks(targetL, maxDiff):
    tError = 0
    with open(fileDir,'a') as fout:
        for i in range(9, -1, -1):
            if (i == 0):
                targetL = targetL + maxDiff
            adc1 = adcPinLoc[pairs[i][0]-1]
            adc2 = adcPinLoc[pairs[i][1]-1]
            fpga2 = fpgaPinLoc[pairs[i][2]-1]
            fpga1 = fpgaPinLoc[pairs[i][3]-1]
            locs1 = []
            locs2 = []
            locs3 = []
            locs4 = []
            angle1 = []
            angle2 = []

            locs1.append(adc1)
            locs2.append(adc2)
            locs3.append(fpga1)
            locs4.append(fpga2)
            calcLength = 0

            #Calculate the in/outs from the pads
            dT = ((adc2[0] - adc1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs1.append(offset(locs1, 0, -padExit))
            locs2.append(offset(locs2, 0, -padExit))
            calcLength += LocsLength(locs1)

            locs1.append(offset(locs1, 0, -dT))  #45 degree bend to parallel point
            locs2.append(offset(locs2, -dT, -dT))
            calcLength += LocsLength(locs1)

            if(i==0):
                maxY[i] += (Rin + Rout)

            locs1.append([locs1[2][0], maxY[i]])  #extend out before starting bends locs[3]
            locs2.append([locs2[2][0], maxY[i]])
            calcLength += LocsLength(locs1)

            dT = ((fpga2[0] - fpga1[0])-tD-tW)          #calculate the required change in path to get the two tracks to the correct distance
            locs3.append(offset(locs3, 0, -padExit))    #move out of pad
            locs4.append(offset(locs4, 0, -padExit))
            calcLength += LocsLength(locs3)

            locs3.append(offset(locs3, dT, -dT))  #45 degree bend to parallel point
            locs4.append(offset(locs4, 0, -dT))
            calcLength += LocsLength(locs3)

            locs3.append([locs3[2][0], maxY[i]])  #extend out before starting bends locs[3]
            locs4.append([locs4[2][0], maxY[i]])
            calcLength += LocsLength(locs3)

            farX = locs3[len(locs3)-1][0]
            deltaX = farX - locs2[3][0] - 2*Rin
            maxCycles = int(deltaX // CycleLength)

            neededLength = targetL - calcLength - math.pi * Rin

            numCycles = min(int((neededLength-deltaX)//(CyclePathLength-CycleLength)), maxCycles);

            if(numCycles > 0):
                xStretch = (deltaX - numCycles*CycleLength)/(2*numCycles+1)
                yStretch = (neededLength - numCycles*CyclePathLength - numCycles*xStretch*2 - xStretch)/(2*numCycles +2)
            else:
                numCycles = 0
                xStretch = deltaX
                yStretch = 0

            if(i > 0 and numCycles == 0):
                tError = 1
                i == -10
                #return tError

            if(i == 0 and numCycles > 0):
                tError = 2
                #return tError

            if(yStretch > 0):
                locs2.append(offset(locs2, 0, -yStretch))
                locs1.append(offset(locs1, 0, -yStretch))

            locs2.append(offset(locs2, Rin, -Rin))
            locs1.append(offset(locs1, Rout, -Rout))

            if(xStretch > 0):
                locs2.append(offset(locs2, xStretch/2, 0))
                locs1.append(offset(locs1, xStretch/2, 0))


            if(i > 0):
                maxY[i-1] = locs2[len(locs2)-1][1] - tS - Rout - Rin

            for j in range(0, numCycles):
                iLocs = []
                oLocs =[]
                iAngle = []
                oAngle = []
                [iLocs, oLocs, iAngle, oAngle] = ReturnMeander(locs2[len(locs2)-1], locs1[len(locs1)-1], Direction.Right, Direction.Up, xStretch, yStretch)
                for k in range(0, len(iLocs)):
                    locs2.append(iLocs[k])
                    locs1.append(oLocs[k])
                    angle1.append(oAngle[k])
                    angle2.append(iAngle[k])

            if(xStretch > 0):
                locs2.append(offset(locs2, xStretch/2, 0))
                locs1.append(offset(locs1, xStretch/2, 0))

            if(numCycles > 0):
                locs2.append(offset(locs2, Rin, Rin))
                locs1.append(offset(locs1, Rout, Rout))
            #write inner wire
            locs3.reverse()
            locs4.reverse()
##            RoundPoints(locs1, 3)
##            RoundPoints(locs2, 3)
##            RoundPoints(locs3, 3)
##            RoundPoints(locs4, 3)
            fout.write("SET WIRE_BEND 7;\n")
            fout.write("Wire '" + sigNames[i*2+1] + "' " + str(tW) + " " + locs2Str(locs2[0:4], True) +
                        locs2Str(locs2[4:len(locs2)], False) + " " + locs2Str(locs3, True) + ";\n")
            fout.write("Wire '" + sigNames[i*2] + "' " + str(tW) + " " + locs2Str(locs1[0:4], True) +
                        locs2Str(locs1[4:len(locs1)], False) + " " + locs2Str(locs4, True) + ";\n")

        fout.flush()
    return tError
    #print "Generated Top Tracks"


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
    for partSpacing in range (1300, 1400, 40):      #cycle through widths
        fpgaLoc[0] = adcLoc[0] + partSpacing
        GeneratePinLocs()
        traceLengths = [0, 0, 0]
        traceLengths[0] = fpgaPinLoc[pairs[31][3]-1][0] - adcPinLoc[pairs[31][2]-1][0] + 9 *(Rout + tS + tD + 2*tW) #theoretical minimum total length
        traceLengths[2] = partSpacing + (2 * 40*MM2MIL) + 30*MM2MIL    #kind of made this up
        searchLength = True
        fileDir =  fileDirN + str(partSpacing) + ".scr"
        r1 = 0
        r2 = 0
        tLTop = 0
        tLBottom = 0
        maxDiff = 10*MM2MIL

        while(searchLength):
            traceLengths[1] = (traceLengths[0]+traceLengths[2])/2
            PlaceComponents()
            r1 = GenerateTopTracks(traceLengths[1], maxDiff)
            print traceLengths[1], r1
            if(r1 == 0 ):
                searchLength = False
                tLTop = traceLengths[1]
            elif (r1 == 1):
                if(traceLengths[2] - traceLengths[0] < 30):
                    searchLength = False
                    tLTop = traceLengths[1]
                else:
                    traceLengths[0] = traceLengths[1]
            elif(r1 == 2):
                traceLengths[2] = traceLengths[1]

        traceLengths[0] = tLTop
        traceLengths[2] = 2*tLTop #made up
        searchLength = True

        while(searchLength):
            traceLengths[1] = (traceLengths[0]+traceLengths[2])/2
            PlaceComponents()
            GenerateDQ2Tracks(traceLengths[1])
            r2 = GenerateBottomTracks(traceLengths[1], maxDiff)
            if(r2 == 0):
                searchLength = False
                tLBottom = traceLengths[1]
            elif (r2 == 1):
                if(traceLengths[2] - traceLengths[0] < 30):
                    searchLength = False
                    tLBottom = traceLengths[1];
                else:
                    traceLengths[0] = traceLengths[1]
            elif(r2 == 2):
                traceLengths[2] = traceLengths[1]

        area = partSpacing*(maxY[33] + maxY[0])
        print "For Spacing = " + str(partSpacing) + " Area = " + str(round(area,0)), round(maxY[33],0), round(maxY[0],0)
        PlaceComponents()
        RouteSideTracks(11, 16, 1)
        RouteSideTracks(17, 24, 1)
        GenerateTopTracks(tLTop, maxDiff)
        GenerateDQ2Tracks(tLBottom)
        GenerateBottomTracks(tLBottom, maxDiff)


if __name__ == '__main__':
    main()
