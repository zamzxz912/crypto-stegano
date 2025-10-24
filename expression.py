print("=== calc hybrid ===")

while True:
    exp = input("\ninput ekspresi: ")

    try:
        res = eval(exp)
        print(f"{exp} = {res}")
    except Exception as e:
        print(f"err: {e}")

    restart = input("\nrestart? (y/n): ").lower()
    if restart != 'y':
        print("finished.")
        break
