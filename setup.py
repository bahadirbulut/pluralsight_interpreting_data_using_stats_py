from distutils.core import setup

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setup(
    name='pluralsight_interpreting_data_using_stats_py',
    version='1.0.0',
    author='Bahadir Bulut',
    author_email='bulutbbahadir@gmail.com',
    # packages=['thinkstats2', 'thinkplot'],
    url='https://github.com/bahadirbulut/The-Statistics-and-Calculus-with-Python-Workshop',
    license='LICENSE.txt',
    description='Supporting code for Pluralsight Interpreting Data Using Statistical Models with Python',
    long_description=readme(),
)