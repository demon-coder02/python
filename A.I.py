import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import sys
import pyautogui
import urllib.parse
import subprocess
from faker import Faker

speaker = win32com.client.Dispatch("SAPI.SpVoice")
selected_voice_index = 1


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pause_threshold = 0.1
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            user_query = r.recognize_google(audio, language="en-in")
            print("Recognizing...")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Something went wrong. Please check the code."



def currectTime():
    timenow = datetime.datetime.now().hour

    if timenow >= 0 and timenow <= 12:
        timenow = "Good Morning"
    elif timenow > 12 and timenow <= 18:
        timenow = "Good Afternoon"
    else:
        timenow = "Good evening"
    return timenow




def open_windows_application():
     subprocess.run("start ms-setting:", sehll=True)



def wishMe():
    query = ""
    # --------------------------------BIRTHDAY----------------------------------------
    if "tejesh birthday" in query.lower() or "birthday tejesh" in query.lower():
        print()
        print("-------------------------------")
        print("Tejesh birthday is on 02/03/2005")
        print("-------------------------------")
        print()
    elif "jayesh birthday" in query.lower() or "birthday jayesh" in query.lower():
        print()
        print("-------------------------------")
        print("Jayesh birthday is on 02/03/2005")
        print("-------------------------------")
        print()
    elif "shakuntala birthday" in query.lower() or "birthday shakuntala" in query.lower():
        print()
        print("-------------------------------")
        print("Shakuntala birthday is on 16/06/1985")
        print("-------------------------------")
        print()
    # --------------------------------------------------------------------------------


    # ------------------------------------DEVELOPER-----------------------------------
    if "developer" in query.lower():
        print()
        print('''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tejesh Patel
-------------
Tejesh Patel (Master Coder) has developed this program  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''')
    elif "show copyright" in query.lower() or "show copyright disclatmer" in query.lower():
        print('''
                                                                                               A.I.
                                                                                              ------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
COPYRIGHT DISCLAIMER
----------------------
All materials, content, and information provided on Master Coder are protected by copyright laws. The owner of Master Coder holds all the copyrights, trademarks, and other intellectual property rights 
related to the content displayed on this website. Any unauthorized use, reproduction, or distribution of the materials, content, or information from this website without prior written consent from the 
copyright owner is strictly prohibited. Visitors, users, or viewers of this website may not modify, republish, distribute, or exploit any part of the content without obtaining proper permission.
Master Coder makes every effort to ensure the accuracy and completeness of the information presented on this website. However, we do not guarantee the accuracy or reliability of the information 
and disclaim any responsibility for errors or omissions in the content. The opinions expressed on this website are solely those of the authors and do not necessarily reflect the views of Master Coder.
Any third-party materials, content, or trademarks displayed on Master Coder are the property of their respective owners and used with permission. Their inclusion on this website does not imply any 
endorsement or affiliation with Master Coder. If you believe that any content on this website infringes your copyright or intellectual property rights, please contact us at [Your Contact Email] to 
address the issue. Master Coder reserves the right to modify, update, or remove any content from the website without prior notice.
          
                                                                                                                                                                       ------------------------- 
                                                                                                                                                                        - Made by Tejesh Patel
                                                                                                                                                                       ------------------------- 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''')
    # --------------------------------------------------------------------------------



def functions(user_input):
    if "table" in query.lower():
        table = 1
        while table<=10:
            print(f"{user_input} X {table} = {user_input*table}")
            table+=1

    elif "check even odd" in query.lower():
        if user_input%2==0:
            speaker.Speak(f"{user_input} is an even number")
        else:
            speaker.Speak(f"{user_input} is an odd number")

    elif "c to f" in query.lower() or "f to c" in query.lower():
        if "c to f" in query.lower():
            f = (user_input * 9/5) + 32
            return f
        elif "f to c" in query.lower():
            c = (user_input - 32) * 9/2
            return c

    elif "factorial" in query.lower():
        factorial = 1;
        i = 1
        while i<=user_input:
            factorial*=i
            i+=1
        return factorial


def generate_writing():
    fake = Faker()
    return fake.sentence()

def writing(topic, num_sentences):
    essay = ""
    for _ in range(num_sentences):
        essay += generate_writing() + " "
    return f"{topic}\n\n{essay}"





while True:
    timenow = wishMe()
    speaker.Voice = speaker.GetVoices().Item(selected_voice_index)
    print('''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            Welcome Sir
                                                                                           -------------

Hello sir I am jarvis I am your A.I Assistance
Please Let me know If I can help you

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''')
    print()
    speaker.Speak(f"{timenow} Sir Please let me know If I can help you")


    while True:
        password_correct = False
        while not password_correct:
            print("Listening...")
            query = takeCommand()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                 Dictionary
#                                                                                                               --------------


            sites = [
            #   -----------------------------GOOGLE WEBSIDES--------------------------------        
                ["google", "https://www.google.com"],
                ["gmail", "https://mail.google.com/mail/u/1/#inbox"],
                ["google drive", "https://drive.google.com/"],
                ["drive", "https://drive.google.com/"],
                ["google map", "https://www.google.com/maps"],
                ["map", "https://www.google.com/maps"],
                ["youtube", "https://www.youtube.com"],
                ["yt", "https://www.youtube.com"],
            #   --------------------------------SOCIAL MEDIA--------------------------------         
                ["instagram", "https://www.instagram.com/"],
                ["insta", "https://www.instagram.com/"],
                ["facebook", "https://www.facebook.com/"],
                ["fb", "https://www.facebook.com/"],
                ["twitter", "https://twitter.com/"],
            #   ------------------------------CODING WEBSIDES-------------------------------           
                ["chatgpt", "https://chat.openai.com/"],
                ["github", "https://github.com/dashboard"],
            #   ------------------------------TYPING WEBSIDES-------------------------------       
                ["monkeytype", "https://monkeytype.com/"],
                ["typing academy", "https://typing.academy"],
            #   ------------------------------SHOPING WEBSIDES------------------------------                
                ["amazon", "https://www.amazon.com/"],
                ["flipkart", "https://www.flipkart.com/"],
            #   ------------------------------SEARCHING WEBSIDES----------------------------
                ["wikipedia", "https://www.wikipedia.org/"],
                ["bing ai", "https://www.bing.com/search?form=NTPCHT&ocid=msedgntp&cvid=1e6dc9a0103d40a68ae55502295cacc4&ei=15&q=What+can+the+new+Bing+chat+do%3F&showconv=1&sydconv=1"]
            ]


            secures = [
                ["omagle", "https://www.omegle.com/"]
            ]


            playlist = [
        # -------------------------------------------------------------------------------------------------DEVICE-----------------------------------------------------------------------------------------------------------
        
            #   ---------------------------------------------------------------------------------ENGLISH SONGS------------------------------------------------------------------------
                ["sketches", "C:\\Users\\tejes\\Music\\Music\\Skechers Full Song(Lyrics)🎵 (320 kbps).mp3"],
            #   ------------------------------------------------------------------------------HINDI SONGS-----------------------------------------------------------------------------
                ["agar tum saath ho", "C:\\Users\\tejes\\Music\\Music\\Agar Tum Sath Ho X Can we kiss forever  Sush & Yohan Remix.mp3"],
                ["yeh jism hai to kya","C:\\Users\\tejes\\Music\\Music\\Ye jism hai toh kya sad song.mp3"],
                ["ajnabi hawaayein", "C:\\Users\\tejes\\Music\\Music\\Ajnabi Hawaayein Full Song Shaapit By Shreya Ghoshal.mp3"],
                ["bad munda", "C:\\Users\\tejes\\Music\\Music\\BAD MUNDA _ Jass Manak Ft. Emiway Bantai (Full Video) Satti Dhillon _ Deep Jandu _ GK _ Geet MP3 (320 kbps).mp3"],
                ["basti ka hasti", "C:\\Users\\tejes\\Music\\Music\\Basti Ka Hasti Official Audio  INSAAN  2022.mp3"],
                ["ek din pyaar", "C:\\Users\\tejes\\Music\\Music\\EK DIN PYAAR  TADIPAAR  2K20.mp3"],
                ["brown munde", "C:\\Users\\tejes\\Music\\Music\\Brown Munde - AP Dhillon X Gurinder Gill X Shinda Kahlon X Gminxr ( lyrics ) (128 kbps).mp3"],
                ["despacito hindi version", "C:\\Users\\tejes\\Music\\Music\\Despacito hindi version.mp3"],
                ["dil ibaadat", "C:\\Users\\tejes\\Music\\Music\\Dil Ibaadat Full Video  Tum MileEmraan HashmiSoha Ali KhanPritamKKSayeed Quadri.mp3"],
                ["hamdard", "C:\\Users\\tejes\\Music\\Music\\Hamdard Full Video Song  Ek Villain  Arijit Singh  Mithoon (1).mp3"],
                ["aur bantai", "C:\\Users\\tejes\\Music\\Music\\EMIWAY-AUR BANTAI (EM 24 7) (FULL HD).mp3"],
                ["goat", "C:\\Users\\tejes\\Music\\Music\\GOAT  Perfectly Slowed  Sidhu Moosewala.mp3"],
                ["jhoom", "C:\\Users\\tejes\\Music\\Music\\Jhoom  RB version  Official video.mp3"],

        # -------------------------------------------------------------------------------------------------YOUTUBE-----------------------------------------------------------------------------------------------------------
                
            #   ------------------------------------------------------------------------------HINDI SONGS-----------------------------------------------------------------------------
                ["ram siya ram", "https://youtu.be/H59OJfVBi30"],
                ["pagol", "https://youtu.be/DEHDRFs5jXY"],
                ["sarkar", "https://youtu.be/uzDZ0x7XiAA"],
                ["aao sunao pyaar ki ek kahani", "https://youtu.be/bb-h4QeXy7Q"],
                ["banjaara", "https://youtu.be/pstd4RIiWBE"],
                ["main agar kahoon", "https://youtu.be/k6eyzRda9zU"],
                ["tere hawale" ,"https://youtu.be/pYkETd4mcRc"],
                ["tere sang yaara" ,"https://youtu.be/nP0UdGVfhmQ"],
                ["khamoshiyan" ,"https://youtu.be/K6hwsVaXOiM"],
                ["saiyyan" ,"https://youtu.be/bWnzXdIUFaM"],
                ["hamari adhuri kahani" ,"https://youtu.be/RxIm1vc2XwM"],
                ["tu jo mila" ,"https://youtu.be/1WnmSeGT1zM"],
            #   -----------------------------------------------------------------------------ENGLISH SONGS----------------------------------------------------------------------------
                ["perfect", "https://youtu.be/eDWzGAspSvM"],
                ["fairytale", "https://youtu.be/3zYCYpbVzHk"],
                ["on my way", "https://youtu.be/dhYOPzcsbGM"],
                ["faded", "https://youtu.be/60ItHLz5WEA"],
                ["lili", "https://youtu.be/9GtmOSPXStw"],
                ["night changes", "https://youtu.be/7KPyunRIjr0"],
                ["motivation", "https://www.youtube.com/watch?v=8Mob3cKtp_4&ab_channel=BSBEATZ"],


        # ------------------------------------------------------------------------------------------- --YOUTUBE PLAYLIST-----------------------------------------------------------------------------------------------------        
                ["english songs", "https://www.youtube.com/watch?v=3zYCYpbVzHk&list=PLC9UXUjrae32tykE8lcnnmAExTW_e9ko5&ab_channel=AlexanderRybak-Topic"],
                ["hindi songs", "https://www.youtube.com/watch?v=95yrZXwZ31w&list=PLC9UXUjrae31fHHyjqUK1MbFq1MULraN8&ab_channel=JassManak-Topic"],
                ["them songs", "https://www.youtube.com/watch?v=tKxwosDpL08&list=PLC9UXUjrae33RomfybE99WS2bKG0O-79e&ab_channel=8DMUSIX-LYF"],
                ["cg songs", "https://www.youtube.com/watch?v=b5ScCu3KrSY&list=PLC9UXUjrae33uOLpisXe5MLxGwI-e7WBv&ab_channel=JOYASERIES_CGMUSIC"]
            ]


            apps = [
                ["photoshop", "C:\\Users\\tejes\\OneDrive\\Desktop\\Adobe Photoshop 2020.lnk"],
                ["premiere pro", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Premiere Pro 2020.lnk"],
                ["pycharm", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2023.1.3.lnk"],
                ["vs code", "C:\\Users\\tejes\\OneDrive\\Desktop\\Visual Studio Code.lnk"],
                ["edge", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"],
                ["word", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"],
            # ------------------------------------------------------------GAMES----------------------------------------------------------------------
                ["free fire", "C:\\Users\\tejes\\OneDrive\\Desktop\\Free Fire.lnk"],
                ["subnautica", "D:\\Apps\Games\\Subnautica.v68654\\Game\\Subnautica.exe"],
                ["tomb raider", "D:\\Apps\\Games\\Tomb Raider\\tra.exe"],
                ["minecraft", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\TLauncher\\TLauncher.lnk"]
            ]


    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #                                                                                                                 OS        
    #                                                                                                                -----


        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            for site in sites:
                if f"open {site[0]}" in query.lower() or f"launch {site[0]}" in query.lower():
                    speaker.Speak(f"Opening {site[0]} sir...")
                    webbrowser.open(site[1])
            
            for secure in secures:
                if f"open {secure [0]}" in query.lower() or f"launch {secure [0]}" in query.lower():
                    password = input("Enter the password to enter the tap: ")
                    if password=="1234":
                        print("The passworld is correct")
                        print()
                        print(f"Opening {secure [0]} sir...")
                        webbrowser.open(secure[1])
                        password_correct = True
                    else:
                        print("Access Denied Password Incorrect")

            # ----------------------------------------------------------------------APPLICATION------------------------------------------------------

            for app in apps:
                if f"open {app[0]}".lower() in query.lower():
                    speaker.Speak(f"Opening {app[0]} sir...")
                    os.startfile(app[1])

            if "open setting" in query.lower():
                if __name__ == "__main__":
                    open_windows_application()


        # ---------------------------------------------------------------------------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------Songs--------------------------------------------------------------------------
            for song in playlist:
                if f"play {song[0]}".lower() in query.lower():
                    speaker.Speak(f"Playing {song[0]} sir...")
                    os.startfile(song[1]) 

            if "show playlist" in query.lower() or "playlist" in query.lower():
                print("Here is your playlist sir...")
                print()
                for index, item in enumerate(playlist, start=1):
                    key = item[0]
                    key = key.capitalize()
                    print(f"{index}: {key}")

            if "pause the song" in query.lower() or "play the song" in query.lower():
                speaker.Speak("Pausing the song sir...")
                pyautogui.press('space')
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------Google--------------------------------------------------------------------------
            if "search in google" in query.lower() or "search on google" in query.lower() or "in google" in query.lower() or "on google" in query.lower():
                search_query = query.lower().replace("search in google", "")
                reaplaced_query = urllib.parse.quote(search_query)
                google_url = "https://www.google.com/search?q="
                search_url = google_url + reaplaced_query
                speaker.Speak(f"Searching in google {search_query}")
                webbrowser.open(search_url)

            if "search in youtube" in query.lower() or "search on youtube" in query.lower() or "search youtube" in query.lower():
                search_query = query.lower().replace("search in youtube", "")
                encoded_query = urllib.parse.quote(search_query)
                youtube_url = "https://www.youtube.com/results?search_query="
                search_url = youtube_url + encoded_query
                speaker.Speak(f"Searching for {search_query} in YouTube...")
                webbrowser.open(search_url)

            if "search in map" in query.lower() or "search in google map" in query.lower() or "locate" in query.lower():
                search_query = query.lower().replace("search in map", "")
                reaplaced_query = urllib.parse.quote(search_query)
                map_url = "https://www.google.com/maps/search/"
                search_url = map_url + reaplaced_query
                speaker.Speak(f"Locating {search_query} on Google Maps")
                webbrowser.open(search_url)
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------Shoping--------------------------------------------------------------------------
            if "search in amazon" in query.lower() or "search on amazon" in query.lower():
                search_query = query.lower().replace("search in amazon", "")
                reaplaced_query = urllib.parse.quote(search_query)
                amazon_url = "https://www.amazon.com/s?k="
                search_url = amazon_url + reaplaced_query
                speaker.Speak(f"Searching in amazon {search_query}")
                webbrowser.open(search_url)

            if"show my orders of amazon" in query.lower() or "order of amazon" in query.lower() or "amazon order" in query.lower():
                speaker.Speak("Shoing all your orders of amazon sir...")
                webbrowser.open("https://www.amazon.in/gp/css/order-history?ref_=nav_AccountFlyout_orders")

            if "search in flipkart" in query.lower() or "search on flipkart" in query.lower():
                search_query = query.lower().replace("search in flipkart", "")
                reaplaced_query = urllib.parse.quote(search_query)
                flipkart_url = "https://www.flipkart.com/search?q="
                search_url = flipkart_url + reaplaced_query
                speaker.Speak(f"Searching in flipkart {search_query}")
                webbrowser.open(search_url)

            if"show my orders of flipkart" in query.lower() or "order of flipkart" in query.lower() or "flipkart order" in query.lower():
                speaker.Speak("Shoing all your orders of flipkart sir...")
                webbrowser.open("https://www.flipkart.com/account/orders?link=home_orders")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------



        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "search in wikipedia" in query.lower() or "search on wikipedia" in query.lower() or "refer to wikipedia" in query.lower():
                search_query = query.lower().replace("search in wikipedia", "")
                reaplaced_query = urllib.parse.quote(search_query)
                wikipedia_url = "https://en.wikipedia.org/wiki/Special:Search?search="
                search_url = wikipedia_url + reaplaced_query
                speaker.Speak(f"Searching {search_query} in wikipedia")
                webbrowser.open(search_url)

            if "calculate" in query.lower():
                search_query = query.lower().replace("calculate", "")
                replaced_query = urllib.parse.quote(search_query)
                calculator_url = "https://www.google.com/search?q="
                serach_url = calculator_url + replaced_query
                speaker.Speak(f"Calculating {search_query} sir...")
                webbrowser.open(serach_url)
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------



        # -----------------------------------------------------------------------------CALCULATION-----------------------------------------------------------------
            if "table" in query.lower():
                print('''
                     TABLE
                    --------
''')
                while True:
                    try:
                        user_inputer = input("Enter the number which table you want to print: ")
                        if "exit" in user_inputer.lower() or "back" in user_inputer.lower():
                            break
                        user_input = int(user_inputer)
                        if user_input<=0:
                            speaker.Speak("Please enter a positve number")
                        else:
                            print()
                            print("----------------------------------------")
                            functions(user_input)
                            print("----------------------------------------")
                            print()
                    except Exception as e:
                        speaker.Speak("Try Again")

            elif "check even odd" in query.lower() or "even odd checker" in query.lower() or "even odd check" in query.lower():
                print('''
                     EVEN ODD CHECKER
                    ------------------
''')
                while True:
                    try:
                        user_inputer = input("Enter the number to check even odd: ")
                        if "exit" in user_inputer.lower() or "back" in user_inputer.lower():
                            break
                        user_input = int(user_inputer)
                        if user_input<=0:
                            speaker.Speak("Please enter a positve number")
                        else:
                            print()
                            functions(user_input)
                            print()
                    except Exception as e:
                        print()
                        speaker.Speak("Something went wrong...")
                        print()

            elif "c to f" in query.lower() or "Celsius to Fahrenhei" in query.lower() or "f to c" in query.lower() or "Fahrenhei to Celsius" in query.lower():
                
                if "c to f" in query.lower() or "Celsius to Fahrenhei" in query.lower():
                    print('''
                      Celsius to Fahrenheit
                     -----------------------
''')
                    while True:
                        try:
                            user_inputer = input("Enter the °C : ")
                            if "exit" in user_inputer.lower() or "back" in user_inputer.lower():
                                break
                            user_input = int(user_inputer)
                            f = functions(user_input)
                            speaker.Speak(f"{user_input}°C = {f:.2f}°F ")
                            print("------------------------------------")
                        except Exception as e:
                            speaker.Speak("Something went wrong")
                            print("Something went wrong")

                elif "f to c" in query.lower() or "Fahrenhei to Celsius" in query.lower():
                    print('''
                     Fahrenhei to Celsius
                    ----------------------
''')
                    while True:
                        try:
                            user_inputer = input("Enter the °F : ")
                            if "exit" in user_inputer.lower() or "back" in user_inputer.lower():
                                break
                            user_input = int(user_inputer)
                            c = functions(user_input)
                            speaker.Speak(f"{user_input}°F = {c:.2f}°C")
                            print("------------------------------------")
                            print(f"{user_input}°F = {c:.2f}°C")
                            print("------------------------------------")
                        except Exception as e:
                            speaker.Speak("Something went wrong")
                            print("Something went wrong")

            elif "factorial" in query.lower():
                user_input = int(input("Enter The number: "))
                if user_input<=0:
                    speaker.Speak("Enter a positive number")
                    print("Enter a positive number")
                else:
                    print()
                    factorial = functions(user_input)
                    speaker.Speak(f"The factorial of {user_input} is {factorial}")
                    print(f"The factorial of {user_input} is {factorial}")
                    print()
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------



        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "write a essay" in query.lower() or "wirte essay" in query.lower() or "write an essay" in query.lower():
                if __name__ == "__main__":
                    topic = input("Enter the topic of your essay: ").capitalize()
                    try:
                        num_sentences = int(input("Enter the number of sentences you want to print: "))
                        if num_sentences<=0:
                            print("Please enter a positive number")
                        else:
                            if num_sentences>100:
                                print()
                                print("It will take time")
                                print()

                            print("Printing...")
                            essay = writing(topic, num_sentences)
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print(essay)
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print()
                    except Exception as e:
                        print("Enter a number")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #                                                                                                                 Rest        
    #                                                                                                                ------    
    #                                                     

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "the date" in query.lower() or "the day" in query.lower() or "the time" in query.lower():
                if "the time" in query.lower() or "time" in query.lower():
                    current_time = strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speaker.Speak(f"Sir the time is {current_time}")
                elif "the day" in query.lower() or "day" in query.lower():
                    current_day = datetime.datetime.now().strftime('%A')
                    speaker.Speak(f"Sir the day is {current_day}")
                elif "the date" in query.lower() or "date" in query.lower():
                    current_date = datetime.date.today()
                    speaker.Speak(f"Sir the date is {current_date}")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
                if "birthday" in query.lower() or "bday" in query.lower() or "developer" in query.lower() or "show copyright" in query.lower() or "show copyright disclatmer" in query.lower():
                    wishMe()
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "hello jarvis" in query.lower() or "hey jarvis" in query.lower() or "ok jarvis" in query.lower():
                print()
                speaker.Speak("Yes Sir May I help you")
                print()

            if "hello jarvis" in query.lower() or "how are you jarvis" in query.lower():
                if "how are you" in query.lower():
                    print()
                    speaker.Speak("I am fine sir! How about you")
                    user_input = input("")
                    print()
                    if "i am fine" in user_input.lower() or "i am good" in user_input.lower():
                        print()
                        speaker.Speak("OK! sir may I help you with something")
                        print()
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "weather" in query.lower():
                speaker.Speak("Weather Report of Raigarh Chhattisgarh")
                webbrowser.open("https://www.msn.com/en-us/weather/forecast/in-?loc=eyJ0IjoxLCJ4Ijo4My4zOTQsInkiOjIxLjg5NH0%3d&ocid=ansmsnweather")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "jor se bolo" in query.lower():
                speaker.Speak("jai mata di")

            if "ganpati bappa" in query.lower():
                speaker.Speak("Moriya")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            if "exit" in query.lower() or "close"  in query.lower():
                speaker.Speak("Have a nice day sir...")
                sys.exit()
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------