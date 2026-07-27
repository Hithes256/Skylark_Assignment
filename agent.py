from utils import find_column, convert_to_number


# -------------------------------------------------
# Revenue Report
# -------------------------------------------------

def get_revenue(work_df):

    col = find_column(work_df, "Amount in Rupees (Incl of GST) (Masked)")

    if col is None:
        return "Revenue data not available."

    revenue = convert_to_number(work_df[col]).sum()

    report = f"""
💰 Revenue Summary

Total Revenue : ₹{revenue:,.2f}

Insight:
• Revenue has been calculated from all available work orders.
"""

    return report


# -------------------------------------------------
# Pipeline Report
# -------------------------------------------------

def get_pipeline(deals_df):

    col = find_column(deals_df, "Deal Stage")

    if col is None:
        return "Pipeline data not available."

    pipeline = deals_df[col].value_counts()

    report = "📊 Pipeline Health\n\n"

    for stage, count in pipeline.items():
        report += f"• {stage} : {count}\n"

    report += "\nInsight:\n"
    report += "• This shows how deals are distributed across different stages."

    return report


# -------------------------------------------------
# Sector Report
# -------------------------------------------------

def get_sector(deals_df):

    col = find_column(deals_df, "Sector/service")

    if col is None:
        return "Sector information not available."

    sector = deals_df[col].value_counts()

    report = "🏭 Sector Performance\n\n"

    for name, count in sector.items():
        report += f"• {name} : {count}\n"

    top = sector.idxmax()

    report += f"\nTop Performing Sector : {top}"

    return report


# -------------------------------------------------
# Execution Report
# -------------------------------------------------

def get_execution(work_df):

    col = find_column(work_df, "Execution Status")

    if col is None:
        return "Execution information not available."

    execution = work_df[col].value_counts()

    report = "🚧 Execution Status\n\n"

    for status, count in execution.items():
        report += f"• {status} : {count}\n"

    report += "\nInsight:\n"
    report += "• Higher completed projects indicate healthy operations."

    return report


# -------------------------------------------------
# Billing Report
# -------------------------------------------------

def get_billing(work_df):

    col = find_column(work_df, "Billing Status")

    if col is None:
        return "Billing information not available."

    billing = work_df[col].value_counts()

    report = "🧾 Billing Status\n\n"

    for status, count in billing.items():
        report += f"• {status} : {count}\n"

    report += "\nRecommendation:\n"
    report += "• Review work orders marked 'Update Required'."

    return report


# -------------------------------------------------
# Collection Report
# -------------------------------------------------

def get_collection(work_df):

    col = find_column(work_df, "Collection status")

    if col is None:
        return "Collection information not available."

    collection = work_df[col].value_counts()

    report = "💵 Collection Status\n\n"

    for status, count in collection.items():
        report += f"• {status} : {count}\n"

    report += "\nInsight:\n"
    report += "• Collection records help track payment recovery."

    return report


# -------------------------------------------------
# Cross Board Analysis
# -------------------------------------------------

def get_cross_board(deals_df, work_df):

    deal_col = find_column(deals_df, "Deal Name")
    work_col = find_column(work_df, "Deal name masked")

    if deal_col is None or work_col is None:
        return "Cross-board analysis not available."

    deals = set(deals_df[deal_col].dropna().astype(str))
    work = set(work_df[work_col].dropna().astype(str))

    missing = list(deals - work)

    if len(missing) == 0:
        return """🔗 Cross Board Analysis

✅ Every deal has a matching work order.
"""

    report = "🔗 Deals Without Work Orders\n\n"

    for deal in missing:
        report += f"• {deal}\n"

    return report


# -------------------------------------------------
# Leadership Update
# -------------------------------------------------

def get_leadership(deals_df, work_df):

    revenue = get_revenue(work_df)
    pipeline = get_pipeline(deals_df)
    sector = get_sector(deals_df)
    execution = get_execution(work_df)

    report = f"""
====================================

LEADERSHIP UPDATE

====================================

{revenue}

------------------------------------

{pipeline}

------------------------------------

{sector}

------------------------------------

{execution}

====================================

Recommendations

• Follow up on proposal-stage deals.

• Improve billing updates.

• Monitor pending execution work.

====================================
"""

    return report