from setuptools import setup, find_packages

setup(
    name="smpl-anthropometry",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "torch>=2.2.0",
        "trimesh>=3.15.1",
        "smplx>=0.1.26",
        "scipy>=1.10.0",
        "scikit-learn>=1.0.2",
        "plotly>=5.10.0",
        "pandas>=1.3.5",
        "tqdm>=4.66.1",
        "chumpy>=0.70",
    ],
    author="David Bojanić",
    author_email="david.bojanic@epfl.ch",
    description="Measure the SMPL/SMPLX body models and visualize the measurements and landmarks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DavidBoja/SMPL-Anthropometry",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 