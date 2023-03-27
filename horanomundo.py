from datetime import datetime
import pytz
import tkinter as tk

# Define the list of capitals and their time zones and CEPs
capitals = {"UTC": {"name": "UTC", "cep": ""}}
for tz_name in pytz.all_timezones:
    # Get the timezone object
    tz = pytz.timezone(tz_name)
    # Check if the timezone is a capital city (name ends in '/capital')
    if tz_name.split('/')[-1].isupper():
        # Add the capital to the list with its corresponding CEP
        capitals[tz_name.split('/')[-1]] = {"name": tz_name.split('/')[-1], "tz_name": tz_name, "cep": "00000-000"}

# Define the format for the time display
formato = "%Y-%m-%d %H:%M:%S %Z%z"

# Define a function to update the time display
def update_time():
    # Get the current UTC time
    hora_utc = datetime.now(pytz.utc)
    
    # Iterate over the list of capitals and update their time labels
    for capital, data in capitals.items():
        # Set the timezone for the capital
        tz = pytz.timezone(data["tz_name"])
        # Convert the UTC time to the local time in the capital
        hora_local = hora_utc.astimezone(tz)
        # Update the time label for the capital with the CEP information
        time_labels[capital].config(text="%s: %s - CEP: %s" % (data["name"], hora_local.strftime(formato), data["cep"]))

    # Schedule the next time update in 1 second
    window.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Time in Capitals")
window.geometry("600x400")

# Create a label for each capital's time
time_labels = {}
for capital in capitals:
    time_labels[capital] = tk.Label(window, font=("Arial", 16), text="%s: calculating..." % capital)
    time_labels[capital].pack(side=tk.TOP, padx=10, pady=10)

# Start the time update function
update_time()

# Start the main event loop
window.mainloop()
