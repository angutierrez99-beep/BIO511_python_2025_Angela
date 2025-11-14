#===== Task 1 =====
### 30 minutes
nums = [3, 8, 0, -2, 11, 6, 6]

result = 0  # Initialize your results variable.
for i in nums:  # Loop through each element of the list.
    if not i % 2:  # Test for even numbers.
        result += (i)
print(result)

nums_squared = []
import math
for i in nums:
    if i > 0:
        nums_squared.append(math.pow(i, 2))
print(nums_squared)


newlist = [] # empty list to hold unique elements from the list
duplicate = None # 


for i in nums:
    if i in newlist:
        duplicate = i
        break  # stop at the first duplicate
    newlist.append(i)

if duplicate:
    print("First duplicate found:", duplicate)
else:
    print("No duplicates")

#===== Task 2.1 =====
#### 10 minutes
import argparse
import csv
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
        description="Read a CSV file and show a statistical summary using pandas."
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Path to the CSV file created in the previous exercise"
    )
    args = parser.parse_args()
    csv_path = args.file

    # Option A — Manual read (explicitly set delimiter to comma)
    rows = []
    with open(csv_path, "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rows.append(row)

    print("\nCSV content (via csv module):")
    for row in rows:
        print(row)

    # Option B — pandas handles everything automatically
    print("\nReading same file via pandas:")
    df = pd.read_csv(csv_path)
    print(df.head())
    print(df.describe())

if __name__ == "__main__":
    main()


#===== Task 2.2 =====
from practice_dugga_func import orderChromosomes
chr_ordered = orderChromosomes()

#===== Task 2.3 =====
# Plot cnv_log2 (y) separated by chromosome (x) as a scatter
# Since chromosomes need correct order -> xunits=chr_ordered
# Check that the plot as saved as a .png in this folder before pushing to github

import sys
import matplotlib.pyplot as plt
import pandas as pd  # again just to follow along

# tiny helper to reuse the -f/--file path from CLI without redoing argparse:
def _get_cli_csv_path(default_name="CNV_log2_skin_melanoma.csv"):
    try:
        i = sys.argv.index("-f")
        return sys.argv[i+1]
    except Exception:
        try:
            i = sys.argv.index("--file")
            return sys.argv[i+1]
        except Exception:
            return default_name  # fallback if user forgot -f

csv_plot_path = _get_cli_csv_path()
print("\n[Task 2.3] Reading for plot from:", csv_plot_path)

# read the data for plotting (again here, since df in Task 2.1 was inside main())
df_plot = pd.read_csv(csv_plot_path)
print("[Task 2.3] Columns detected:", list(df_plot.columns))


x_col = "chromosome"
y_col = "cnv_log2"

print(f"[Task 2.3] Using x='{x_col}' (chromosomes) and y='{y_col}' (CNV log2)")

# to make the scatter
plt.figure(figsize=(10, 6))
# the key bit: xunits=chr_ordered to have the correct chromosome order
plt.scatter(x=df_plot[x_col], y=df_plot[y_col], s=10, xunits=chr_ordered)

plt.xlabel("Chromosome")
plt.ylabel("CNV (log2)  [cnv_log2]")
plt.title("CNV overview vs chromosome (scatter)")
plt.tight_layout()

dugga_png = "CNV_scatterplot_dugga.png"
plt.savefig(dugga_png, dpi=300)
print(f"[Task 2.3] Saved plot as: {dugga_png}")
plt.show()
