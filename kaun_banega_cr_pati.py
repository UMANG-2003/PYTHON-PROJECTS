questions = [
["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],
["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],
["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],
["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],
 ["Which language was used to create fb","python","french","java-script","php","none",4],

 ["Which language was used to create fb","python","french","java-script","php","none",4],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,500000,10000000]

for i in range(0,len(questions)):
   question = questions[i]
   print(f"Question for Rs.{levels[i]}")
   print(f"a.{question[1]}             b. {question[2]}")
   print(f"c.{question[3]}        d. {question[4]}")

   reply = int(input("Enter your answer(1-4) :"))
   if(reply == question[-1]):
      print(f"Correct answer, you won {levels[i]}")
      if(i == 4):
         money = 10000
         print("credited money : \n",money)   
      elif (i == 9):
         money = 32000
         print("credited money : \n",money)   
      elif (i == 9):
         money = 10000000
         print("credited money : \n",money)   
       
   else:
      print("wrong answer")
      break  