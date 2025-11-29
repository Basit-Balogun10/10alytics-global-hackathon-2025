# 🗺️ 10Alytics Hackathon 2025: From Zero to Hero Roadmap

**Goal:** Transform fragmented fiscal data into actionable intelligence for SDGs.
**Theme:** "From Data to Decision" - Evidence-based policy making.
**Deadline:** [Insert Date/Time]

---

## 🏁 Phase 1: Setup & Ingestion (0% - 10%)
*Objective: Get the data ready for analysis.*

- ✅ **Verify Environment:** Ensure `pandas`, `matplotlib`, `seaborn` are working.
- [ ] **Load Data:**
    - Load `data/raw/10Alytics Hackathon- Fiscal Data.csv` into `notebooks/01_data_exploration.ipynb`.
    - Check dimensions (`df.shape`), columns (`df.columns`), and data types (`df.info()`).
    - **Note:** CSV is in "Long" format (23,784 rows × 9 columns, 14 countries, 27 indicators).
- [ ] **Initial Audit:**
    - Identify missing values (`df.isnull().sum()`). **Expected:** ~10,503 missing in `Currency`, ~59 in `Amount`.
    - Check for **duplicate indicators** (e.g., `"GDP per Capita"` vs `"GDP per Capita "`—trailing spaces).
    - Verify `Amount` column is **text** (due to commas like `1,000`). Convert to numeric.
    - Identify outliers (e.g., negative GDP, impossible percentages).
    - Check for consistency (e.g., Country names spelling, Year formats).
- [ ] **🎯 SDG Scoping (Data-Driven Approach):**
    - **Strategy:** Start broad → narrow based on data completeness.
    - Map each indicator to its relevant SDG(s).
    - Calculate **data completeness score** per SDG (% of non-missing values).
    - Identify which SDGs have the **strongest data coverage** (Target: 3-5 SDGs).
    - Document findings to inform narrative selection in Phase 3.

## 🧹 Phase 2: Cleaning & Enrichment (10% - 30%)
*Objective: Create a "Master Dataset" that tells a story.*

- [ ] **Data Cleaning:**
    - **Fix Indicator Names:** Consolidate duplicates (e.g., `"GDP per Capita"` → standardize).
    - **Fix Amount Column:** Convert from text to numeric (remove commas, handle NaNs).
    - **Standardize Frequency:** Dataset has Mixed frequency (Monthly inflation, Yearly GDP).
        - *Strategy:* Aggregate to **Yearly** for SDG analysis (use yearly average for monthly metrics).
    - **Missing Data Strategy:** Do NOT just drop rows.
        - *Time Series:* Use interpolation (e.g., `df.interpolate()`) if data is missing in a sequence of years.
        - *Cross-Sectional:* Use Median imputation for skewed economic data.
        - *Document it:* Note exactly *why* you chose a method (Judges love this transparency).
- ✅ **Data Transformation (Critical):**
    - **Pivot from Long to Wide:** Transform data so each row = Country-Year, columns = indicators.
        - *Target:* Rows: `2010-Nigeria`, `2011-Nigeria`... Columns: `Health Expenditure`, `GDP Growth`, etc.
- ✅ **Feature Engineering:**
    - Create "Per Capita" metrics (e.g., `Health Expenditure / Population`).
    - Create "Growth Rates" (Year-over-Year change in GDP/Inflation).
    - Create "Ratios" (e.g., `Debt-to-GDP`, `Tax-to-GDP`, `Tax-to-Revenue`).
- [ ] **🚀 The "Winning" Move: External Data Enrichment:**
    - **The Key Insight:** Your CSV has *INPUTS* (spending, GDP) but no *OUTCOMES* (lives saved, literacy).
    - **Action:** Download and merge external "Outcome" data by `Country` and `Year`:
        - **SDG 3 (Health):** Under-5 Mortality Rate, Life Expectancy (World Bank / WHO).
        - **SDG 4 (Education):** Literacy Rate, Primary School Enrollment (World Bank).
        - **SDG 1 (Poverty):** Poverty Headcount Ratio at $2.15/day (World Bank).
        - **SDG 16 (Governance):** Corruption Perception Index (Transparency International).

## 🔍 Phase 3: Exploratory Data Analysis (EDA) & Story Finding (30% - 50%)
*Objective: Find the "Big Domino" (The Root Cause).*

- [ ] **Correlation Analysis (INPUTS vs OUTCOMES):**
    - Run a correlation matrix. Does `Health Expenditure` actually correlate with `Under-5 Mortality`?
    - **The "Efficiency Gap" Test:** Compare countries with similar spending but different outcomes.
    - *If Correlation is Weak:* This is your **winning insight**! "More spending ≠ Better outcomes" (governance issue).
    - *Trap:* If correlation is low, admit it! "We found no link between X and Y, suggesting inefficiency."
- [ ] **Country Segmentation:**
    - Don't treat all 14 countries the same. Cluster them:
        - "High Debt / Low Growth" vs "Low Debt / High Growth"
        - "High Spend / Poor Outcomes" vs "Low Spend / Good Outcomes"
- [ ] **Trend Analysis:**
    - Visualize key metrics over time (Line charts).
    - Identify "Shocks" (e.g., COVID-19 impact on Debt/GDP in 2020).
- [ ] **Select Your Narrative:**
    - Don't try to solve all SDGs. Pick **ONE** strong narrative arc.
    - *Suggested Arc:* **"The Efficiency Gap: Why More Spending Isn't Saving Lives"** (Governance + Health).
    - *Alternative:* "Inefficient Tax Collection (SDG 8) → Low Revenue → Underfunded Health (SDG 3)."
    - *Focus:* Identify the "Lowest Hanging Fruit" (Low Effort, High Impact).

## 🧠 Phase 4: Modeling & AI (50% - 70%)
*Objective: Move from "What happened?" to "Why?" and "What will happen?".*

- [ ] **Explainable AI:**
    - Use **Clustering (K-Means):** Group countries into "High Risk," "Emerging," "Stable."
        - *Defense:* Be ready to explain Silhouette Score or why you chose K=3 clusters.
    - Use **Regression/Random Forest:** To find *Feature Importance*.
        - *Question:* What is the #1 predictor of Mortality? (Is it Spending? Or Governance?)
- [ ] **Validation:**
    - If using ML, calculate RMSE or R-Squared.
    - *Crucial:* Be able to explain the model in plain English. "The model shows that for every 1% increase in Tax Revenue, we see a X% drop in Debt."
- [ ] **The "Black Box" Defense:**
    - If you can't explain the math behind your model in 30 seconds, stick to simpler methods (Scatter Plot + Regression).

## 📊 Phase 5: Visualization & Dashboarding (70% - 90%)
*Objective: The "5-Second Rule".*

- [ ] **Tool Selection:** Power BI / Tableau (Recommended for final presentation) or polished Python charts (Seaborn/Plotly).
- [ ] **Dashboard Design:**
    - **Executive View:** High-level KPIs (GDP Growth, Debt Ratio).
    - **Drill Down:** Allow filtering by Region/Country.
    - **The "So What?":** Every chart must have a title that states the insight (e.g., "Debt Spiked in 2020 due to Pandemic").
- [ ] **Avoid Clutter:** No 3D charts. No walls of text.

## 🎤 Phase 6: The Pitch & Submission (90% - 100%)
*Objective: Sell the Solution.*

- [ ] **The Presentation Deck (PDF/PPT):**
    - **Slide 1: The Hook (Executive Summary)**
        - *Example:* "The Efficiency Gap: Why $X Billion in Health Spending Isn't Saving Lives."
        - *Visual:* Chart showing Health Spending ↑ but Mortality staying flat.
    - **Slide 2: The Diagnosis (Visual Proof)**
        - *Visual:* Correlation heatmap or scatter plot (Inputs vs Outcomes).
        - *Insight:* "Country A spends less than Country B but has better outcomes."
    - **Slide 3: The Root Cause (Data-backed)**
        - *Focus:* Governance (SDG 16) or Tax Inefficiency (SDG 8).
    - **Slide 4: The Solution (Actionable Recommendation)**
        - *Example:* "Fiscal Transparency Framework" to ensure allocations reach clinics.
    - **Slide 5: The Impact (Projected ROI)**
        - *Prediction:* "10% efficiency gain = X lives saved, no new taxes needed."
- [ ] **The "Limitations" Defense:**
    - Prepare answer: "We used median imputation for 2023 gaps because mean would be skewed by outliers."
- [ ] **The "One-Pager":** A concise summary for judges.
- [ ] **Final Code Cleanup:** Ensure notebooks are readable and commented.
- [ ] **Submission:** Zip the Code, Dashboard Link, and Presentation PDF.

---

---

## 🛠️ Immediate Next Steps
1. ✅ ~~Set up environment~~
2. ✅ ~~Load CSV and run Initial Audit~~ 
3. ✅ ~~Clean and Pivot data to Wide format~~
4. **NOW: Feature Engineering** - Create ratios, per capita metrics, growth rates
5. **Next: Download and merge external data** (World Bank: Corruption, Poverty, Literacy)
6. **Then: EDA & Correlation Analysis** - Find the story in the data
