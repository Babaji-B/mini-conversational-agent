# modules/memory.py
"""
Memory module for our agent.
Implements a simple in-memory store to retain user information across conversation turns.
"""

class Memory:
    """
    A simple memory class to store and retrieve user profile information like name and city.
    Uses an internal dictionary for in-memory storage.
    """

    def __init__(self):
        """
        Initializes an empty memory store.
        """
        self.store = {}

    def update(self, key, value):
        """
        Updates the memory with a key-value pair.
        Input:
            key (str): The name of the field to store (e.g., 'user_name', 'user_city').
            value (str): The value to store.
        """
        self.store[key] = value

    def get(self, key):
        """
        Retrieves the value associated with a key from memory.
        Input:
            key (str): The field to retrieve.
        Returns:
            str or None: The stored value, or None if the key is not found.
        """
        return self.store.get(key, None)

    def clear(self):
        """
        Clears all stored memory data.
        """
        self.store.clear()

    def show_memory(self):
        """
        Prints the current memory store for debugging or demonstration purposes.
        """
        print("Current Memory State:", self.store)
