from importlib import resources
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

# Paths
ccs_path = resources.files("lavender_sscc").joinpath(f"ccs.txt")
features_pca_path = resources.files("lavender_sscc").joinpath(f"features_pca.npy")

# Read ccs list
ccs = []
with open(ccs_path, "r") as f:
    ccs = list(f.read())

# Read features PCA dataset
features_pca = np.load(features_pca_path)

# Look-up functions
char_to_index = {ch: i for i, ch in enumerate(ccs)}


# Functions
def similarity_between(c1, c2):
    idx1 = char_to_index.get(c1)
    idx2 = char_to_index.get(c2)
    if idx1 is None or idx2 is None:
        return 0.0
    v1 = features_pca[idx1].reshape(1, -1)
    v2 = features_pca[idx2].reshape(1, -1)
    return cosine_similarity(v1, v2)[0][0]


__all__ = ["similarity_between"]
