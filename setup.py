from setuptools import setup

setup(
    name="users-ms",
    version="0.0.1",
    description="MS for users",
    py_modules=["main"],
    package_dir={'':'src'},
    install_requires=[
        "redis >= 4.3.4",
        "fastapi >= 0.78.0",
        "uvicorn >= 0.18.2",
        "pymongo >= 4.1.1"
    ],
)