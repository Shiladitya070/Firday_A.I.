'''
This My First A.I projet 
Name : Friday 
Developer : Shiladitya das
Version : 2.0
'''
import pyttsx3,datetime,wikipedia,webbrowser,os,smtplib
import tkinter 

# ----------setting the voice of the assistent---------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[0].id) #voice depends on the voices available in the system 

b = open('Conversation.txt','a+') 
# conversation.txt is a file that records the conversation with friday
b.write('\n')
today = str(datetime.date.today()) 
Time_now = datetime.datetime.now().strftime('%H:%M:%S')
print(f"todays's date:{today} Time : {Time_now}")
b.write('----------' + today + ' time:' + Time_now +'----------' '\n')

def speak(audio):
    #this is the speak method for the assistant 
    b.write(audio + '\n')
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    #it checks the time and wish you accordind to time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak('good morning sir')
    elif hour >=12 and hour <18:
        speak('good afternoon sir')
    else:
        speak('good evening sir')
    speak('Hello sir.')
def sendEmail(to,content):
    #it helps you to send emails 
    addr = str(input('Enter your email id:'))
    password = str(input('password: '))
    sever = smtplib.SMTP('smtp.gmail.com',587)
    sever.ehlo()
    sever.starttls()
    sever.login(addr,password)
    sever.sendmail(addr,to,content)
    sever.close()

if __name__ == "__main__":
     WishMe()
     act = True
     speak('I am Friday')
     speak('how can i help you')
     while act:
        query = str(input()).lower()
        b.write(query + '\n')

        if "wikipedia" in query:
            #it helps to search wikipedia for a subject
            try:
                speak('searching wikipedia..')
                query = query.replace('wikipedia','')
                result = wikipedia.summary(query, sentences = 3)
                speak('according to wikipedia')
                speak(result)
            except Exception as e:
                # print(e)
                speak('Sorry i can not found that ')
                speak('try again')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            Playing_Music = True
            music_dir = 'E:\\Old Songs'
            songs = os.listdir(music_dir)
            # print(songs)
            try:
                os.startfile(os.path.join(music_dir,songs[0]))
            except Exception as e:
                speak('path does not exsits')
        elif 'time' and 'now' in query:
            Time_now = datetime.datetime.now().strftime('%H hour %M minutes')
            speak(f'Sir the time is {Time_now}')
        elif 'open code' in query:
            code_path = 'C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            # code_path is the path for the app
            try:
                os.startfile(code_path)
            except Exception as e:
            
                speak('Apllication Does not Exists')
        elif 'ls folder' in query:
            ls_dir ='E:\\BACKUP_08_05_2019\\DESKTOP\\ls'
            os.startfile(ls_dir)
        elif 'your folder' in query:
            Your_dir = "your folder"
            os.startfile(Your_dir)
        elif 'who are you' in query:
            speak('I am Friday')
            speak('Your personal assistant')
            speak('I was created on 23 Augest 2019 by Shiladitya')
        elif 'send a mail' in query:
            try:
                speak('what should i say sir')
                content = str(input())
                to = str(input('Emali id of the receiver:'))
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Unable to sent the mail at this moment')
                speak('Sorry for the inconvience')
        elif 'exit' in query:
            speak("Have a good day sir")
            act = False
        elif 'version' in query:
            speak("I am Currently Version 2.0")
        elif 'open app' in query:
            code_path = 'C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            Your_dir = 'E:\\BACKUP_08_05_2019\\DESKTOP\\ls\\programming\\python\\projects\\JARVIS A.I'
            speak('which app do you want to open')
            app = str(input('APP:')).lower()
            if 'code' in app:
                os.startfile(code_path)
            elif 'your folder' in app:
                os.startfile(Your_dir)
        else:
            speak('I could not understand that')
b.close()

    
    



    
 
