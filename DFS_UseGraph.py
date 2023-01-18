import networkx as nx
def Depth_First_Search(initialState, goalTest):
    frontier = []
    frontier.append(initialState)
    explored = []
    while len(frontier) > 0:
        print("frontier: ", frontier)
        state = frontier.pop(len(frontier)-1)  
        explored.append(state)
        if goalTest == state:
            return "Thu tu dinh kham pha: ",explored
        for neighbor in reversed(list(G.neighbors(state))):
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return "Khong tim thay duong di"
if __name__ == "__main__":
    G = nx.Graph()
    V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] 
    E = [
            ('S', 'A', 1), 
            ('S', 'B', 1), 
            ('S', 'C', 1),
            ('A', 'D', 1),
            ('B', 'F', 1), 
            ('B', 'G', 1), 
            ('C', 'F', 1), 
            ('D', 'E', 1), 
            ('E', 'F', 1), 
            ('E', 'G', 1), 
            ('F', 'H', 1), 
            ('H', 'G', 1), 
        ]
    G.add_nodes_from(V)
    G.add_weighted_edges_from(E)
    result = Depth_First_Search("S", "G")
    print(result)