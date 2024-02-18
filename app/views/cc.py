from tkinter import Tk
import customtkinter as ctk

# Create a Tkinter window
root = Tk()

# Set the window title
root.title("Fullscreen Window")

# Maximize the window size using Tkinter's `state("zoomed")`
root.state("zoomed")

# Create a CTk frame to hold your content
content_frame = ctk.CTkFrame(master=root)
content_frame.pack(fill="both", expand=True)  # Fill the entire window

# Add your customtkinter content to the frame
# ... your CTk widgets and layout here ...

# Start the event loop (using Tkinter's)
root.mainloop()
