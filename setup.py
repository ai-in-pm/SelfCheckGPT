```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="selfcheckgpt",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for detecting hallucinations in large language model outputs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/selfcheckgpt",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "torch>=1.7.0",
        "transformers>=4.0.0",
    ],
)
```
