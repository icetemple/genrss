from setuptools import setup


with open('README.md', 'r') as f:
    readme = f.read()


if __name__ == '__main__':
    setup(
        name='genrss',
        version='1.0.3',
        author='Dmitriy Pleshevskiy',
        author_email='dmitriy@ideascup.me',
        description='RSS feed generator for python',
        long_description=readme,
        long_description_content_type='text/markdown',
        package_data={'': ['LICENSE', 'README.md']},
        include_package_data=True,
        license='MIT',
        packages=['genrss'],
        install_requires=[
            'lxml==4.3.4',
            'pytz==2019.1'
        ]
    )
