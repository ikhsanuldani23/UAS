import requests,re
reqlist = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()
cari = input("masukkan nama provinsi : ")
for x in reqlist:
	a = re.search(cari,x['attributes']['Provinsi'].lower())
	if a!=None:
		print("\n"+x['attributes']['Provinsi']+"\nterdeteksi \t: "+str(x['attributes']['Kasus_Posi'])+"\nmati \t\t: "+str(x['attributes']['Kasus_Meni'])+"\nsembuh \t\t: "+str(x['attributes']['Kasus_Semb'])+"\nsakit \t\t: "+str(x['attributes']['Kasus_Posi']-x['attributes']['Kasus_Meni']-x['attributes']['Kasus_Semb']))
