# graph.py

from collections import defaultdict

class Graph:
    def __init__(self):
        # Adjacency list representation
        self.adj_list = defaultdict(set)

    def add_user(self, user):
        """Add a new user to the network."""
        if user not in self.adj_list:
            self.adj_list[user] = set()

    def add_friendship(self, user1, user2):
        """Create an undirected friendship."""
        self.adj_list[user1].add(user2)
        self.adj_list[user2].add(user1)

    def remove_friendship(self, user1, user2):
        """Remove friendship between two users."""
        self.adj_list[user1].discard(user2)
        self.adj_list[user2].discard(user1)

    def get_friends(self, user):
        """Return direct friends of a user."""
        return self.adj_list.get(user, set())

    def get_all_users(self):
        """Return all users in the network."""
        return list(self.adj_list.keys())

    def display(self):
        """Print the graph structure."""
        for user, friends in self.adj_list.items():
            print(f"{user}: {list(friends)}")