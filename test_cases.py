# test_cases.py

from graph import Graph
from recommendation import RecommendationEngine

def run_tests():
    print("Running Test Cases...\n")

    # Create graph
    network = Graph()

    # Add users
    users = ["A", "B", "C", "D", "E", "F"]
    for user in users:
        network.add_user(user)

    # Add friendships
    network.add_friendship("A", "B")
    network.add_friendship("A", "D")
    network.add_friendship("B", "C")
    network.add_friendship("B", "E")
    network.add_friendship("D", "E")
    network.add_friendship("E", "F")

    print("Graph Structure:")
    network.display()
    print("\n")

    recommender = RecommendationEngine(network)

    # Test Case 1: Mutual Friend Recommendation
    print("Test 1: Mutual Friend Recommendation for A")
    result = recommender.recommend_by_mutual_friends("A")
    print("Recommended:", result)
    print("Expected: E (2 mutual), C (1 mutual)\n")

    # Test Case 2: BFS Recommendation
    print("Test 2: BFS Recommendation for A")
    result = recommender.recommend_by_bfs("A")
    print("Recommended:", result)
    print("Expected: E, C\n")

    # Test Case 3: User with no friends
    print("Test 3: Recommendation for isolated user F")
    result = recommender.recommend_by_mutual_friends("F")
    print("Recommended:", result)
    print("Expected: [] or minimal\n")

    # Test Case 4: Non-existent user
    print("Test 4: Recommendation for unknown user X")
    result = recommender.recommend_by_mutual_friends("X")
    print("Recommended:", result)
    print("Expected: []\n")


if __name__ == "__main__":
    run_tests()