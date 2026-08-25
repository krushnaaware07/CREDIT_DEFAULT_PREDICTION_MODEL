# Credit Default Prediction Prototype

**Training source:** Synthetic prototype data (Kaggle unavailable in execution environment)

This prototype contains:
- trained classification model
- model evaluation
- borrower input form
- Streamlit browser interface

## Run locally
1. Install Python 3.10+
2. `pip install streamlit pandas scikit-learn joblib`
3. Put `credit_default_model.pkl` and `app.py` in the same folder.
4. Run: `streamlit run app.py`

## Important
This is a prototype. It must be retrained and validated on Nashik Urban Cooperative Credit Society's historical data before any real lending use. Risk thresholds are illustrative and must be approved/validated by the Society.
