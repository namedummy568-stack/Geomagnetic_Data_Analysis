
import numpy as np
import pandas as pd

def load_geomagnetic_data(filepath):
    """Loads geomagnetic data from a CSV file."""
    return pd.read_csv(filepath)

def apply_calibration(data, calibration_factors):
    """Applies calibration factors to raw geomagnetic data."""
    # Simulate calibration by multiplying with factors
    calibrated_data = data.copy()
    for sensor, factor in calibration_factors.items():
        if sensor in calibrated_data.columns:
            calibrated_data[sensor] = calibrated_data[sensor] * factor
    return calibrated_data

def save_calibrated_data(data, filepath):
    """Saves calibrated data to a new CSV file."""
    data.to_csv(filepath, index=False)

if __name__ == "__main__":
    # Example usage
    raw_data_path = "raw_geomagnetic_data.csv"
    output_data_path = "calibrated_geomagnetic_data.csv"
    
    # Create dummy raw data for demonstration
    dummy_data = pd.DataFrame({
        'timestamp': pd.to_datetime(np.arange(10), unit='s'),
        'sensor_x': np.random.rand(10) * 100,
        'sensor_y': np.random.rand(10) * 100,
        'sensor_z': np.random.rand(10) * 100
    })
    dummy_data.to_csv(raw_data_path, index=False)

    calibration_factors = {
        'sensor_x': 1.01,
        'sensor_y': 0.99,
        'sensor_z': 1.02
    }

    print(f"Loading raw data from {raw_data_path}")
    raw_data = load_geomagnetic_data(raw_data_path)
    
    print("Applying calibration...")
    calibrated_data = apply_calibration(raw_data, calibration_factors)
    
    print(f"Saving calibrated data to {output_data_path}")
    save_calibrated_data(calibrated_data, output_data_path)
    print("Calibration complete.")
