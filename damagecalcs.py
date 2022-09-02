import math

job = 115
LvMAIN = 390
LvSUB = 400
LvDIV = 1900
Trait = 130
buff_1 = 1.2
buff_2 = 1
WD = 126
M = 195
TNC = 400
Potency = [260,310,310,310,310,310,310,500,340,260,310,760]
buff_2 = [0.7,1.8,1.8,1.8,1.8,1.8,1.8,1.8,1.8,0.7,1,1]
  

def damagecalcs(AP,DH,CRIT,DET,Speed):
  dam=0
  fWD = math.floor((LvMAIN*job/1000)+WD)
  fATK = math.floor(M*(AP-390)/390)+100
  fSPD = (1000+math.floor(130*(Speed-LvSUB)/LvDIV))/1000
  fTNC = 1000+math.floor(100*(TNC-LvSUB)/LvDIV)
  #fGCD = math.floor(((GCD*(1000+math.ceiling(130*(LvSUB-Speed)/LvDIV)))/10000)/100)
  fDET = math.floor(140*(DET-LvMAIN)/LvDIV+1000)
  fCRIT = 1400+math.floor(200*(CRIT-LvSUB)/LvDIV)
  
  pDH = math.floor(550*(DH-LvSUB)/LvDIV)/10
  pCRIT = math.floor(200*(CRIT-LvSUB)/LvDIV+50)/10
  
  CRITS = ((100-pCRIT)/100)*1000+(pCRIT*fCRIT)
  DHS = ((100-pDH)/100)*100+(pDH*125)


  def Damage(Potency,buff_2):
    D1 = math.floor(math.floor(math.floor(Potency*fATK*fDET)/100)/1000)
    D2 = math.floor(math.floor(math.floor(math.floor(math.floor(math.floor(math.floor(D1*fTNC))/1000)*fWD)/100)*Trait)/100)
    D3 = math.floor(math.floor(math.floor(math.floor(D2*CRITS)/1000)*DHS)/100)
    D = math.floor(math.floor(math.floor(math.floor(D3*100)/100)*buff_1)*buff_2) #technically D3*1 is supposed to be *math.rand(95,105) but for simulation's sake we're negating that

#CRIT?: If you do not critical hit, CRIT? = 1000. If you critical hit, CRIT? = f(CRIT).
#DH?: If you do not direct hit, DH? = 100. If you direct hit, DH? = 125
    return D

  def Damage_overtime(Potency):
    D1 = math.floor(math.floor(math.floor(math.floor(math.floor(math.floor(Potency*fWD)/100)*fATK)/100)*fSPD) /1000)
    D2 = math.floor(math.floor(math.floor(math.floor(math.floor(math.floor(D1*fDET)/1000)*fTNC)/1000)*Trait)/100)+1
    D3 = math.floor(math.floor(D2*100)/100)  #technically D2*1 is supposed to be *math.rand(95,105) but for simulation's sake we're negating that
    D = math.floor(math.floor(math.floor(math.floor(math.floor(math.floor(D3*CRITS)/1000)*DHS)/100)*buff_1)*1)
    return D
  #Add in following for calculation:
  # 1 standard BLM rotation: F3, F4x6, PDX, DSP, B3, B4, XG
  # 1 full T3 DOT
  # Add together for relative result?
  
  for i,j in zip(Potency,buff_2):
    d=Damage(i,j)
    dam=dam+d

  d=Damage_overtime(35)*10
  dam=dam+d
  
  return(dam)