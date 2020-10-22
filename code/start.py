import text2voice as t2v
import main

s="*"*100
e="-"*100
print(s)
print("Welcome to Voice based text summarization system (Natural Language Processing Project)")
print(e)
t2v.speechTrans("Welcome to Voice based text summarization system (Natural Language Processing Project)")
print("Contributors - 1. Gauri Shanakar Gupta \n2. Yash Jhunjunwala \n3. Sachi Sainath \n4. Ritul Koladiya")

print("\nInstructions - \n1.Make Sure python3 is installed and added to the path.\n2.If not check the python location by running location.bat file \n3.Now you need to run req.bat file to download all the dependencies.\n4.After Installing all dependencies press 1 to start with the summarizer.")
n=int(input())

while n!=1:
    print("Not a valid input")
    t2v.speechTrans("Not a valid input")
    n=int(input("Enter valid input-"))

if n==1:
    main.final()
