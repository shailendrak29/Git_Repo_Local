# movie = input("What\'s your favorite movie?:")

# print("movie is " + movie      )

# try:
#     YOB = int(input("What\'s your year of birth?:"))
# # print("Year of birth is " + str(YOB))
# except Exception:
#     YOB = "INVALID INPUT"

# print("Year of birth is {}".format(YOB))



def printtype(in_par):
    # out_par = "Blank"
    if type(in_par) is str :
        return ("String")
    elif type(in_par) is int :
        return ("Int")
    elif type(in_par) is float:
        return("Float")

printtype("Hello")

print (type("Hello"))
print (type(5))
print (type(5.5))

if type("Hello") is str :
    print ("String")

    