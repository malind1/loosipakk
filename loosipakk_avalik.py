##Mari-Ann Lind
##Katrin Linno

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Oled sisenenud loosipaki keskkonda.")
kingi_suurus = 0
while True: #kontrollib, et sisestatud väärtus oleks number
  try:
     kingi_suurus = int(input("Palun sisestage kingi suurus eurodes: "))       
  except ValueError:
     print("Sisestatud väärtus ei ole arv! Palun sisesta täisarv!")
     continue
  else:
     break #kui väärtus on number, siis liigub järgmise etapi juurde

print("Sisestage vähemalt 2 inimese nimed ja e-posti aadressid.")

while True: #kontrollib, et väärtus oleks kas "jah" või "ei"
    andmed = input("Kas soovid sisestada nimed ja e-posti aadressid failist? [Jah/Ei]: ")
    if andmed.lower() == 'jah':
        break
    elif andmed.lower() == 'ei':
        break
    else:
        print('Palun vastake, kas "Jah" või "Ei"')

def andmesisestus():
    global osalejad
    if andmed.lower() == 'jah':
        failinimi = input("Palun sisestage failinimi: ")
        fail = open(failinimi, encoding="UTF-8")
        # alustame tühja listiga
        osalejad = []
        for rida in fail:
            rida = rida.strip() #annab järjendid ilma reavahetuse märgita
            osalejad += [rida.split(', ')] #listi elemendid on komaga eraldatud
        fail.close()

    elif andmed.lower() == 'ei':
        # alustame tühja listiga
        osalejad = []
        while True:
            nimi = input("Sisesta inimese nimi (lõpetamiseks jäta tühjaks): ")
            if nimi == "":
                break
            email = input("Sisesta e-mail: ")
            sub_list=[]
            sub_list.append(nimi)
            sub_list.append(email)
            osalejad.append(sub_list)

andmesisestus()

while True:
    if len(osalejad) < 2:
        print("Sisestama peab vähemalt 2 osalejat! Sisesta kõik osalejad uuesti.")
        andmesisestus()
    else:
        break

osalejad.sort()
       
def sulgudeta(list):  #listi kuvamine ilma sulgudeta
    for i in range(len(list)):  #kõigepealt järjend kõigi elementidega
        for j in range(len(list[i])): 
            if j < len(list[i])-1:  #järjend ilma viimase elemendita, et viimase elemendi lõppu ei jääks kooloneid
                print(list[i][j], end=': ')
        else:
            print(list[i][j])
    return

sulgudeta(osalejad)

# sisestatud nimede kontrollimine
while True:
    kontroll = str(input("Kas kõik nimed on korrektsed? [Jah/Ei]: "))
    if kontroll.lower() == "jah":
        break
    nimi = str(input("Sisesta isiku täisnimi, kelle nime soovid parandada: "))
    
    #kui nime ei ole listis, siis märkus, et sisesta uuesti
    uus_list1=[] #nime indeksi leidmiseks teen uue listi nimede jaoks
    for i in osalejad:
        uus_list1.append(i[0])
    try:
        asukoht=uus_list1.index(nimi) #sisestatud nime indekseerimine järjendis
    except:
        asukoht=i
        print("Sellist nime ei ole nimekirjas! Sisestatud nimed: " + str(uus_list1).replace('[','').replace(']','').replace("'",''))
        while nimi not in uus_list1:
            nimi = str(input("Proovi uuesti: "))           
        else:
            uus_nimi = input("Sisesta õige nimi: ")
            asukoht=uus_list1.index(nimi)
            osalejad[asukoht][0] = uus_nimi
            print("Uuendatud osalejate nimekiri:")
            sulgudeta(osalejad)
    else:
        uus_nimi = input("Sisesta õige nimi: ")
        osalejad[asukoht][0] = uus_nimi
        print("Uuendatud osalejate nimekiri:")
        sulgudeta(osalejad)
    

#sisestatud e-mailide kontrollimine
while True:
    kontroll = str(input("Kas kõik e-mailid on korrektsed? [Jah/Ei]: "))
    if kontroll.lower() == "jah":
        break #kui kõik sisestatud nimed on õiged, siis programm ei liigub e-maili muutmisest edasi
    nimi = str(input("Sisesta isiku täisnimi, kelle e-maili soovid parandada: "))
    uus_list2=[] #nime indeksi leidmiseks teen uue listi nimede jaoks   
    for i in osalejad:
        uus_list2.append(i[0]) 
    try:
        asukoht=uus_list2.index(nimi) #sisestatud nime indekseerimine järjendis
    except:
        asukoht=i
        print("Sellist nime ei ole nimekirjas! Sisestatud nimed: " + str(uus_list2).replace('[','').replace(']','').replace("'",''))
        while nimi not in uus_list2: #kui sisestatud nime ei ole nimekirjas, siis tsükkel jätkab tööd, kuni sisestatakse õige nimi
            nimi = str(input("Proovi uuesti: "))
        else:
            uus_email = input("Sisesta õige e-mail: ")
            asukoht=uus_list2.index(nimi)
            osalejad[asukoht][1] = uus_email
            print("Uuendatud osalejate nimekiri:")
            sulgudeta(osalejad)
    else:
        uus_email = input("Sisesta õige e-mail: ") #varem sisestatud e-mail asendadatakse uuega
        osalejad[asukoht][1] = uus_email
        print("Uuendatud osalejate nimekiri:")
        sulgudeta(osalejad)

################################################################################
    ##############LOOSIMINE###########################################
 
osalejate_nr=[] # tehakse list, mis koosneb ainult osalejate järjekorranumbritest
loendaja=1 #listi elemendi indeksi jaoks
for i in range(len(osalejad)):
    osalejate_nr.append(loendaja) #lisab järjekorra nr listi numbri
    loendaja +=1

def paki_unikaalsus():
    global kellele_pakk 
    kellele_pakk = random.sample(osalejate_nr,len(osalejate_nr)) # teeb uue listi, mille elemendid on samad kui listis osalejate_nr, ainult et juhuslikus järjekorras
    for i in range(len(osalejate_nr)): 
        if osalejate_nr[i] == kellele_pakk[i]: #kontrollib ega keegi iseendale pakki ei tee
            return False
    return kellele_pakk #kui keegi isendale pakki ei tee, väljastatakse list numbritega kellele peab tegema paki


while paki_unikaalsus() == False: #kutsub funktsiooni välja seniakaua kuni, keegi loosis iseennast ei saa
    paki_unikaalsus()
    
loendaja=0
for i in range(len(osalejad)): #lisab osalejate listi iga inimese alalisti kellele see inimene peab paki tegema
    for j in range(1): # sisemise listi struktuur: [nimi, meiliaadress, järjekorra nr, inimese nr kellele peab paki tegema]
        osalejad[i].append(kellele_pakk[loendaja])
        loendaja +=1

#####################################################################
        ############# E-MAILI SAATMINE ###########################
        
loendaja=0    
while loendaja<len(osalejad):
    for i in range(len(osalejad)):
        pakk_teha = osalejad[i][2]
    
        fromaddr = "loosipakk@gmail.com" # meiliaadress millelt kirjad välja saadetakse
        toaddr = osalejad[i][1]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Loosipaki tegemine" 
        body = ("Tere, " + osalejad[i][0] + "!\n" + "Sina teed jõulupaki isikule: " + osalejad[pakk_teha-1][0] + ".\n" +  "Tervitades \n Mr. Loosipaki Robot \n" + "P.S. ära vasta sellele kirjale!")
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "*******") #Asendada õige parooliga. Parooli saab programmi loojatele kirjutades. 
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        loendaja+=1

print("E-kirjad on teele saadetud. Ilusat jõuluaega!")