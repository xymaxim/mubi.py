from setuptools import setup

setup(
    name='mubi',
    version='0.2.0',
    description='Helps you log in to mubi.com',
    long_description=__doc__,
    url='https://github.com/mstolyarchuk/mubi.py',
    author='Maxim Stolyarchuk',
    author_email='maxim.stolyarchuk@gmail.com',
    py_modules=['mubi'],
    zip_safe=False,
    include_package_data=True,
    install_requires=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
