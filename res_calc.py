import math
import tkinter as tk
from tkinter import messagebox

# Function to calculate the new resolution based on percentage
def calculate_new_resolution(base_width, base_height, percentage):
    # Calculate the total number of pixels in the original resolution
    total_pixels = base_width * base_height
    
    # Calculate the total number of pixels for the new resolution
    new_total_pixels = (total_pixels * percentage) / 100
    
    # Maintain aspect ratio
    aspect_ratio = base_width / base_height
    
    # Calculate the new width and height
    new_width = math.sqrt(new_total_pixels * aspect_ratio)
    new_height = new_total_pixels / new_width
    
    return int(round(new_width)), int(round(new_height))

# Function to handle the button click event for calculating the resolution
def on_calculate():
    # Get the input values
    resolution_input = entry_resolution.get()
    percentage_input = entry_percentage.get()

    try:
        # Split the input resolution into width and height
        base_width, base_height = map(int, resolution_input.lower().split('x'))

        # Convert percentage input to a float
        percentage = float(percentage_input)

        # Calculate new resolution
        new_width, new_height = calculate_new_resolution(base_width, base_height, percentage)

        # Display the result in the output entry widget
        output_result.delete(0, tk.END)  # Clear previous result
        output_result.insert(0, f"{new_width}x{new_height}")  # Insert new result

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid inputs. Example resolution: 3440x1440, Percentage: 78")

# Function to handle the copy to clipboard button click event
def copy_to_clipboard():
    result_text = output_result.get()
    root.clipboard_clear()
    root.clipboard_append(result_text)
    messagebox.showinfo("Copied", "Resolution copied to clipboard!")

# Function to open the help window with instructions for NVIDIA and AMD
def open_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help - Create Custom Resolution")
    
    label_help = tk.Label(help_window, text="Select your graphics card brand for instructions:")
    label_help.pack(pady=10)

    # Button for NVIDIA instructions
    button_nvidia = tk.Button(help_window, text="NVIDIA", command=show_nvidia_instructions)
    button_nvidia.pack(pady=5)

    # Button for AMD instructions
    button_amd = tk.Button(help_window, text="AMD", command=show_amd_instructions)
    button_amd.pack(pady=5)

    # Button for About App instructions
    button_about_app = tk.Button(help_window, text="About App", command=show_app_instructions)
    button_about_app.pack(pady=5)

# Function to show NVIDIA instructions
def show_nvidia_instructions():
    instructions = (
        "NVIDIA Custom Resolution Instructions:\n\n"
        "1. Open the NVIDIA Control Panel.\n"
        "2. Go to 'Display' > 'Change resolution'.\n"
        "3. Click 'Customize...' at the bottom.\n"
        "4. Check the box for 'Enable resolutions not exposed by the display'.\n"
        "5. Click 'Create Custom Resolution...'.\n"
        "6. Enter your desired resolution settings (e.g., width, height, refresh rate).\n"
        "7. Click 'Test'. If the resolution works, save the settings."
    )
    messagebox.showinfo("NVIDIA Instructions", instructions)

# Function to show AMD instructions
def show_amd_instructions():
    instructions = (
        "AMD Custom Resolution Instructions:\n\n"
        "1. Open AMD Radeon Software (right-click on your desktop and select 'AMD Radeon Software').\n"
        "2. Go to the 'Display' tab.\n"
        "3. Scroll down to find 'Custom Resolutions'.\n"
        "4. Click 'Create' to add a new custom resolution.\n"
        "5. Enter your desired resolution settings (e.g., width, height, refresh rate).\n"
        "6. Click 'Save' and apply the new resolution."
    )
    messagebox.showinfo("AMD Instructions", instructions)

# Function to show About App instructions
def show_app_instructions():
    instructions = (
        "About This App:\n\n"
        "This application helps you calculate a new screen resolution based on a percentage of your current resolution.\n"
        "You can use this app to find a lower or higher resolution that maintains the aspect ratio of your original display.\n\n"
        "Steps to Use:\n"
        "1. Enter your base resolution in the format 'WidthxHeight' (e.g., 3440x1440).\n"
        "2. Enter the desired percentage to calculate the new resolution.\n"
        "3. Click 'Calculate' to see the new resolution.\n"
        "4. You can copy the new resolution to the clipboard by clicking 'Copy to Clipboard'.\n"
        "5. For guidance on setting up a custom resolution in your graphics control panel, click the 'Help' button and choose your graphics card brand."
    )
    messagebox.showinfo("About App", instructions)

# Create the main window
root = tk.Tk()
root.title("Resolution Calculator")

# Create and place the resolution input field
label_resolution = tk.Label(root, text="Enter the base resolution (e.g., 3440x1440):")
label_resolution.pack(pady=5)

entry_resolution = tk.Entry(root)
entry_resolution.pack(pady=5)

# Create and place the percentage input field
label_percentage = tk.Label(root, text="Enter the percentage (e.g., 50 for 50%):")
label_percentage.pack(pady=5)

entry_percentage = tk.Entry(root)
entry_percentage.pack(pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate", command=on_calculate)
button_calculate.pack(pady=10)

# Create and place the output field for the result
label_result = tk.Label(root, text="New resolution:")
label_result.pack(pady=5)

output_result = tk.Entry(root)
output_result.pack(pady=5)

# Create and place the copy to clipboard button
button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=10)

# Create and place the help button
button_help = tk.Button(root, text="Help", command=open_help)
button_help.pack(pady=10)

# Run the GUI event loop
root.mainloop()
