
States = [[[1,2],[2,3],[7,0]], [[3,3],[2,2],[1,3]], [(3,1),(2,2),(1,3)]]
Heuristic = [23, 78, 54]
#print(MyStack[0][0])
#print(MyStack[0][1])
state = [(1,4),(1,3),(3,2)]
heuristic = 58
States.append(state)
for item in States:
  print(item)
print(min(Heuristic))
index = Heuristic.index(min(Heuristic))
print(index)
States[index][1][0] = 9
for item in States:
  print(item)
""" dictionary = {
  "states": [[(1,2),(2,3),(7,0)], [(3,3),(2,2),(1,3)], [(3,3),(2,2),(1,3)]],
  "heuristics": [23, 78, 54]
}

print(dictionary["states"])
print(dictionary.get("heuristics"))

for x, y in dictionary.items():
   """