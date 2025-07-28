import setuptools

setuptools.setup(
    name="cepton_sdk3",
    version="3.0.17.14",
    description="Cepton SDK3 Python3 bindings",
    url="https://www.cepton.com",
    author="Cepton Technologies, Inc.",
    author_email="will.lauer@cepton.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    packages=["cepton_sdk3"],
    install_requires=["numpy"],
    zip_safe=True,
)
