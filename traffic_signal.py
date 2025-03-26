def control_traffic_signal(car_count_lane1, car_count_lane2):
    """
    Adjusts traffic signal timing based on the number of cars in each lane.
    """
    if car_count_lane1 > car_count_lane2:
        return "Lane 1 is congested. Redirecting cars to Lane 2. (Lane 2: Green, Lane 1: Red)"
    else:
        return "Lane 2 is congested. Redirecting cars to Lane 1. (Lane 1: Green, Lane 2: Red)"

# Example usage
if __name__ == "__main__":
    car_count_lane1 = 10  # Number of cars detected in Lane 1
    car_count_lane2 = 5   # Number of cars detected in Lane 2
    signal_status = control_traffic_signal(car_count_lane1, car_count_lane2)
    print(signal_status)