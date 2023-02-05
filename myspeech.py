import speech_recognition as sr
#ECE 331 Project by Engr Peace
r = sr.Recognizer()
print("Recognising my speech...")

harvard = sr.AudioFile('kossi.wav')
with harvard as source:
    audio = r.record(source)
    
    type(audio)
    
    r.recognize_google(audio)
    
    print("Ending my speech Recognition..")
    
    
    
    
  #Speech To Text Program  