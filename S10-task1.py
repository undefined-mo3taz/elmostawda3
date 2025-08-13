treasure={
    "clues":["beach","cave","waterfall"],
    "locations":{
        "beach":{
            "items":["compass","shovel"],
            "hint":"dig here"
        },
        "cave":{
            "items":["lantern","gold coin"],
            "hint":"look behind rocks"
        } 
    },
    "crew":["first mate","navigator"]
}
print(treasure)
print()
treasure["crew"].append("cook")
treasure["locations"]["volcano"]={
    "items":["diamond","lava boots"],
    "hint":"wear protection"
}
treasure["clues"].append("volcano")
treasure["crew"].remove("navigator")
print(treasure)
for location_name in treasure["locations"]:
    if "gold coin"in treasure["locations"][location_name]["items"]:
        print(f"treasure in {location_name}")
for location_name in treasure["locations"]:
    print(f"{location_name}:{treasure["locations"][location_name]["items"]}")









