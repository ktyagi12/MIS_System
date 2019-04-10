print '*'* 140
print '\n\t\t\t\t\t\t\t\t','WELCOME TO KENDRIYA VIDYALAYA'
print '='* 140

choice = 0
student = {1: {'Division': 'A', 'Gender': 'M', 'Marks': [12, 23, 34, 45, 56], 'Name': 'ABC', 'Class': 'FE'},
		   2: {'Division': 'A', 'Gender': 'F', 'Marks': [34, 45, 56, 67, 78], 'Name': 'XYZ', 'Class': 'FE'},
		   4: {'Division': 'A', 'Gender': 'F', 'Marks': [98, 97, 54, 76, 78], 'Name': 'JKL', 'Class': 'FE'}
		  }

while (True):
	print '\n\t\t\t\t\t\t\t\t',' MIS SYSTEM'
	print '\t\t\t\t\t\t\t\t','1. ADD A STUDENT','\n\t\t\t\t\t\t\t\t','2. NUMBER OF GIRLS AND BOYS'
	print '\t\t\t\t\t\t\t\t','3. WHO\'S THE TOPPER','\n\t\t\t\t\t\t\t\t','4. COUNT OF STUDENTS'
	print '\t\t\t\t\t\t\t\t','5. DISPLAY STUDENT\'S DETAILS','\n\t\t\t\t\t\t\t\t','6. EXIT'
	choice = int(raw_input('Enter your choice: '))
	if (choice ==1):
		num_items = int(raw_input('\nHow many students you wanna add: '))
		for i in range(num_items):
			subject_list =[0]
			roll_no = int(raw_input('Roll number of the student: '))
			name_student = raw_input('Name of the student: ').upper()
			class_student = raw_input('Class of the student: ').upper()
			div_student= raw_input('Division of the student: ').upper()
			gender_student = raw_input('Gender of the student(M/F): ').upper()
			m1 = int(raw_input('Marks of subject1: ' ))
			m2 = int(raw_input('Marks of subject2: ' ))
			m3 = int(raw_input('Marks of subject3: ' ))
			m4 = int(raw_input('Marks of subject4: ' ))
			m5 = int(raw_input('Marks of subject5: ' ))
			subject_list = [m1,m2,m3,m4,m5]

			temp_student = {'roll_no' :roll_no,'name_student':name_student,'class_student':class_student,'div_student':div_student,'gender_student':gender_student,'marks': subject_list}
			if student.has_key(temp_student.get('roll_no')):
				print 'SORRY!! WRONG DETAILS.... SAME ROLL NO CANNOT BE ACCEPTED'
				exit()
			else:
				student[temp_student.get('roll_no')] ={'Name':temp_student.get('name_student'),'Class':temp_student.get('class_student'),'Division':temp_student.get('div_student'),'Gender':temp_student.get('gender_student'),
				'Marks':temp_student.get('marks')}
								
		print 'Your student has been admitted to our system:', student

	elif (choice ==2):
		count_girls = 0
		count_boys = 0
		class_student = raw_input('Class of the student: ').upper()
		div_student = raw_input('Division of the student: ').upper()
		for i in student.keys():
			if student.get(i)['Class'] == class_student and student.get(i)['Division'] == div_student :
				if student.get(i)['Gender'] == 'M' or student.get(i)['Gender'] == 'MALE':
					count_boys= count_boys + 1
				else:
					count_girls = count_girls + 1


			else:
				print '...NO SUCH CLASS AND DIVISION COMBINATION EXISTS...' 

		print 'Number of boys are: ' , count_boys
		print 'Number of girls are: ' , count_girls

	elif (choice ==3):
		sum = 0
		Percentage_list= []
		class_student = raw_input('Class of the student: ').upper()
		div_student = raw_input('Division of the student: ').upper()
		for i in student.keys():
			if student.get(i)['Class'] == class_student and student.get(i)['Division'] == div_student :
				for j in range(5):
					sum = sum + student.get(i)['Marks'][j]
										
				perc = (sum/5)
				Percentage_list.append(perc)
				print 'Roll number %d secured %d percent.' %(i,perc)
				sum = perc = 0
		#print 'Percentage_list: ', Percentage_list		
		for k in range(len(Percentage_list)):
			max_perc = Percentage_list[0]
			if Percentage_list[k] > max_perc:
				max_perc = Percentage_list[k]
				ind = k
		
		print 'Max is %d of index %d: ' %(max_perc,ind) 
		
		print 'The topper of this class is: '
		print '*' * 80
		print 'ROLL NUMBER: ', (ind+1)
		print 'NAME OF THE STUDENT', student.get(ind)['Name']
		print 'CLASS OF THE STUDENT', student.get(ind)['Class']
		print 'DIVISION OF THE STUDENT', student.get(ind)['Division']
		print 'GENDER OF THE STUDENT', student.get(ind)['Gender']
		print 'PERCENTAGE OF THE STUDENT',max_perc
		print '*' * 80
		
	elif (choice ==4):
		count_students = 0
		class_student = raw_input('Class of the student: ').upper()	
		for i in student.keys():
			if student.get(i)['Class'] == class_student:
				count_students = count_students +1
			else:
				print '...NO SUCH CLASS EXISTS'
		print 'Total number of students are:', count_students

	elif (choice ==5):
		roll_no = int(raw_input('Roll number of the student: '))
		if student.has_key(roll_no):
			print '*' * 80
			print 'ROLL NUMBER: ', roll_no
			print 'NAME OF THE STUDENT', student.get(roll_no)['Name']
			print 'CLASS OF THE STUDENT', student.get(roll_no)['Class']
			print 'DIVISION OF THE STUDENT', student.get(roll_no)['Division']
			print 'GENDER OF THE STUDENT', student.get(roll_no)['Gender']
			for j in range(5):
				print 'MARKS OF THE STUDENT IN SUBJECT %d ARE: %d' %((j+1),student.get(roll_no)['Marks'][j]) 
		else:
			print '...NO SUCH STUDENT EXISTS...'
			break

	elif (choice ==6):
		exit()
	else:
		print '\nOops!! Sorry!! No such option is available with us..'