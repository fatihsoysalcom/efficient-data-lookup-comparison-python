import time
import random

def generate_user_data(num_users):
    """Generates a list of dummy user dictionaries."""
    users = []
    for i in range(num_users):
        users.append({'id': i + 100000, 'name': f'User_{i+1}'})
    return users

def linear_search(users, user_id):
    """
    Performs a linear search to find a user by ID.
    This is a simple, brute-force algorithm.
    Time complexity: O(n) in the worst case.
    """
    for user in users:
        if user['id'] == user_id:
            return user
    return None

def build_user_index(users):
    """
    Builds a hash map (Python dictionary) for efficient user lookup by ID.
    This demonstrates using a data structure optimized for fast access.
    Time complexity for building: O(n).
    """
    user_index = {user['id']: user for user in users}
    return user_index

def hash_map_lookup(user_index, user_id):
    """
    Performs a lookup using a hash map (dictionary).
    This leverages the efficient O(1) average time complexity of hash maps.
    """
    return user_index.get(user_id)

if __name__ == "__main__":
    NUM_USERS = 1_000_000  # Simulate a large dataset
    NUM_SEARCHES = 100     # Number of search operations to perform

    print(f"Generating {NUM_USERS} user records...")
    all_users = generate_user_data(NUM_USERS)
    print("Data generation complete.\n")

    # --- Demonstrate Linear Search ---
    print("--- Linear Search Performance ---")
    search_ids_linear = [random.choice(all_users)['id'] for _ in range(NUM_SEARCHES)]
    start_time = time.perf_counter()
    for user_id in search_ids_linear:
        linear_search(all_users, user_id)
    end_time = time.perf_counter()
    linear_search_time = end_time - start_time
    print(f"Time taken for {NUM_SEARCHES} linear searches: {linear_search_time:.6f} seconds")
    # Linear search is simple but inefficient for large datasets (O(N)).

    # --- Demonstrate Hash Map Lookup ---
    print("\n--- Hash Map Lookup Performance ---")
    print("Building hash map (user index)...")
    start_time = time.perf_counter()
    user_index = build_user_index(all_users) # DSA concept: building an efficient data structure
    end_time = time.perf_counter()
    build_time = end_time - start_time
    print(f"Time taken to build hash map: {build_time:.6f} seconds")

    search_ids_hash_map = [random.choice(all_users)['id'] for _ in range(NUM_SEARCHES)]
    start_time = time.perf_counter()
    for user_id in search_ids_hash_map:
        hash_map_lookup(user_index, user_id) # DSA concept: O(1) average time lookup
    end_time = time.perf_counter()
    hash_map_lookup_time = end_time - start_time
    print(f"Time taken for {NUM_SEARCHES} hash map lookups: {hash_map_lookup_time:.6f} seconds")

    print("\n--- Summary ---")
    print(f"Linear Search (O(N)): {linear_search_time:.6f} seconds")
    print(f"Hash Map Lookup (O(1) avg): {hash_map_lookup_time:.6f} seconds (after O(N) build time)")
    print("\nThis example highlights how choosing the right data structure and algorithm (DSA) can dramatically improve performance for common operations like searching, especially with large datasets. While DSA is fundamental, real-world problems often require combining these foundational skills with broader system design and engineering principles.")
