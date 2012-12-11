#parser.py
#This file will calculate the shortest and cheapest route between two underground stations
#It uses a modified version of Dijkstra's algorithm. READ THE WIKIPEDIA ARTICLE FOR A FULL EXPLANATION
#Uncomment this first line if you want it to randomly select stations for example purposes
#from random import choice

#Parser section
def arrayFromBlock(block):
	#Strip whitespace
	block = block.strip();
	#Strip opening and closing square brackets
	block = block[block.find("[") + 1: block.rfind("]")].strip()
	#Split at comma
	splitAtComma = block.split(",")
	createdArray = []
	#Create the array, easy.
	for s in splitAtComma:
		createdArray.append(s.replace("\"", "").strip())
	return createdArray

#Assume an example is being fed to the function (note that the file is already split at @ symbols)
#zone
#{
#	name = "zone_name",
#	neighbours = ["neighbour1", "neighbour2", "neighbour3"]
#}
def dictionaryFromBlock(block):
	#Create a dictionary to return
	dict = {}
	#Remove whitespace
	block = block.strip()
	#Get rid of the opening and closing braces
	block = block[block.find("{") + 1: block.rfind("}") - 1].strip()
	#Split at each equal sign
	splitAtEquals = block.split("=")
	#The value of the array is now the following:
	#'name', '"zone_name",\nneighours','["neighbour1", "neighbour2", "neighbour3"]'
	newSplit = []
	#Iterate over each block to build the split array and appropriately group arrays
	for n in range(0, len(splitAtEquals)):
		#This gets rid of surrounding whitespace (so ' name ' becomes 'name')
		splitAtEquals[n] = splitAtEquals[n].strip()
		#I.e. if the value being examined couldn't be an array value
		if "[" not in splitAtEquals[n]:
			#Split at a new line so zone_name\nneighbours -> 'zone_name', 'neighbours'
			splitAtNewLine = splitAtEquals[n].split("\n")
			#Add the split values to the new array
			for l in splitAtNewLine:
				newSplit.append(l.strip())
		#Else If this is not the final value in the array (because it contains a [ or ])
		elif n != len(splitAtEquals) - 1:
			#At this stage something like '"station",\n"neighbour"' becomes 'station', '\nneighbour'
			#Seperate at the very last comma (which, if this is an array value, will be after the array)
			newSplit.append(splitAtEquals[n][0:splitAtEquals[n].rfind(",")].strip())
			#Split everything after the comman
			newSplit.append(splitAtEquals[n][splitAtEquals[n].rfind(",")+1:len(splitAtEquals[n])].strip())
		else:
			#Otherwise just add the contents
			newSplit.append(splitAtEquals[n])
	#If the above loop isn't making much sense it is probably worth uncommenting the print() calls so you can examine
	#the array at different stages to understand how it is getting built
	#Build the dictionary
	for n in range(0, len(newSplit), 2):
		if n + 1 < len(newSplit):
			if "[" not in newSplit[n + 1]:
				dict[newSplit[n]] = newSplit[n + 1].replace("\"", "").replace(",", "")
			else:
				dict[newSplit[n]] = arrayFromBlock(newSplit[n + 1])
	return dict

#Routing section

#Read in the zones.txt file
zoneFile = open("zones.txt").read()

#Blocks all begin with @ symbols, so therefore we split at them
zoneBlocks = zoneFile.split("@")

#Station connections is a dictionary where the station name is the key and each value is an array of
#connected sations
sC = {}
#Station list is an array of all the known stations
stationList = []

#The connection types. It is a dictionary of dictionaries:
#sCTypes[stationA][connectedStation] = [lines,that,connect,them]
sCTypes = {}

#The zone that each station is in (station name is the key, value is zone)
stationZones = {}
#A dictionary of dictionaries for the cost of travel between zones. zoneCost[zoneA][zoneB] = cost
zoneCosts = {}

#Iterate over the zones
for zBlock in zoneBlocks:
	#Ignore whitespace
	if zBlock != "":
		#Get a dictionary from the block
		zDict = dictionaryFromBlock(zBlock)
		#Get rid of the zone part of the name and then get the value of the zone. 'zone1' -> 1
		zone = int(zDict["name"].replace("zone", ""))
		#Iterate over stations in the zone
		for station in zDict['stations']:
			#Create a blank array for connected stations
			sC[station] = []
			#Create empty dictionary
			sCTypes[station] = {}
			#Add the station to the station list (allows for repetitions, doesn't matter)
			stationList.append(station)
			#Add the station to the zone
			stationZones[station] = zone
		#Insert the costs for the zone
		zoneCosts[zone] = {}
		#The data only has 6 zones, MUST UPDATE for future zone additions
		for i in range(1, 6):
			zoneCosts[zone][i] = float(zDict["zone" + str(i)])

#Open up the stations data file
stationsFile = open("stations.txt").read()

#Again, split at the @ symbol
stationsBlocks = stationsFile.split("@")

#Iterate over the station blocks
for sBlock in stationsBlocks:
	if sBlock != "":
		#Get a dictionary for the station
		dictForStation = dictionaryFromBlock(sBlock)
		#This is the only effective way of iterating keys of a dictionary in Python 2.7

		for key, value in dictForStation.items():
			#All of the keys that aren't 'name' are Underground lines and the stations that are
			#connected by that line
			if key != 'name':
				#Iterate over the stations on that line
				for connectedStation in dictForStation[key]:
					#If this station isn't already in sC (should be added in the zone loop)
					if not dictForStation['name'] in sC:
						#Add empty array
						sC[dictForStation['name']] = [connectedStation]
					else:
						if connectedStation not in sC[dictForStation['name']]:
							#If we didn't know that the stations are connected, connect them
							sC[dictForStation['name']].append(connectedStation)
					#Now do the same for the connection type (i.e. the line that the two stations are on)
					if connectedStation not in sCTypes[dictForStation['name']]:
						sCTypes[dictForStation['name']][connectedStation] = [key]
					else:
						sCTypes[dictForStation['name']][connectedStation].append(key)

#Use these two lines if you want the user to enter their desired station
#Remember that they must enter the exact text
location = raw_input("Please enter your start station: ")
target = raw_input("Please enter your end station: ")

for station in  stationList:
	if station.lower().find(location.lower()) == 0:
		location = station
	if station.lower().find(target.lower()) == 0:
		target = station;

#When testing I was randomly selecting stations, uncomment the top line to import choice to use these
#location = choice(stationList)
#target = choice(stationList)

#This line is in case the computer is selecting a station
print("\nAt " + location + ", going to " + target + "\n")

#Look up difference in zones and present cost

#This dictionary contains the station as the key and the total number of stops required to reach it
distances = {} #Create new dictionary for calculating distances to Station

#Iterate over all stations and set the distance to that station to Infinity
for key, value in sC.items():
	distances[key] = float("+inf") #Positive Infinity

#We don't have to visit anywhere else to visit the current station, so the distance is set to 0
distances[location] = 0

#This function is recursive, you call it with a station that you know the distance to
def visitNode(node):
	changed = [] #Keep track of any nodes whose distance has been changed
	#Iterate over the neighbours of the current station
	for neighbour in sC[node]:
		#If it is easier to visit the current station by coming from this station update its distance
		if distances[node] + 1 < distances[neighbour]:
			distances[neighbour] = distances[node] + 1
			changed.append(neighbour) #Changed distance, add it to change list
	#Now visit everything that got changed
	for neighbour in changed:
		visitNode(neighbour) #Update anything that got changed

#Start by visiting the current point and recursively calculating the total distance to each point
visitNode(location)

#This finds the lowest distance of any of the neighbours of this point
def lowestNeighbourDistance(stationPoint):
	lowest = float("+inf")
	for neighbour in sC[stationPoint]:
		if distances[neighbour] < lowest:
			lowest = distances[neighbour]
	return lowest

#Now we need to figure out the route that we took through

#Create a route and start at the end point working backwards
route = []
route.append(target)

#Start at the end of the route
point = target
previous = point

#Stop iterating when we have returned to the beginning, which will happen eventually
while point != location:
	#Set the default next point to the first neighbour of the current point
	newPoint = sC[point][0]
	newPointDistance = distances[point]


	#The 'lowest neighbour distance' is the lowest distance of a neighbour station of the current point
	lowestN = float("+inf")

	#Go over the neighbours of the current point
	for neighbour in sC[point]:
		#If it is the start point STOP because we've got back to the beginning :)
		if neighbour == location:
			newPoint = neighbour
			break
		#Otherwise check to see if it would be better to move to this neighbour
		if lowestNeighbourDistance(neighbour) < lowestN:
			newPointDistance = distances[neighbour]
			newPoint = neighbour
			lowestN = lowestNeighbourDistance(neighbour)
	#Move back to this point
	route.append(newPoint)
	previous = point
	point = newPoint
	
#Flip the route in reverse so that we can present the route in the correct route.
route.reverse()
routeString = ""
n = 0

#Uncomment this line if you want to present a list of all the stations that need to be visited
#print(" -> ".join(route))

#This is a dictionary of arrays where the key is each station on the route and the array is an
# array of the lines that station is on
linesOfStationsOnRoute = {}

#Figure out all the lines that it is possible to complete the journey on
for station in route:
	linesOfStationsOnRoute[station] = []
	for neighbour in sC[station]:
		for line in sCTypes[station][neighbour]:
			if line not in linesOfStationsOnRoute[station]:
				linesOfStationsOnRoute[station].append(line)

#Establish which route is easiest with as little change of lines as possible
#Only the stations where one has to change line are presented
while n < len(route):
	maxReach =  n + 1
	matchingLine = ""
	#Iterate over all the stations in the route to find the last station we can get to staying on
	#a line that goes through the current station
	for s in range(n + 1, len(route)):
		for line in linesOfStationsOnRoute[route[s]]:
			if line in linesOfStationsOnRoute[route[n]]:
				maxReach = s
				matchingLine = line
	#Add the station to the route and the line that one has to leave that station on
	routeString += route[n]
	if n != len(route) - 1:
		routeString += " (" + matchingLine.title() + ") -> "

	n = maxReach

#Present the final route string that just contains the stations where a change needs to be made
print(routeString)

#This is a stupid long line of code that will establish the ccost of the journey
print(location + " (Zone " + str(stationZones[location]) + ") -> " + target + " (Zone " + str(stationZones[target]) + ") costs " + u"\xA3" + "{:20,.2f}".format(zoneCosts[stationZones[location]][stationZones[target]]).strip())