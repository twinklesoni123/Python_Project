from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_friendship(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def recommend_friends(self, user):
        if user not in self.graph:
            return []

        visited = set([user])
        queue = deque([(user, 0)])
        recommendations = defaultdict(int)

        while queue:
            current, level = queue.popleft()

            if level == 2:
                recommendations[current] += 1
                continue

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

        # Remove direct friends
        for friend in self.graph[user]:
            recommendations.pop(friend, None)

        return sorted(recommendations, key=lambda x: -recommendations[x])