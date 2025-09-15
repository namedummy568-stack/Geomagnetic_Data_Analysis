
import numpy as np
import pandas as pd

def load_geomagnetic_data(filepath):
    """Loads geomagnetic data from a CSV file."""
    return pd.read_csv(filepath)

def validate_data(data):
    """Validates the geomagnetic data for missing values."""
    if data.isnull().any().any():
        print("Warning: Missing values detected in data.")
    return data

def apply_calibration(data, calibration_factors, offset_correction=None):
    """Applies calibration factors and optional offset correction to raw geomagnetic data."""
    # Simulate calibration by multiplying with factors
    calibrated_data = data.copy()
    for sensor, factor in calibration_factors.items():
        if sensor in calibrated_data.columns:
            calibrated_data[sensor] = calibrated_data[sensor] * factor
    
    if offset_correction:
        for sensor, offset in offset_correction.items():
            if sensor in calibrated_data.columns:
                calibrated_data[sensor] = calibrated_data[sensor] + offset
                
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
    
    offset_correction_values = {
        'sensor_x': 0.5,
        'sensor_y': -0.2,
        'sensor_z': 0.1
    }

    print(f"Loading raw data from {raw_data_path}")
    raw_data = load_geomagnetic_data(raw_data_path)
    
    print("Validating data...")
    validated_data = validate_data(raw_data)

    print("Applying calibration with offset correction...")
    calibrated_data = apply_calibration(validated_data, calibration_factors, offset_correction_values)
    
    print(f"Saving calibrated data to {output_data_path}")
    save_calibrated_data(calibrated_data, output_data_path)
    print("Calibration complete.")
