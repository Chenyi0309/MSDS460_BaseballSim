# Product Backlog

## Features
- ✅ Simulate baseball games between any two MLB teams
- ✅ Pull real player stats by year
- ✅ Estimate win probabilities and scores via simulation
- ⏳ Add ballpark/environmental effects (Future)
- ⏳ Model baserunning and scoring from BB/walks (Future)

## Known Bugs
- ❌ Potential divide-by-zero in BF (batters faced) estimation if IP is malformed
- ❌ Some players may have zero PA/AB, causing missing values in rate calculations

## Technical Tasks
- [ ] Add baserunning simulation logic for more realistic scoring
- [ ] Allow year selection from user input
- [ ] Enhance output with visualizations (e.g., seaborn heatmaps, win curves)
