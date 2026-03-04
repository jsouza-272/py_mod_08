import sys


def in_matrix() -> None:
    print("\nMATRIX STATUS: Welcome to the construct")

    # sys.executable path to the Python executable
    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment:", sys.prefix.split('/')[-1])
    print("Environment Path:", sys.prefix)

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting "
          "the global system.")

    print("\nPackage installation path:")
    # sys.path list of directories that Python searches
    # for modules when import is used
    print(sys.path[-1])


def out_matrix() -> None:
    print("\nMATRIX STATUS: You're still plugged in")

    # sys.executable path to the Python executable
    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print('activate # On Windows')

    print("\nThen run this program again.")


if __name__ == "__main__":
    # sys.prefix current Python prefix
    # sys.base_prefix original Python prefix
    if sys.prefix == sys.base_prefix:
        out_matrix()
    else:
        in_matrix()
