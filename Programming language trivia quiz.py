print("Hello , welcome to trivia!")               

ans = input("Are you ready to begin (yes/no): ")
score = 0
total_q = 10

if ans == "yes":
    ans = input("1.What was the world's first commercially available programming language? ").lower()
    if ans == "fortran" :
        score += 1
        print("correct")
    else:
        print("incorrect")
        
    ans = input("2.What is the name of the programming language created by Guido van Rossum? ").lower()
    if ans == "python" :
        score += 1
        print("correct")
    else:
        print("incorrect")    
        
    ans = input("3.When 'C' language was created? ").lower()
    if ans == "1972" :
        score += 1
        print("correct")
    else:
        print("incorrect")   
        
    ans = input("4.Name the text-based programming language used to make web pages interactive? ").lower()
    if ans == "javascript" :
        score += 1
        print("correct")
    else:
        print("incorrect")    
        
    ans = input("5.Which language has a filename extension '.pp'? ").lower()
    if ans == "pascal" :
        score += 1
        print("correct")
    else:
        print("incorrect")   
        
    ans = input("6.What is the website of the language C#? ").lower()
    if ans == "csharp.net" :
        score += 1
        print("correct")
    else:
        print("incorrect")  
        
    ans = input("7.The basic building block language of the Web is? ").lower()
    if ans == "html" :
        score += 1
        print("correct")
    else:
        print("incorrect")    
    
    ans = input("8.Who was the developer of BASIC? ").lower()
    if ans == "microsoft" :
        score += 1
        print("correct")
    else:
        print("incorrect") 
        
    ans = input("9.Name the language which originated in Japan and its name resembles to a gem? ").lower()
    if ans == "ruby" :
        score += 1
        print("correct")
    else:
        print("incorrect")   
        
    ans = input("10.Which language is represented with the image of a Camel? ").lower()
    if ans == "perl" :
        score += 1
        print("correct")
    else:
        print("incorrect")    
        

    print(" Thank you for playing, you got " , score, " questions correct.").lower()
    mark = (score/total_q) * 100

    print("Mark:" , mark)

print("Goodbye") 
