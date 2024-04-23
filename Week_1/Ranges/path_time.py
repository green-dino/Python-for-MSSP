def calculate_position(time):
    """
    Calculate the position of a vehicle along a path at a given time.

    Args:
        time (int): Time in seconds.

    Returns:
        int: Position of the vehicle at the given time.
    """
    # Example calculation logic
    speed = 2  # Constant speed of the vehicle in meters per second
    position = speed * time
    return position

# Example usage:
path_length = 100  # Length of the path in meters
time_intervals = range(0, 60, 5)  # Time intervals in seconds
for t in time_intervals:
    position = calculate_position(t)  # Calculate position of the vehicle at each interval
    print(f"At time {t} seconds, the vehicle is at position {position} meters.")
