func resultArray(nums []int, k int, queries [][]int) []int {
	n := len(nums)
	type Node struct {
		cnt [6]int
		mul int
	}
	tree := make([]Node, 4*n)
	merge := func(a, b Node) Node {
		var res Node
		res.mul = (a.mul * b.mul) % k
		for i := 0; i < k; i++ {
			res.cnt[i] = a.cnt[i]
		}
		for i := 0; i < k; i++ {
			res.cnt[(a.mul*i)%k] += b.cnt[i]
		}
		return res
	}
	leaf := func(v int) Node {
		var res Node
		r := v % k
		if r < 0 {
			r += k
		}
		res.cnt[r] = 1
		res.mul = r
		return res
	}
	var build func(int, int, int)
	build = func(p, l, r int) {
		if l == r {
			tree[p] = leaf(nums[l])
			return
		}
		m := l + (r-l)/2
		build(p*2, l, m)
		build(p*2+1, m+1, r)
		tree[p] = merge(tree[p*2], tree[p*2+1])
	}
	var update func(int, int, int, int, int)
	update = func(p, l, r, idx, v int) {
		if l == r {
			tree[p] = leaf(v)
			return
		}
		m := l + (r-l)/2
		if idx <= m {
			update(p*2, l, m, idx, v)
		} else {
			update(p*2+1, m+1, r, idx, v)
		}
		tree[p] = merge(tree[p*2], tree[p*2+1])
	}
	var query func(int, int, int, int, int) Node
	query = func(p, l, r, ql, qr int) Node {
		if ql <= l && r <= qr {
			return tree[p]
		}
		m := l + (r-l)/2
		if qr <= m {
			return query(p*2, l, m, ql, qr)
		}
		if ql > m {
			return query(p*2+1, m+1, r, ql, qr)
		}
		return merge(
			query(p*2, l, m, ql, qr),
			query(p*2+1, m+1, r, ql, qr),
		)
	}
	build(1, 0, n-1)
	ans := make([]int, 0, len(queries))
	for _, q := range queries {
		update(1, 0, n-1, q[0], q[1])
		res := query(1, 0, n-1, q[2], n-1)
		ans = append(ans, res.cnt[q[3]])
	}
	return ans
}