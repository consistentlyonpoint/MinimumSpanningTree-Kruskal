# -*- coding: utf-8 -*-
"""
    mst.py       Intro to Graduate Algorithms
    
    You will implement Kruskal's algorithm for finding a Minimum Spanning Tree.
    You will also implement the union-find data structure using path compression
    See [DPV] 51.3 & 5.14 for details
"""

import argparse
import GA_ProjectUtils as util

class unionFind:
    def __init__(self, n):
        self.pi = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        # print("what is self.pi: ", self.pi)
        # print("what is self.rank: ", self.rank)

    def areConnected(self, p, q):
        """
            return true if 2 nodes are connected or false if they are
            not by comparing their roots
        """
        #pass
        # print("what is root of ", p,": ", self.find(p),"\n what is root of ", q,": ", self.find(q))
        if self.find(p) == self.find(q):
            # print("", p, " and ", q," are connected")
            return True
        else:
            # print("", p, " and ", q," are not connected")
            return False

    def union(self, u, v):
        """
            build union of 2 components
            Be sure to maintain self.rank as needed to
            make sure your algorithm is optimal.
        """
        #pass
        r_u = self.find(u)
        r_v = self.find(v)
        if r_u == r_v:
        # if self.areConnected(u, v) is True:
            return
        # print("what is root v: ", r_v)
        # print("what is root u: ", r_u)
        # print("what is rank of ",r_u,": ",self.rank[r_u],""
        #                     "\n what is rank of ",r_v,": ",self.rank[r_v])
        # print("what is the parent of root v: ", self.pi[r_v])
        # print("what is the parent of root u: ", self.pi[r_u])
        if self.rank[r_u] > self.rank[r_v]:
            # print("what is root of v: ", self.rank[r_v])
            # print("what is root of u: ", self.rank[r_u])
            # print("what is pointer of root v: ", self.pi[r_v])
            # print("what is pointer of root u: ", self.pi[r_u])
            self.pi[r_v] = r_u
        # else:
        elif self.rank[r_v] > self.rank[r_u]:
            self.pi[r_u] = r_v
            # if self.rank[r_u] == self.rank[r_v]:
        else:
            # print("do we hit this else")
                # elif self.rank[r_u] == self.rank[r_v]:
            self.pi[r_v] = r_u
            self.rank[r_u] += 1
            # self.rank[r_v] = self.rank[r_v] + 1
        # print("'after if' what is the parent of root u: ", self.pi[r_u])
        # print("'after if' what is the parent of root v: ", self.pi[r_v])
        # print("'after if' what is the rank of r_u: ", self.rank[r_u],"\n what is the rank of r_v: ", self.rank[r_v])
        # print("dummy")

    def find(self, p):
        """
            find the root of the set containing the
            passed vertex p - Must use path compression!
        """
        #pass
        # print("what is p ", p)
        # print("what is self.pi when called:\n", self.pi)
        # print("what is self.pi[p] when called:\n", self.pi[p])
        if p != self.pi[p]:
            # self.pi(p) = self.pi.find(p)
            self.pi[p] = self.find(self.pi[p])
        # print("'after if' what is self.pi when called:\n", self.pi)
        # print("'after if' what is self.pi[p] when called:\n", self.pi[p])
        return self.pi[p]

def kruskal(G):
    """
        Kruskal algorithm
        G : graph object
    """
    #Build unionFind Object
    print("what does input to class look like")
    print(G.numVerts)
    uf = unionFind(G.numVerts)
    #Make MST as a set
    MST = set()    
    #Get list of edges sorted by increasing weight
    sortedEdges = G.sortedEdges()   
    #Go through edges in sorted order smallest, to largest
    # print("what is sorted edges: \n", sortedEdges)
    for e in sortedEdges:
        #print("what is an edge ", e)
        #print("e type is : ", type(e))
        #define vertex u and v of edge e
        u = e[0]
        v = e[1]
        #print("what is vertex u: ", u,"\n what is vertex v: ", v)
        # if unionFind.self.find(u) != unionFind.self.find(v):
        #     unionFind.self.union(u, v)
        # if uf.find(u) != uf.find(v):
        # if uf.areConnected(u, v) == 0:
        if uf.areConnected(u, v) is False:
            # use the following line to add an edge to the MST.
            # You may change it's indentation/scope within the loop
            # print("what is u: ", u,"\n what is v: ", v,"\n"
            #             "what is the result of are connected ", uf.areConnected(u, v))
            # while uf.areConnected(u, v) is False:
            # if uf.areConnected(u, v) == 0:
            MST.add(util.buildMSTEdge(G,e))
            # print("do i make it here?")
            uf.union(u, v)

        #TODone - do not modify any other code below this line
    return MST, uf

def main():
    """
    main
    """
    #DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Minimum Spanning Tree Coding Quiz')
    #use this flag, or change the default here to use different graph description files
    parser.add_argument('-g', '--graphFile',  help='File holding graph data in specified format', default='small.txt', dest='graphDataFileName')
    #use this flag to print the graph and resulting MST
    parser.add_argument('-p', '--print', help='Print the MSTs?', default=False, dest='printMST')

    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-n', '--sName',  help='Student name, used for autograder', default='GT', dest='studentName')
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')
    args = parser.parse_args()

    #DO NOT MODIFY ANY OF THE FOLLOWING CODE
    #Build graph object
    graph = util.build_MSTBaseGraph(args)
    #you may print the configuration of the graph -- only effective for graphs with up to 10 vertex
    #graph.printMe()

    #Calculate kruskal's alg for MST
    MST_Kruskal, uf = kruskal(graph)

    #verify against provided prim's algorithm results
    util.verify_MSTKruskalResults(args, MST_Kruskal, args.printMST)

if __name__ == '__main__':
    main()