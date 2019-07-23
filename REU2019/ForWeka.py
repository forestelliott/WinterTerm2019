
#Makes weka dataset for all testers, but not pooled
def AllData(num_testers,type):
	AOIfile=open("AOIMetrics"+type+".csv","r")
	file = open("WekaData/Weka"+type+"All.arff","w")
	attributes = ["AU1","AU2","AU4","AU6","AU7","AU9","AU12","AU15","AU16","AU20","AU23","AU26","Left","Lower","Right","Upper","class"]
	file.write("@relation emotion\n")
	file.write("\n")

	#Write the attributes in the correct format
	for i in range(len(attributes)-1):
		file.write("@attribute "+attributes[i]+" numeric\n")

	file.write("@attribute "+attributes[len(attributes)-1]+" {Angry,Sad,Happy,Disgust,Neutral,Fear}\n")

	file.write("\n@data\n")

	done = False
	while not done:
		line = AOIfile.readline() 
		if line == "":
			break
		if "_DIS_" in line:
			line = AOIfile.readline()
			for i in range(num_testers): 
				temp = [0]*16
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Disgust\n")
			

		elif "_HAP_" in line:
			line = AOIfile.readline()
			
			for i in range(num_testers):
				temp = [0]*16 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Happy\n")

		elif "_ANG_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Angry\n")

		elif "_FEA_" in line:
			line = AOIfile.readline()
			
			for i in range(num_testers):
				temp = [0]*16 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Fear\n")

		elif "_NEU_" in line:
			line = AOIfile.readline()
			
			for i in range(num_testers):
				temp = [0]*16 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Neutral\n")

		elif "_SAD_" in line:
			line = AOIfile.readline()
			
			for i in range(num_testers):
				temp = [0]*16 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Sad\n")


	file.close()
	AOIfile.close()


#Does it for all testers
def testerData(num_testers,type):
	AOIfile=open("AOIMetrics"+type+".csv","r")
	for k in range(num_testers):
		AOIfile.seek(0)
		file = open("WekaData/Weka"+type+"Tester"+str(k+1)+".arff","w")
		attributes = ["AU1","AU2","AU4","AU6","AU7","AU9","AU12","AU15","AU16","AU20","AU23","AU26","Left","Lower","Right","Upper","class"]
		file.write("@relation emotion\n")
		file.write("\n")

		for i in range(len(attributes)-1):
			file.write("@attribute "+attributes[i]+" numeric\n")

		file.write("@attribute "+attributes[len(attributes)-1]+" {Angry,Sad,Happy,Disgust,Neutral,Fear}\n")

		file.write("\n@data\n")
		done = False
		while not done:
			line = AOIfile.readline() 
			if line == "":
				break
			if "_DIS_" in line:
				line = AOIfile.readline()
				temp = [0]*16
				for i in range(k+1): 
					line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Disgust\n")

			elif "_HAP_" in line:
				line = AOIfile.readline()
				temp = [0]*16
				for i in range(k+1): 
					line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Happy\n")

			elif "_ANG_" in line:
				line = AOIfile.readline()
				temp = [0]*16
				for i in range(k+1): 
					line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Angry\n")

			elif "_FEA_" in line:
				line = AOIfile.readline()
				temp = [0]*16
				for i in range(k+1): 
					line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Fear\n")

			elif "_NEU_" in line:
				line = AOIfile.readline()
				temp = [0]*16
				for i in range(k+1): 
					line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Neutral\n")

			elif "_SAD_" in line:
				line = AOIfile.readline()
				temp = [0]*16
				for i in range(k+1): 
					line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
				st = ','.join(str(e) for e in temp)
				file.write(st+",Sad\n")
		file.close()
	AOIfile.close()


#Writes to a file a arff file that pools all data between testers
def PooledData(num_testers,type):
	AOIfile=open("AOIMetrics"+type+".csv","r")
	file = open("WekaData/Weka"+type+"Pooled.arff","w")
	attributes = ["AU1","AU2","AU4","AU6","AU7","AU9","AU12","AU15","AU16","AU20","AU23","AU26","Left","Lower","Right","Upper","class"]
	file.write("@relation emotion\n")
	file.write("\n")

	#Write the attributes in the correct format
	for i in range(len(attributes)-1):
		file.write("@attribute "+attributes[i]+" numeric\n")

	file.write("@attribute "+attributes[len(attributes)-1]+" {Angry,Sad,Happy,Disgust,Neutral,Fear}\n")

	file.write("\n@data\n")

	done = False
	while not done:
		line = AOIfile.readline() 
		if line == "":
			break
		if "_DIS_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Disgust\n")

		elif "_HAP_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Happy\n")

		elif "_ANG_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Angry\n")

		elif "_FEA_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Fear\n")

		elif "_NEU_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Neutral\n")

		elif "_SAD_" in line:
			line = AOIfile.readline()
			temp = [0]*16
			for i in range(num_testers): 
				line=AOIfile.readline()
				part = line.split(",")
				for j in range(16):
					if part[j+2] != "" and part[j+2] != "\n":
						temp[j] += float(part[j+2])
			st = ','.join(str(e) for e in temp)
			file.write(st+",Sad\n")


	file.close()
	AOIfile.close()


def main():
	PooledData(6,"Sequential")
	testerData(6,"Sequential")
	AllData(6,"Sequential")

	PooledData(6,"Random")
	testerData(6,"Random")
	AllData(6,"Random")

main()