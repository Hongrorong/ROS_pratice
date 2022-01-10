from setuptools import setup
import os
import glob

package_name = 'ros_pratice'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*launch.py'))),
        ('share/' + package_name +'/param', glob.glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hongmin',
    maintainer_email='ghdals6864@naver.com',
    description='TODO: circle turtle',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'info_pub = ros_pratice.info_pub:main',
            'info_sub = ros_pratice.info_sub:main'
        ],
    },
)
