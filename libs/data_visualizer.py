import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
import numpy as np


def list_o_strings_to_list_o_ints(array):
	list_int = []
	for x, y in enumerate(array):
	    list_int.append([int(y) for y in y])
	return list_int

def process_data(dataset):
	'''
	t = get_movement(dataset[::10])

	from libs.data_visualizer import process_data

	process_data(t)
	'''
	for data in dataset:

		#get the int from the string 
		iteration = data.split()[1]

		#num of occurance
		num_of_occurance = dataset[data]['occurence']['num_of_occurences']
		#print(num_of_occurance)

		plt.plot(iteration, int(num_of_occurance), 'o')

	plt.show()

def plot_lines(data):
	'''
	a = build_the_dataset(t, dataset)

	plot_lines(a)
	'''
	for line in data:
		parsed = np.array(list_o_strings_to_list_o_ints(line))
		x, y = parsed.T
		plt.plot(x, y)

	plt.show()