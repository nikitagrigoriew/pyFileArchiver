import setuptools


with open('README.md') as fr:
    long_description = fr.read()

setuptools.setup(
    name='pyFileArchiverGrigoriew',
    version='1.0.0',
    author='Grigoriew N.A.',
    author_email='nickita.grigoriew2012@yandex.ru',
    description='Python archiver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nikitagrigoriew/pyFileArchiver',
    packages=setuptools.find_packages(),
    install_requires=[],
    test_suite='tests',
    python_requires='>=3.7',
    platforms=["any"]
)
