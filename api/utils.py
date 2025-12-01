import pandas as pd
import unicodedata
import os
import glob

def load_master_csv(base_path, file_pattern):
    """Load master CSV from assets directory."""
    search_path = os.path.join(base_path, f'*{file_pattern}*.csv')
    list_of_files = glob.glob(search_path)
    if not list_of_files:
        return pd.DataFrame()
    latest_file = max(list_of_files, key=os.path.getmtime)
    encodings = ['utf-8-sig', 'utf-8', 'cp932', 'shift_jis']
    for encoding in encodings:
        try:
            df = pd.read_csv(latest_file, encoding=encoding, dtype=str).fillna('')
            if not df.empty:
                df.columns = df.columns.str.strip()
                return df
        except Exception:
            continue
    return pd.DataFrame()

def match_bento_data(pdf_bento_list, master_df):
    """
    Match extracted bento names with master data.
    """
    if master_df is None or master_df.empty:
        return [[name, "", "", ""] for name in pdf_bento_list]

    master_df.columns = master_df.columns.str.strip()
    required_cols = ['商品予定名', 'パン箱入数', '売価単価', '弁当区分']

    if not all(col in master_df.columns for col in required_cols):
        return [[name, "", "マスタ列不足", ""] for name in pdf_bento_list]
    
    master_tuples = master_df[required_cols].astype(str).to_records(index=False).tolist()
    matched_results = []
    
    norm_master = [
        (unicodedata.normalize('NFKC', name).replace(" ", ""), name, pan_box, price, bento_type)
        for name, pan_box, price, bento_type in master_tuples
    ]

    for pdf_name in pdf_bento_list:
        if not pdf_name: continue
        pdf_name_stripped = str(pdf_name).strip()
        norm_pdf = unicodedata.normalize('NFKC', pdf_name_stripped).replace(" ", "")
        result_data = [pdf_name_stripped, "", "", ""]
        best_match = None
        
        # 1. Exact match
        for norm_m, orig_m, pan_box, price, bento_type in norm_master:
            if norm_m == norm_pdf:
                best_match = [orig_m, pan_box, price, bento_type]
                break
        
        # 2. Partial match
        if not best_match:
            candidates = []
            for norm_m, orig_m, pan_box, price, bento_type in norm_master:
                if norm_m and norm_m in norm_pdf:
                    candidates.append((orig_m, pan_box, price, bento_type))
            if candidates:
                best_match = max(candidates, key=lambda x: len(x[0]))

        if best_match:
            result_data = best_match
        
        matched_results.append(result_data)
        
    return matched_results

def safe_write_df(worksheet, df, start_row=1):
    """Write DataFrame to Excel sheet safely."""
    # Clear existing data first (simple approach)
    # In a real scenario, we might want to be more careful, but for this template it's okay to overwrite
    for r_idx, row_data in enumerate(df.itertuples(index=False), start=start_row):
        for c_idx, value in enumerate(row_data, start=1):
            worksheet.cell(row=r_idx, column=c_idx, value=value)

def paste_dataframe_to_sheet(ws, df, start_row=1, start_col=1):
    """Paste DataFrame to Excel sheet."""
    for c_idx, col_name in enumerate(df.columns, start=start_col):
        ws.cell(row=start_row, column=c_idx, value=col_name)
    
    for r_idx, row in df.iterrows():
        for c_idx, value in enumerate(row, start=start_col):
            ws.cell(row=start_row + r_idx + 1, column=c_idx, value=value)
