f = open('Students.txt','r')
students = f.readlines()
f.close()
#print students

f = open('Marks.txt','r')
marks = f.readlines()
f.close()
#print marks

student_data = {}
marks_data = {}

for j in range(len(marks)):
	temp2 = marks[j]
	templist2 = temp2.split(",")
	templist2[2] =templist2[2].replace("\n", "")
	if marks_data.has_key(templist2[0]):
		marks_data[templist2[0]][templist2[1]] = templist2[2]
	else:
		marks_data[templist2[0]] = {templist2[1]:templist2[2]}
#print 'Marks: ',marks_data

for i in range(len(students)):
	temp = students[i]
	templist = temp.split(",")
	templist[4] =templist[4].replace("\n", "")
	student_data [templist[0]] = [templist[1],templist[2],templist[3],templist[4]]
#print 'Students: ',student_data

for i in student_data:
	if marks_data.has_key(i):
		student_data[i].append(marks_data[i])
		
print 'Students Data: ',  student_data

while (True):
	print '\n\t\t\t\t\t\t\t\t',' MIS SYSTEM'
	print '\t\t\t\t\t\t\t\t','1. ADD A STUDENT','\n\t\t\t\t\t\t\t\t','2. NUMBER OF GIRLS AND BOYS'
	print '\t\t\t\t\t\t\t\t','3. WHO\'S THE TOPPER','\n\t\t\t\t\t\t\t\t','4. COUNT OF STUDENTS'
	print '\t\t\t\t\t\t\t\t','5. DISPLAY STUDENT\'S DETAILS','\n\t\t\t\t\t\t\t\t','6. EXIT'
	choice = int(raw_input('Enter your choice: '))
	topper_keys = []
	topper_values =[]
	if (choice ==1):
		num_items = int(raw_input('\nHow many students you wanna add: '))
		for i in range(num_items):
			student_dict={}
			marks_dict ={}
			roll_no = str(int(raw_input('Roll number of the student: ')))
			if student_data.has_key(roll_no):
				print 'Roll number already exists...'
				break
			else:
				name_student = raw_input('Name of the student: ').upper()
				gender_student = raw_input('Gender of the student(M/F): ').upper()
				class_student = raw_input('Class of the student: ').upper()
				div_student= raw_input('Division of the student: ').upper()
				SUB1 = int(raw_input('Marks for Subject1: '))
				SUB2 = int(raw_input('Marks for Subject2: '))
				SUB3 = int(raw_input('Marks for Subject3: '))
				SUB4 = int(raw_input('Marks for Subject4: '))
				SUB5 = int(raw_input('Marks for Subject5: '))
				
				marks_dict[roll_no] = {'SUB1': SUB1, 'SUB2':SUB2,'SUB3':SUB3,'SUB4':SUB4,'SUB5':SUB5 }
				student_data[roll_no] = [name_student,gender_student,class_student,div_student,marks_dict[roll_no]]

		print student_data


	elif (choice ==2):
		count_girls = 0
		count_boys = 0
		class_student = raw_input('Class of the student: ').upper()
		div_student = raw_input('Division of the student: ').upper()
		
		for i in student_data.keys():
		
			if student_data.get(i)[2] == class_student and student_data.get(i)[3] == div_student :
		
				if student_data.get(i)[1] == 'M' or student_data.get(i)[1] == 'MALE':
		
					count_boys= count_boys + 1
				else:
					count_girls = count_girls + 1

		print 'Number of boys are: ' , count_boys
		print 'Number of girls are: ' , count_girls


	elif (choice ==3):
		print '\nStudents: ', student_data
		sum = 0
		ind = 0
		Percentage_list= {}
		class_student = raw_input('\nClass of the student: ').upper()
		div_student = raw_input('Division of the student: ').upper()
		
		for i in student_data.keys():
			if student_data.get(i)[2] == class_student and student_data.get(i)[3] == div_student :
				temp = student_data.get(i)[4].values()
				for j in range(5):
					sum = sum + int(temp[j])
				perc = (sum/5)
				
				Percentage_list[i]=perc
				print '\nRoll number %s secured %d percent.' %(i,perc)
				sum = perc = 0
		topper_keys= list (Percentage_list.keys())
		topper_values= list(Percentage_list.values())
		
		for l in range(len(topper_values)) :
			max_perc = topper_values[0]
			if topper_values[l] >= max_perc:
				max_perc = topper_values[l]
				
			ind = topper_values.index(max_perc)
		print 'The topper of this class is: '
		print '*' * 80
		print 'ROLL NUMBER: ', topper_keys[ind]
		print 'NAME OF THE STUDENT', student_data.get(topper_keys[ind])[0]
		print 'CLASS OF THE STUDENT', student_data.get(topper_keys[ind])[2]
		print 'DIVISION OF THE STUDENT', student_data.get(topper_keys[ind])[3]
		print 'GENDER OF THE STUDENT', student_data.get(topper_keys[ind])[1]
		print 'PERCENTAGE OF THE STUDENT',max_perc
		print '*' * 80


	elif (choice ==4):
		count_students = 0
		class_student = raw_input('Class of the student: ').upper()	
		for i in student_data.keys():
			if student_data.get(i)[2] == class_student:
				count_students = count_students +1
		print 'Total number of students are:', count_students



	elif (choice ==5):
		roll_no = str(int(raw_input('Roll number of the student: ')))
		if student_data.has_key(roll_no):
			print '*' * 80
			print 'ROLL NUMBER: ', roll_no
			print 'NAME OF THE STUDENT: ', student_data.get(roll_no)[0]
			print 'CLASS OF THE STUDENT: ', student_data.get(roll_no)[2]
			print 'DIVISION OF THE STUDENT: ', student_data.get(roll_no)[3]
			print 'GENDER OF THE STUDENT: ', student_data.get(roll_no)[1]
			print 'MARKS OBTAINED BY THE STUDENT ARE: ',student_data.get(roll_no)[4]
		else:
			print '...NO SUCH STUDENT EXISTS IN OUUR RECORDS...'


	elif (choice ==6):
		exit()


	else:
		print '\nOops!! Sorry!! No such option is available with us..'
	
		