#Python for Programmers 
#Grading system

pointspossible = 100
# score = 60
studentname = "Shailendra Kelkar"


try : 
    score = int(input("Enter the score : " ))
    if score < 0 or score > pointspossible:
        grade = "OUT OF RANGE"
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 0:
        grade = "F"
except Exception :
    grade = "INVALID INPUT"
    
print ("Student Name: {} received grade {}".format(studentname, grade))
