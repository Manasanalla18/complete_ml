from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads requirements.txt and returns a list of dependencies.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Remove spaces and newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove "-e ." safely

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Manasa",
    author_email="manasanalla11@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
