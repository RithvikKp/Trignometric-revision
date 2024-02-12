import random
import Question_options as mod

def sin():
  qa = random.choice(mod.ques_sin) 
  print("Here is your question: ",qa)

  print("Here is your options:\n")

  #loop to take the key from the disctionary
  for i in mod.sin_value: 
    #loop to get the value of that key
    for j in range(int(i),len(mod.sin_value)+1): 
      print(i,")",mod.sin_value[str(j)]) #printing the options, with the key and value visible
      break #breaking to give the next option

  print()

  #getting user's answer
  ans = input("Enter your answer: ") #getting user answer
  #collecting the value from module for the key entered by the user
  Input_ans = mod.Sin(ans)
  print()
  #finding, position of the question in the list
  position_of_question = mod.ques_sin.index(qa) 
  #increasing by one so that the index value matches the key of the dictionary
  position_of_question += 1 

  #Loop to find the possition of the correct answer to the question generated
  for i in range(1,len(mod.sin_value)+1):
    #Once found storing it in one variable
    if (i == position_of_question): 
     position_of_answer = str(i)
     break

  #cheking if both the  values are same, correct answer and input answer
  if (str(i) == str(ans)):
    print("Congratulation you got the correct answer!!")

  else:
    print("Oops!, Sorry better luck next time")
    print("The answer you entered is: ",Input_ans) #printing the user's answer
    print("The correct answer is: ",mod.sin_value[str(i)]) #printing the correct answer

def cos():
  qa = random.choice(mod.ques_cos) 
  print("Here is your question: ",qa)

  print("Here is your options:\n")

  #loop to take the key from the disctionary
  for i in mod.cos_value: 
    #loop to get the value of that key
    for j in range(int(i),len(mod.cos_value)+1): 
      print(i,")",mod.cos_value[str(j)]) #printing the options, with the key and value visible
      break #breaking to give the next option

  print()

  #getting user's answer
  ans = input("Enter your answer: ") #getting user answer
  #collecting the value from module for the key entered by the user
  Input_ans = mod.Cos(ans)
  print()
  #finding, position of the question in the list
  position_of_question = mod.ques_cos.index(qa) 
  #increasing by one so that the index value matches the key of the dictionary
  position_of_question += 1 

  #Loop to find the possition of the correct answer to the question generated
  for i in range(1,len(mod.cos_value)+1):
    #Once found storing it in one variable
    if (i == position_of_question): 
     position_of_answer = str(i)
     break

  #cheking if both the  values are same, correct answer and input answer
  if (str(i) == str(ans)):
    print("Congratulation you got the correct answer!!")

  else:
    print("Oops!, Sorry better luck next time")
    print("The answer you entered is: ",Input_ans) #printing the user's answer
    print("The correct answer is: ",mod.cos_value[str(i)]) #printing the correct answer

def tan():
    qa = random.choice(mod.ques_tan) 
    print("Here is your question: ",qa)

    print("Here is your options:\n")

    #loop to take the key from the disctionary
    for i in mod.tan_value: 
      #loop to get the value of that key
      for j in range(int(i),len(mod.tan_value)+1): 
        print(i,")",mod.tan_value[str(j)]) #printing the options, with the key and value visible
        break #breaking to give the next option

    print()

    #getting user's answer
    ans = input("Enter your answer: ") #getting user answer
    #collecting the value from module for the key entered by the user
    Input_ans = mod.Tan(ans)
    print()
    #finding, position of the question in the list
    position_of_question = mod.ques_tan.index(qa) 
    #increasing by one so that the index value matches the key of the dictionary
    position_of_question += 1 

    #Loop to find the possition of the correct answer to the question generated
    for i in range(1,len(mod.tan_value)+1):
      #Once found storing it in one variable
      if (i == position_of_question): 
       position_of_answer = str(i)
       break

    #cheking if both the  values are same, correct answer and input answer
    if (str(i) == str(ans)):
      print("Congratulation you got the correct answer!!")

    else:
      print("Oops!, Sorry better luck next time")
      print("The answer you entered is: ",Input_ans) #printing the user's answer
      print("The correct answer is: ",mod.tan_value[str(i)]) #printing the correct answer

def cot():
  qa = random.choice(mod.ques_cot) 
  print("Here is your question: ",qa)

  print("Here is your options:\n")

  #loop to take the key from the disctionary
  for i in mod.cot_value: 
    #loop to get the value of that key
    for j in range(int(i),len(mod.cot_value)+1): 
      print(i,")",mod.cot_value[str(j)]) #printing the options, with the key and value visible
      break #breaking to give the next option

  print()

  #getting user's answer
  ans = input("Enter your answer: ") #getting user answer
  #collecting the value from module for the key entered by the user
  Input_ans = mod.Cot(ans)
  print()
  #finding, position of the question in the list
  position_of_question = mod.ques_cot.index(qa) 
  #increasing by one so that the index value matches the key of the dictionary
  position_of_question += 1 

  #Loop to find the possition of the correct answer to the question generated
  for i in range(1,len(mod.cot_value)+1):
    #Once found storing it in one variable
    if (i == position_of_question): 
     position_of_answer = str(i)
     break

  #cheking if both the  values are same, correct answer and input answer
  if (str(i) == str(ans)):
    print("Congratulation you got the correct answer!!")

  else:
    print("Oops!, Sorry better luck next time")
    print("The answer you entered is: ",Input_ans) #printing the user's answer
    print("The correct answer is: ",mod.cot_value[str(i)]) #printing the correct answer
