"""
*
* Author: Deepak Begrajka
*
* Brief Explanation:
* In the code below I have gone through the directory and looked for all the csv files in the directory
* store them in the list, itterate through the last and check if both the row are correct, if yes store the output in a dict were key is a class name and value is last of marks in the range of (0,100)
* store all the students with 0 marks in dictToStoreZeroListOfStudentwithZeroMarks, I was thinking of student with simillar names to avoid but, it is possible that students might have same names in the class.
* After that I have iterated through the dictionary and calculated the class avg and overall overgae.
* To get the highest performance class I have to reverse the list called classAvg which has keys as class and value as avg of class sum, and get max of it.
*  Next is iterating through the first dict and storing the required output in the list of string.
* Last step is opening the file output, iterating through the listOfOutput strings and writting in the file and at the end closing the file.
*
"""

import csv
import os
from glob import glob

dict = {}
dictToStoreZeroListOfStudentwithZeroMarks = {}
classAvg = {}
listOfOutput = []

def findAllCsv():
    listOfFile = []
    try:
        PATH =  "C:/Users/deepak.begrajka/Downloads/Dev Test/Dev Test"
        EXT = "*.csv"
        listOfFile = list(filter(lambda x: '.csv' in x, os.listdir(PATH)))
    except:
        print("Wrong path \n")
    #all_csv_files = [file for path, subdir, files in os.walk(PATH) for file in glob(os.path.join(path, EXT))]
    #print(len(all_csv_files))
    #check if any csv file exist
    if len(listOfFile) is 0:
        listOfOutput.append("No Class Grade File Exist. \n")
    else:
        for f in listOfFile:
            calculateGrades(f)
    #print(dict)
    #print(dictToStoreZeroListOfStudentwithZeroMarks)
    #check if the csv file contains write data and are stored inside the dictionary
    if len(dict) is 0:
        listOfOutput.append("No class with correct row format exist. \n")
    else:
        TotalAvg=0.0
        for k,v in dict.items():
            classAvg[k] = "{0:0.1f}".format(sum(v)/len(v))
            TotalAvg += float("{0:0.1f}".format(sum(v)/len(v)))
        #print(classAvg)
        d3={v:k for k,v in classAvg.items()}
        listOfOutput.append("The Highest Performing class = " + d3[max(d3)] + " \n")
        listOfOutput.append("The average score for all students regardless of class = " +  "{0:0.1f}".format(TotalAvg / len(classAvg)) + "\n")
        listOfOutput.append("Average Score for classes:\n")
        for k,v in classAvg.items():
            listOfOutput.append(" -> "+"Average Score for " + k + " = " + v + "\n")
        for k,v in dict.items():
            listOfOutput.append(k + " Information: \n")
            if dictToStoreZeroListOfStudentwithZeroMarks.get(k):
                listOfOutput.append("-Total number of students within the " + k + " = " + str(len(dictToStoreZeroListOfStudentwithZeroMarks[k]) + len(v)) +"\n")
                listOfOutput.append("-Discarded Students in " + k + ":\n")
                for name in  dictToStoreZeroListOfStudentwithZeroMarks[k]:
                    listOfOutput.append(" -> " + name + "\n")
            else:
                listOfOutput.append("-Total number of students within the " + k + " = " + str(len(v)) + "\n")
                listOfOutput.append("-No Students Discarded. \n")
            listOfOutput.append("-Total Number of Student used to calculate " + k + " Average = " + str(len(v)) + "\n")
    insertIntoOutputFile()

def insertIntoOutputFile():
    try:
        output_file = open("Output.txt","w")
        for line in listOfOutput:
            output_file.write(line)
        output_file.close()
    except:
        print("File IO Exception")

def calculateGrades(f):
    try:
        listOfGrade = []
        listOfStudentWithMarksZero = []
        with open(f) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #print(row["Student Name"], row["Grade"])
                if row["Student Name"] and row["Grade"]:
                    if float(row["Grade"]) > 0 and float(row["Grade"]) <= 100:
                        listOfGrade.append(int(float(row["Grade"])))
                    else:
                        listOfStudentWithMarksZero.append(row["Student Name"])
        className = f.split('.')
        if len(listOfStudentWithMarksZero) != 0:
            dictToStoreZeroListOfStudentwithZeroMarks[className[0]] = listOfStudentWithMarksZero
        dict[className[0]] = listOfGrade

    except:
        listOfOutput.append(f + " row header is of wrong format" + "\n")

if __name__ == "__main__":
    findAllCsv()
