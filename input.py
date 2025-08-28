def get_user_input(filenames, storage_names):
    for one_file in filenames:
        print(one_file)
    filename = input("Please enter the name of the file you'd like to analyse : ")
    while filename not in filenames:
        filename = input("Please enter a valid file : ")
    print("Enter the name of the file to store the results : ")
    for one in storage_names:
        print(one)
    storage = input("Enter a valid storage : ")
    while storage not in storage_names:
        storage = input("Enter a valid storage : ")
    return (filename, storage)