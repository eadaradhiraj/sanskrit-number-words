from setuptools import setup, find_packages

setup(
    name='sanskrit-number-words',
    version='0.0.1',
    packages=find_packages('sanskrit_number_words', exclude=['test']),
    package_dir = {'': 'sanskrit_number_words'},
    url="https://github.com/eadaradhiraj/sanskrit-number-words",
    license='',
    author='Dhiraj Eadara',
    author_email='eadaradhiraj@gmail.com',
    description='Convert Sanskrit number words into actual numbers'
)