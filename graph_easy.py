import matplotlib.pyplot as graph

# pip install matplotlib
# Line graph

x = [1,2,3]
y = [6,1,9]

graph.plot(x, y)
  
# naming the x axis
graph.xlabel('x - axis')
# naming the y axis
graph.ylabel('y - axis')
  
# giving a title to my graph
graph.title('My first graph!')
  
# function to show the plot
graph.show()