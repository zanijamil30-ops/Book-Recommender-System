"""
==========================================
 Book Recommender System - Main Script
==========================================

This script serves as the entry point for running the Book Recommender System.
It loads configuration parameters from config/params.yaml and then runs
the main functions defined in src/book_recommender_system.py.

Author: zainab jamil
License: MIT
"""

# --- Import Required Libraries ---
import yaml
import os
import sys

# --- Import Your Recommender Script ---
# Assuming your recommender code is located in src/book_recommender_system.py
from src.book_recommender_system import interactive_recommend

# --- Load Configuration Parameters ---
def load_params(config_path="config/params.yaml"):
    """Load project parameters from YAML configuration file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, "r") as file:
        params = yaml.safe_load(file)
    print("Configuration loaded successfully.")
    return params


# --- Main Function ---
def main():
    print("Starting Book Recommender System...")
    params = load_params()

    # Display some key configuration parameters
    print("\nParameters:")
    print(f"  RATING_THRESHOLD: {params['RATING_THRESHOLD']}")
    print(f"  MIN_USER_RATINGS: {params['MIN_USER_RATINGS']}")
    print(f"  MIN_BOOK_RATINGS: {params['MIN_BOOK_RATINGS']}")
    print(f"  TOP_K: {params['TOP_K']}")
    print("\nInitializing model and recommendation process...\n")

    # Run the recommendation function (you can adjust based on your code)
    try:
        interactive_recommend()
        print("\nRecommender system executed successfully.")
    except Exception as e:
        print(f"\nError running recommender: {e}")


# --- Run Script ---
if __name__ == "__main__":
    main()
