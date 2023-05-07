import pandas as pd

def clean(block):
	block = block.replace(",","")
	block = block.replace(" + ",". ")
	block = block.replace("+"," ")
	block = block.replace(" = ",". ")
	block = block.replace("=","")
	block = block.replace("-","")
	block = block.replace("\n"," ")
	return block


filenames = ["text/monologues_continuous.txt", "text/dialogues_continuous.txt"]
texts = []
for filename in filenames:
	with open(filename) as file:
		block = ""
		for line in file:
			if len(line) == 8 and len(line.split(" ")) == 3:
				if not block:
					sound_name = line.strip().replace(" ", "_")
				else:
					texts.append({"id": "monologues/"+sound_name})
					with open("text/monologues/"+sound_name+".txt", "w+") as out:
						out.write(clean(block))
					block = ""
					sound_name = line.strip().replace(" ", "_")

			elif (len(line) == 16 and len(line.split(" ")) == 5) or (len(line) == 12 and len(line.split(" ")) == 5):
				if not block:
					sound_name = line.strip().replace(" ", "_")
				else:
					texts.append({"id": "dialogues_mono_soundfiles/"+sound_name})
					with open("text/dialogues_mono_soundfiles/"+sound_name+".txt", "w+") as out:
						out.write(clean(block))
					block = ""
					sound_name = line.strip().replace(" ", "_")

			else:
				block += line

pd.DataFrame(texts).to_csv("all.csv", index=False)

