# Raw Data Processing

This folder contains the scripts used to download and prepare the 2023 MLB season data from the [pybaseball](https://github.com/jldbc/pybaseball) library.

## Contents

- `pull_mlb_data.ipynb`: Jupyter notebook used to retrieve and save batting/pitching data for White Sox and Cubs
- `schedule_data.ipynb`: Pulls full 2023 schedule with results using `schedule_and_record()`
- Output CSVs saved in `prepared_data/` folder for reuse

## Notes

- All player stats are pulled using official MLB abbreviations (`CHW`, `CHC`)
- Scripts are reproducible and only require `pybaseball` and `pandas`
