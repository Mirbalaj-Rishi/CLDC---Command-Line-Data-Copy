import argparse

def main(): # boiler plate argument parser
    # Initialize the parser
    parser = argparse.ArgumentParser(description="Command Line Data Copy")

    # Add arguments
    parser.add_argument("required_argument", help="A required argument.")
    parser.add_argument("-o", "--optional_argument", help="An optional argument.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments
    required_arg = args.required_argument
    optional_arg = args.optional_argument
    verbose = args.verbose

    # Example usage
    print(f"Required argument: {required_arg}")
    if optional_arg:
        print(f"Optional argument: {optional_arg}")
    if verbose:
        print("Verbose mode enabled.")

if __name__ == "__main__":
    main()