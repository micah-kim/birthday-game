
import requests
import sys,time,random
from zipfile import ZipFile
import urllib.request
import cv2
from datetime import date

def main():
    url = 'https://www.dropbox.com/s/9svg39hypcc6l8g/IMG_1132.MOV.zip?dl=1'
    r = requests.get(url)
    today = date.today()
    today = str(today) + ".txt"
    fd = open(today, "w")

    while True:
        if game(fd) == True:
            print_slow("You win. Congratulations.\n")
            time.sleep(3)

            with open('gift.zip', 'wb') as f:
                f.write(r.content)

            with ZipFile('gift.zip', 'r') as f:
                f.extractall()

            vid = cv2.VideoCapture('IMG_1132.MOV')
            
            while (vid.isOpened()):
                ret, frame = vid.read()
                cv2.imshow("video", frame)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            
            vid.release()
            cv2.destroyAllWindows()
         
            return
        else:
            print_slow("You lose.\n")
            return
        
def game(fd):
    # return True
    print_slow("It is your birthday, Jasmine.\n")
    print_slow("Your task is to complete the game in order to receive your gift.\n")
    
    if start_game():
        print_slow("Great!\n")
    else:
        print_slow("Ok bye.\n")
        return False
    
    if game_1(fd):
        if game_2(fd):
            if game_3():
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            

def game_1(fd):
    print_slow("\nGAME 1\n")
    print_faster("In one sentence, explain what your favorite memory this semester was.\n")
    print_slow("Response: ")
    user_in = input()
    
    while len(user_in) < 10:
        print_slow("do better.\n")
        print_slow("Response: ")
        user_in = input()

    fd.write(user_in)
    fd.write("\n\n")
    
    return True

def game_2(fd):
    print_slow("\nGAME 2\n")
    print_faster("In one sentence, explain WHY it was your favorite memory.\n")
    print_slow("Response: ")
    user_in = input()

    while len(user_in) < 10:
        print_slow("do better.\n")
        print_slow("Response: ")
        user_in = input()
        
    fd.write(user_in)

    return True

def game_3():
    choices = ["H", "T"]
    print_slow("\nGAME 3\n")

    print_faster("This is a game of luck. Heads (H) or tails (T)? \n")
    print_slow("Type your selection: ")
    
    user_in = input()
    
    for i in range(3):
        print_slow("spinning", end="")
        time.sleep(1)
        print_slow("...\n")
    
    ans = random.randint(0, 1)
    print_slow("The outcome is" + choices[ans - 1] + "!\n")
    time.sleep(1)
    print_slow("jk.\n")
    time.sleep(1)
    print_slow("The outcome is" + choices[ans] + ".\n")
    time.sleep(1)

    while user_in != choices[ans]:
        print_slow("You lose.")

        print_slow("Type your selection: ")
    
        user_in = input()
        
        for i in range(4):
            print("spinning", end="")
            print_slow("...\n")
            time.sleep(3)
        
        ans = random.randint(0, 1)
        print_slow("The outcome is" + choices[ans - 1] + "!\n")
        time.sleep(1)
        print_slow("jk.\n")
        time.sleep(1)
        print_slow("The outcome is" + choices[ans] + ".\n")

    return True    



def start_game():
    print("Wanna play? (Y/N): ", end="")
    ans = input()
    if ans == "Y":
        return True
    else:
        return False

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


def print_faster(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

main()


