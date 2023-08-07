from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='wkey',
      version='0.1',
      description='Integrate OpenAI speech-to-text Whisper with your keyboard',
      url='https://github.com/vlad-ds/whisper-keyboard',
      author='Vlad Gheorghe',
      author_email='vlad.datapro@gmail.com',
      license='MIT',
      packages=['wkey'],
      scripts=['scripts/wkey', 'scripts/fkey'],
      install_requires=required,
      include_package_data=True,
      zip_safe=False
      )
 