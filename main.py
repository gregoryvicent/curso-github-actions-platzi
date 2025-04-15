import os


def main():
    username = os.getenv("USERNAME")
    print(f"Hello {username}, how are you?")

if __name__ == "__main__":
    main()
