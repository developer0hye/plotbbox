import setuptools
import os

README_FILE_DIR = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "README.md")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotbbox", # Replace with your own username
    version="0.1.1",
    author="Yonghye Kwon",
    author_email="developer.0hye@gmail.com",
    description="A package to plot pretty bounding boxes for object detection task",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/developer0hye/plotbbox",
    keywords=["object-detection", "bounding-box", "bbox", "box"],
    install_requires=["numpy", "opencv-python", "Pillow"],
    packages=setuptools.find_packages(exclude = ['docs']),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)