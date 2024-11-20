def get_cutting_plan(total_length, cut_sizes):
    """
    Function to determine the most efficient cutting plan that minimizes waste.
    total_length: the total length of wood available.
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
    Function to print the cutting plan and leftover wood.
    cuts: the cutting plan (list of lists).
    remaining_length: the leftover wood after cutting.
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
    Function to prompt the user for input, interactively, with validation.
    """
    print("Welcome to EffiCut - the efficient cutting optimizer!")

    # Get the total length of the wood with input validation
    while True:
        try:
            total_length = int(input("Enter the total length of wood (in units): "))
            if total_length <= 0:
                print("Total length must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the total length.")

    # Get the sizes of cuts needed with input validation
    cut_sizes = []
    print("Enter the sizes of cuts you need (enter 0 to stop):")
    
    while True:
        try:
            cut_size = int(input("Enter a cut size: "))
            if cut_size < 0:
                print("Cut size cannot be negative. Please enter a valid size.")
                continue
            if cut_size == 0:
                break
            cut_sizes.append(cut_size)
        except ValueError:
            print("Invalid input! Please enter a valid integer for the cut size.")
    
    return total_length, cut_sizes

def main():
    """
    Main function to run the EffiCut program.
    """
    total_length, cut_sizes = get_input()

    if not cut_sizes:
        print("No cuts specified. Exiting the program.")
        return
    
    cuts, remaining_length = get_cutting_plan(total_length, cut_sizes)
    
    print_cutting_plan(cuts, remaining_length)

if __name__ == "__main__":
    main()
