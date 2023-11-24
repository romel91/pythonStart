# It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
def main(Romel):
    print("This code is executed when you run this file directly.")
if __name__ == "__main__":
    main()

# The main() function will only be called if the script is run directly, not when it's imported as a module into another script.
#  This helps organize and separate code that is intended for direct execution from code that is intended to be used as a module.