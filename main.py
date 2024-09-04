import os
from datetime import timedelta
import pandas as pd

from battery_simulator.simulator import simulate_battery_data
from battery_simulator.config import SCENARIOS, INITIAL_SOH, OUTPUT_DIR


def main():
    end_date = pd.Timestamp.now().date()
    start_date = end_date - timedelta(days=3*365)

    for usage, charging in SCENARIOS:
        df = simulate_battery_data(start_date, end_date, INITIAL_SOH, usage, charging)
        print(f"\n{usage.capitalize()} Usage, {charging.replace('_', ' ').capitalize()} Charging Scenario:")
        print(df[['Temperature', 'Charge_Start', 'Charge_End', 'Total_Cycles', 'SOH']].describe())
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filename = f'{usage}_usage_{charging}_charging_battery_data.csv'
        filepath = os.path.join(OUTPUT_DIR, filename)
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")

if __name__ == "__main__":
    main()