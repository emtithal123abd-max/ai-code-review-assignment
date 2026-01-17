# corrected implementation for Task 3.

def average_valid_measurements(values):
    if not values:
        return 0.0
    
    total = 0.0
    valid_measurements_count = 0

    for v in values:
        if v is None:
            continue
        try: 
            total += float(v)
        except (TypeError, ValueError):
            continue
        
        valid_measurements_count += 1

    return total / valid_measurements_count if valid_measurements_count else 0.0
