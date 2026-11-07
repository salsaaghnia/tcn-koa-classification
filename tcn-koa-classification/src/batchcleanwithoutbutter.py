import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os
import glob

# import data csv
input_raw = './fix_raw/'
output_clean = './new_clean/'
os.makedirs(output_clean, exist_ok=True)

raw_files = glob.glob(os.path.join(input_raw, '*_RAW.csv'))
print(f"finished loading {len(raw_files)} files")

# loop through each raw csv file
for i, csv_file in enumerate(raw_files):
    base_filename = os.path.basename(csv_file).replace('_RAW.csv', '')

    df = pd.read_csv(csv_file)

    # interpolation process
    # limit_direction='both' filled up the NaN values
    df['cleaned_angles'] = df['knee_angle'].interpolate(method='linear', limit_direction='both')


    clean_filename = f"{base_filename}_CLEAN.csv"
    clean_filepath = os.path.join(output_clean, clean_filename)

    #new csv file with cleaned data
    df.to_csv(clean_filepath, index=False)
    print(f"done. data saved in {clean_filename}")

print("all files processed and saved in new_clean folder")

# #visualization
# plt.figure(figsize=(12, 6))
# plt.plot(df['frame'], df['knee_angle'], label='Raw (with NaN)', marker='o', linestyle='dashed', alpha=0.5)
# plt.plot(df['frame'], df['cleaned_angles'], label='Clean (after filtering)', linewidth=2, color='red')
# plt.title('angles comparison between raw and cleaned data')
# plt.xlabel('Frame')
# plt.ylabel('knee angle (degrees)')
# plt.legend()
# plt.grid(True)
# plt.show()