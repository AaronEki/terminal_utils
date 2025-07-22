# y = yank, p = paste, u = undo
import json

# Add item function to add a new item to the to do list
# ================
# WORK IN PROGRESS
# ================
def add_item(file_path, name, subtask_list, due):
    # read file and use the .append function to add the data to the file
    with open(file_path, 'r+') as file:
        file_data = json.load(file)

        # Getting the ID of the last object in the file (+1)
        new_id=file_data[-1]["id"] + 1

        # Building the new json object
        new_date = {
            "id": new_id,
            "task_name": name,
            "subtasks": subtask_list,
            "due": due,
            "complete": False        
        }

        # Write the new json data to the database file
        try:
            file_data.append(new_data)
            
            # Move the cursor to the beginning of the file
            file.seek(0)
            
            # Write the updated data back to the file
            json.dump(file_data, file, indent=4)
            print(f"Item ID: {new_id} successfully written to a file")

        except Exception as e:
            print(f"Exception raised: {e}")

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

    # Test the new add_item function
    # name = <USER INPUT NAME flag? or stdin?>
    # subtask_list = <build a user prompt with while loop to build up subtask list>
    # due = <user input- flag or stdin?>
    # add_item(file_path, name, subtask_list, due)
   
if __name__ == "__main__":
    file_path = "/home/binieki/.local/util_files/database.json"
    main(file_path)
