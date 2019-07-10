import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="onap-multicloud-base",
    version="0.0.2",
    author="Haibin Huang",
    author_email="haibin.huang@intel.com",
    description="A multicloud share package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hhb584520/hpa_discovery",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
