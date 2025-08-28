# setup.py
from setuptools import setup, find_packages

setup(
    name="image-to-pencil-sketch",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to convert images to pencil sketches",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
    ],
    entry_points={
        "console_scripts": [
            "image-to-sketch=cli:main",
        ],
    },
    python_requires=">=3.7",
)