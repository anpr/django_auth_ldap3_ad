from distutils.core import setup

setup(
    name='django_auth_ldap3_ad',
    version='0.1',
    packages=['django_auth_ldap3_ad'],
    url='',
    license='GPL V3',
    author='Pierre-Olivier VERSCHOORE',
    author_email='po.verschoore@sd-libre.fr',
    description='very simple authentication module for python3 / django / LDAP or AD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=["ldap3>=0.9.8.*"],
)