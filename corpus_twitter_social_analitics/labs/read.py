import sys

foa = open("emo_amo", "r")
fof = open("emo_feliz", "r")
fom = open("emo_miedo", "r")
fot = open("emo_triste", "r")

txt=[]
stt=""
for i in foa.readlines():
	stt+=i
txt.append(stt)
stt=""
for i in fof.readlines():
        stt+=i
txt.append(stt)
stt=""
for i in fom.readlines():
        stt+=i
txt.append(stt)
stt=""
for i in fot.readlines():
        stt+=i
txt.append(stt)
stt=""

print len(txt)
