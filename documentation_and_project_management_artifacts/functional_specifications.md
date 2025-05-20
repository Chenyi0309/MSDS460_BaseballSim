# Functional Specifications

## User Stories
- As a data analyst, I want to retrieve player statistics for the White Sox and Cubs so I can simulate head-to-head games.
- As a system user, I want to input a season year and automatically fetch batting and pitching data for both teams.
- As a product owner, I want to see the simulation-based win probabilities between two teams to support prediction efforts.

## Requirements
- Use `pybaseball` to acquire 2023 batting and pitching stats.
- Clean the data by removing players with missing values or fewer than 50 plate appearances (PA).
- Calculate matchup probabilities between batters and pitchers using AVG (batting average), HR rate, BB rate, and SO rate.
- Simulate 9-inning games using pitch-by-pitch outcomes.
- Run large-scale simulations (e.g., 10,000 games) to estimate team win probabilities.

## Acceptance Criteria
- Successfully acquire and clean the data for both teams.
- Simulate at-bat outcomes with probabilistic modeling (Hit, HR, BB, SO, Out).
- Generate team-level average scores and win distributions.
- Provide simulation outputs in readable formats (DataFrames and visual plots).
