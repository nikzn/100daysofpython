names=[]
content=''
with open("/home/alignminds/Desktop/Nikhil Workspace/COURSES/PYTHON/pythonProject/DAY 24/Mail Merge Project Start/Input/Names/invited_names.txt") as name:
    for x in name:
        text=x.strip("\n")
        names.append(text)

with open("/home/alignminds/Desktop/Nikhil Workspace/COURSES/PYTHON/pythonProject/DAY 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
        content= file.read()


for mail in names:
    contents=content.replace("[name]",f"{mail}")
    with open(f"/home/alignminds/Desktop/Nikhil Workspace/COURSES/PYTHON/pythonProject/DAY 24/Mail Merge Project Start/Output/ReadyToSend/{mail}_mail.txt",mode="w") as mail:
        mail.write(contents)
