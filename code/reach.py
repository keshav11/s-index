def dp(n, cutoff):
	memo = [[None] * cutoff for _ in range(n)]

dp()

def reach(p, h, adj, visited, cutoff):
	if p is in visited:
		return None

	if h > cutoff:
		return None

	visited.add(p)

	if dp.memo[p][h] is not None:
		return dp.memo[p][h]

	rp = len(adj[p]) * (2 ^ h)
	np = 1
	hp = h
	for q in adj[p]:
		reach_tuple = reach(q, h + 1, dp.memo, adj, visited)
		if reach_tuple is None:
			continue

		rq, hq, nq = reach_tuple
		rp = rp + rq
		hp = max(hp, hp + hq)	
		np = np + nq

	dp.memo[p][h] = (rp, hp, np)

	return (rp, hp, np)


