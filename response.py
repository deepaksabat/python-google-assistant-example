import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import speek

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
text = r.recognize_google(audio)
lang = 'en'
speek.tts(text, lang)

url = "https://www.google.co.in/search?q=" + text

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
for item in soup.select(".r a"):
    f_url = item.get('href')
    myurl = f_url.replace(f_url[:7], '')
    myurl = myurl.split('&')
    myurl = myurl[0]
    print(myurl)
    break

print ('Searching from:\n' + myurl)
# myurl = 'http://www.desy.de/user/projects/Physics/Relativity/SR/light_mass.html'
f_response = requests.get(myurl)
f_soup = BeautifulSoup(f_response.text,"lxml")

for item in f_soup.find_all('p'):
	raw_text = item
	break

text = raw_text.getText()
print(text)
speek.tts(text, lang)

# print (f_soup.get_text())
