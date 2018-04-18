"""
Bipartite and matching functions by Zachary Thomas, James Lund, Scott Weaver
and Mohamed Cleric
"""
    
# This function returns the powerset of the list, as long as the
# input from the list is a set.
def power(graph):
    output = [] 
    totalLength = len(graph)
    for each in range(1 << totalLength): # Append each element to make a powerset
        output.append([graph[some] for some in range(totalLength) if (each & (1 << some))])
    return (output) 
    
# Testing power function
#list1 = ["A", "B"] #  [[], [“A”], [“B”], [“A”, “B”]]
#list2 = ["A", "B", "C"] #  [[], [“A”], [“B”], [“C”], [“A”, “B”], [“A”, “C”], [“B”, “C”], [“A”, “B”, “C”]]
#
#print(power(list1))
#print(power(list2))


# This function returns the two sets of a bipartite graph, as long as the graph
# is bipartite.    
def partite_sets(graph):
    setX = []
    setY = []
    output = []
    # Only add the first vertex to set X
    for vertex in graph:
        setX += vertex
        break
    for vertex in graph: # Goes through each vertex to add to the set Y
        if vertex in setX:
            for connection in graph[vertex]:
                if connection not in setY:
                    setY += connection # Add connection for set
        else: # Add remaining vertexes to set X
            for remaining in graph[vertex]:
                 if remaining not in setX:
                    setX += remaining
    # Add sets to list output
    output.append(setX)
    output.append(setY)
    return output

# Testing partite_sets functions
#print(partite_sets({'A' : ['B', 'C'], 'B' : ['A'], 'C' : ['A']})) # should return [“A”], [“B”, “C”] (or[“B”, “C”], [“A”])
#print(partite_sets({'A' : ['B', 'C'], 'B' : ['A', 'D'], 'C' : ['A', 'D'], 'D' : ['B', 'C']})) # should return [“A”, “D”], [“B”, “C”] (or [“B”, “C”], [“A”, “D”]))
    

# This function determins if the graph passed in is bipartite
def is_bipartite(graph):
    partiteList = partite_sets(graph)
    setX = partiteList[0]
    setY = partiteList[1]
    output = True # boolean to hold if the graph is bipartite, true unless proven false
    for vertex in setX: # go trhough each vertex in set X
        if vertex in setY: # if the vertex is found in the set Y, it is false, not bipartite
            output = False
    return output

# Tests is_bipartite function
#print(is_bipartite({'A' : ['B', 'C'], 'B' : ['A'], 'C' : ['A']})) # should return True
#print(is_bipartite({'A' : ['B', 'C'], 'B' : ['A', 'C'], 'C' : ['A', 'B']})) # should return False
   
    
# This function determines if the graph passed in has a perfect matching, where
# there exists a matching and all verticies are used. Must be bipartite.
def is_perfect(graph):
    sets = partite_sets(graph) # Get both sets
    setX = sets[0]
    setY = sets[1]
    output = True # True unless proven false
    if(len(setX)!=len(setY)): # If one side has more verticies, not all were used.
        return False;
    return output

# Testing is_perfect function
#print(is_perfect({'A' : ['B', 'C'], 'B' : ['A', 'D'], 'C' : ['A', 'D'], 'D' : ['B', 'C']})) # should return True
#print(is_perfect({'A' : ['B', 'C'], 'B' : ['A'], 'C' : ['A']})) # should return False