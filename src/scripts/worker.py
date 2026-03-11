import time


def main() -> None:
    print("worker started")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("worker stopped")


if __name__ == "__main__":
    main()