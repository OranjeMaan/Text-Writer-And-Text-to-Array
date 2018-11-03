def Writing(theSource):
    continuation = True
    #While the user hasn't enter "#End#", add a line to the text file with the user's input
    while(continuation):
        writing = input("Please enter the next line of text. Enter '#End#' to end writing to file.")
        if(writing == "#End#"):
            continuation = False
            theSource.writelines(writing)
        else:
            theSource.writelines(writing + "\n")
    theSource.close()

def Sorting(theSource, listNumber):
    #List of Variables
    continuation = True
    count = 0
    currentItem = ""
    #Check's the file if it can be read
    try:
        currentItem = theSource.readline()
    except:
        continuation = False
        print("Reading has failed")
        return
    #Commence the reading of the file
    #Removing the last charcter of the line (as it's "\n")
    currentItem = currentItem[:-1]
    while(continuation):
        #Set for sorting items into an array
        if (currentItem == "#Greetings"):
            continuation = True
            listGreetings = []
            #Add all lines below the the tag into an array until the next tag
            while(continuation):
                currentItem = theSource.readline()
                if (currentItem[0] != "#"):
                    listGreetings.append(currentItem[:-1])
                else:
                    continuation = False
            currentItem = currentItem[:-1]
            count = 0
        #Second set for Goodbyes
        if (currentItem == "#Goodbyes"):
            continuation = True
            listGoodbyes = []
            while(continuation):
                currentItem = theSource.readline()
                if (currentItem[0] != "#"):
                    listGoodbyes.append(currentItem[:-1])
                else:
                    continuation = False
            continuation = True
            currentItem = currentItem[:-1]
            count = 0
        #End of Templates
        #Force stop to prevent infinite loop; stops loop after the second loop
        count += 1
        if (count == 2):
            continuation = False
    if (currentItem == "#End"):
        theSource.close()
        if (listNumber == 1):
            return listGreetings
        elif (listNumber == 2):
            return listGoodbyes

def main():
    listPhrases = open("listPhrases.txt","w+")
    Writing(listPhrases)
    listPhrases = open("listPhrases.txt","r")
    print(Sorting(listPhrases,1))
    
main()
