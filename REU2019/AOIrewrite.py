def perceptionTotals(AOIfile, Pedic, MPedic, mispercieved):
	AOIfile.seek(0)
	index = 0
	done = False
	while not done:
		line = AOIfile.readline() 
		if line == "":
			break
		if "_DIS_" in line:
			index += 1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						if index in mispercieved["Tester"+str(i+1)]:
							MPedic["DIS"][i][j] += float(part[j+2])
						else:
							Pedic["DIS"][i][j] += float(part[j+2])

		elif "_HAP_" in line:
			index += 1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						if index in mispercieved["Tester"+str(i+1)]:
							MPedic["HAP"][i][j] += float(part[j+2])
						else:
							Pedic["HAP"][i][j] += float(part[j+2])

		elif "_ANG_" in line:
			index += 1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						if index in mispercieved["Tester"+str(i+1)]:
							MPedic["ANG"][i][j] += float(part[j+2])
						else:
							Pedic["ANG"][i][j] += float(part[j+2])

		elif "_FEA_" in line:
			index += 1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						if index in mispercieved["Tester"+str(i+1)]:
							MPedic["FEA"][i][j] += float(part[j+2])
						else:
							Pedic["FEA"][i][j] += float(part[j+2])

		elif "_NEU_" in line:
			index += 1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						if index in mispercieved["Tester"+str(i+1)]:
							MPedic["NEU"][i][j] += float(part[j+2])
						else:
							Pedic["NEU"][i][j] += float(part[j+2])	

		elif "_SAD_" in line:
			index += 1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						if index in mispercieved["Tester"+str(i+1)]:
							MPedic["SAD"][i][j] += float(part[j+2])
						else:
							Pedic["SAD"][i][j] += float(part[j+2])
	

def Totals(AOIfile, edic, numemo):
	#Creating the totals of the emotions
	done = False
	k=0
	while not done:
		line = AOIfile.readline() 
		if line == "":
			break
		if "_DIS_" in line:
			numemo[0]+=1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						edic["DIS"][i][j] += float(part[j+2])
		elif "_HAP_" in line:
			numemo[1]+=1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						edic["HAP"][i][j] += float(part[j+2])
		elif "_ANG_" in line:
			numemo[2]+=1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						edic["ANG"][i][j] += float(part[j+2])
		elif "_FEA_" in line:
			numemo[3]+=1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						edic["FEA"][i][j] += float(part[j+2])
		elif "_NEU_" in line:
			numemo[4]+=1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						edic["NEU"][i][j] += float(part[j+2])	
		elif "_SAD_" in line:
			numemo[5]+=1
			line = AOIfile.readline()
			for i in range(6): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						edic["SAD"][i][j] += float(part[j+2])

def writeTotals(edic,key,addon,type):
	file = open("AOIData"+type+"/AOI"+key+addon+".csv","w")
	file.write("Participant,AU1,AU2,AU4,AU6,AU7,AU9,AU12,AU15,AU16,AU20,AU23,AU26,Left,Lower,Right,Upper\n")
	#write the totals to appropriate csv file
	for i in range(6):
		file.write("Tester"+str(i+1))
		for j in range(16):
			file.write(","+ str(edic[key][i][j]))
		file.write("\n")

	
	file.close()


def main():	
	#-----------This is for sequential data-------------
	#File opening and such
	AOIfile=open("AOIMetricsSequential.csv","r")
	

	#This is the indices of the mispercieved emotions per tester
	mispercieved = {'Tester1': [1, 2, 6, 9, 12, 15, 17, 24, 26, 27, 30, 33, 40, 42, 45, 46, 47, 48, 51, 52, 58, 59, 72, 74, 75, 78], 'Tester2': [10, 20, 22, 24, 26, 27, 30, 32, 33, 40, 42, 44, 45, 46, 48, 49, 52, 56, 57, 58, 70, 72, 74, 75, 78, 81, 91, 92], 'Tester3': [5, 6, 8, 15, 20, 24, 26, 30, 40, 42, 45, 46, 48, 49, 52, 70, 72, 76, 78, 80, 89], 'Tester4': [4, 5, 6, 12, 17, 21, 24, 26, 27, 29, 30, 33, 39, 40, 42, 45, 46, 48, 51, 52, 58, 59, 62, 70, 72, 78, 83, 86, 92], 'Tester5': [2, 6, 20, 22, 23, 24, 29, 41, 46, 47, 48, 54, 55, 58, 66, 70, 77, 78, 80], 'Tester6': [2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 21, 23, 24, 27, 29, 30, 32, 33, 36, 39, 40, 42, 45, 46, 48, 49, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 81, 84, 88, 89, 91, 92]}
	
	#This is the totals for the mispercieved emotions
	MPedic = {"DIS":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"HAP":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"ANG":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"NEU":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"FEA":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"SAD":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]}
	
	#This is the totals for the pervieved emotions
	Pedic = {"DIS":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"HAP":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"ANG":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"NEU":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"FEA":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"SAD":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]}
	
	#Totals for all emotions
	edic = {"DIS":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"HAP":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"ANG":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"NEU":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"FEA":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"SAD":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]}
	
	#Number of emotions per timeline with indices|| 0: Dis | 1: Hap | 2: Ang | 3: Fea | 4: Neu | 5: Sad ||
	numemo=[0]*6
	
	Totals(AOIfile,edic, numemo)
	perceptionTotals(AOIfile, Pedic, MPedic, mispercieved)

	#writing the totals
	for key in edic:
		writeTotals(edic,key,"","Sequential")

	#writing the percieved totals
	for key in Pedic:
		writeTotals(Pedic, key,"Percieved","Sequential")

	#writing the mispercieved totals
	for key in MPedic:
		writeTotals(MPedic, key,"MisPercieved","Sequential")
	
	print(numemo)
	#-----------This is for random data-------------
	#File opening and such
	AOIfile=open("AOIMetricsRandom.csv","r")
	

	#This is the indices of the mispercieved emotions per tester
	mispercieved = {'Tester1': [6, 7, 8, 9, 10, 14, 15, 17, 19, 21, 25, 26, 27, 28, 29, 32, 33, 34, 35, 38, 44, 45, 47, 50, 57, 58, 59, 60, 63, 64, 65, 66, 67, 68, 72, 76, 79, 81, 83, 88, 92, 94, 98, 99, 102, 103, 104, 105, 106, 107, 110, 111, 112, 113, 114, 115, 116, 117], 'Tester2': [5, 8, 9, 13, 14, 15, 16, 17, 19, 21, 26, 27, 28, 29, 31, 32, 34, 38, 39, 44, 45, 46, 47, 50, 52, 54, 55, 57, 58, 59, 64, 65, 69, 71, 76, 79, 81, 93, 98, 99, 101, 103, 104, 105, 106, 108, 109, 110, 111, 112, 116], 'Tester3': [1, 4, 5, 6, 13, 14, 19, 21, 26, 27, 28, 29, 31, 32, 33, 35, 38, 45, 46, 47, 50, 52, 54, 55, 57, 58, 59, 64, 65, 71, 74, 76, 83, 85, 88, 89, 93, 94, 99, 101, 102, 103, 104, 105, 106, 107, 109, 110, 112, 114, 115, 116, 117], 'Tester4': [1, 2, 4, 5, 7, 8, 12, 19, 21, 25, 26, 27, 28, 31, 32, 33, 36, 38, 44, 45, 46, 47, 50, 54, 55, 57, 58, 59, 65, 69, 71, 76, 79, 86, 87, 88, 89, 90, 94, 99, 100, 102, 105, 106, 107, 109, 110, 112, 114, 115], 'Tester5': [1, 2, 5, 7, 14, 16, 19, 26, 28, 29, 32, 35, 39, 44, 45, 46, 47, 50, 55, 58, 59, 64, 65, 71, 81, 93, 94, 95, 99, 104, 105, 109, 111, 116, 117], 'Tester6': [6, 7, 8, 9, 11, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 41, 43, 45, 46, 47, 48, 50, 55, 57, 60, 65, 66, 67, 70, 72, 76, 78, 79, 80, 81, 83, 85, 86, 87, 89, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 111, 112, 113, 114, 115, 116]}
	
	#This is the totals for the mispercieved emotions
	MPedic = {"DIS":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"HAP":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"ANG":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"NEU":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"FEA":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"SAD":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]}
	
	#This is the totals for the pervieved emotions
	Pedic = {"DIS":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"HAP":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"ANG":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"NEU":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"FEA":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"SAD":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]}
	
	#Totals for all emotions
	edic = {"DIS":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"HAP":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"ANG":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"NEU":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"FEA":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16],"SAD":[[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]}
	
	#Number of emotions per timeline with indices|| 0: Dis | 1: Hap | 2: Ang | 3: Fea | 4: Neu | 5: Sad ||
	numemo=[0]*6
	
	Totals(AOIfile,edic, numemo)
	#perceptionTotals(AOIfile, Pedic, MPedic, mispercieved)

	#writing the totals
	for key in edic:
		writeTotals(edic,key,"","Random")
	
	#writing the percieved totals
	for key in Pedic:
		writeTotals(Pedic, key,"Percieved","Random")

	#writing the mispercieved totals
	for key in MPedic:
		writeTotals(MPedic, key,"MisPercieved","Random")
	
	
	#print(edic["DIS"],edic["SAD"],edic["ANG"],edic["HAP"],edic["NEU"],edic["FEA"])
	print(numemo)
	AOIfile.close()
	
main()
