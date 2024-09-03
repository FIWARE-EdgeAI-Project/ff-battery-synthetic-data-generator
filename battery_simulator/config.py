# Battery simulation scenarios
SCENARIOS = [
    ('low', 'optimal'),
    ('normal', 'optimal'),
    ('normal', 'full'),
    ('normal', 'frequent_top_ups'),
    ('normal', 'deep_discharge'),
    ('high', 'optimal')
]

# Degradation rates of the State of Health(SOH) for each scenario
DEGRADATION_RATES = {
    ('low', 'optimal'): (0.05, 0.10),
    ('normal', 'optimal'): (0.10, 0.15),
    ('normal', 'full'): (0.15, 0.20),
    ('normal', 'frequent_top_ups'): (0.12, 0.18),
    ('normal', 'deep_discharge'): (0.18, 0.25),
    ('high', 'optimal'): (0.18, 0.25)
}

# Battery charging patterns 
CHARGING_BEHAVIORS = {
    'optimal': (20, 80),
    'full': (10, 100),
    'frequent_top_ups': (60, 80),
    'deep_discharge': (5, 95)
}

# SOH configuration parameters
INITIAL_SOH = 100
MINIMUM_SOH = 70

# Folder name in which the synthtic data is saved
OUTPUT_DIR = "synthetic_datasets"