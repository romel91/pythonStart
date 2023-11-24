import os 
# cwd = os.getcwd() 
# print("Current working directory:", cwd) 





def current_path():
    print("Current working directory after:")
    print(os.getcwd())  # Print or use the result of os.getcwd()

print("Current working directory before:")
print("Original working directory:", os.getcwd())  # Print the original working directory
os.chdir('../')

# Call the current_path function to print the updated working directory
current_path()


