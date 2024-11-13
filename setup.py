from setuptools import setup

version = __import__("src").get_version()

setup(
    name="crypto_xor",
    version="0.1",
    description="Encrypt-decrypt string with your password",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/crypto-xor",
    license="MIT",
    packages=["src"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
)