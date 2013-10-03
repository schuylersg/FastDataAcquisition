#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     26/09/2013
# Copyright:   (c) Owner 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

fileDirN = "C:\Program Files (x86)\EAGLE-6.5.0\scr\\fda_place.scr"
ADC = [1180, 1970]
FPGA = [2520, 2010]

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


def Offset(O, x, y):
    return [O[0]+x, O[1]+y]

def OffsetFromOrig(NewOrigin, OldOrigin, OldPos):
    x = OldOrigin[0] - OldPos[0]
    y = OldOrigin[1] - OldPos[1]
    return[NewOrigin[0] - x, NewOrigin[1] - y]

def FlipL(Origin, locs):
    for i in range (0, len(locs)):
        locs[i][0] = (Origin[0]-locs[i][0]) + Origin[0]
        locs[i][1] = (Origin[1]-locs[i][1]) + Origin[1]

def Place(comp, pos):
    return "Move " + comp + " (" + str(pos[0]) + ' ' + str(pos[1]) + ");\n"

def Rotate(comp, angle, flip = 0):
    if(flip == 1):
        return "Rotate =MR" + str(angle) + " '"  + comp + "';\n"
    return "Rotate =R" + str(angle) + " '"  + comp + "';\n"

def Wire(NewOrigin, OldOrigin, SigName, Width, locs):
    strOut = "Wire '" + str(SigName) + "' " + str(Width) + " "
    for i in range(0, len(locs)):
        x = NewOrigin[0] - (OldOrigin[0] - locs[i][0])
        y = NewOrigin[1] - (OldOrigin[1] - locs[i][1])
        strOut = strOut + "(" + str(x) + " " + str(y) +")"
    strOut = strOut + ";\n"
    return strOut

def Via(NewOrigin, OldOrigin, SigName, locs):
    strOut = "Via '" + SigName + "' "
    for i in range(0, len(locs)):
        x = NewOrigin[0] - (OldOrigin[0] - locs[i][0])
        y = NewOrigin[1] - (OldOrigin[1] - locs[i][1])
        strOut = strOut + "(" + str(x) + " " + str(y) +")"
    strOut = strOut + ";\n"
    return strOut

def PlaceCaps():
    FPGAEdge = 455
    ADCEdge = 455
    minPartSpace = 10
    with open(fileDirN,'w') as fout:
##        #write 1v9A bypass caps
##        fout.write("GRID Mil;\n")
##        partWidth = 40
##
##        e = ADCEdge + minPartSpace + partWidth/2
##        fout.write(Place("C8", Offset(ADC, -e, RoundMIL(7.5*MM2MIL))))
##        fout.write(Rotate("C8", 90))
##        fout.write(Place("C9", Offset(ADC, -e, RoundMIL(5.5*MM2MIL))))
##        fout.write(Rotate("C9", 90))
##        fout.write(Place("C10", Offset(ADC, -e, RoundMIL(4*MM2MIL))))
##        fout.write(Rotate("C10", 90))
##        fout.write(Place("C11", Offset(ADC, -e, RoundMIL(2*MM2MIL))))
##        fout.write(Rotate("C11", 90))
##        fout.write(Place("C12", Offset(ADC, -e, RoundMIL(.25*MM2MIL))))
##        fout.write(Rotate("C12", 90))
##        fout.write(Place("C13", Offset(ADC, -e, RoundMIL(-2*MM2MIL))))
##        fout.write(Rotate("C13", 90))
##        fout.write(Place("C14", Offset(ADC, -e, RoundMIL(-4*MM2MIL))))
##        fout.write(Rotate("C14", 90))
##        fout.write(Place("C15", Offset(ADC, -e, RoundMIL(-5.5*MM2MIL))))
##        fout.write(Rotate("C15", 90))
##        fout.write(Place("C16", Offset(ADC, RoundMIL(-8*MM2MIL), -e)))
##        fout.write(Rotate("C16", 0))
##        fout.write(Place("C17", Offset(ADC, RoundMIL(-8*MM2MIL), e)))
##        fout.write(Rotate("C17", 180))
##
##        #1V9D bypass caps
##        fout.write(Place("C22", Offset(ADC, RoundMIL(-4*MM2MIL), -e)))
##        fout.write(Rotate("C22", 0))
##        fout.write(Place("C23", Offset(ADC, RoundMIL(1.5*MM2MIL), -e)))
##        fout.write(Rotate("C23", 0))
##        fout.write(Place("C24", Offset(ADC, RoundMIL(7*MM2MIL), -e)))
##        fout.write(Rotate("C24", 0))
##        fout.write(Place("C25", Offset(ADC, e, RoundMIL(-3.5*MM2MIL))))
##        fout.write(Rotate("C25", 90))
##        fout.write(Place("C26", Offset(ADC, e, RoundMIL(3.5*MM2MIL))))
##        fout.write(Rotate("C26", 270))
##        fout.write(Place("C27", Offset(ADC, RoundMIL(7*MM2MIL), e)))
##        fout.write(Rotate("C27", 0))
##        fout.write(Place("C28", Offset(ADC, RoundMIL(1.5*MM2MIL), e)))
##        fout.write(Rotate("C28", 0))
##        fout.write(Place("C29", Offset(ADC, RoundMIL(-4*MM2MIL), e)))
##        fout.write(Rotate("C29", 0))
##
##        fout.write(Place("R9", Offset(ADC, -e, -e+130)))
##        fout.write(Rotate("R9", 90))
##
##        #LMH6555
##        LMH6555 = Offset(ADC, -730, 120)
##        fout.write(Place("U$10", LMH6555))
##        LMHWidth = 160
##        Cwidth = 40
##        e = (LMHWidth + Cwidth)/2 + minPartSpace + 20
##        fout.write(Place("C89", Offset(LMH6555, e, 25)))
##        fout.write(Rotate("C89", 90))
##        fout.write(Place("C90", Offset(LMH6555, e, -40)))
##        fout.write(Rotate("C90", 270))
##        fout.write(Place("C91", Offset(LMH6555, e-25, -60)))
##        fout.write(Rotate("C91", 0, 1))
##
##        e = (LMHWidth + 20)/2 + minPartSpace + 20
##        fout.write(Place("R51", Offset(LMH6555, -20, -e)))
##        fout.write(Rotate("R51", 180))
##
##        fout.write(Place("X2", Offset(LMH6555, -450, 75)))
##        fout.write(Rotate("X2", 0))
##
##        #LMV321
##        LMV321 = Offset(ADC, -630, 330)
##        fout.write(Place("U$11", LMV321))
##        fout.write(Rotate("U$11", 0, 1))
##        fout.write(Place("C104", Offset(LMV321, 20, 90)))
##        fout.write(Rotate("C104", 0, 1))
##
##        #SI530
##        SI530 = Offset(ADC, -700, -250)
##        fout.write(Place("Y1", SI530))
##        fout.write(Rotate("Y1", 90))
##        fout.write(Place("C76", Offset(SI530, -100, 140)))
##        fout.write(Rotate("C76", 0))
##        fout.write(Place("C77", Offset(SI530, -100, 180)))
##        fout.write(Rotate("C77", 0))
##        fout.write(Place("C78", Offset(SI530, -100, 180)))
##        fout.write(Rotate("C78", 180, 1))
##
##
##        fout.write(Place("C79", Offset(ADC, -ADCEdge - 85, -25)))
##        fout.write(Rotate("C79", 0))
##        fout.write(Place("C82", Offset(ADC, -ADCEdge - 85, -55)))
##        fout.write(Rotate("C82", 0))
##
##        #TMP421
##        TMP421 = Offset(ADC, -ADCEdge+100, -ADCEdge - 220)
##        fout.write(Place("U$8", TMP421))
##        fout.write(Rotate("U$8", 180))
##        fout.write(Place("C88", Offset(TMP421, 25, 100)))
##        fout.write(Rotate("C88", 180))
##        fout.write(Place("C87", Offset(TMP421, 50, -110)))
##        fout.write(Rotate("C87", 0))
##
##        #ADCMP553
##        ADCMP553 = Offset(ADC, -700, -600)
##        fout.write(Place("IC3", ADCMP553))
##        fout.write(Rotate("IC3", 0))
##        fout.write(Place("R59", Offset(ADCMP553, -140, -25)))
##        fout.write(Rotate("R59", 90))
##        fout.write(Place("C103", Offset(ADCMP553, 130, 25)))
##        fout.write(Rotate("C103", 90))
##        fout.write(Place("C102", Offset(ADCMP553, 175, 25)))
##        fout.write(Rotate("C102", 90))
##
##
##        #DAC101
##        DAC101 = Offset(ADCMP553, 0, -180)
##        fout.write(Place("U$9", DAC101))
##        fout.write(Rotate("U$9", 0))
##        fout.write(Place("C95", Offset(DAC101, 20, -100)))
##        fout.write(Rotate("C95", 0))
##        fout.write(Place("C94", Offset(DAC101, 20, -130)))
##        fout.write(Rotate("C94", 0))
##        fout.write(Place("C93", Offset(DAC101, 20, -110)))
##        fout.write(Rotate("C93", 0, 1))
##        fout.write(Place("C98", Offset(DAC101, 20, -180)))
##        fout.write(Rotate("C98", 180, 1))
##
##        a =Offset(LMH6555, -450, 75)
##        b = Offset(ADCMP553, -450, -20)
##        fout.write(Place("X3", [a[0], b[1]]))
##        fout.write(Rotate("X3", 0))


##        #VCCINT Bypass
##        fout.write(Place("C35", Offset(FPGA, -16, -1.4)))
##        fout.write(Rotate("C35", 90))
##        fout.write(Place("C36", Offset(FPGA, 0.9, -15.9)))
##        fout.write(Rotate("C36", 90))
##        fout.write(Place("C37", Offset(FPGA, 14, -1.5)))
##        fout.write(Rotate("C37", 180))
##        fout.write(Place("C38", Offset(FPGA, 1, 12.75)))
##        fout.write(Rotate("C38", 0))
##
##        #VCCAUX Bypass
##        fout.write(Place("C39", Offset(FPGA, -13, -1.4)))
##        fout.write(Rotate("C39", 90))
##        fout.write(Place("C40", Offset(FPGA, 0.9, -12.9)))
##        fout.write(Rotate("C40", 90))
##        fout.write(Place("C41", Offset(FPGA, 8.75, -12.9)))
##        fout.write(Rotate("C41", 90))
##        fout.write(Place("C42", Offset(FPGA, 14.5, 0)))
##        fout.write(Rotate("C42", 270))
##        fout.write(Place("C43", Offset(FPGA, .5, 14.5)))
##        fout.write(Rotate("C43", 0))
##        fout.write(Place("C44", Offset(FPGA, .5, 16)))
##        fout.write(Rotate("C44", 0))
##        fout.write(Place("C45", Offset(FPGA, -14.5, -1.4)))
##        fout.write(Rotate("C45", 90))
##        fout.write(Place("C46", Offset(FPGA, 13, -0.5)))
##        fout.write(Rotate("C46", 90))
##
##        #VCC_0 Bypass
##        fout.write(Place("C47", Offset(FPGA, -13, -4.5)))
##        fout.write(Rotate("C47", 90))
##        fout.write(Place("C48", Offset(FPGA, -13, .8)))
##        fout.write(Rotate("C48", 90))
##        fout.write(Place("C49", Offset(FPGA, -13, 2.2)))
##        fout.write(Rotate("C49", 90))
##
##        #VCC_1 Bypass
##        fout.write(Place("C50", Offset(FPGA, 2.4, 14)))
##        fout.write(Rotate("C50", 270))
##        fout.write(Place("C51", Offset(FPGA, 7, 12.5)))
##        fout.write(Rotate("C51", 180))
##        fout.write(Place("C52", Offset(FPGA, -6, 13)))
##        fout.write(Rotate("C52", 0))
##
##        #VCC_2 Bypass
##        fout.write(Place("C59", Offset(FPGA, 14.5, -6.5)))
##        fout.write(Rotate("C59", 90))
##        fout.write(Place("C60", Offset(FPGA, 13, -6.5)))
##        fout.write(Rotate("C60", 270))
##        fout.write(Place("C61", Offset(FPGA, 13, 4.5)))
##        fout.write(Rotate("C61", 90))
##
##
##        #VCC_3 Bypass
##        fout.write(Place("C62", Offset(FPGA, 0.9, -18.9)))
##        fout.write(Rotate("C62", 90))
##        fout.write(Place("C63", Offset(FPGA, -7.5, -12.9)))
##        fout.write(Rotate("C63", 180))
##        fout.write(Place("C64", Offset(FPGA, 6.5, -12.9)))
##        fout.write(Rotate("C64", 0))
##
##        #LTC3374 layout
        fout.write("GRID MIL;\n")
        LTC3374 = [2000, 2200] #Offset(FPGA, 30, 0)
        LTCOrig = [2000, 2200]
        fout.write(Place("U$4", LTC3374))
        fout.write(Rotate("U$4", 0))
        #RoundMIL(7.5*MM2MIL)
        fout.write(Place("C4", OffsetFromOrig(LTC3374, LTCOrig, [1790, 2020])))
        fout.write(Rotate("C4", 180))
        fout.write(Place("C21", OffsetFromOrig(LTC3374, LTCOrig, [1970, 1855])))
        fout.write(Rotate("C21", 270))
        fout.write(Place("C6", OffsetFromOrig(LTC3374, LTCOrig, [1585, 1925])))
        fout.write(Rotate("C6", 270))
        fout.write(Place("L3", OffsetFromOrig(LTC3374, LTCOrig, [1770, 1870-20])))
        fout.write(Rotate("L3", 180))

        fout.write(Place("C32", OffsetFromOrig(LTC3374, LTCOrig, [2210,2020])))
        fout.write(Rotate("C32", 0))
        fout.write(Place("C70", OffsetFromOrig(LTC3374, LTCOrig, [2030, 1855])))
        fout.write(Rotate("C70", 270))
        fout.write(Place("C34", OffsetFromOrig(LTC3374, LTCOrig, [2365, 1785])))
        fout.write(Rotate("C34", 270))
        fout.write(Place("L7", OffsetFromOrig(LTC3374, LTCOrig, [2230, 1870])))
        fout.write(Rotate("L7", 0))
        fout.write(Place("L10", OffsetFromOrig(LTC3374, LTCOrig, [2110, 1675])))
        fout.write(Rotate("L10", 270))
        fout.write(Place("C74", OffsetFromOrig(LTC3374, LTCOrig, [2290, 1625])))
        fout.write(Rotate("C74", 0))

        fout.write(Place("C53", OffsetFromOrig(LTC3374, LTCOrig, [2210, 2380])))
        fout.write(Rotate("C53", 0))
        fout.write(Place("C58", OffsetFromOrig(LTC3374, LTCOrig, [2030, 2545])))
        fout.write(Rotate("C58", 90))
        fout.write(Place("C55", OffsetFromOrig(LTC3374, LTCOrig, [2415, 2475])))
        fout.write(Rotate("C55", 270))
        fout.write(Place("L8", OffsetFromOrig(LTC3374, LTCOrig, [2230, 2530+20])))
        fout.write(Rotate("L8", 0))

        fout.write(Place("C65", OffsetFromOrig(LTC3374, LTCOrig, [1790, 2380])))
        fout.write(Rotate("C65", 180))
        fout.write(Place("C1", OffsetFromOrig(LTC3374, LTCOrig, [1970, 2545])))
        fout.write(Rotate("C1", 90))
        fout.write(Place("C67", OffsetFromOrig(LTC3374, LTCOrig, [1635, 2615])))
        fout.write(Rotate("C67", 90))
        fout.write(Place("L9", OffsetFromOrig(LTC3374, LTCOrig, [1770, 2530])))
        fout.write(Rotate("L9", 180))
        fout.write(Place("L1", OffsetFromOrig(LTC3374, LTCOrig, [1890, 2725])))
        fout.write(Rotate("L1", 90))
        fout.write(Place("C3", OffsetFromOrig(LTC3374, LTCOrig, [1710, 2775])))
        fout.write(Rotate("C3", 180))

        fout.write(Place("R17", Offset(LTC3374, -130, -95)))
        fout.write(Rotate("R17", 0, 1))
        fout.write(Place("C5", Offset(LTC3374, -215, -95)))
        fout.write(Rotate("C5", 180, 1))
        fout.write(Place("R15", Offset(LTC3374, -215, -135)))
        fout.write(Rotate("R15", 0, 1))

        fout.write(Place("R20", Offset(LTC3374, 130, -95)))
        fout.write(Rotate("R20", 0, 1))
        fout.write(Place("C33", Offset(LTC3374, 215, -95)))
        fout.write(Rotate("C33", 0, 1))
        fout.write(Place("R19", Offset(LTC3374, 215, -135)))
        fout.write(Rotate("R19", 180, 1))
        fout.write(Place("R33", Offset(LTC3374, 95, -185)))
        fout.write(Rotate("R33", 270, 1))
        fout.write(Place("R31", Offset(LTC3374, 95, -265)))
        fout.write(Rotate("R31", 270, 1))
        fout.write(Place("C71", Offset(LTC3374, 135, -265)))
        fout.write(Rotate("C71", 90, 1))

        fout.write(Place("R24", Offset(LTC3374, 130, 95)))
        fout.write(Rotate("R24", 0, 1))
        fout.write(Place("C54", Offset(LTC3374, 215, 95)))
        fout.write(Rotate("C54", 180, 1))
        fout.write(Place("R21", Offset(LTC3374, 215, 135)))
        fout.write(Rotate("R21", 0, 1))

        fout.write(Place("R29", Offset(LTC3374, -130, 95)))
        fout.write(Rotate("R29", 0, 1))
        fout.write(Place("C66", Offset(LTC3374, -215, 95)))
        fout.write(Rotate("C66", 180, 1))
        fout.write(Place("R27", Offset(LTC3374, -215, 135)))
        fout.write(Rotate("R27", 0, 1))
        fout.write(Place("R11", Offset(LTC3374, -95, 185)))
        fout.write(Rotate("R11", 90, 1))
        fout.write(Place("R10", Offset(LTC3374, -95, 265)))
        fout.write(Rotate("R10", 90, 1))
        fout.write(Place("C2", Offset(LTC3374, -135, 265)))
        fout.write(Rotate("C2", 270, 1))

        #VCC Cap
        fout.write(Place("C18", Offset(LTC3374, -295, 20)))
        fout.write(Rotate("C18", 180))

        #write wires
        fout.write("SET WIRE_BEND 2;\n")
        l = [[1890.16, 2100.98],[1855.98, 2100.98],[1846, 2091], [1846, 2065]]
        fout.write(Wire(LTC3374, LTCOrig, 'S1FB', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S5FB', 10, l))

        l = [[1911.42, 2100.98],[1911.42, 2050], [1897.42, 2036], [1894.5, 2033.08], [1881.42, 2020], [1821.5, 2020]]
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 10, l))

        #[1920.55, 2015]]
        a = (1931.1 + 1950.79)/2
        l = [[1931.1, 2100.98], [1931.1, 2070]]
        fout.write(Wire(LTC3374, LTCOrig, 'S1SW', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S5SW', 10, l))

        l = [[1950.79, 2100.98], [1950.79, 2070]]
        fout.write(Wire(LTC3374, LTCOrig, 'S1SW', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S5SW', 10, l))

        l = [[a, 2070], [a, 2015]]
        fout.write(Wire(LTC3374, LTCOrig, 'S1SW', 25, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S5SW', 25, l))

        l = [[1940-4, 2015-4], [1860, 1935], [1860, 1895]]
        fout.write(Wire(LTC3374, LTCOrig, 'S1SW', 35, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S5SW', 35, l))

        l = [[1970.47, 2100.98], [1970.47, 1973.47], [1956, 1959], [1956, 1906]]
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 12, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 12, l))

        l = [[1990.16, 2100.98], [1990.16, 2080], [1970.47, 2080 - (1990.16 - 1970.47)]]
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 10, l))


        l = [[2009.84,2100.98], [2009.84, 1945]]
        fout.write(Wire(LTC3374, LTCOrig, 'S3FB', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S7FB', 10, l))

        l = [[2029.53, 2100.98], [2029.53, 1975], [2044, 1960.53], [2044, 1906]]
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 12, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 12, l))

        l = [[2049.21, 2100.98], [2049.21, 1994], [2054.61, 1988.61]]
        fout.write(Wire(LTC3374, LTCOrig, 'S3SW', 12, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S7SW', 12, l))

        l = [[2054.61, 1988.61], [2110, 1933.21], [2110, 1912.21]]
        fout.write(Wire(LTC3374, LTCOrig, 'S3SW', 25, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S7SW', 25, l))

        l = [[2110, 1912.21], [2110, 1724.61]]
        fout.write(Wire(LTC3374, LTCOrig, 'S3SW', 30, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S7SW', 30, l))

        l = [[2068.9, 2100.98], [2068.9, 2026.55], [2079.45, 2016]]
        fout.write(Wire(LTC3374, LTCOrig, 'S4SW', 12, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S8SW', 12, l))

        l = [[2079.45, 2016], [2173.9, 1922], [2173.9, 1872]]
        fout.write(Wire(LTC3374, LTCOrig, 'S4SW', 25, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S8SW', 25, l))

        l = [[2088.58, 2100.98], [2088.58, 2050.42], [2103, 2036], [2109, 2030], [2180, 2030]]
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'VIN', 10, l))

        l = [[2109.86, 2101], [2145, 2101], [2155, 2091], [2155, 2065]]
        fout.write(Wire(LTC3374, LTCOrig, 'S4FB', 10, l))
        FlipL(LTCOrig, l)
        fout.write(Wire(LTC3374, LTCOrig, 'S8FB', 10, l))

        #Write vias
        fout.write("CHANGE DRILL 10mil;\n")
        l = [[1846, 2065]]
        fout.write(Via(LTC3374, LTCOrig, "S1FB", l))
        FlipL(LTCOrig, l)
        fout.write(Via(LTC3374, LTCOrig, "S5FB", l))

        l = [[1810, 1990], [1839, 1990], [1940, 1895], [1940, 1870], [2060, 1870], [2060, 1895], [2165, 1990], [2190, 1990]]
        fout.write(Via(LTC3374, LTCOrig, "VIN", l))
        FlipL(LTCOrig, l)
        fout.write(Via(LTC3374, LTCOrig, "VIN", l))

        #all gnd vias
        l = [[1725, 2025], [1725, 2000], [1545, 1965], [1545, 1995], [1625, 1965], [1625, 1995], [1940, 1830], [1940, 1800], [2000, 1800], [2060, 1830], [2060, 1800],
             [2330, 1665], [2360, 1665], [2330, 1585], [2360, 1585], [2325, 1745], [2325, 1720], [2405, 1720], [2405, 1745], [2275, 2025], [2275, 2000]]
        fout.write(Via(LTC3374, LTCOrig, "GND", l))
        FlipL(LTCOrig, l)
        fout.write(Via(LTC3374, LTCOrig, "GND", l))

        l = [[2009.84, 1945]]
        fout.write(Via(LTC3374, LTCOrig, "S3FB", l))
        FlipL(LTCOrig, l)
        fout.write(Via(LTC3374, LTCOrig, "S7FB", l))

        l = [[2155, 2065]]
        fout.write(Via(LTC3374, LTCOrig, "S4FB", l))
        FlipL(LTCOrig, l)
        fout.write(Via(LTC3374, LTCOrig, "S8FB", l))


        fout.write("Ratsnest;")
        fout.flush()


def main():
    adcLoc = [20, 50]
    fpgaLoc = [65, 51]
    PlaceCaps()

if __name__ == '__main__':
    main()
