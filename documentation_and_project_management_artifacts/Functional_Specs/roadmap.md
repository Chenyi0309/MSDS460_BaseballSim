# Roadmap – Baseball Simulation Project

This roadmap outlines the planned phases of our AI-assisted Monte Carlo baseball simulator. Each phase builds toward greater realism, flexibility, and analytical depth.

---

## 4-Day High-Level Plan

- **Day 1**: Complete core simulation logic with scoring rules  
- **Day 2**: Finalize visualizations and parameter tuning  
- **Day 3**: Incorporate AI-generated documentation and model explanations  
- **Day 4**: Final testing, packaging, and GitHub submission

---

# Product Roadmap & Iteration Plan

## MVP 1 – Core Simulation Engine (Complete)
**Goal**: Build a working engine that simulates realistic full-length baseball games using probabilistic scoring.

- [x] Initialize game state and team info
- [x] Simulate innings using Poisson-distributed scores (`simulate_baseball_game`)
- [x] Handle tie games and simulate extra innings
- [x] Run multi-game simulations and aggregate results
- [x] Unit tests for score integrity and edge cases
- [x] AI-assisted: modular code generation + testing scenarios (ChatGPT)

---

## MVP 2 – Visualization & Reporting (In Progress)
**Goal**: Create insightful visualizations and summaries from simulation output.

- [x] Generate score distribution histograms (matplotlib)
- [ ] Compute and display win probabilities, average scores
- [ ] Visualize result sensitivity under varying parameters (λ)
- [ ] Build minimal dashboard or notebook output
- [ ] Export CSV/JSON summary files for further use

---

## MVP 3 – Documentation & Collaboration Tools (In Progress)
**Goal**: Enable reproducibility and transparency with clear, AI-assisted project documentation.

- [x] Functional specs, status log, activity list
- [x] Work breakdown structure and roadmap files
- [x] Record AI prompt usage and explain AI teammate role
- [ ] Set up developer onboarding and usage guide
- [ ] Finalize GitHub structure with clear folder separation

---

## MVP 4 – Advanced Modeling (Optional for Final Deliverable)
**Goal**: Improve simulation realism with deeper modeling.

- [ ] Batter vs. pitcher matchup statistics
- [ ] Pitch velocity and selection behavior
- [ ] Pitcher fatigue, bullpen substitution logic
- [ ] Salary, contracts, and injuries as lineup constraints
- [ ] Base running and defensive event modeling

---

## MVP 5 – Data Integration & Automation
**Goal**: Incorporate real-world data and improve pipeline automation.

- [ ] Use `pybaseball` or MLB API to load team schedules and rosters
- [ ] Clean and format real player stat CSVs
- [ ] Automate score simulation with scheduled matchups
- [ ] Support saving and loading scenario presets

---

## MVP 6 – Analysis & Extensions
**Goal**: Support game analysis, "what-if" exploration, and broader accessibility.

- [ ] Compare hypothetical team performance across seasons
- [ ] Add dashboard-style report interface (Streamlit / HTML)
- [ ] Performance profiling and simulation speed improvements
- [ ] Optional: multi-language support (English + Chinese)

---
