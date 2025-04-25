from lavender_sscc import similarity_between
import numpy as np
import os
import pandas as pd
from tqdm import tqdm

# Paths
ccs_path = os.path.join(os.path.dirname(__file__), "ccs.txt")
features_pca_path = os.path.join(os.path.dirname(__file__), "features_pca.npy")
df_path = os.path.join(os.path.dirname(__file__), "top_sccs.csv")

# Read ccs list
ccs = []
with open(ccs_path, "r") as f:
    ccs = list(f.read())
N = len(ccs)

# Read features PCA dataset
features_pca = np.load(features_pca_path)

# Look-up functions
char_to_index = {ch: i for i, ch in enumerate(ccs)}

# Generate rank list
top_sccs_list = []
for cc in tqdm(ccs):

    similarities = [(similarity_between(cc, ccs[i]), ccs[i]) for i in range(N)]
    similarities.sort(key=lambda x: -x[0])

    top_sccs_list.append("".join([(x[1]) for x in similarities[:10]]))

# Make dataframe
df = pd.DataFrame(list(zip(ccs, top_sccs_list)), columns=["character", "top sccs"])
df.to_csv(df_path, index=False)