# Text-Writer-And-Text-to-Array
This Python script does two things:
1) Writes a text file based on input 
2) Takes the previous used text file to sort its items into arrays based by tag

The following is the steps of the two functions within the script:

Writing (theSource):
1. Create the variable continuation set to true
2. Do Steps 3 - 5 while continuation is true
3. Create the variable writing set to the user's input
4. if the variable writing is equal to the string "#End#", set continuation to false and add the writing to the file theSource
5. If the conditions in step 4 are false, add the writing along with a new line indicator to the file the Source
6. close theSource

Sorting(theSource, listNumber):
1. Create these variables: continuation set to true, count set to 0, and currentItem set to ""
2. Try to set currentItem to the first line read in theSource
3. When an exception occurs, set continuation to false, print "Failed Reading", and return
4. Set currentItem to itself without the last character in the string
5. Do steps 6 - 23 while continuation is true
6. If currentItem is equal to the string "#Greetings", do steps ## - ##
7. Set continuation to true, create empty array listGreetings
8. Do lines 9 - 11 while continuation is true
9. Set currentItem to the next line read in theSource
10. If currentItem doesn't start with a "#", add currentItem without the last character to the listGreetings array
11. If the conditions in step 10 are false, set continuation to false
12. Set currentItem to itself without the last character
13. Set count to 0
14. If currentItem is equal to the string "#Goodbyes", do steps ## - ##
15. Set continuation to true, create empty array listGoodbyes
16. Do lines 16 - 19 while continuation is true
17. Set currentItem to the next line read in theSource
18. If currentItem doesn't start with a "#", add currentItem without the last character to the listGoodbyes array
19. If the conditions in step 10 are false, set continuation to false
20. Set currentItem to itself without the last character
21. Set count to 0
22. Increment count by 1
23. If count is equal to 2, set continuation to false
24. If the currentItem is equal to "#End", close theSource. If listNumber is 1, return listGreetings. If listNumber is 2, return listGoodbyes
