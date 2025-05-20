# Status Log – Baseball Simulation Project

This is the ongoing status log for our AI-assisted Monte Carlo baseball simulation. Each iteration includes a summary of work performed, notes, and the next plan of action.

---

## Status Format
Each iteration includes:
- Summary of completed work
- AI contributions (if any)
- Issues, insights, or observations
- Plan for the next iteration
- Handoff notes (if applicable)

---

## Iteration 1 – May 18, 2025

**Summary of Work Performed:**
- Reviewed initial GitHub repo structure and created foundational folders (`functional_code/`, `prepared_data/`, `documentation_and_project_management_artifacts/`).
- Drafted and reviewed the initial backlog, added task IDs (e.g., BL-001 to BL-030).
- Prompted AI to generate functional specs and documentation scaffolding (e.g., status log template, activity list design).
- Established versioned checklist format in `activity_list.md`.
- Identified core simulation phases (Poisson-based scoring, extra innings, parameter control).

**AI Collaboration:**
- Used ChatGPT to generate backlog templates, structure activity/task checklists, and functional spec framework.

**Plan for Next Iteration:**
- Start implementing core simulation logic in Python using Poisson distribution for per-inning scoring.
- Test a basic 9-inning match simulation with fixed λ parameters.
- Begin visualization development with matplotlib.

---

## Iteration 2 – May 18, 2025

**Summary of Work Performed:**
- Implemented simulation engine prototype (`simulate_baseball_game`) using NumPy and Poisson distribution.
- Created early test simulations of 10–100 games with λ_A = 0.5, λ_B = 0.4.
- Verified output logic and tested tie game resolution with extra innings.
- Drafted `simulate_inning()` modular structure for expansion.
- Integrated `matplotlib` histograms to visualize scoring outcomes.

**AI Collaboration:**
- Collaborated with ChatGPT to tune simulation logic and handle edge cases (e.g., infinite tie loop, input validation).
- Used prompts to co-generate early visual summary commentary.

**Plan for Next Iteration:**
- Expand game simulation to batch 1000 runs and analyze distribution results.
- Start writing unit tests for edge cases.
- Refactor simulation functions into reusable modules.

---

## Iteration 3 – May 18, 2025

**Summary of Work Performed:**
- Added parameter controls (lambda input) for different team strengths.
- Implemented batch simulation: 1000-game run, aggregated results.
- Verified mean score trends aligned with expected Poisson(λ).
- Refined score histogram bins and added team labels.
- Generated synthetic test CSV files with dummy team names, used for schedule integration planning.

**Plan for Next Iteration:**
- Finalize player schedule CSV pre-processing logic.
- Expand visualization outputs with win probabilities and score distributions.
- Start integrating `pybaseball` functions (schedule_and_record) if API access allows.

---

## Iteration 4 – May 19, 2025

**Summary of Work Performed:**
- Completed simulation results visualization (score histograms for both teams).
- Modularized simulation and plotting functions for reproducibility.
- Began adding CLI input flexibility for λ parameters and game counts.
- Organized results into `results/` folder with labeled plots.
- Cleaned all player/roster/fielding CSVs for Cubs and White Sox.
- Finalized position normalization, handedness, and error-free height parsing.
- Updated `activity_list.md`, `roadmap.md`, and `backlog.md` based on completed features.

**AI Collaboration:**
- Used ChatGPT to generate plotting code with matplotlib and optimize histogram labeling.
- Co-authored status report documentation and WBS alignment.

**Plan for Next Iteration:**
- Clean and normalize the `2025_schedule.csv` for both teams.
- Integrate cleaned schedule data into the simulation pipeline.
- Start scenario-based simulation using real opponent matchups.
- Polish documentation (`README.md`, `Functional_Specs.md`, `Status_Log.md`) for final submission.

---

## Handoff Note for Next Contributor

- Core simulation engine (`simulate_baseball_game`) is working and modular.
- Visual output (histograms of team scores over 1000 games) is complete and saved to `results/`.
- Roster, player stats, and position columns are normalized and output-ready.
- `2025_schedule.csv` files are now included for Cubs and Sox.
- **Next Task**:
  - Normalize schedule CSVs into structured matchlists.
  - Integrate schedule-based simulation logic (e.g., simulate a full season).
  - Validate input/output paths and finalize `data_prepper` if used.

