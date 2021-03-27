from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setup(
  name = 'exaroton',
  packages=['exaroton'],
  version = '1.0.0',
  license='MIT',
  description = 'API wrapper for exaroton',
  author = 'Joshua',
  author_email = 'bluewyechache@gmail.com',
  url = 'https://github.com/BluewyDev/python-exaroton-api/',
  download_url = 'https://github.com/BluewyDev/python-exaroton-api.git',
  install_requires=['aiohttp'],
  long_description=long_description,
  long_description_content_type="text/markdown",
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)
