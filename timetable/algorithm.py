# -*- coding: utf-8 -*-
"""Time table automation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CMZII-7q-BiPwQCS-uiTeThCJxPVeLmg
"""

def syllabus():
    """ Store syllabus for particular semester here """
    # syllabus for 2nd semester
    lab3 = ["CSEN1021"]    # which labs which have 6hr 
    lab2 = ["LANG1001","MECH1001"]  # which labs which have 4hr 
    lab1 = ["CHEM1001P","EECE1001P","CLAD1041"] # which labs which have 2hr 
    the1 = []
    the2 = ["MATH1041", "MATH1051"]
    the3 = ["EECE1001", "CHEM1001"]
    the4 = []

def get_rcode(a):
    """Get remaining codes."""
    nob = ["B", 0, "TB", 0]
    noc = ["C", 0, "TC", 0]
    nod = ["D", 0, "TD", 0]
    noe = ["E", 0, "TE", 0]
    nof = ["F", 0, "TF", 0]
    nog = ["G", 0, "TG", 0]
    noh = ["H", 0, "TH", 0]
    noi = ["I", 0, "TI", 0]
    for i in range(0,5):
        for j in range (0,8):
            if len(a[i][j]) == 2 or len(a[i][j]) == 3 or len(a[i][j]) == 4 :
                if a[i][j][0]=='B':
                    nob[1] = nob[1]+1
                if a[i][j][0]=='C':
                    noc[1] = noc[1]+1
                if a[i][j][0]=='D':
                    nod[1] = nod[1]+1
                if a[i][j][0]=='E':
                    noe[1] = noe[1]+1
                if a[i][j][0]=='F':
                    nof[1] = nof[1]+1
                if a[i][j][0]=='G':
                    nog[1] = nog[1]+1
                if a[i][j][0]=='H':
                    noh[1] = noh[1]+1
                if a[i][j][0]=='I':
                    noi[1] = noi[1]+1
                if a[i][j][0:2] == 'TB':
                    nob[3] = nob[3] + 1
                if a[i][j][0:2] == 'TC':
                    noc[3] = noc[3] + 1
                if a[i][j][0:2] == 'TD':
                    nod[3] = nod[3] + 1
                if a[i][j][0:2] == 'TE':
                    noe[3] = noe[3] + 1
                if a[i][j][0:2] == 'TF':
                    nof[3] = nof[3] + 1
                if a[i][j][0:2] == 'TG':
                    nog[3] = nog[3] + 1
                if a[i][j][0:2] == 'TH':
                    noh[3] = noh[3] + 1
                if a[i][j][0:2] == 'TI':
                    noi[3] = noi[3] + 1
    list = [nob, noc, nod, noe, nof, nog, noh, noi]
    return list

def main(sets):
    # number of sets requried
    nos=sets
    # syllabus for 2nd semester
    lab3 = ["CSEN1021"]    # which labs which have 6hr 
    lab2 = ["LANG1001","MECH1001"]  # which labs which have 4hr 
    lab1 = ["CHEM1001P","EECE1001P","CLAD1041"] # which labs which have 2hr 
    the1 = []
    the2 = ["MATH1041", "MATH1051"]
    the3 = ["EECE1001", "CHEM1001"]
    the4 = []
    lk = 0  # just a random initialisation

    for cg in range (0,nos):
        if cg == 0:
            sks1 = {
            }
            tts1 = [["B1","C1","D1","E1","F1","G1","TH1","TI1"],["H1","I1","G2","TF12","TE12","TD12","TB1","TC1"],["C2","B2","D2","E2","F2","TG11","Student Life","Student Life"],["H2","I2","G3","TF11","TE11","TD11","C3","B3"],["I3","H3","D3","E3","F3","TG12","Student Life","Student Life"]]
            theon = []
            for j in range(0, len(the1)):
                theon.append(the1[j])
            thetw = []
            for j in range(0, len(the2)):
                thetw.append(the2[j])
            theth = []
            for j in range(0, len(the3)):
                theth.append(the3[j])
            thefo = []
            for j in range(0, len(the4)):
                thefo.append(the4[j])
            tts1[0][6] = lab3[0]
            tts1[0][7] = lab3[0]
            tts1[1][2] = lab3[0]
            tts1[1][3] = lab3[0]
            tts1[3][0] = lab3[0]
            tts1[3][1] = lab3[0]
            sks1["L4"] = lab3[0]
            sks1["L6"] = lab3[0]
            sks1["L12"] = lab3[0]
            tts1[1][6] = lab2[0]
            tts1[1][7] = lab2[0]
            tts1[3][6] = lab2[0]
            tts1[3][7] = lab2[0]
            sks1["L8"] = lab2[0]
            sks1["L15"] = lab2[0]
            tts1[2][4] = lab2[1]
            tts1[2][5] = lab2[1]
            tts1[4][0] = lab2[1]
            tts1[4][1] = lab2[1]
            sks1["L11"] = lab2[1]
            sks1["L16"] = lab2[1]
            tts1[0][0] = lab1[0]
            tts1[0][1] = lab1[0]
            sks1["L7"] = lab1[0]
            tts1[4][4] = lab1[1]
            tts1[4][5] = lab1[1]
            sks1["L18"] = lab1[1]
            tts1[3][4] = lab1[2]
            tts1[3][5] = lab1[2]
            sks1["L14"] = lab1[2]
            for i in range(0, 5):
                if len(tts1[i][4]) == 2 or len(tts1[i][4]) == 3 or (
                        len(tts1[i][4]) == 4 and (tts1[i][4] != "CLAD" and tts1[i][4] != "LANG")):
                    tts1[i][4] = "LUNCH"
                else:
                    tts1[i][3] = "LUNCH"
            lists1 = get_rcode(tts1)
            if 3 or 2 in lists1:
                for i in range(0, len(lists1)):
                    if len(theth) > 0:
                        if lists1[i][1] == 3:
                            sks1[lists1[i][0]] = theth[lk]
                            del theth[lk]
                            lists1[i][1] = 0
                        elif lists1[i][1] + lists1[i][3] == 3:
                            sks1[lists1[i][0]] = theth[lk]
                            sks1[lists1[i][2]] = theth[lk]
                            del theth[lk]
                            lists1[i][1] = lists1[i][3] = 0
                    if len(thetw) > 0:
                        if lists1[i][1] == 2:
                            sks1[lists1[i][0]] = thetw[lk]
                            del thetw[lk]
                            lists1[i][1] = 0
                        elif lists1[i][1] + lists1[i][3] == 2:
                            sks1[lists1[i][0]] = thetw[lk]
                            sks1[lists1[i][2]] = thetw[lk]
                            del thetw[lk]
                            lists1[i][1] = lists1[i][3] = 0
                    if len(theon) > 0:
                        if lists1[i][1] == 1:
                            sks1[lists1[i][0]] = theon[lk]
                            del theon[lk]
                            lists1[i][1] = 0
            
            # returning set 1
            return sks1
            # print("\n")
        if cg == 1:
            sks2 = {
            }
            tts2 = [["B1","C1","D1","E1","F1","G1","TH1","TI1"],["H1","I1","G2","TF12","TE12","TD12","TB1","TC1"],["C2","B2","D2","E2","F2","TG11","Student Life","Student Life"],["H2","I2","G3","TF11","TE11","TD11","C3","B3"],["I3","H3","D3","E3","F3","TG12","Student Life","Student Life"]]
            theon = []
            for j in range(0, len(the1)):
                theon.append(the1[j])
            thetw = []
            for j in range(0, len(the2)):
                thetw.append(the2[j])
            theth = []
            for j in range(0, len(the3)):
                theth.append(the3[j])
            thefo = []
            for j in range(0, len(the4)):
                thefo.append(the4[j])
            tts2[0][2] = lab3[0]
            tts2[0][3] = lab3[0]
            tts2[2][2] = lab3[0]
            tts2[2][3] = lab3[0]
            tts2[4][2] = lab3[0]
            tts2[4][3] = lab3[0]
            sks2["L2"] = lab3[0]
            sks2["L10"] = lab3[0]
            sks2["L17"] = lab3[0]
            tts2[1][2] = lab2[0]
            tts2[1][3] = lab2[0]
            tts2[3][2] = lab2[0]
            tts2[3][3] = lab2[0]
            sks2["L6"] = lab2[0]
            sks2["L13"] = lab2[0]
            tts2[0][0] = lab2[1]
            tts2[0][1] = lab2[1]
            tts2[2][0] = lab2[1]
            tts2[2][1] = lab2[1]
            sks2["L1"] = lab2[1]
            sks2["L9"] = lab2[1]
            tts2[3][6] = lab1[0]
            tts2[3][7] = lab1[0]
            sks2["L15"] = lab1[0]
            tts2[1][6] = lab1[1]
            tts2[1][7] = lab1[1]
            sks2["L8"] = lab1[1]
            tts2[1][0] = lab1[2]
            tts2[1][1] = lab1[2]
            sks2["L5"] = lab1[2]
            for i in range(0, 5):
                if len(tts2[i][4]) == 2 or len(tts2[i][4]) == 3 or (
                        len(tts2[i][4]) == 4 and (tts2[i][4] != "CLAD" and tts2[i][4] != "LANG")):
                    tts2[i][4] = "LUNCH"
                else:
                    tts2[i][3] = "LUNCH"
            lists2 = get_rcode(tts2)
            if 3 or 2 in lists2:
                for i in range(0, len(lists2)):
                    if len(theth) > 0:
                        if lists2[i][1] == 3:
                            sks2[lists2[i][0]] = theth[lk]
                            del theth[lk]
                            lists2[i][1] = 0
                        elif lists2[i][1] + lists2[i][3] == 3:
                            sks2[lists2[i][0]] = theth[lk]
                            sks2[lists2[i][2]] = theth[lk]
                            del theth[lk]
                            lists2[i][1] = lists2[i][3] = 0
                    if len(thetw) > 0:
                        if lists2[i][1] == 2:
                            sks2[lists2[i][0]] = thetw[lk]
                            del thetw[lk]
                            lists2[i][1] = 0
                        elif lists2[i][1] + lists2[i][3] == 2:
                            sks2[lists2[i][0]] = thetw[lk]
                            sks2[lists2[i][2]] = thetw[lk]
                            del thetw[lk]
                            lists2[i][1] = lists2[i][3] = 0
            #print(sks2)
            print("\n")
        if cg == 2:
            sks3 = {
            }
            tts3 = [["B1","C1","D1","E1","F1","G1","TH1","TI1"],["H1","I1","G2","TF12","TE12","TD12","TB1","TC1"],["C2","B2","D2","E2","F2","TG11","Student Life","Student Life"],["H2","I2","G3","TF11","TE11","TD11","C3","B3"],["I3","H3","D3","E3","F3","TG12","Student Life","Student Life"]]
            theon = []
            for j in range(0, len(the1)):
                theon.append(the1[j])
            thetw = []
            for j in range(0, len(the2)):
                thetw.append(the2[j])
            theth = []
            for j in range(0, len(the3)):
                theth.append(the3[j])
            thefo = []
            for j in range(0, len(the4)):
                thefo.append(the4[j])
            tts3[0][4] = lab3[0]
            tts3[0][5] = lab3[0]
            tts3[2][4] = lab3[0]
            tts3[2][5] = lab3[0]
            tts3[4][4] = lab3[0]
            tts3[4][5] = lab3[0]
            sks3["L3"] = lab3[0]
            sks3["L11"] = lab3[0]
            sks3["L18"] = lab3[0]
            tts3[0][0] = lab2[0]
            tts3[0][1] = lab2[0]
            tts3[2][0] = lab2[0]
            tts3[2][1] = lab2[0]
            sks3["L1"] = lab2[0]
            sks3["L9"] = lab2[0]
            tts3[1][6] = lab2[1]
            tts3[1][7] = lab2[1]
            tts3[3][6] = lab2[1]
            tts3[3][7] = lab2[1]
            sks3["L8"] = lab2[1]
            sks3["L15"] = lab2[1]
            tts3[3][2] = lab1[0]
            tts3[3][3] = lab1[0]
            sks3["L13"] = lab1[0]
            tts3[4][0] = lab1[1]
            tts3[4][1] = lab1[1]
            sks3["L16"] = lab1[1]
            tts3[1][4] = lab1[2]
            tts3[1][5] = lab1[2]
            sks3["L7"] = lab1[2]
            for i in range(0, 5):
                if len(tts3[i][4]) == 2 or len(tts3[i][4]) == 3 or (
                        len(tts3[i][4]) == 4 and (tts3[i][4] != "CLAD" and tts3[i][4] != "LANG")):
                    tts3[i][4] = "LUNCH"
                else:
                    tts3[i][3] = "LUNCH"
            lists3 = get_rcode(tts3)
            if 3 or 2 in lists3:
                for i in range(0, len(lists3)):
                    if len(theth) > 0:
                        if lists3[i][1] == 3:
                            sks3[lists3[i][0]] = theth[lk]
                            del theth[lk]
                            lists3[i][1] = 0
                        elif lists3[i][1] + lists3[i][3] == 3:
                            sks3[lists3[i][0]] = theth[lk]
                            sks3[lists3[i][2]] = theth[lk]
                            del theth[lk]
                            lists3[i][1] = lists3[i][3] = 0
                    if len(thetw) > 0:
                        if lists3[i][1] == 2:
                            sks3[lists3[i][0]] = thetw[lk]
                            del thetw[lk]
                            lists3[i][1] = 0
                        elif lists3[i][1] + lists3[i][3] == 2:
                            sks3[lists3[i][0]] = thetw[lk]
                            sks3[lists3[i][2]] = thetw[lk]
                            del thetw[lk]
                            lists3[i][1] = lists3[i][3] = 0
            #print(sks3)
            #print("\n")
        if cg == 3:
            sks4 = {
            }
            tts4 = [["B1","C1","D1","E1","F1","G1","TH1","TI1"],["H1","I1","G2","TF12","TE12","TD12","TB1","TC1"],["C2","B2","D2","E2","F2","TG11","Student Life","Student Life"],["H2","I2","G3","TF11","TE11","TD11","C3","B3"],["I3","H3","D3","E3","F3","TG12","Student Life","Student Life"]]
            theon = []
            for j in range(0, len(the1)):
                theon.append(the1[j])
            thetw = []
            for j in range(0, len(the2)):
                thetw.append(the2[j])
            theth = []
            for j in range(0, len(the3)):
                theth.append(the3[j])
            thefo = []
            for j in range(0, len(the4)):
                thefo.append(the4[j])
            tts4[0][0] = lab3[0]
            tts4[0][1] = lab3[0]
            tts4[1][6] = lab3[0]
            tts4[1][7] = lab3[0]
            tts4[3][6] = lab3[0]
            tts4[3][7] = lab3[0]
            sks4["L1"] = lab3[0]
            sks4["L8"] = lab3[0]
            sks4["L15"] = lab3[0]
            tts4[1][0] = lab2[0]
            tts4[1][1] = lab2[0]
            tts4[3][0] = lab2[0]
            tts4[3][1] = lab2[0]
            sks4["L5"] = lab2[0]
            sks4["L12"] = lab2[0]
            tts4[1][2] = lab2[1]
            tts4[1][3] = lab2[1]
            tts4[3][2] = lab2[1]
            tts4[3][3] = lab2[1]
            sks4["L6"] = lab2[1]
            sks4["L13"] = lab2[1]
            tts4[0][6] = lab1[0]
            tts4[0][7] = lab1[0]
            sks4["L4"] = lab1[0]
            tts4[2][0] = lab1[1]
            tts4[2][1] = lab1[1]
            sks4["L9"] = lab1[1]
            tts4[4][0] = lab1[2]
            tts4[4][1] = lab1[2]
            sks4["L16"] = lab1[2]
            for i in range(0, 5):
                if len(tts4[i][4]) == 2 or len(tts4[i][4]) == 3 or (len(tts4[i][4]) == 4 and (tts4[i][4] != "CLAD" and tts4[i][4] != "LANG")) :
                    tts4[i][4] = "LUNCH"
                else:
                    tts4[i][3] = "LUNCH"
            lists4 = get_rcode(tts3)
            if 3 or 2 in lists4:
                for i in range(0, len(lists4)):
                    if len(theth) > 0:
                        if lists4[i][1] == 3:
                            sks4[lists4[i][0]] = theth[lk]
                            del theth[lk]
                            lists4[i][1] = 0
                        elif lists4[i][1] + lists4[i][3] == 3:
                            sks4[lists4[i][0]] = theth[lk]
                            sks4[lists4[i][2]] = theth[lk]
                            del theth[lk]
                            lists4[i][1] = lists4[i][3] = 0
                    if len(thetw) > 0:
                        if lists4[i][1] == 2:
                            sks4[lists4[i][0]] = thetw[lk]
                            del thetw[lk]
                            lists4[i][1] = 0
                        elif lists4[i][1] + lists4[i][3] == 2:
                            sks4[lists4[i][0]] = thetw[lk]
                            sks4[lists4[i][2]] = thetw[lk]
                            del thetw[lk]
                            lists4[i][1] = lists4[i][3] = 0
            print(sks4)
            print("\n")