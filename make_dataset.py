from libs.data_visualizer import *



file = "data/data.txt"


class parseFile:
	'''
	@this will parse the file for the cords and return a list of them
	:path :str  
	'''
	def __init__(self, path: str):
		self.path = path
		self.dataset = []

		with open(self.path, "r") as file:
			for x in file.read().split('|'):
				try:
					self.dataset.append(self.get_points_from_slice(x))
				except IndexError:
					pass

	def get_points_from_slice(self, slice: str):
		cord = slice.split(', ')
		return [cord[0], cord[1]]

 

#goal to plot the points in linear time, based on occurence
def get_movement(dataset):
	'''
	{
		point 1:{
			x: "",
			y: "",
			occurence:{
				num_of_occurences: 1,
				start: 1,
				end: 54
			}
		}
	}
	'''
	pointDict = {}

	Preveus_Point = [0,0]
	Preveus_String = None

	Point_Counter = 0

	for cord in dataset:
		first_string = f"Point  {Point_Counter}" 

		#first add the first point
		if len(pointDict) == 0:

			pointDict[first_string] = {'x': int(cord[0]),\
										'y': int(cord[1]),\
										'occurence': {
											"num_of_occurences":1,\
											"start":Point_Counter,\
											"end":Point_Counter
										}}

			#update the previous points
			Preveus_Point = cord[0], cord[1]

			#update the key name of the previous string so we can access it on the next iteration
			Preveus_String = first_string

			#finally update the point counter
			Point_Counter += 1

			continue


		#if the next cords are the same as the previouse cords
		if (cord[0], cord[1]) == (Preveus_Point[0], Preveus_Point[1]):

			#update the occurance 
			pointDict[Preveus_String]['occurence']['num_of_occurences'] +=1

			#update the end
			pointDict[Preveus_String]['occurence']['end'] += 1


		else:


			#add the new point
			pointDict[first_string] = {'x': int(cord[0]),\
										'y': int(cord[1]),\
										'occurence': {
											"num_of_occurences":1,\
											"start":Point_Counter,\
											"end":Point_Counter
										}}

			#update the previous points
			Preveus_Point = cord[0], cord[1]

			#update the key name of the previous string so we can access it on the next iteration
			Preveus_String = first_string


		#finally update the point counter
		Point_Counter += 1


	return pointDict





#make an json file of point arrays without the pauses 
def build_the_dataset(data_info, dataset):

	'''
	@set accuraccy

		space_range: how long was the mouse in one position
		move_buffer: how long the mouse was in motion

	'''
	movement_arrays = []

	#this is the space buffer range
	space_buffer = list(range(4,500))

	#move buffer range
	move_buffer = list(range(10,500))

	#end of the space
	temp_end = 0


	#get highest points
	for x in data_info:
		if data_info[x]['occurence']['num_of_occurences'] in space_buffer:
			
			#print(f"start {data_info[x]['occurence']['start']}")
			#print(f"end {data_info[x]['occurence']['end']}")


			#if we pass the first space
			if temp_end != 0:
				#print(temp_end, data_info[x]['occurence']['start'])
				if len(dataset[temp_end:data_info[x]['occurence']['start']]) in move_buffer:
					movement_arrays.append(dataset[temp_end:data_info[x]['occurence']['start']])

			#update the temp end
			temp_end = data_info[x]['occurence']['end']

	return movement_arrays


pf = parseFile(file)
dataset = pf.dataset

t = get_movement(dataset)
a = build_the_dataset(t, dataset)

plot_lines(a)


