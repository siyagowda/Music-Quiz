#importing libraries
import csv
import random
import time

#logging in
global name
name = input("Enter name: ")
password = input("Enter password: ")
if name.lower() == "siya" and password.lower() == "watermelon":
    print("Login successful")
    login = True #if name and password match, then user can play
elif name.lower() == "vic" and password.lower() == "cat":
    print("Login successful")
    login = True
elif name.lower() == "holly" and password.lower() == "veg":
    print("Login successful")
    login = True
elif name.lower() == "rebecca" and password.lower() == "village":
    print("Login successful")
    login = True
elif name.lower() == "bridget" and password.lower() == "papaya":
    print("Login successful")
    login = True
else:
    print("Login unsuccessful")
    login = False #user/password are not correct so user cannot play
    win = False #stops user from playing

time.sleep(2)
#start game
if login == True: #tells the user how the game works
    print("\nWelcome " + name.capitalize() +", let's get started")
    time.sleep(2)
    print("This is how the game works")
    time.sleep(3)
    print("I'm going to show you an artist")
    time.sleep(3)
    print("And you have to guess the song")
    time.sleep(3)
    print("From only the first letters of each word of the song")
    time.sleep(3)
    print("If you guess it right on your first guess you get 3 points")
    time.sleep(3)
    print("If you guess it right on your second guess you get 1 point")
    time.sleep(3)
    print("If you can't guess it right after two guesses, you lose\n\n")
    win = True

points = 0 #creates points variable 
while win == True:

    time.sleep(3)

    #getting random song and artist from .csv file
    with open("Songs.csv") as f: #opens csv file
        reader = csv.reader(f) #reads csv file
        for index, row in enumerate(reader):
            if index == 0:
                song = row #assigns rows to a song
            else:
                r = random.randint(0, index)
                if r == 0:
                    song = row

    #splits the string into artist and song
    artist = song[1]
    title = song[0]

    print("\nThe artist is " + artist)
    time.sleep(1)
    print("And the song is ")
    time.sleep(2)

    #displays only the first letter of each word in the song title
    words = song[0].split() #splits the first chraracters from the rest of the words
    for word in words:
        print(word[0].capitalize())#prints only the first letter capitalised

    #starts game
    fGuess = input("What is your first guess?\n")
    if fGuess.lower() == title: #if the answer is correct
        print("Well done " + name +"!")
        points += 3 #adds 3 points to the variable
        score = (str(points)) #converts the numerical variable into a string
        print("Your score so far is " + score) #displays a running total
    else:#if the answer is incorrect
        print("Uh oh, try again")
        sGuess = input("What is your second guess?\n")
        if sGuess.lower() == title: #if the answer is correct the second time
            print("Yes you got it this time!")
            points += 1 #adds 1 point to variable
            score = (str(points))#converts the numerical variable into a string
            print("Your score so far is " + score)#displays a running total
        else: #if the answer is incorrect again
            time.sleep(1)
            print("Oh dear you got it wrong again")
            time.sleep(1)
            print("\nThat's game over for you")
            time.sleep(1)
            print("\nThe answer was actually:")
            time.sleep(1)
            print (', '.join(map(str, song)))#displays the answer
            win = False
            #ends game

    #displaying score
    if win == False:
        score = (str(points))#converts the numerical variable into a string
        time.sleep(2)
        print("\nYour total score is " + score)#displays final total
        #saving it to a csv file
        file = open("HighScores.csv","a")#opens csv to append
        newrecord=name.capitalize()+", "+score+"\n"#creates variable with name and score
        file.write(str(newrecord))#appends variable to the the csv file
        file.close()

        #displaying high score
        with open("HighScores.csv","r") as fh:#opens csv file
            reader = csv.reader(fh, delimiter = ',')
            sort = sorted(reader, key=lambda x: int(x[1]), reverse=True)#sorts the scores from high to low
            print("\nLEADERBOARD:")
            time.sleep(1)
            print (',\t'.join(map(str, sort[0])))#shows the name and score at the top of the leaderboard
            time.sleep(1)
            print (',\t'.join(map(str, sort[1])))
            time.sleep(1)
            print (',\t'.join(map(str, sort[2])))
            time.sleep(1)
            print (',\t'.join(map(str, sort[3])))
            time.sleep(1)
            print (',\t'.join(map(str, sort[4])))

### end of game ###




                  

        



