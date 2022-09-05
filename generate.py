import json
import os


command_start="execute store result score @s smithed.data if entity @s[scores={smithed.data=0}] if data storage smithed.crafter:input recipe"
command_end=" run loot replace block ~ ~ ~ container.16 loot "


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
			return recipe,result,count

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
	recipes=os.listdir("recipes")
	#recipes=["acacia_boat.json"]

	with open("Vanilla Craft Addon DataPack/data/vanilla_craft_addon/functions/recipes.mcfunction","w") as f:
		for r in recipes:
			a=create_craft(r)
			if not a is None:
				recipe,result,count=a
				#create the loot_table
				table=loot_table(result,count)
				with open("Vanilla Craft Addon DataPack/data/vanilla_craft_addon/loot_tables/"+str(result).replace("minecraft:","")+"_"+str(count)+".json","w") as g:
					json.dump(table,g,indent=4)
				#create the command
				recipe_command=str(recipe)
				recipe_command=recipe_command.replace("\'Slot\'","Slot")
				recipe_command=recipe_command.replace("\'id\'","id")
				recipe_command=recipe_command.replace("\'item_tag\'","item_tag")
				recipe_command=recipe_command.replace("\'0\'","0")
				recipe_command=recipe_command.replace("\'1\'","1")
				recipe_command=recipe_command.replace("\'2\'","2")
				recipe_command=recipe_command.replace(": 0,",":0b,")
				recipe_command=recipe_command.replace(": 1,",":1b,")
				recipe_command=recipe_command.replace(": 2,",":2b,")
				f.write(command_start+recipe_command+command_end+"vanilla_craft_addon:"+str(result).replace("minecraft:","")+"_"+str(count)+"\n")
