from src.FileHandler import save_cutting_plan_to_file
import os
from colorama import init, Fore, Style

init(autoreset=True)

# Initialize colorama
init(autoreset=True)

def clear_screen(preserve_logo=True, logo_height=14):
    """
    Clears the console screen.
    If preserve_logo is True, skips clearing the first `logo_height` lines.
    """
    if preserve_logo:
        # ANSI escape code to move the cursor below the logo
        print("\033[" + str(logo_height + 1) + "H\033[J", end="")
    else:
        os.system("cls" if os.name == "nt" else "clear")
    
def get_cutting_plan(total_length, cut_sizes):
    """
    Function to determine the most efficient cutting plan that minimizes waste.
    total_length: the total length of beam available.
    cut_sizes: list of the required cut sizes.
    
    Returns: a list of cuts, each represented by a length of the cut, and the remaining waste.
    """
    cuts = []
    cut_sizes.sort(reverse=True)  # Sort cuts in descending order for optimal fitting

    # Try to fill as many cuts as possible into the total length
    while cut_sizes:
        remaining_length = total_length
        current_cut_plan = []

        # Try to fit as many cuts as possible into the remaining length
        for cut_size in cut_sizes[:]:
            if remaining_length >= cut_size:
                remaining_length -= cut_size
                current_cut_plan.append(cut_size)
                cut_sizes.remove(cut_size)

        cuts.append(current_cut_plan)

    return cuts, remaining_length


def print_cutting_plan(cuts, remaining_length):
    """
    Function to print the cutting plan and leftover beam.
    cuts: the cutting plan (list of lists).
    remaining_length: the leftover beam after cutting.
    """
    print("\nEffiCut Cutting Plan:\n")

    total_cut_count = sum(len(cut_group) for cut_group in cuts)
    print(f"Total number of cuts: {total_cut_count}")
    print("Cutting Plan:")

    for i, cut_group in enumerate(cuts, 1):
        print(f"  Cut {i}: {cut_group}")

    print(f"\nRemaining waste: {remaining_length} units")


def get_input():
    """
    Function to prompt the user for input interactively with validation.
    Validates each cut size against the total length and asks for quantity immediately.
    """
    # Get the total length of the beam with input validation
    while True:
        clear_screen()
        print(Fore.WHITE + "Enter the total length of the beam (in units):")
        try:
            total_length = int(input(Fore.WHITE + "Length: "))
            if total_length <= 0:
                print(Fore.RED + "Total length must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid integer for the total length.")

    # Get the sizes of cuts needed with validation and ask for quantity after each size
    quantities = []
    while True:
        clear_screen()
        print(Fore.WHITE + "Enter the sizes of cuts you need (enter 0 to stop):")
        try:
            cut_size = int(input(Fore.WHITE + "Cut size: "))
            if cut_size == 0:  # Stop when user enters 0
                break
            if cut_size <= 0:
                print(Fore.RED + "Cut size must be a positive integer. Please enter a valid size.")
                continue
            if cut_size > total_length:
                print(Fore.RED + "Fill in a valid Unit size! Not too big.")
                continue

            # Ask for the quantity of this cut size
            while True:
                print(Fore.WHITE + f"For cut size {cut_size}, how many pieces do you need?")
                try:
                    quantity = int(input(Fore.WHITE + "Quantity: "))
                    if quantity <= 0:
                        print(Fore.RED + "Quantity must be a positive integer. Please try again.")
                        continue
                    quantities.append((cut_size, quantity))
                    break
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a valid integer for the quantity.")
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid integer for the cut size.")

    clear_screen()  # Clear after input process is complete
    return total_length, quantities

def main():
    """
    Main function to run the EffiCut program with options for multiple calculations.
    """
    while True:
        clear_screen()  # Clear at the start of the program
        print("\n--- EffiCut - Efficient Cutting Optimizer ---")
        total_length, quantities = get_input()

        if not quantities:
            print("No cuts specified. Exiting the program.")
            return

        # Flatten the quantities into a list of cut sizes
        cut_sizes = [cut_size for cut_size, quantity in quantities for _ in range(quantity)]

        cuts, remaining_length = get_cutting_plan(total_length, cut_sizes)
        clear_screen()  # Clear before showing the cutting plan
        print_cutting_plan(cuts, remaining_length)

        # Prompt user for project name and color
        project_name = input("\nEnter the project name (e.g., Shopping Cart): ").strip()
        color = input("Enter the color of the beam being cut (e.g., Black): ").strip()

        # Generate folder name and file name
        folder_name = project_name
        color_initial = color[0].lower() if color else "x"  # Use 'x' if no color
        project_initials = "".join(word[0].lower() for word in project_name.split()[:2])  # First two initials
        file_name = f"output-{color_initial}-{project_initials}.txt"

        # Save the cutting plan
        clear_screen()  # Clear before saving the file
        save_cutting_plan_to_file(cuts, remaining_length, total_length, project_name=folder_name, filename=file_name, color=color)
        print(f"Cutting plan saved as '{file_name}' in folder '{folder_name}'.\n")

        # Ask if the user wants to perform another calculation
        while True:
            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice == "yes":
                clear_screen()  # Clear before starting a new calculation
                break  # Continue to the next calculation
            elif continue_choice == "no":
                # Confirm quitting with an additional prompt
                while True:
                    quit_choice = input("Are you sure you want to quit? (yes/no): ").strip().lower()
                    if quit_choice == "yes":
                        clear_screen()  # Clear before exiting
                        print("Thank you for using EffiCut! Goodbye.")
                        return  # Exit the program
                    elif quit_choice == "no":
                        clear_screen()  # Clear before returning to the main menu
                        print("Returning to the main menu.")
                        break  # Return to the main menu
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                break  # Exit the quit confirmation loop if the user chose "no"
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
