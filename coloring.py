"""
Spyder Editor
@author JL3
This is a temporary coloring program for MTH 325
"""
# =============================================================================
#DONE
def isProper(graph, color):
    """
    Function that determines if a graph has a proper vertex coloring
    """
    for vertex in graph:
        for neighbor in graph[vertex]:
            if color[vertex] == color[neighbor]:
                print ("False")
                return False
              
    print ("True")
    return True

# =============================================================================
#DONE
def three_color(graph):
    """
    Function that returns all possible proper and nonproper 
    vertex colorings of a graph. 
    """
    
    temp = {}
    output = []
    #Initializes every vertex color to 1
    for vertex in graph:
        temp[vertex] = 1
    output.append(dict(temp))
    
        #loops through the number of possible graph
    for vertex in graph:
        
        #Power needed after graph for all possible colorings
        for x in range(len(graph)**2):
            
        #loops through vertices in temp, if it is less than 3, it adds 1
        #adds it to the final and breaks out to the next possibility
        #otherwise if it is >=3 it sets it back to one and moves on to the next
        #vertex in the temp
            for vertex in graph:
                if temp[vertex] < 3:
                    temp[vertex] += 1
                    output.append(dict(temp))
                #Break statement needed for duplicate colorings.
                    break
            
                else:
                    temp[vertex] = 1
    return output

# =============================================================================
#
def is_three_color(graph):
    """
    Function that determines if a given graph can be colored 
    with only 3 colors
    
    NOTE: the multiple false statements are denying all colorings
     possible for the function because those specific colorings 
     are not proper. If "True" is printed, that means that a 
     possible vertex coloring exists.
    """
    combo = three_color(graph)
    
    #Loops through all combinations of vertex colorings
    for ThreeColor in combo:
        if isProper(graph, ThreeColor):
            
            #Print statement prints the acceptable coloring for this graph
            print(ThreeColor)
            return True
        
    return False

# =============================================================================
#DONE
def is_proper_edge(graph):
    """
    Function that determines if a inputted graph has a proper 
    edge coloring
    """
    for vertex in graph:
        for edge in graph[vertex]:
            for l in graph[edge[0]]:
                if l[0] != vertex and l[1] == edge[1]:
                    print ("False")
                    return False
    print ("True")
    return True
    
# =============================================================================
#DONE
def greedy(graph, order):
    """
    This function performs the greedy algorithm to find the proper 
    vertex coloring and lists vertices in order of color
    """
    color = {}
  
    #Loops through order
    for vertex in order:
        #Color dict with color "1"
        color[vertex] = 1
        
        #Adds connected vertices to a list and colors them
        neighborColors = []
        for neighbor in graph[vertex]:
            if neighbor in color:
                neighborColors.append(color[neighbor])
        #While current color is the same as the neighboring vertices,
        # increments that vertex color by 1
        while(color[vertex] in neighborColors):
            color[vertex] += 1
    print (color)
        
# =============================================================================


#isProper({"A" :["B", "C"],"B" :["A", "C"],"C" :["A", "B"]}, {"A" :1, "B" :2, "C" :3})
#isProper({"A" :["B", "C"],"B" :["A", "C"],"C" :["A", "B"]}, {"A" :1, "B" :1, "C" :3})
#print(three_color({"A" : ["B"], "B" : ["A"]}))
#is_three_color({"A" :["B", "C"], "B" :["A", "C"], "C" :["A", "B"]})
#is_three_color({"A" :["B", "C", "D"], "B" :["A", "C", "D"], "C" :["A", "B", "D"], "D" :["A", "B", "C"]})
#is_proper_edge({'A' :[['B', 1], ['C', 2]], 'B' :[['A', 1], ['C', 3]], 'C' :[['A', 2], ['B', 3]]})
#is_proper_edge({"A" :[["B", 1], ["C", 2]], "B" :[["A", 1], ["C", 2]], "C" :[["A", 2], ["B", 2]]})
#greedy({"A" :["B", "C"], "B" :["A"], "C" :["A"]}, ["A", "B", "C"])
#greedy({"A" :["B"], "B" :["A", "C"], "C" :["B", "D"], "D" :["C"]}, ["A", "D", "B", "C"])



