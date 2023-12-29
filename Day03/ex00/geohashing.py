import sys
import antigravity

def geohash(latitude, longitude, datedow):
    try:
        antigravity.geohash(float(latitude), float(longitude), datedow.encode())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: geohashing.py latitude longitude datedow")
        sys.exit(1)

    geohash(sys.argv[1], sys.argv[2], sys.argv[3])