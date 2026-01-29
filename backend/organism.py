"""
organism.py - The Living Worker
This script performs tasks and can be mutated by the Architect.
"""
import time
import random


def run():
    """Main execution loop of the organism"""
    print("🧬 Organism Generation 1 - ALIVE")
    print("=" * 50)
    
    # Simulating work - sorting task
    data = [random.randint(1, 100) for _ in range(10)]
    print(f"📊 Processing data: {data}")
    
    # Bubble sort (intentionally slow - the AI will optimize this)
    sorted_data = data.copy()
    n = len(sorted_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    
    print(f"✅ Sorted: {sorted_data}")
    
    # Simulating computation time
    time.sleep(0.5)
    
    print("💚 Work cycle complete")
    print("=" * 50)


if __name__ == "__main__":
    run()
