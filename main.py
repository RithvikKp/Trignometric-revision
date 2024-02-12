#importing the manual built module
import Answers as ans

#Getting input to start the revision
start = input("Do you want to start the revision session?\ny/n: ")

while(True): #Loop will continue till the user decides to stop
  print()
  if start == "y": 
    #generating a question from the list of questions
    choice = int(input('''Enter 1 for revising sin formulas\nEnter 2 for revising cos formulas\nEnter 3 for revising tan formulas\nEnter 4 for revising cot formulas\n'''))
    
    print()
    
    if(choice == 1):
      ans.sin()
    elif(choice == 2):
      ans.cos()
    elif(choice == 3):
      ans.tan()
    elif(choice == 4):
      ans.cot()
 
    print("\n")
    
    re_try = input("Do you want to continue the revision?\ny/n: ") #Asking oppinion for playing again
    re_try = re_try.upper()
    if (re_try == "Y"):
      continue
    elif(re_try == "N"):
      print()
      print("Hope you will come back soon!")
      break
