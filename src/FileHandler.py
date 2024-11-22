import os

def normalize_color(color):
    """
    Function to normalize color names by converting to lowercase and replacing spaces.
    Ensures unique, consistent folder names for all color inputs.
    """
    return color.strip().lower().replace(" ", "_").replace("-", "_")

def clear_screen(preserve_logo=False, logo_height=14):
    """
    Clears the console screen.
    If preserve_logo is True, skips clearing the first `logo_height` lines.
    """
    if preserve_logo:
        # ANSI escape code to move the cursor below the logo
        print("\033[" + str(logo_height + 1) + "H\033[J", end="")
    else:
        os.system("cls" if os.name == "nt" else "clear")

def save_cutting_plan_to_file(cuts, remaining_length, total_length, project_name="DefaultProject", filename="File.txt", color="N/A"):
    """
    Function to save the cutting plan, total length, and leftover wood to a file in the project folder.
    cuts: the cutting plan (list of lists).
    remaining_length: the leftover wood after cutting.
    total_length: the original total length of the wood.
    project_name: name of the project to organize files.
    filename: name of the file to save the output.
    color: the color of the material being cut.
    """
    clear_screen()  # Clear screen before starting the save process
    print("Saving the cutting plan...")

    # Normalize the color
    normalized_color = normalize_color(color)

    # Locate the directory containing main.py (project root folder)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Define the target folder path with normalized color
    folder_path = os.path.join(project_root, "cuts", project_name, normalized_color)
    os.makedirs(folder_path, exist_ok=True)  # Create directories if they don't exist
    
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)
    
    # Write the cutting plan to the file
    with open(file_path, "w") as file:
        file.write("EffiCut Cutting Plan:\n\n")
        file.write(f"Project Name: {project_name}\n")
        file.write(f"Color of Material: {normalized_color.replace('_', ' ').capitalize()} ({color})\n")
        file.write(f"Total Length of Material: {total_length} units\n")
        
        total_cut_count = sum(len(cut_group) for cut_group in cuts)
        file.write(f"Total Number of Cuts: {total_cut_count}\n")
        file.write("Cutting Plan:\n")
        
        for i, cut_group in enumerate(cuts, 1):
            file.write(f"  Cut {i}: {cut_group}\n")
        
        file.write(f"\nRemaining Waste: {remaining_length} units\n")
    
    clear_screen()  # Clear screen after saving
    print(f"Cutting plan successfully saved to: {file_path}")
