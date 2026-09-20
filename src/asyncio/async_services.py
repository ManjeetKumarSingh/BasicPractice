import asyncio
import time


async def fetch_data(name, sequence):
    print("--" * 40)
    print(f"{sequence}: Fetching data for {name}...")
    print("--" * 40)
    await asyncio.sleep(4)  # Simulate a delay of 4 seconds
    print("--" * 20)
    print(f"{sequence}: Data fetched for {name}.")
    print("--" * 20)
    return f"Data for {name}"


async def main():
    start = time.time()
    results = await asyncio.gather(
        fetch_data("Alice", 1), fetch_data("Bob", 2), fetch_data("Charlie", 3)
    )
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
    # print("=="*40)
    # print("All data fetched:", results)
    # print("=="*40)
    return results


data = asyncio.run(main())
print(data)
