def dictionary():
	d = {}
	schoice2 = 1
	while (schoice2 != 0):
		print '1. Create dictionary'
		print '2. Display dictionary'
		print '3. Clear dictionary'
		print '4. Display keys'
		print '5. Display values'
		print '0. Exit'
		schoice2=input('Enter your choice - ')
		if schoice2 == 0:
			break
		elif schoice2 == 1:
			d = input('Enter dictionary elements - ')
		elif schoice2 == 2:
			print d
		elif schoice2 == 3:
			d.clear()
		elif schoice2 == 4:
			print d.keys()
		elif schoice2 == 5:
			print d.values()

def lists():
	li = []
	schoice2 = 1
	while(schoice2 != 0):
		print '1. Create list'
		print '2. Display list'
		print '3. Search list'
		print '4. Slice list'
		print '5. Append list'
		print '6. Extend list'
		print '7. Insert into list'
		print '8. Search list'
		print '9. Delete element'
		print '0. Exit'
		schoice2=input('Enter your choice - ')
		if schoice2 == 0:
			break
		elif schoice2 == 1:
			li=input('Enter list elements - ')
		elif schoice2 == 2:
			print li
		elif schoice2 == 3:
			index=0
			index=input('Enter the index - ')
			print li[index]
		elif schoice2 == 4:
			index1=0
			index2=0
			index1=input('Enter index 1 - ')
			index2=input('Enter index 2 - ')
			print li[index1:index2]
		elif schoice2 == 5:
			li2=[]
			li2=input('Enter list to append - ')
			li.append(li2)
		elif schoice2 == 6:
			li2=[]
			li2=input('Enter list to extend - ')
			li.extend(li2)
		elif schoice2 == 7:
			index_elem=0
			index_elem=input('Enter the index - ')
			element=input('Enter the element - ')
			li.insert(index_elem,element)
		elif schoice2 == 8:
			element=input('Enter element to search - ')
			if element in li:
				print li.index(element)
			else:
				print 'Element not found'
		elif schoice2 == 9:
			element=input('Enter element to delete - ')
			if element in li:
				li.remove(element)
			else:
				print 'Element not found'

def tuples():
	tuples = []
	schoice2 = 1
	while(schoice2 != 0):
		print '1. Create list'
		print '2. Display list'
		print '3. Search list'
		print '4. Slice list'
		print '5. Check list'
		print '0. Exit'
		schoice2=input('Enter your choice - ')
		if schoice2 == 0:
			break
		elif schoice2 == 1:
			tuples=input('Enter list elements - ')
		elif schoice2 == 2:
			print tuples
		elif schoice2 == 3:
			index=0
			index=input('Enter the index - ')
			print tuples[index]
		elif schoice2 == 4:
			index1=0
			index2=0
			index1=input('Enter index 1 - ')
			index2=input('Enter index 2 - ')
			print tuples[index1:index2]
		elif schoice2 == 5:
			element=input('Enter element to check - ')
			if element in tuples:
				print 'Element present'
			else:
				print 'Element not present'

schoice = 1
while (schoice != 0):
	print '1. Dictionary'
	print '2. List'
	print '3. Tuples'
	print '0. Exit'
	schoice=input('Enter your choice - ')
	if schoice == 0:
		break
	elif schoice == 1:
		dictionary()
	elif schoice == 2:
		lists()
	elif schoice == 3:
		tuples()
