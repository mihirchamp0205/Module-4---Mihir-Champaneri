#What is File function in python? What is keywords to create and write file.
#Ans: A file objects allows us to use,access and manipulate all the user accessible files.

    # "x" - Create -will create a file, returns an error if the file exist.
    # "w" - Write  - will create a file if the specifiled file does not exist.

#Write a Python program to read an entire text file.

f=open("myfile.txt","r")

print(f.read())
f.close()


#Write a Python program to append text to a file and display the text.

f=open("myfile.text","a")
f.write("\nEight")
f.close()



#Write a Python program to read a file line by line and store it into a list.

with open("data.txt") as f:
    content_list = f.readlines()

# print the list
print("Given List is :" ,content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print("New List is :" ,content_list)


#Write a Python program to read a file line by line store it into a variable.

f = open("data1.txt","r")
str=""

for i in range(0,100):
    str=str + f.read(i)

print(str)



#Write a python program to find the longest words.

n=int(input("Enter The Value of N:"))

f=open("data.txt","r")
s=f.read()
lst=s.split()

for i in lst:
    if(len(i)>n):
       print(i)




#Write a python program to find the max and min words.

n=int(input("Enter The Max or min words Length of N:"))

f=open("data.txt","r")
s=f.read()
lst=s.split()

print(max(lst,key=len))
print(min(lst,key=len))


#Write a Python program to count the number of lines in a text file.

file=open("data1.txt","r")
count=0
# store the string in content

content=file.read()
list=content.split('\n')

print(list)

for i in list:
    if i:
        count+=1
print("Number of Line in File Are:",count)

file.close()



#Write a Python program to count the frequency of words in a file.

file=open("data.txt","r")

wrd=input("Enter The Word To Be Search:")

# store in string in s

s=file.read()
lst=s.split()

count=0
for i in lst:
    if i==wrd:
        count+=1

print("Word {} Occurred {} Time".format(wrd,count))


#Write a Python program to count the frequency of words in a file.

file=open("data.txt","r")

wrd=input("Enter The Word To Be Search:")

# store in string in s

s=file.read()
lst=s.split()

count=0
for i in lst:
    if i==wrd:
        count+=1

print("Word {} Occurred {} Time".format(wrd,count))


#Write a Python program to copy the contents of a file to another file.

file1=open("data1.txt","r")
file2=open("copy.txt","w")

s=file1.read()
file2.write(s)

file1.close()
file2.close()














