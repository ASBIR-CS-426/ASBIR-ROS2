#!/usr/bin/env python3
from geometry_msgs.msg import Point
import math
# Class for aStar
class AStar:

    def hValue(self, cell, goalNode):
        p1 = cell
        p2 = goalNode
    
        # eucledian distance
        distance = math.sqrt((p2.source.pos.point.x-p1.source.pos.point.x)**2 + (p2.source.pos.point.y-p1.source.pos.point.y)**2 + (p2.source.pos.point.z-p1.source.pos.point.z)**2)
        return distance

    # function to trace back from goal node
    def pathBack(self, bestPath, presentNode):
        lastPath = []
        lastPath.insert(0,presentNode)
        while presentNode in bestPath:
        #for i in range(1,len(bestPath)):
            presentNode = bestPath[presentNode].source.id
            lastPath.insert(0,presentNode)
        # lastPath.insert(0,bestPath[presentNode].target.id)
        return lastPath, bestPath

    def aStar(self, verticeGraph, startNode, goalNode):
        # nodes that have not yet been evaluated but found.
        openList = [startNode]

        # nodes that have been found and evaluated.
        closedList = []

        # dictionary for fastest path 
        bestPath = {}

        # dictionary for graph weight
        gWeight = {}

        # initialize all nodes in graph to infinity
        # dictionary for loop
        for key in verticeGraph:
            gWeight[key] = 100

        # initialize start node with zero
        gWeight[startNode] = 0

        # cost to goal from start noded
        fScore = {}

        for key in verticeGraph:
            fScore[key] = 100

        # start cost is h only
        fScore[startNode] = self.hValue(verticeGraph[startNode][0], verticeGraph[goalNode][0])
        while openList:
            # find smallest fScore 
            minVal = 500
            for node in openList:
                if fScore[node] < minVal:
                    minVal = fScore[node]
                    minNode = node
            # set node to present node
            presentNode = minNode
            
            if presentNode == goalNode:
                return self.pathBack(bestPath, presentNode)
            
            # add to already evaluated list
            closedList.append(presentNode)
            # remove and evaluate present node
            openList.remove(presentNode)
            
            # check neighbors of present node
            for neigh in verticeGraph[presentNode]:
                # if neighbor exists ignore
                if neigh.target.id in closedList:
                    continue
                # else add it to list
                elif neigh.target.id not in openList:
                    openList.append(neigh.target.id)

                # replace best path with presentNode
                bestPath[neigh.target.id] = neigh
                # if approximate g weight is greater replace
                gWeight[neigh.target.id] = neigh.distance + gWeight[presentNode]
                # calculate fScore f(n) = g(n) + h(n)
                fScore[neigh.target.id] = gWeight[neigh.target.id] + self.hValue(verticeGraph[neigh.target.id][0], verticeGraph[goalNode][0])
        return False
