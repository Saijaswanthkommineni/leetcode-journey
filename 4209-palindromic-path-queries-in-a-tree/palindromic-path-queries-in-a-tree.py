class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
    def update(self, node, start, end, idx, char_bit):
        if start == end:
            self.tree[node] = char_bit
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, char_bit)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, char_bit)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 ^ p2
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        def dfs_sz(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_c_size = 0
            for v in adj[u]:
                if v != p:
                    c_size = dfs_sz(v, u, d + 1)
                    size += c_size
                    if c_size > max_c_size:
                        max_c_size = c_size
                        heavy[u] = v
            return size
        def dfs_hld(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs_hld(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs_hld(v, v)
        dfs_sz(0, -1, 0)
        dfs_hld(0, 0)
        seg_tree = SegmentTree(n)
        s_list = list(s)
        for i in range(n):
            bit = 1 << (ord(s_list[i]) - ord('a'))
            seg_tree.update(1, 0, n - 1, pos[i], bit)
        def query_path(u, v):
            res_mask = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res_mask ^= seg_tree.query(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res_mask ^= seg_tree.query(1, 0, n - 1, pos[u], pos[v])
            return res_mask
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                bit = 1 << (ord(c) - ord('a'))
                seg_tree.update(1, 0, n - 1, pos[u], bit)
            else:
                u = int(parts[1])
                v = int(parts[2])
                path_mask = query_path(u, v)
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
        return ans