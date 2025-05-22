"""
Basic example of using SMPL-Anthropometry to measure a SMPL model.
"""

import torch
from measure import MeasureBody
from measurement_definitions import STANDARD_LABELS

def main():
    # Create a measurer instance for SMPL model
    measurer = MeasureBody("smpl")

    # Create a zero-shaped T-posed female model
    betas = torch.zeros((1, 10), dtype=torch.float32)
    measurer.from_body_model(gender="FEMALE", shape=betas)

    # Get all possible measurements
    measurement_names = measurer.all_possible_measurements

    # Take measurements
    measurer.measure(measurement_names)

    # Print measurements
    print("\nMeasurements (in cm):")
    for name, value in measurer.measurements.items():
        print(f"{name}: {value:.2f}")

    # Label measurements with standard labels
    measurer.label_measurements(STANDARD_LABELS)
    print("\nLabeled measurements (in cm):")
    for label, value in measurer.labeled_measurements.items():
        print(f"{label}: {value:.2f}")

    # Visualize the measurements
    measurer.visualize(
        measurement_names=measurement_names,
        title="SMPL Female Model Measurements"
    )

if __name__ == "__main__":
    main() 