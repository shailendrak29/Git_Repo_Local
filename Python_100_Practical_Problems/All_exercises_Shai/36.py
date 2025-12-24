# Question: Please download the words1.txt file from the attachment and then
# create a Python function that takes a text file as input and returns the number of words contained in the text file.

file_path1= "D:\\Shailendra Kelkar\\Projects\\My_Git_Repo\\Python_100_Practical_Problems\\resources\\words1.txt"


def word_count (file_path) :
    try :
#         with open (file_path,'r', encoding='utf-8') as f: content = f.read()
        with open (file_path,'r', encoding='utf-8') as f:
            content = f.read()
            print (content)
            return (len(content.split()))
    except Exception as e:
        print (f"An error occurred : {e}")

print(word_count(file_path1))

# try :
#     with open (file_path,'r', encoding='utf-8') as f:
#         content = f.read()
#         print (content)
#         print (len(content.split()))
# except Exception as e:
#     print (f"An error occurred : {e}")