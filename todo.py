# y = yank, p = paste, u = undo
import json

def add_item(file_path):
    print("")

def del_item(file_path):
    # Add a "are you sure you want to delete {print item here} y/n before deletion]
    # append deleted item to an archive.json 
    print("")

def edit_item(file_path):
    # Do like an edit name, date, etc.
    # Return to edit and use a q to back out of edit mode
    print("")

def complete_item(file_path):
    # Set the completion on a task / subtask based on id
    print("")

# Function to display the to do list in the terminal
def display_list(file_path):
    
    # read file
    with open(f"{file_path}", "r") as data:
        file_data = json.load(data)
    
    print("")
    
    count = 0

    # Parse json and print to do items
    for item in file_data:
        if count !=0:
            print("-")
        if item["complete"] == False:
            output = f"[ x ]  {item["id"]}. {item["task_name"]} - {item["due"]}"
        else:
            output = f"[ ✓ ]  {item["id"]}. {item["task_name"]} - {item["due"]}"
        
        print(output)
        
        # printing subtasks
        if item["subtasks"]:
            for subtask in item["subtasks"]:
                if subtask[2] == False:
                    print(f"         > [ x ]  {subtask[0]}.  {subtask[1]}")
                else:
                    print(f"         > [ ✓ ]  {subtask[0]}.  {subtask[1]}")
        count += 1 
    print("")


def main(file_path):
    # Add functionality for running the program with flags, calling different 
    display_list(file_path)
   
if __name__ == "__main__":
    file_path = "/home/binieki/.local/util_files/database.json"
    main(file_path)
