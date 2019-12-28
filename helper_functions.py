import csv

def generate_array(name):
	"""This method opens the passed file and returns an array filled with data
	from the file."""
	with open(name, 'r') as training_data:
		training_data = list(csv.reader(training_data, delimiter=';'))
	training_data = [j.split(',') for i in training_data for j in i]
	new_data = []
	holder = []
	for i in training_data:
		for j in i:
			holder.append(float(j))
		new_data.append(holder)
		holder = []
	return new_data

def collapse(list_1, list_2):
	"""This method takes in two lists and puts the two lists in one."""
	master_list = []
	for i in list_1:
		master_list.append(i)
	for i in list_2:
		master_list.append(i)
	return master_list