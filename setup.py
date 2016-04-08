from setuptools import setup

setup(
    name='gitignore_creator',
    version='0.1',
    py_modules=['gitignore_creator'],
    install_requires=[
        'Click',
        'requests',
        'pyfiglet'
    ],
    entry_points="""
    [console_scripts]
    gitignore-creator=gitignore_creator:gitignore_creator
    """
)
