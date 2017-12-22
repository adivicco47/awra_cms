from setuptools import setup,find_packages

setup(name='awrams.models',
      namespace_packages=['awrams'],
      packages=['awrams.models','awrams.models.awral','awrams.models.runoffcoeff'],
      package_data={'awrams.models.awral':['core/awral_t.*','core/build_cache/empty.txt']},
      # install_requires=['numpy==1.9.3'],
      version='0.1',
      description='AWRAL Model',
      url='https://gitlab.bom.gov.au/awra/awrams_cm.git',
      author='awrams team',
      author_email='awrams@bom.gov.au',
      license='MIT',
      zip_safe=False,
      include_package_data=True,
      setup_requires=['nose>=1.3.3'],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
