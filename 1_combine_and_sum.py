#!/usr/bin/env python3
import sys
import pandas as pd

def main():
    # --- Paths ---
    color_results_fn = "SOAPP/output/color_results.csv"
    results_fn      = "SOAPP/output/results.csv"
    map_fn          = "SOAPP/output/images_to_sequencing.csv"
    glds_fn         = "RNAseq/GLDS-476_rna_seq_Normalized_Counts.csv"
    out_fn          = "RNAseq/combined_with_rna_sums.csv" 

    # 1) Read inputs
    color_df  = pd.read_csv(color_results_fn)
    results_df= pd.read_csv(results_fn)
    map_df    = pd.read_csv(map_fn)
    glds_raw  = pd.read_csv(glds_fn)

    # 2) Merge color_results and results on image_name
    merged = pd.merge(color_df, results_df, on="image_name", how="outer", suffixes=("_color", "_results"))

    # 3) Validate mapping columns
    if "image_name" not in map_df.columns or "GSM_number" not in map_df.columns:
        raise ValueError("images_to_sequencing.csv must contain columns: image_name, GSM_number")

    # 4) Prepare GLDS matrix with gene IDs as index
    gene_col = glds_raw.columns[0]  # first column = gene IDs
    glds = glds_raw.set_index(gene_col)

    # ensure numeric values
    for c in glds.columns:
        glds[c] = pd.to_numeric(glds[c], errors="coerce")

    # normalize IDs
    map_df["GSM_number"] = map_df["GSM_number"].astype(str).str.strip()
    glds.columns = glds.columns.astype(str).str.strip()

    # 5) Build final rows, but keep only if GSM exists in RNA file
    all_rows = []
    for _, base_row in merged.iterrows():
        img = base_row.get("image_name")
        if pd.isna(img):
            continue

        gsm_list = map_df.loc[map_df["image_name"] == img, "GSM_number"].tolist()
        for gsm in gsm_list:
            if gsm in glds.columns:   # only keep GSMs with data
                new_row = base_row.to_dict()
                new_row["GSM_number"] = gsm
                new_row.update(glds[gsm].to_dict())  # gene expression values
                all_rows.append(new_row)

    final_df = pd.DataFrame(all_rows)

    # 6) Save
    final_df.to_csv(out_fn, index=False)
    print(f"Saved: {out_fn}")
    print(f"Rows kept: {len(final_df)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e, file=sys.stderr)
        sys.exit(1)
