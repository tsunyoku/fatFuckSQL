import setuptools

with open('README.md', 'r') as rm:
    ld = rm.read()

setuptools.setup(
    name='fatFuckSQL',
    version='0.0.1',
    author='tsunyoku',
    author_email='tsunyoku@gmail.com',
    description='Light wrapper for asycnpg',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/tsunyoku/fatFuckSQL',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)