# Activity List – Baseball Simulation Project

This activity log documents major development activities for our baseball simulation project using Monte Carlo methods and probabilistic modeling. The project includes AI-assisted development, simulation code, and documentation for reproducibility and collaboration.

---

## 🗓️ Development Activities (Chronological Log)

- **May 17 18:00–20:00**: Designed simulation framework with innings, scoring rules, and Poisson-based assumptions (Lead: Andrew, AI-assisted).
- **May 18 09:00–10:30**: Implemented base game simulation loop in Python; simulated 10 games with static lambda parameters (Andrew).
- **May 18 14:00–15:00**: Developed histogram visualization for score distributions and tested 1000-game output (Sam).
- **May 18 15:30–17:00**: Drafted simulation model explanation (EDA rationale, statistical logic) using AI-assisted prompts (Andrew + ChatGPT).
- **May 19 09:00–10:00**: Reviewed and refactored AI-generated EDA code for readability and modularity (Andrew).
- **May 19 10:00–11:00**: Wrote unit test cases for simulation edge cases: tie games, negative λ input handling (Sam).
- **May 20 13:00–14:00**: Updated README and wrote draft for `Functional_Specs.md` (Priya).
- **May 20 15:00–16:00**: Added Poisson-based score comparison visualization and summary stats (Sam).
- **May 21 10:00–11:00**: Created roadmap and WBS breakdown for advanced modeling features (AI-assisted draft + team edits).

---

## 📌 Backlog Checklist

### 🟢 Open Items

#### Simulation Engine
- [ ] **BL-004**: Simulate pitch-by-pitch logic (expand beyond inning-level)
- [ ] **BL-006**: Update game state per batter/pitch
- [ ] **BL-007**: Handle extra innings in tie scenarios
- [ ] **BL-009**: Add simulation parameter CLI flags

#### Advanced Features
- [ ] **BL-021**: Use real batter/pitcher splits
- [ ] **BL-023**: Integrate salary + contract constraints
- [ ] **BL-024**: Account for player injuries or availability
- [ ] **BL-025**: Include pitch type/velocity effects

#### Visualization & Reporting
- [ ] **BL-014**: Add scoreboard-style live game output
- [ ] **BL-016**: Dynamic win probability graph during simulation

#### Documentation
- [ ] **BL-028**: Host Hugo-based docs site
- [ ] **BL-030**: Contributor onboarding guide
- [ ] **BL-031**: Issue tracker + PR workflow setup

---

### ✅ Completed Items

#### Core Simulation
- [x] **BL-032**: Simulate games using Poisson-distributed runs per inning
- [x] **BL-033**: Handle tie scenarios and simulate extra innings
- [x] **BL-034**: Generate and visualize score histograms (matplotlib)

#### Data & Parameters
- [x] **BL-035**: Define base scoring parameters (λ_A, λ_B) and conduct what-if analysis
- [x] **BL-036**: Test model behavior under different λ ranges (0.3 to 0.8)

#### Collaboration & AI Usage
- [x] **BL-037**: AI-assisted design of simulation components and user stories
- [x] **BL-038**: Integrated AI-generated starter code and customized logic

---

