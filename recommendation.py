# recommendation.py

from collections import defaultdict, deque

class RecommendationEngine:
    def __init__(self, graph):
        self.graph = graph

    def recommend_by_mutual_friends(self, user):
        """
        Recommend friends based on number of mutual friends.
        Returns a sorted list (highest mutual count first).
        """
        if user not in self.graph.adj_list:
            return []

        mutual_counts = defaultdict(int)
        user_friends = self.graph.get_friends(user)

        for friend in user_friends:
            for mutual in self.graph.get_friends(friend):
                if mutual != user and mutual not in user_friends:
                    mutual_counts[mutual] += 1

        # Sort by highest mutual friend count
        return sorted(mutual_counts.items(), key=lambda x: -x[1])

    def recommend_by_bfs(self, user):
        """
        Recommend friends using BFS (distance = 2).
        """
        if user not in self.graph.adj_list:
            return []

        visited = set([user])
        queue = deque([(user, 0)])
        recommendations = defaultdict(int)

        while queue:
            current, level = queue.popleft()

            if level == 2:
                recommendations[current] += 1
                continue

            for neighbor in self.graph.get_friends(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

        # Remove direct friends if accidentally included
        for friend in self.graph.get_friends(user):
            recommendations.pop(friend, None)

        return sorted(recommendations.items(), key=lambda x: -x[1])