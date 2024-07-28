import win32com.client

def speak(text):
    
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    speaker.Speak(text)
    
speak("Hello, welcome to this virtual assistant!")
