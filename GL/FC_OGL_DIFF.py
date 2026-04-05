import pandas as pd

# ---------------- CONFIG ----------------
INPUT_FILE  = r"C:\\Users\\Preksha Asati\\PY\\GL\\Input\\27Mar26\\205045002.ods"
OUTPUT_FILE = r"C:\\Users\\Preksha Asati\\PY\\GL\\Output\\27Mar26\\205045002_final.xlsx"

TOLERANCE = 0.5   # minimum abs(diff) to keep in Filtered_Diff
# ----------------------------------------


# 1) Read the sheet
df = pd.read_excel(INPUT_FILE, sheet_name=0, engine="odf")

# ---------------------------------------------------------
# 2) Split into OGL (left block) and FC (right block)
#    Assumption:
#    - Columns A:D  = OGL  (GL, PRODUCT, BRANCH, SUM)
#    - Columns I:L  = FC   (SUM, BRANCH, PRODUCT, GL)
#    Adjust iloc slices if your layout changes.
# ---------------------------------------------------------

# OGL block: A:D
ogl_raw = df.iloc[:, :4].copy()
ogl_raw.columns = ["gl_ogl", "product_ogl", "branch_ogl", "sum_ogl"]

# FC block: I:L
fc_raw = df.iloc[:, 8:12].copy()
fc_raw.columns = ["sum_fc", "branch_fc", "product_fc", "gl_fc"]

# For aggregation
ogl_for_sum = ogl_raw[["branch_ogl", "product_ogl", "sum_ogl"]]
fc_for_sum  = fc_raw[["branch_fc", "product_fc", "sum_fc"]]

# ---------------------------------------------------------
# 3) Group by (branch, product) like SQL GROUP BY
# ---------------------------------------------------------
ogl_grouped = (
    ogl_for_sum
    .groupby(["branch_ogl", "product_ogl"], as_index=False)["sum_ogl"]
    .sum()
)

fc_grouped = (
    fc_for_sum
    .groupby(["branch_fc", "product_fc"], as_index=False)["sum_fc"]
    .sum()
)

# ---------------------------------------------------------
# 4) FULL OUTER JOIN to see which combos exist where
# ---------------------------------------------------------
merged = pd.merge(
    ogl_grouped,
    fc_grouped,
    left_on=["branch_ogl", "product_ogl"],
    right_on=["branch_fc", "product_fc"],
    how="outer",
    indicator=True
)

merged["status"] = merged["_merge"].map({
    "both": "Present in both",
    "left_only": "Only in OGL",
    "right_only": "Only in FC"
})

# ---------------------------------------------------------
# 5) Pad each side:
#    - Combos only in FC -> add to OGL with sum_ogl = 0
#    - Combos only in OGL -> add to FC with sum_fc = 0
# ---------------------------------------------------------

# Only in OGL
only_in_ogl = merged[merged["status"] == "Only in OGL"][["branch_ogl", "product_ogl"]]

# Only in FC
only_in_fc = merged[merged["status"] == "Only in FC"][["branch_fc", "product_fc"]]

# New rows to add into FC for combos only present in OGL
new_fc_rows = only_in_ogl.rename(
    columns={"branch_ogl": "branch_fc", "product_ogl": "product_fc"}
).copy()
new_fc_rows["sum_fc"] = 0

# New rows to add into OGL for combos only present in FC
new_ogl_rows = only_in_fc.rename(
    columns={"branch_fc": "branch_ogl", "product_fc": "product_ogl"}
).copy()
new_ogl_rows["sum_ogl"] = 0

# Padded tables
ogl_padded = pd.concat([ogl_grouped, new_ogl_rows], ignore_index=True)
fc_padded  = pd.concat([fc_grouped, new_fc_rows], ignore_index=True)

ogl_padded = ogl_padded.sort_values(
    ["branch_ogl", "product_ogl"]
).reset_index(drop=True)

fc_padded = fc_padded.sort_values(
    ["branch_fc", "product_fc"]
).reset_index(drop=True)

# ---------------------------------------------------------
# 6) FC GL mapping: (branch_fc, product_fc) -> gl_fc
# ---------------------------------------------------------
fc_gl_map = (
    fc_raw
    .groupby(["branch_fc", "product_fc"], as_index=False)["gl_fc"]
    .first()    # if multiple GL per combo, takes the first
)

# ---------------------------------------------------------
# 7) Final comparison: OGL_padded vs FC_padded
# ---------------------------------------------------------
final = pd.merge(
    ogl_padded,
    fc_padded,
    left_on=["branch_ogl", "product_ogl"],
    right_on=["branch_fc", "product_fc"],
    how="inner"
)

# Calculate diff
final["diff"] = final["sum_fc"] - final["sum_ogl"]

# Rename to final names
final = final.rename(columns={
    "branch_ogl": "branch_final",
    "product_ogl": "product_final"
})

final = final[["branch_final", "product_final", "sum_ogl", "sum_fc", "diff"]]

# ---------------------------------------------------------
# 8) Apply tolerance filter & add abs_diff + C/D indicator
# ---------------------------------------------------------
# Filter by absolute difference
final_filtered = final[final["diff"].abs() > TOLERANCE].copy()

# Absolute value of difference
final_filtered["abs_diff"] = final_filtered["diff"].abs()

# Credit/Debit indicator: C if diff < 0, D if diff > 0
final_filtered["cr_dr_indicator"] = final_filtered["diff"].apply(
    lambda x: "C" if x < 0 else ("D" if x > 0 else "")
)

# ---------------------------------------------------------
# 9) Attach FC_GL from original FC data
# ---------------------------------------------------------
final_filtered = final_filtered.merge(
    fc_gl_map,
    left_on=["branch_final", "product_final"],
    right_on=["branch_fc", "product_fc"],
    how="left"   # Some combos might not exist in original FC
)

# Drop merge helper columns
final_filtered = final_filtered.drop(columns=["branch_fc", "product_fc"])

# Rename GL column
final_filtered = final_filtered.rename(columns={"gl_fc": "FC_GL"})

# Reorder columns nicely
# final_filtered = final_filtered[
#     ["branch_final", "product_final", "FC_GL",
#      "sum_ogl", "sum_fc", "diff", "abs_diff", "cr_dr_indicator"]
# ]

final_filtered = final_filtered[
    ["branch_final","FC_GL", "abs_diff", "cr_dr_indicator", "product_final", 
    "diff", "sum_ogl", "sum_fc" ]
]


final_filtered = final_filtered.sort_values(
    ["branch_final", "product_final"]
).reset_index(drop=True)

# ---------------------------------------------------------
# 10) Save everything to Excel
# ---------------------------------------------------------
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    ogl_padded.to_excel(writer, sheet_name="OGL_padded", index=False)
    fc_padded.to_excel(writer, sheet_name="FC_padded", index=False)
    final.to_excel(writer, sheet_name="All_Diff", index=False)
    final_filtered.to_excel(writer, sheet_name="Filtered_Diff", index=False)

print("✅ Reconciliation completed.")
print("Output file:", OUTPUT_FILE)
