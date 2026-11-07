import pandas as pd
import os
import glob

# folder paths
input_knee  = './new_clean/'        # folder berisi *_CLEAN.csv (lutut)
input_hip   = './hip_clean/'        # folder berisi *_HIP_CLEAN.csv (panggul)
output_merged = './merged/'
os.makedirs(output_merged, exist_ok=True)

# ambil semua file lutut (exclude file HIP supaya tidak dobel)
knee_files = [
    f for f in glob.glob(os.path.join(input_knee, '*_CLEAN.csv'))
    if '_HIP_CLEAN' not in f
]
print(f"Ditemukan {len(knee_files)} file lutut")

success, skipped = 0, 0

for knee_path in knee_files:
    base = os.path.basename(knee_path)                      # 001_EL_KOA_LEFT_CLEAN.csv
    prefix = base.replace('_CLEAN.csv', '')                 # 001_EL_KOA_LEFT
    hip_filename = f"{prefix}_HIP_CLEAN.csv"
    hip_path = os.path.join(input_hip, hip_filename)

    # cek pasangan HIP ada atau tidak
    if not os.path.exists(hip_path):
        print(f"  [SKIP] pasangan HIP tidak ditemukan: {hip_filename}")
        skipped += 1
        continue

    # baca kedua file
    df_knee = pd.read_csv(knee_path)
    df_hip  = pd.read_csv(hip_path)

    # ambil kolom yang relevan saja
    df_knee = df_knee[['frame', 'cleaned_angles']].rename(columns={'cleaned_angles': 'knee_angle_clean'})
    df_hip  = df_hip[['frame', 'cleaned_hip_angles']].rename(columns={'cleaned_hip_angles': 'hip_angle_clean'})

    # merge berdasarkan frame
    df_merged = pd.merge(df_knee, df_hip, on='frame', how='inner')

    # simpan
    out_filename = f"{prefix}_MERGED.csv"
    out_path = os.path.join(output_merged, out_filename)
    df_merged.to_csv(out_path, index=False)

    print(f"  [OK] {out_filename}  ({len(df_merged)} frames)")
    success += 1

print(f"\nSelesai: {success} berhasil, {skipped} dilewati.")