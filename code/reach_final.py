import pickle

def dp():
    dp.memo = {}
    dp.k_table = {}

def k(p, adj, categories):
    res = None
    if len(categories.get(p, set([]))) == 0:
        for q in adj.get(p, []):
            dp.k_table[(p, q)] = 1
        return

    for q in adj.get(p, []):
        diff = categories.get(q, set([])) - categories.get(p, set([]))
        if len(diff) == 0:
            res = 1
        else:
            res = len(diff)
        dp.k_table[(p, q)] = res

# Run k(p) for all nodes before running reach. It will take time proportional to O(V + E)

def reach(p, parent, h, adj, visited, cutoff):
    if p in visited:
        return None
    
    if h > cutoff:
        return None

    visited.add(p)

    if (p, h) in dp.memo:
        return dp.memo[(p, h)]

    rp = len(adj.get(p,[])) * dp.k_table.get((parent, p), 1) * h
    np = 1
    hp = h
    for q in adj.get(p,[]):
        reach_tuple = reach(q, p, h + 1, adj, visited, cutoff)
        if reach_tuple is None:
            continue

        rq, hq, nq = reach_tuple
        rp = rp + rq
        hp = max(hp , hq)   
        np = np + nq

    dp.memo[(p, h)] = (rp, hp, np)

    return (rp, hp, np)

# Call for each paper : reach(p, None, 0, adj, set([]), cutoff)
graph = pickle.load(open('graph.pickle', 'rb'))
category_map = pickle.load(open('category_map.pickle', 'rb'))

dp()
for p in graph.keys():
    k(p, adj=graph, categories=category_map)

reach_vals = dict()

for p in graph.keys():
    r = reach(p=p, parent=None, h=0, adj=graph, visited=set([]), cutoff=50)
    reach_vals[p] = r

pickle.dump(reach_vals, open('reach_vals_with_category_50.pickle', 'wb'))
