#Header Information

def maze(MazeMatrix,start,finish):
    #MazeMatrix is a binary matrix (2D list of lists)
    #start & finish are tuples containing the starting and finishing point indices e.g. (1,1) & (5,5)
    
    #import statements, function body
    
    def MazeMatrix2Graph(MazeMatrix):
        #MazeMatrix is a binary matrix (2D list of lists)
        
        #function body
        
        return MazeGraph #a networkx graph whose nodes represent the '1's in the input matrix. node labels are tuples.
    
    def MazeAnswerBFS(MazeGraph,start,finish):
        #MazeGraph is a networkx graph 
        #start and finish are tuples containing the starting and finishing point indices
        
        #function body 
                
        return shortest_path #list of tuples containing indices of the points in the answer
    
    def MazeComponentsDFS(MazeGraph):
        #MazeGraph is a networkx graph
        
        #function body  
        
        return components #list of lists, each containing tuples of the indices of points in that component
    
    #function body
    
    print(a)
    print('\n')
    print(b)
    #a is the output of MazeAnswerBFS and b is the output of MazeComponentsDFS

if __name__ == '__main__':
    #DO NOT MODIFY THE FOLLOWING
    hw3bmaze=    [[1,0,1,1,0,1],
                  [1,1,0,0,0,0],
                  [0,1,0,1,1,1],
                  [0,1,1,1,0,1],
                  [1,0,0,1,1,1],
                  [1,1,0,0,0,1],
                  [0,0,1,1,0,1]]
    
    hw3bstart=(0,0)
    hw3bfinish=(6,5)
    print(maze(hw3bmaze,hw3bstart,hw3bfinish))
    
#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]
