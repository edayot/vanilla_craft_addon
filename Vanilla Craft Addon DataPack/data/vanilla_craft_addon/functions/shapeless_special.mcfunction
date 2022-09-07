execute store result score @s smithed.data if entity @s[scores={smithed.data=0}] if score count smithed.data matches 2 if data storage smithed.crafter:input {recipe:[{id: 'minecraft:gunpowder', Count:2b}, {id: 'minecraft:paper', Count:1b}]} run loot replace block ~ ~ ~ container.16 loot vanilla_craft_addon:firework_rocket_3_2
execute store result score @s smithed.data if entity @s[scores={smithed.data=0}] if score count smithed.data matches 2 if data storage smithed.crafter:input {recipe:[{id: 'minecraft:gunpowder', Count:3b}, {id: 'minecraft:paper', Count:1b}]} run loot replace block ~ ~ ~ container.16 loot vanilla_craft_addon:firework_rocket_3_3



