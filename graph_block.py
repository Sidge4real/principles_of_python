
import matplotlib.pyplot as graph
  
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5]
  
# heights of bars
height = [10, 24, 36, 40, 5]
  
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']
  
# plotting a bar chart
graph.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'blue'])
  
# naming the x-axis
graph.xlabel('x - axis')
# naming the y-axis
graph.ylabel('y - axis')
# plot title
graph.title('My first bar chart!')
  
# function to show the plot
graph.show()