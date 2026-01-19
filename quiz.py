print("Hi,welcome to the Quiz!")
play = input("Do you want to play(yes/no) :\n").lower()
if play != "yes":
    quit()
print("Okay,Let's Play!!!")
score = 0 
answer = input("What does RAG stands for : \n").lower()
if answer == "retrieval augmented generation":
    print("Correct!!!")
    score = score + 1
else:
    print("Incorect!") 
answer = input("What does GAN stands for : \n").lower()
if answer == "generative adversial network":
    print("Correct!!!")
    score = score + 1
else:
    print("Incorect!")  
answer = input("What does  DFS for : \n").lower()
if answer == "depth first search":
    print("Correct!!!")
    score = score + 1
else:
    print("Incorect!")  
answer = input("What does BFS stands for : \n").lower()
if answer == "breadth first search":
    print("Correct!!!")
    score = score + 1
else:
    print("Incorect!")      
print(f"Your score is {score}")
print("Thank You !!")