from setuptools import setup, find_packages

setup(
    name='hpa_discovery',
    version='1.0',

    description='HPA discovery package for stevedore',

    author='Haibin Huang',
    author_email='haibin.huang@intel.com',

    url='https://opendev.org/openstack/stevedore',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['hpa_discovery',
              ],

    packages=find_packages(),
    install_requires=['stevedore'],
    include_package_data=True,

    entry_points={
        'hpa_discovery.formatter': [
            'simple = hpa_discovery.hsimple:Simple',
            'plain = hpa_discovery.hsimple:Simple',
        ],
    },

    zip_safe=False,
)
