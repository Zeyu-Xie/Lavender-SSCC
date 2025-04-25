# Lavender-SSCC

**Lavender-SSCC** (Similarity-Shaped Chinese Characters) is a Python package for recognizing, comparing, and analyzing Chinese characters based on visual similarity.

## Quick Start

### Installation

Install the package using pip:

```bash
pip install Lavender-SSCC
```

### Importing

Import the package in your Python scripts:

```python
from lavender_sscc import *
```

## Functions

| Usage                          | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| `similarity_between(cc1, cc2)` | Returns the similarity between two Chinese characters `cc1` and `cc2` as a float. |
| `top_similarities_of(cc)`      | Returns a list of the top ten most visually similar Chinese characters to `cc` (including itself). |

## Data Sources

### Included in the Published Package

The following files are included in the published package:

1. `ccs.txt`: Contains 20,992 distinct Chinese characters.
2. `features_pca.npy`: A NumPy array containing visual feature vectors for all Chinese characters.

These files were created by the repo author and are licensed under the [GPL-3.0 License](./LICENSE).

### During Development

During development, the following data sources were used or referenced:

1. **Tables of East Asian Scripts** from the [Unicode Character Code Charts](https://www.unicode.org/charts/) — used to generate `ccs.txt`.

2. **Fonts** used to generate Chinese character images:

   | Font Name | Font File                              | Copyright                                                    |
   | --------- | -------------------------------------- | ------------------------------------------------------------ |
   | STHeiti   | [STHeiti Medium](./STHeiti_Medium.ttc) | Copyright © 2002, Changzhou SinoType Technology Co., Ltd. All rights reserved. |
