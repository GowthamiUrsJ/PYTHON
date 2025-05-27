ipl_teams = []

ipl_teams.append("RCB")
print("After appending RCB:", ipl_teams) 

ipl_teams.append("CSK")
print("After appending CSK:", ipl_teams) 

ipl_teams.insert(0, "MI")
print("After inserting MI at index 0:", ipl_teams)  


ipl_teams.extend(["GT", "RR"])
print("After extend:", ipl_teams)  

ipl_teams.remove("CSK")
print("After removing 'CSK':", ipl_teams) 

popped_team = ipl_teams.pop()
print("After pop:", ipl_teams)  
print("Popped team:", popped_team) 

index_of_rcb = ipl_teams.index("RCB")
print("Index of 'RCB':", index_of_rcb) 

print("Count of 'RCB':", ipl_teams.count("RCB"))  

ipl_teams.sort()
print("After sort:", ipl_teams)


ipl_teams.reverse()
print("After reverse:", ipl_teams)

copied_list = ipl_teams.copy()
print("Copied list:", copied_list)

ipl_teams.clear()
print("After clear:", ipl_teams)  