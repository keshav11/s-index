import pickle
import math
def dp():
    dp.memo = {}

def reach(p, h, adj, visited, cutoff):
    if p in visited:
        return None
    
    if h > cutoff:
        return None

    visited.add(p)

    if (p, h) in dp.memo:
        return dp.memo[(p, h)]

    rp = len(adj.get(p,[])) * (h)
    np = 1
    hp = h
    for q in adj.get(p,[]):
        reach_tuple = reach(q, h + 1, adj, visited, cutoff)
        if reach_tuple is None:
            continue

        rq, hq, nq = reach_tuple
        rp = rp + rq
        hp = max(hp , hq)   
        np = np + nq

    dp.memo[(p, h)] = (rp, hp, np)

    return (rp, hp, np)


graph = pickle.load(open('graph.pickle', 'rb'))
reach_vals = dict()
dp()
for p in graph.keys():
    r = reach(p=p, h=0, adj=graph, visited=set([]), cutoff=6)
    reach_vals[p] = r

pickle.dump(reach_vals, open('reach_vals_cutoff_6.pickle', 'wb'))

