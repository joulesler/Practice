class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        toVisit = {}
        visited = {}
        
        if source == destination:
            return True
        
        for i in edges:
            #Unidirectional set of nodes
            if toVisit.get(i[1]) == None:
                toVisit[i[1]] = [i[0]] 
            else: 
                toVisit[i[1]].append(i[0])
            
            #BiDirectional map of nodes
            if toVisit.get(i[0]) == None:
                toVisit[i[0]] = [i[1]] 
            else: toVisit[i[0]].append(i[1])
                
        def searchNode(node):
            neighbours = toVisit.get(node)
            if neighbours == None:
                return
            else:
                visited[node] = True
                for i in neighbours:
                    if destination == i:
                        return True
                    if visited.get(i) != None:
                        continue
                    else:
                        result = searchNode(i)
                        if result:
                            return True

        return searchNode(source)
    