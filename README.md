Got it! Based on your feedback, I've updated the usage instructions to reflect a more interactive approach where the program asks for the total wood length in millimeters and then prompts the user to input the sizes of cuts they need, one by one, until all required sizes are provided.

Here's the updated **README** for **Efficut**:

---

# Efficut - README

## Overview

**Efficut** is a simple and efficient wood cutting optimization tool designed to minimize waste when cutting wood into specific lengths. You provide the total wood length and the sizes you need, and Efficut will calculate the most efficient way to cut your wood, ensuring minimal leftover material.

## Features

- **Cutting Optimization**: Automatically calculates the most efficient cutting plan to minimize waste.
- **Interactive Input**: Efficut prompts you to input the total length of wood and the specific sizes of cuts you need, one by one.
- **Minimal Waste**: Efficut ensures that leftover material is as minimal as possible.
- **Simple and Intuitive**: Easy-to-follow prompts guide you through the cutting process without needing any prior experience.

## Installation

Efficut is easy to install and works on all major platforms (Windows, macOS, and Linux).

### Prerequisites

- No special dependencies are required.
- Efficut runs directly on Python 3.x.

### Install via Download

To install Efficut, download the latest release from the [GitHub Releases page](https://github.com/yourusername/efficut/releases).

### Install via Source (Optional)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/efficut.git
   ```
2. Navigate to the project directory:
   ```bash
   cd efficut
   ```
3. Run the program:
   ```bash
   python efficut.py
   ```

## Usage

### How to Use Efficut

Efficut provides an interactive command-line interface (CLI) that guides you through the process of entering your wood lengths and required cuts.

1. **Total Wood Length**: You’ll first be prompted to enter the total available length of wood in millimeters (e.g., 1920 mm).
2. **Required Cut Sizes**: After that, you’ll be prompted to enter the size of each piece you need. You can continue entering the required sizes, and Efficut will keep asking for more until you've entered all the cuts.
3. **Efficient Cutting Plan**: After entering all the sizes, Efficut will calculate the optimal cutting plan and output the sequence of cuts, as well as the leftover wood (waste).

### Example

Here’s an example of what the interactive session might look like when you run the program:

```
Efficut: Wood Cutting Optimization Tool

Step 1: Enter the total length of available wood in mm:
1920

Step 2: Enter the length of the first piece you need in mm:
720

Step 3: Enter the length of the next piece you need in mm (or press Enter to finish):
720

Step 4: Enter the length of the next piece you need in mm (or press Enter to finish):
1500

Step 5: Enter the length of the next piece you need in mm (or press Enter to finish):
[Press Enter without entering a value to finish input]

Cutting Plan:
1. Cut 720 mm
2. Cut 720 mm
3. Cut 480 mm
4. Waste: 0 mm
```

The program will keep asking you to input the required lengths until you press **Enter** without entering a number, signaling the end of the input.

### Running the Program

To run the program, simply execute the script from the command line:

```bash
python efficut.py
```

### What the Program Does

1. It will ask you to input the total length of the wood (in millimeters).
2. Then, it will repeatedly ask for the size of each piece you need to cut from that wood.
3. After you've entered all the required sizes, Efficut will calculate the most efficient way to cut the wood, displaying a list of the cuts and any waste material left over.

### Example Run (Python File):

```bash
$ python efficut.py
Efficut: Wood Cutting Optimization Tool

Step 1: Enter the total length of available wood in mm:
1920

Step 2: Enter the length of the first piece you need in mm:
720

Step 3: Enter the length of the next piece you need in mm (or press Enter to finish):
720

Step 4: Enter the length of the next piece you need in mm (or press Enter to finish):
1500

Step 5: Enter the length of the next piece you need in mm (or press Enter to finish):
[Press Enter without entering a value to finish input]

Cutting Plan:
1. Cut 720 mm
2. Cut 720 mm
3. Cut 480 mm
Waste: 0 mm
```

### Output

Efficut will display a step-by-step cutting plan, showing which pieces to cut and how much waste material (if any) remains after all cuts have been made.

## License

Efficut is open-source software and is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Efficut** helps you optimize your wood cutting by ensuring minimal waste, saving you money on materials, and making your project more efficient.

---
