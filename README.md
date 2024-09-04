# ff-battery-synthetic-data-generator
This project generates synthetic data simulating the State of Health (SOH) degradation of electric vehicle batteries over time. The data is created to mimic real-world scenarios with various usage patterns and charging behaviors. 

## Synthetic Datasets Description

The generated datasets simulate battery performance over a three-year period, with daily entries. Each dataset represents a different combination of usage frequency and charging behavior varying temperature conditions.

### File Naming Convention

Files are named according to the pattern: `{usage}_usage_{charging}_charging_battery_data.csv`

Where:
- `{usage}` can be: low, normal, or high
- `{charging}` can be: optimal, full, frequent_top_ups, or deep_discharge

### Data Fields

Each CSV file contains the following columns:

1. **Date**: The date of the entry (daily frequency)
2. **Temperature**: Simulated ambient temperature in Celsius
3. **Charge_Start**: Starting charge level for the day (%)
4. **Charge_End**: Ending charge level for the day (%)
6. **Daily_Cycles**: Number of charge cycles completed in the day
7. **Total_Cycles**: Cumulative number of charge cycles
8. **SOH**: State of Health of the battery (%)

### Scenarios

The data is generated for six different scenarios:

1. Normal usage, optimal charging
2. Normal usage, full charging
3. Normal usage, frequent top-ups
4. Normal usage, deep discharge
5. High usage, optimal charging
6. Low usage, optimal charging

### Data Generation Parameters

- **Initial SOH**: 100%
- **Minimum SOH**: 70%
- **Temperature Ranges**:
  - Winter: -10°C to 10°C
  - Spring: 5°C to 25°C
  - Summer: 15°C to 35°C
  - Autumn: 0°C to 20°C
  - Extreme events (10% chance): -20°C to -10°C or 40°C to 50°C
- **Usage Factors**:
  - Low: 0.2 to 0.5
  - Normal: 0.5 to 1.0
  - High: 1.0 to 2.0
- **Charging Behaviors**:
  - Optimal: 20% to 80%
  - Full: 10% to 100%
  - Frequent top-ups: 60% to 80%
  - Deep discharge: 5% to 95%

### SOH Degradation Factors

The SOH degradation is calculated based on:
- Base degradation rate (daily degradation)
- Temperature effects
- Cycling effects
- Charging behavior

## Usage

This synthetic data can be used for:
- Training machine learning models for SOH prediction
- Analyzing the impact of different usage patterns on battery life

## Running the Battery Simulator

To run the battery simulation, follow these steps:

1. **Clone the repository:**

    ```shell
    git clone https://github.com/FIWARE-EdgeAI-Project/ff-battery-synthetic-data-generator.git
    ```

2. **Install the required dependencies:**
    ```shell
    pip install -r requirements.txt
    ```
3. **Customizing the Simulation**

    To modify the simulation parameters:

    1. Open `battery_simulator/config.py` module
    2. Adjust the values in `DEGRADATION_RATES`, `CHARGING_BEHAVIORS`, or `SCENARIOS` as needed
    3. Save the file and run the simulation again

4. **Run the simulation:**
    ```shell
    python main.py
    ```

    The simulation results will be saved in the `synthetic_datasets` directory.


## Limitations

- This is synthetic data and may not perfectly represent real-world battery behavior
- The degradation model is simplified and does not account for all factors affecting battery life
- Extreme scenarios or edge cases may not be fully represented

