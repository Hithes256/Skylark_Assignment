import streamlit as st

from monday_api import get_deals, get_workorders
from utils import clean_dataframe

from agent import (
    get_revenue,
    get_pipeline,
    get_sector,
    get_execution,
    get_billing,
    get_collection,
    get_cross_board,
    get_leadership
)

# ---------------------------------------
# Page
# ---------------------------------------

st.set_page_config(
    page_title="Monday.com BI Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Monday.com Business Intelligence Agent")

st.write(
    "Ask business questions about your Monday.com Deals and Work Orders."
)

st.divider()

# ---------------------------------------
# Load Data
# ---------------------------------------

try:

    deals = clean_dataframe(get_deals())
    work = clean_dataframe(get_workorders())

except Exception as e:

    st.error(f"Unable to load Monday.com data.\n\n{e}")

    st.stop()

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.header("Example Questions")

st.sidebar.write("""
• Revenue

• Pipeline

• Sector Performance

• Execution Status

• Billing Status

• Collection Status

• Leadership Update

• Cross Board
""")

# ---------------------------------------
# User Question
# ---------------------------------------

question = st.text_input(
    "Ask a Question"
)

if st.button("Get Answer"):

    if question.strip() == "":

        st.warning("Please enter a question.")

        st.stop()

    q = question.lower()

    # ---------------- Revenue ----------------

    if "revenue" in q or "amount" in q:

        st.success("Answer")

        st.markdown(get_revenue(work))

    # ---------------- Pipeline ----------------

    elif "pipeline" in q:

        st.success("Answer")

        st.markdown(get_pipeline(deals))

    # ---------------- Sector ----------------

    elif "sector" in q:

        st.success("Answer")

        st.markdown(get_sector(deals))

    # ---------------- Execution ----------------

    elif "execution" in q or "operation" in q:

        st.success("Answer")

        st.markdown(get_execution(work))

    # ---------------- Billing ----------------

    elif "billing" in q:

        st.success("Answer")

        st.markdown(get_billing(work))

    # ---------------- Collection ----------------

    elif "collection" in q:

        st.success("Answer")

        st.markdown(get_collection(work))

    # ---------------- Cross Board ----------------

    elif "cross" in q or "work order" in q:

        st.success("Answer")

        st.markdown(get_cross_board(deals, work))

    # ---------------- Leadership ----------------

    elif "leader" in q or "summary" in q or "report" in q:

        st.success("Answer")

        st.markdown(get_leadership(deals, work))

    # ---------------- Help ----------------

    else:

        st.warning("I couldn't understand your question.")

        st.write("Try one of these:")

        st.info("""
Revenue

Pipeline

Sector Performance

Execution Status

Billing Status

Collection Status

Cross Board

Leadership Update
""")

# ---------------------------------------
# Footer
# ---------------------------------------

st.divider()

st.caption("Built using Streamlit + Monday.com API")