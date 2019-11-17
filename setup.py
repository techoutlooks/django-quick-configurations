import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quick_configs",
    version="0.1.0",
    author="Edouard Carvalho",
    author_email="ceduth@techoutlooks.com",
    description="Quick OOP-based settings as plugins, based on Jezdez's django-configurations plus some goodies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/techoutlooks/django-quick-configurations",
    packages=setuptools.find_packages(),
    python_requires='>=2.7',
    install_requires=[
        "django-configurations>=2.1",
        "python-dotenv>=0.10.3",
        "dj-database-url>=0.5.0",
        "django-extensions>=2.2",
    ]
)
