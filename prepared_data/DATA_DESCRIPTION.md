
## Data Description: White Sox and Cubs (2023 Season)

This project uses real MLB statistics from the 2023 season, specifically for the **Chicago White Sox** and **Chicago Cubs**. All data are dynamically retrieved using the [pybaseball](https://github.com/jldbc/pybaseball) Python package, which provides streamlined access to data from [Baseball Reference](https://www.baseball-reference.com/) and [Baseball Savant](https://baseballsavant.mlb.com/).

No static `.csv` files are stored in this folder. The data used in our simulation and modeling are generated live each time the code is run, ensuring reproducibility and alignment with the most current available records.

---

## Data Types Used

We collected two main types of data for each team:

1. **Game Schedule and Results**
   - Source function: `pybaseball.schedule_and_record()`
   - Description: Includes each game played by the team in the 2023 season, with scores, opponents, dates, and game outcomes.

2. **Player Statistics**
   - Batting data: `pybaseball.batting_stats(2023)`
   - Pitching data: `pybaseball.pitching_stats(2023)`
   - Description: Season-long statistics for all players, including batting averages, home runs, walks, strikeouts, and innings pitched. Data is filtered by team using the `Team` column.

---

## How to Retrieve the Data (Python Code)

To reproduce the exact data used in our project, simply run the following code:

```python
from pybaseball import schedule_and_record, batting_stats, pitching_stats

# 1. Team game-level data
white_sox_schedule = schedule_and_record(2023, "CHW")
cubs_schedule = schedule_and_record(2023, "CHC")

# 2. Player-level statistics
batters_2023 = batting_stats(2023)
pitchers_2023 = pitching_stats(2023)

# 3. Filter by team
white_sox_batters = batters_2023[batters_2023['Team'] == 'CHW']
cubs_batters = batters_2023[batters_2023['Team'] == 'CHC']

white_sox_pitchers = pitchers_2023[pitchers_2023['Team'] == 'CHW']
cubs_pitchers = pitchers_2023[pitchers_2023['Team'] == 'CHC']
````

> You must run `pybaseball` with an active internet connection to access the data.

---

## Column Examples

Here are some key variables used in our analysis:

### Game Schedule (`schedule_and_record`)

| Column      | Description                            |
| ----------- | -------------------------------------- |
| `Date`      | Date of the game                       |
| `Home_Away` | Indicates if the game was home or away |
| `Opp`       | Opponent team                          |
| `R`         | Runs scored by the team                |
| `RA`        | Runs allowed (opponent's score)        |
| `W/L`       | Win or loss result                     |

### Batting Stats (`batting_stats`)

| Column | Description                    |
| ------ | ------------------------------ |
| `Name` | Player name                    |
| `Team` | Team abbreviation (CHW or CHC) |
| `AVG`  | Batting average                |
| `HR`   | Home runs                      |
| `BB`   | Walks                          |
| `SO`   | Strikeouts                     |
| `PA`   | Plate appearances              |

### Pitching Stats (`pitching_stats`)

| Column | Description             |
| ------ | ----------------------- |
| `Name` | Player name             |
| `Team` | Team abbreviation       |
| `IP`   | Innings pitched         |
| `ERA`  | Earned run average      |
| `SO`   | Strikeouts              |
| `BB`   | Walks                   |
| `H`    | Hits allowed            |
| `AVG`  | Batting average against |

---

## Reproducibility

All data are pulled at runtime using the above scripts. This ensures that the simulation remains fully **transparent**, **up-to-date**, and **easy to verify**.

No proprietary or offline data sources are used. All statistics are publicly available through MLB-affiliated databases.

