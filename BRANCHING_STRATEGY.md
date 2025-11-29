# 🌿 BRANCHING STRATEGY FOR ALTERNATIVE SDG ANALYSIS

## PROBLEM:
Your friend wants to try **SDG 8 + 1 + 10** (Inequality angle) instead of your **SDG 8 + 16 + 9** (Governance angle).

## SOLUTION: Git Branches (Keep Everything in One Repo)

### **Why Branches > Separate Repo:**
1. ✅ Share common infrastructure (data cleaning, notebooks 01-02)
2. ✅ Easy comparison (switch between branches)
3. ✅ Same GitHub repo URL (judges see both if needed)
4. ❌ Separate repo = duplicate 80% of code

---

## BRANCH STRUCTURE:

```
main (your current work)
├── SDG 8 + 16 + 9 (Governance-Growth Gap)
├── notebooks/01-06
└── "Africa needs better builders"

alternative-sdg-inequality (new branch for friend)
├── SDG 8 + 1 + 10 (Growth Without Equity)
├── notebooks/01-02 (same as main)
├── notebooks/03-06 (modified for inequality focus)
└── "Growth ≠ Wealth"
```

---

## SETUP COMMANDS:

### **1. Create Alternative Branch (From Current State)**
```bash
cd /c/Users/USER/Documents/10Alatytics-2025

# Create new branch from main
git checkout -b alternative-sdg-inequality

# Now you're on alternative branch
# Main branch is untouched
```

### **2. Modify for Inequality Analysis**
```bash
# Keep notebooks 01-02 (data cleaning is same)
# Modify 03: Feature engineering for SDG 1 + 10 metrics
# Example changes:
```

**In `03_feature_engineering.ipynb` (alternative branch):**
```python
# ADD new features for inequality:
GDP_per_Capita_Growth = (GDP_per_Capita[t] - GDP_per_Capita[t-1]) / GDP_per_Capita[t-1]
Budget_Deficit_per_Capita = Budget_Deficit / Population
Inequality_Index = (GDP_Growth_Rate / GDP_per_Capita_Growth)  # High = unequal

# REMOVE governance features:
# Tax_to_GDP_Ratio (not needed for inequality story)
# Instead focus on:
Expenditure_Distribution = Education_Exp / (Education_Exp + Defence_Exp)
```

### **3. Update Narrative**
```bash
# Modify 04_eda_story_finding.ipynb
# New finding: "Ethiopia grows 7.7% but GDP per capita is $1,020
# Egypt grows 3.6% but GDP per capita is $3,850
# Conclusion: Fast growth doesn't reduce poverty"

# Modify 05_visualization_dashboard.ipynb
# New chart: GDP Growth vs GDP per Capita (scatter)
# Show: Negative correlation (high growth, low wealth)
```

### **4. Commit Changes to Alternative Branch**
```bash
git add -A
git commit -m "Alternative SDG analysis: Inequality angle (SDG 8+1+10)"
```

### **5. Push Both Branches to GitHub**
```bash
# Push main (your governance analysis)
git checkout main
git push origin main

# Push alternative (friend's inequality analysis)
git checkout alternative-sdg-inequality
git push origin alternative-sdg-inequality
```

---

## ON GITHUB:

Judges will see:
```
Repository: 10alytics-global-hackathon-2025
Branches: 
  - main (default - Governance-Growth Gap) ⭐
  - alternative-sdg-inequality (Inequality angle)
  
README.md on main branch: "For inequality-focused analysis, see branch: alternative-sdg-inequality"
```

---

## SWITCHING BETWEEN BRANCHES (LOCAL):

```bash
# Work on your governance analysis:
git checkout main

# Work on friend's inequality analysis:
git checkout alternative-sdg-inequality

# Compare differences:
git diff main alternative-sdg-inequality
```

---

## SUBMISSION STRATEGY:

### **Option A: Submit Main Only (Your Approach)**
- ZIP from main branch
- Alternative branch = backup/research

### **Option B: Submit Both (Show Breadth)**
- Create 2 ZIPs:
  - `Submission_Governance_Angle.zip` (from main)
  - `Submission_Inequality_Angle.zip` (from alternative)
- Upload note: "Two complementary analyses of same dataset"
- **Advantage:** Shows you explored multiple SDG combinations (judges love thoroughness)

### **Option C: Merge Best Insights**
- Keep main as primary
- Cherry-pick best chart from alternative:
  ```bash
  git checkout main
  git cherry-pick alternative-sdg-inequality~3  # Merge specific commit
  ```
- Add inequality chart as "Bonus Finding" slide

---

## FILE DIFFERENCES BETWEEN BRANCHES:

### **Files That Stay Same:**
- `01_data_exploration.ipynb` (initial audit)
- `02_data_cleaning.ipynb` (cleaning pipeline)
- `data/raw/` (original CSV)
- `data/processed/fiscal_data_clean.csv` (cleaned data)

### **Files That Change:**
- `03_feature_engineering.ipynb` (different features for inequality)
- `04_eda_story_finding.ipynb` (different narrative)
- `05_visualization_dashboard.ipynb` (different charts)
- `06_interactive_visualizations.ipynb` (different dashboard)
- `presentation/*.pptx` (different story)
- `README.md` (different executive summary)

---

## EXAMPLE: Feature Engineering Differences

**Main Branch (Governance):**
```python
# Focus on efficiency ratios
Tax_to_GDP_Ratio = Tax Revenue / GDP
Infrastructure_ROI = GDP_Growth / Capital_Expenditure
```

**Alternative Branch (Inequality):**
```python
# Focus on distribution metrics
GDP_per_Capita_Change = current - previous
Expenditure_Inequality = (Defence_Exp - Social_Exp) / Total_Exp
Poverty_Persistence = 1 / (GDP_per_Capita_Growth + 0.01)
```

---

## TIMELINE FOR FRIEND:

1. **Clone your repo** (30 mins)
   ```bash
   git clone https://github.com/Basit-Balogun10/10alytics-global-hackathon-2025.git
   cd 10alytics-global-hackathon-2025
   git checkout -b alternative-sdg-inequality
   ```

2. **Modify notebooks 03-06** (4-6 hours)
   - Change features in 03
   - Change narrative in 04
   - Change charts in 05-06

3. **Update presentation** (2 hours)
   - New story: "Growth ≠ Wealth"
   - Ethiopia vs Egypt from inequality lens

4. **Push to GitHub** (10 mins)
   ```bash
   git push origin alternative-sdg-inequality
   ```

**Total time: 6-8 hours** (vs 12+ hours starting from scratch)

---

## BEST PRACTICE:

**Before friend starts, create the branch yourself and push skeleton:**

```bash
git checkout -b alternative-sdg-inequality
git push origin alternative-sdg-inequality

# Then friend clones and works on this branch:
git clone -b alternative-sdg-inequality https://github.com/...
```

This way friend doesn't accidentally mess with your main branch!

---

**SUMMARY:**
- ✅ Use branches (not separate repos)
- ✅ Share common code (01-02 notebooks)
- ✅ Diverge at feature engineering (03+)
- ✅ Submit main as primary, alternative as research
- ✅ Friend can work independently on alternative branch without affecting your submission
