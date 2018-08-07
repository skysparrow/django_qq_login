from setuptools import setup, find_packages

setup(
    name="advisorhelper",
    packages=find_packages(),
    version='0.9.3',
    description="command line tool for auto tuner",
    author="libbyandhelen",
    author_email='libbyandhelen@163.com',
    url="https://github.com/username/reponame",
    download_url='https://github.com/username/reponame/archive/0.1.tar.gz',
    keywords=['command', 'line', 'tool'],
    classifiers=[],
    entry_points={
        'console_scripts': [
        'command1 = advisorhelper.cmdline:execute'
        'command2 = adviserserver.create_algorithm:run',
        'command3 = adviserserver.run_algorithm:run'
    ]
    },
    install_requires=[
        'grpcio>=1.7.0',
        'numpy',
        'requests',
    ]
)