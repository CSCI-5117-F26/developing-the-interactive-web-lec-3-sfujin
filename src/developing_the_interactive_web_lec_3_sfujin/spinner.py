from halo import Halo

def main() -> None:
    print("Hello from uv-test!")

    with Halo(text='Loading... Press any key!', spinner='dots'):
      input()

main()
