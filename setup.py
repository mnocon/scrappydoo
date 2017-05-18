setup(
    name='scrappydoo',
    version=scrappydoo.__version__,
    url='https://github.com/mnocon/scrappydoo',
    license='MIT',
    author='Marek Nocoń',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='markno@gmail.com',
    description='A customizable website scraper',
    packages=['scrappydoo'],
    platforms='any',
    test_suite='scrappydoo.test.scrappydoo',
    extras_require={
        'testing': ['pytest'],
    }
)