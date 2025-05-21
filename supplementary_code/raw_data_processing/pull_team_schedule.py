from pybaseball import schedule_and_record
import pandas as pd

# Fetch 2023 season schedule and game results
white_sox_schedule = schedule_and_record(2023, "CHW")
cubs_schedule = schedule_and_record(2023, "CHC")

# Save to CSV
white_sox_schedule.to_csv('../prepared_data/white_sox_schedule_2023.csv', index=False)
cubs_schedule.to_csv('../prepared_data/cubs_schedule_2023.csv', index=False)

print("Team schedules saved successfully.")
