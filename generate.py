import json
import os





def create_craft(r):
	recipe={	"0":[{"Slot":0,"id":"minecraft:air"},{"Slot":1,"id":"minecraft:air"},{"Slot":2,"id":"minecraft:air"}],
				"1":[{"Slot":0,"id":"minecraft:air"},{"Slot":1,"id":"minecraft:air"},{"Slot":2,"id":"minecraft:air"}],
				"2":[{"Slot":0,"id":"minecraft:air"},{"Slot":1,"id":"minecraft:air"},{"Slot":2,"id":"minecraft:air"}]
	}

	with open("recipes/"+r,"r") as f:
		data=json.load(f)

		if data["type"]=="minecraft:crafting_shaped":
			for i in range(len(data["pattern"])):
				for j in range(len(data["pattern"][i])):
					item_id=None
					item_tag=None
					if data["pattern"][i][j]!=" ":
						try:
							item_id=data["key"][data["pattern"][i][j]]["item"]
						except:
							try:
								item_tag=data["key"][data["pattern"][i][j]]["tag"]
							except:
								item_id="minecraft:air"
								if type(data["key"][data["pattern"][i][j]])==list:
									item_id=None
									if data["key"][data["pattern"][i][j]]==[{"item": "minecraft:coal"},{"item": "minecraft:charcoal"}]:
										item_tag="minecraft:coals"
					else:
						item_id="minecraft:air"
					if not item_id is None:
						recipe[str(i)][j]["id"]=item_id
					if not item_tag is None:
						try:
							recipe[str(i)][j]["item_tag"].append("#"+item_tag)
						except:
							recipe[str(i)][j]["item_tag"]=[]
							recipe[str(i)][j]["item_tag"].append("#"+item_tag)
						del recipe[str(i)][j]["id"]

			result=data["result"]["item"]
			count=1
			try:
				count=data["result"]["count"]
			except:
				pass
			return "shaped",recipe,result,count,len(data["pattern"])
		elif data["type"]=="minecraft:crafting_shapeless":
			recipe=[]
			for i in range(len(data["ingredients"])):
				print(r)
				try:
					try:
						try:
							recipe.append({"id":data["ingredients"][i]["item"],"Count":data["ingredients"][i]["count"]})
						except:
							recipe.append({"id":data["ingredients"][i]["item"],"Count":1})
					except:
						try:
							recipe.append({"item_tag":[data["ingredients"][i]["tag"]],"Count":data["ingredients"][i]["count"]})
						except:
							recipe.append({"item_tag":[data["ingredients"][i]["tag"]],"Count":1})
				except:
					if type(data["ingredients"][i])==list:
						if data["ingredients"][i]==[{"item": "minecraft:coal"},{"item": "minecraft:charcoal"}]:
							recipe.append({"item_tag":["#minecraft:coals"],"Count":1})
				
			result=data["result"]["item"]
			count=1
			try:
				count=data["result"]["count"]
			except:
				pass
			return "shapeless",recipe,result,count




def loot_table(id,count):
	table={
		"pools": [
			{
			"rolls": 1,
			"entries": [
				{
				"type": "minecraft:item",
				"name": id,
				"functions": [
					{
					"function": "minecraft:set_count",
					"count": count
					}
				]
				}
			]
			}
		]
	}
	return table

def main():
	recipes=["torch.json"]

	recipes=os.listdir("recipes")

	with open("Vanilla Craft Addon DataPack/data/vanilla_craft_addon/functions/recipes.mcfunction","w") as f:
		with open("Vanilla Craft Addon DataPack/data/vanilla_craft_addon/functions/shapeless_recipes.mcfunction","w") as f2:
			for r in recipes:
				a=create_craft(r)
				
					
				
				if not a is None:
					if a[0]=="shaped":
						command_start="execute store result score @s smithed.data if entity @s[scores={smithed.data=0}] if data storage smithed.crafter:input recipe"
						command_end=" run loot replace block ~ ~ ~ container.16 loot "
						bonjour,recipe,result,count,recipe_type=a
						#create the loot_table
						#create the command
						recipe_command=str(recipe)

						if recipe_type==2:
							del recipe["2"]
							recipe_command=str(recipe)
							command_end=" if data storage smithed.crafter:input recipe{2:[]}"+command_end

						elif recipe_type==1:
							del recipe["2"]
							del recipe["1"]
							recipe_command=str(recipe)
							command_end=" if data storage smithed.crafter:input recipe{1:[],2:[]}"+command_end
						
						table=loot_table(result,count)
						with open("Vanilla Craft Addon DataPack/data/vanilla_craft_addon/loot_tables/"+str(result).replace("minecraft:","")+"_"+str(count)+".json","w") as g:
							json.dump(table,g,indent=4)
						recipe_command=recipe_command.replace("\'Slot\'","Slot")
						recipe_command=recipe_command.replace("\'id\'","id")
						recipe_command=recipe_command.replace("\'item_tag\'","item_tag")
						recipe_command=recipe_command.replace("\'0\'","0")
						recipe_command=recipe_command.replace("\'1\'","1")
						recipe_command=recipe_command.replace("\'2\'","2")

						for i in range(64):
							recipe_command=recipe_command.replace(": SSS,".replace("SSS",str(i)),":SSSb,".replace("SSS",str(i)))
						
						f.write(command_start+recipe_command+command_end+"vanilla_craft_addon:"+str(result).replace("minecraft:","")+"_"+str(count)+"\n")


					elif a[0]=="shapeless":
						command_start="execute store result score @s smithed.data if entity @s[scores={smithed.data=0}] if score count smithed.data matches XXX if data storage smithed.crafter:input {recipe:"
						command_end="} run loot replace block ~ ~ ~ container.16 loot "

						bonjour,recipe,result,count=a
						recipe_command=str(recipe)

						command_start=command_start.replace("XXX",str(len(recipe)))

						table=loot_table(result,count)
						with open("Vanilla Craft Addon DataPack/data/vanilla_craft_addon/loot_tables/"+str(result).replace("minecraft:","")+"_"+str(count)+".json","w") as g:
							json.dump(table,g,indent=4)

						recipe_command=recipe_command.replace("\'Count\'","Count")
						recipe_command=recipe_command.replace("\'Slot\'","Slot")
						recipe_command=recipe_command.replace("\'id\'","id")
						recipe_command=recipe_command.replace("\'item_tag\'","item_tag")
						recipe_command=recipe_command.replace("\'0\'","0")
						recipe_command=recipe_command.replace("\'1\'","1")
						recipe_command=recipe_command.replace("\'2\'","2")

						for i in range(64):
							recipe_command=recipe_command.replace(": SSS".replace("SSS",str(i)),":SSSb".replace("SSS",str(i)))
						
						f2.write(command_start+recipe_command+command_end+"vanilla_craft_addon:"+str(result).replace("minecraft:","")+"_"+str(count)+"\n")


