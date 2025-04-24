import numpy as np
import os
from PIL import Image
from sklearn.decomposition import PCA
from skimage.feature import hog
from tqdm import tqdm


# Functions
def extract_hog(img_path):
    img = Image.open(img_path).convert("L").resize((48, 48))
    arr = np.array(img).astype("float32") / 255.0
    return hog(arr, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)


# Paths
features_pca_path = os.path.join(os.path.dirname(__file__), "similarity_hog_pca.py")

if __name__ == "__main__":

    # Read all files
    image_dir = "images_48x48"
    files = sorted([f for f in os.listdir(image_dir) if f.endswith(".png")])
    chars = [chr(int(f[:-4])) for f in files]

    # HOG
    print("Extracting HOG features...")
    features = [extract_hog(os.path.join(image_dir, f)) for f in tqdm(files)]
    features = np.array(features)

    # PCA
    print("PCA running...")
    pca = PCA(n_components=64)
    features_pca = pca.fit_transform(features)

    # Save model parameters
    np.save("features_pca.npy", features_pca)
