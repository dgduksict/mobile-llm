import setuptools

setuptools.setup(
    name="mobile-llm",
    version="0.1.0",
    author="Duke",
    author_email="bdulguunod@gmail.com",
    description="Scripts for exporting MobileLLM-R1-950M to ONNX for Android deployment",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dgduksict/mobile-llm",
    packages=setuptools.find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.40.0",
        "optimum[exporters,onnxruntime]>=1.17.0",
        "onnxruntime>=1.19.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
)