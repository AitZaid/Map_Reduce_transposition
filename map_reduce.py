import csv
import sys

#Open CSV file as inputfile, read it and store it readinput
with open('test.csv', "rt") as inputfile:
    readinput = csv.reader(inputfile, delimiter=',')    
    
    print ('---------- CSV FILE ----------', end = '\n\n')
    
    MyMap = []
    val_x= 0

#Mapping
    for row in readinput:
        # here we print each row of the csv file
        print(row, end='\n')

        # we initialize the column value so that it comes back to 0 at each row
        val_y = 0

        # this for loop allow us to fill the map with the different key values and the data of the csv file
        for data in row :
            MyMap.append([[val_x,val_y], data])
            val_y += 1

        val_x += 1
    print('\n')

    # here we print the results of our mapping
    print('---------- MAP ----------', end='\n\n')
    print (MyMap, end = '\n\n')

    # Reducing
    # here the goal is to create another list for the reduction so that we can put our new key values associated to our data
    reduced = []
    for position in MyMap :
        reduced.append([[position[0][1], position[0][0]],position[1]])

    # here we print the result of our reducing
    print ('---------- REDUCING ----------', end = '\n\n')
    print (reduced, end = '\n\n\n')


    # now we want to print the new reduced tab :
    #first we calculate the length and depth of the new tab
    y = reduced[len(reduced)-1][0][1]+1
    x = reduced[len(reduced)-1][0][0]+1

    #here we initialize our final transposed tab
    transposed = [[0 for length in range (y)] for depth in range(x)]

    # this loop allows us to fill our final transposed tab we put each data into it's new position in the transposed tab
    for position in reduced:
        transposed [position[0][0]][position [0][1]] = position[1]

    #finally we can print the transposed tab
    print ('---------- TRANSPOSED TAB ----------', end = '\n\n')
    for row in transposed :
        print (row)
