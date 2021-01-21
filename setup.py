import setuptools

setuptools.setup(
    name="hybro",
    version="0.0.1a",
    author="Jakob Vanhoefer, Paul F. Lang, Paul Stapor, Yannik Schaelte",
    author_email="jakob.vanhoefer@uni-bonn.de",
    description="A package for hybrid optimization",
    url="https://github.com/HYBRO-dev/HYBRO",
    packages=setuptools.find_packages(),
    install_requires=["numpy>=1.16.4"],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6+",
        "License :: OSI Approved :: MIT License",  # TODO
        "Operating System :: Unix",
    ]
)
