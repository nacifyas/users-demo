from setuptools import setup

setup(
    name="users-ms",
    version="0.0.1",
    description="MS for users",
    py_modules=["main"],
    package_dir={'':'src'},
    install_requires=[
        "redis-om >= 0.0.27",
        "fastapi >= 0.78.0",
        "uvicorn >= 0.18.2"
    ],
    extras_require = {
        "dev": [
            "mypy==0.942",
            "flake8==4.0.1",
            "pytest-asyncio==0.19.0",
            "requests==2.28.1"
        ]
    },    
)