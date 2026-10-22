#2.1 Vocabulary Review

#1. Git is the local software used to track changes in your code, while GitHub is a cloud-based platform built to host those Git projects and help teams collaborate.
#2. Terminal is the graphical window application that displays text, while the command line is the actual text-based interface system. 
#3. A local repository resides directly on your own computer, whereas a remote repository is hosted on an external server or internet-based platform.
#4. Version control is a software engineering practice that tracks, records, and manages changes to files and source code over time.
#5. A staging area is a designated physical or digital location where people, vehicles, equipment, or data are temporarily gathered, organized, and prepared before moving on to their final destination or operational phase. 
#6. The git add command moves changes from your working directory into the staging area.
#7. The git commit is a save point or local snapshot of my project's files at a specific moment in time.
#8. The git push is the command used to upload your local repository commits to a remote repository.  
#9. The git status is a core utility used to display the current state of your working directory and staging area.
#10. The git pull is a Git command used to download changes from a remote repository and immediately merge them into your local working branch.
#11. pwd = shows which folder you are currently in
#12. ls = lists files and folders in your current folder 
#13. cd = moves into a folder
#14. nano = opens a file for editing in the terminal
#15. touch = creates new file 
#16. mv = move
#17. rm = remove
#18. cat = reads files and prints contents

#2.2 A Directory Tree

#1. pwd
#2. ls
#3. cd ../brianna_repo
#   git pull
#4. mv homework.py ../judy_decal/homework/
#5. cd ../judy_decal/homework/
#6. cat homework.py
#7. git add homework.py
#   git command -m "Done homework"
#   git push
#8. git pull --rebase origin main
#   git push origin main
#   git add homework.py
#   git rebase --continue
#   git push origin main
#9. cd ~/Recent/

#2.3 Draw Your Directory Tree

#3. 
#3.1 Data Types
def checkDataType(blank):
	return type(blank).__name__

blank = 15
print(checkDataType(blank))

#3.2 Conditionals
def evenOrOdd(number):
	if number % 2 == 0:
		return "Even"
	else: 
		return "Odd"

number = 15
print(evenOrOdd(number))

#4 Loops
numbers = [1, 2, 3, 4, 5]

def sumWithLoop(numbers):
	total_sum = 0
	for i in numbers:
		total_sum += i
	return total_sum

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

#5 Homework 4 Review

#5.1 Lists
items = ['a', 'b', 'c']

def duplicateList(items):
	result = []
	for i in items:
		result.append(items)
		result.append(items)
	return result

print(duplicateList(items))

#5.2 Debugging

def square(num):
	return num * num

num = 12
print(square(num))

#Favorite Function

items = ['apple', 'peach', 'grape']

def duplicateList(items):
	result = []
	for item in items:
		result.append(items)
		result.append(items)
	return result

print(duplicateList(items))
