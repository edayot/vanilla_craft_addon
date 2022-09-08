data modify storage vanilla_craft_addon:main dye_id set from storage smithed.crafter:input recipe[{item_tag:["#vanilla_craft_addon:dyes"]}].id

data modify storage vanilla_craft_addon:main item_out set from storage smithed.crafter:input recipe[{item_tag:["#vanilla_craft_addon:shulker_boxes"]}]
data modify storage vanilla_craft_addon:main item_out.Slot set value 16b

execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:black_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:black_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:blue_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:blue_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:brown_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:brown_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:cyan_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:cyan_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:gray_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:gray_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:green_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:green_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:light_blue_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:light_blue_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:light_gray_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:light_gray_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:lime_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:lime_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:magenta_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:magenta_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:orange_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:orange_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:pink_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:pink_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:purple_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:red_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:red_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:white_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:white_shulker_box"
execute if data storage vanilla_craft_addon:main {dye_id:"minecraft:yellow_dye"} run data modify storage vanilla_craft_addon:main item_out.id set value "minecraft:yellow_shulker_box"

data modify block ~ ~ ~ Items append from storage vanilla_craft_addon:main item_out