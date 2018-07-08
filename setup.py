import setuptools

__version__ = '1.0.1'

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    reqs = f.read().splitlines()

setuptools.setup(
    name="PVGeo",
    version=__version__,
    author="Bane Sullivan",
    author_email="info@pvgeo.org",
    description="Geoscientific visualization tools for VTK and ParaView",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenGeoVis/PVGeo",
    packages=setuptools.find_packages(),
    install_requires=reqs,
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
)