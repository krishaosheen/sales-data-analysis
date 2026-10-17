# Sales Performance Analysis — Beginner Data Science Portfolio

**Project status:** Self-directed learning project  
**Data:** Synthetic / invented sample data; not real company data  
**Tools:** Python, pandas, Matplotlib, SQL, Streamlit (optional dashboard)

## Business question
How do sales, estimated profit, products, and regions compare across January–September 2026 in this practice dataset?

## Objectives
- Validate the dataset and check for missing values and duplicate rows.
- Calculate revenue, estimated cost, profit, and profit margin.
- Compare monthly performance, products, and regions.
- Communicate findings and limitations clearly.

## Key findings (for this synthetic dataset only)
- Number of transaction rows: **42**
- Total units sold: **1,336**
- Total revenue: **$37,003.50**
- Estimated total profit: **$17,931.70**
- Overall estimated profit margin: **48.5%**
- Highest-revenue product: **Monitor** ($15,660.00)
- Highest-revenue region: **South** ($11,292.00)

These results only describe the invented data included here. They do not establish real-world market trends or company performance.

## Files
- `sales_data.csv` — synthetic data with date, region, product, units, unit price, and unit cost
- `sales_analysis.py` — data checks, calculations, summaries, and chart generation
- `practice_queries.sql` — example SQL questions
- `explanation_and_interview_guide.md` — plain-English walkthrough and sample interview answers
- `app.py` — optional interactive Streamlit dashboard
- `requirements.txt` — Python packages needed
- PNG files — exported charts

## Run the analysis
Install Python 3.10+ and dependencies:
```bash
pip install -r requirements.txt
```
Run:
```bash
python sales_analysis.py
```

## Optional interactive dashboard
```bash
streamlit run app.py
```

## Limitations and next steps
This small dataset is synthetic, has a limited number of products and regions, and uses fixed sample unit costs. Profit is an estimate based on those invented costs; it excludes shipping, overhead, taxes, returns, and discounts. Future work could use a larger dataset, add validation tests, model seasonality, and compare profit after all operating costs.
