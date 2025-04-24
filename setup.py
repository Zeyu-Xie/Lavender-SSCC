from setuptools import setup, find_packages

setup(
    name="Lavender-SSCC",
    version="0.0.4",
    description="A pip package to calculate similarity in shape among Chinese characters.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zeyu Xie",
    author_email="xie.zeyu20@gmail.com",
    url="https://github.com/Zeyu-Xie/Lavender-SSCC",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy>=1.26.4",
        "scikit-learn>=1.6.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)