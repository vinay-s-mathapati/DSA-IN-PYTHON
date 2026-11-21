class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Step 1: Build original tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        # Step 2: Build modified tree
        new_tree = [[] for _ in range(n)]
        last_seen = {}

        stack = [(0, False, -1)]

        while stack:
            node, exiting, previous = stack.pop()
            ch = s[node]

            if exiting:
                if previous == -1:
                    last_seen.pop(ch, None)
                else:
                    last_seen[ch] = previous
                continue

            old = last_seen.get(ch, -1)

            if node != 0:
                new_parent = old if old != -1 else parent[node]
                new_tree[new_parent].append(node)

            last_seen[ch] = node

            stack.append((node, True, old))

            for child in reversed(tree[node]):
                stack.append((child, False, -1))

        # Step 3: Calculate subtree sizes
        order = [0]

        for node in order:
            for child in new_tree[node]:
                order.append(child)

        size = [1] * n

        for node in reversed(order):
            for child in new_tree[node]:
                size[node] += size[child]

        return size