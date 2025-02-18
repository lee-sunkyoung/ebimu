from setuptools import find_packages, setup

package_name = 'ebimu_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='e2box',
    maintainer_email='e2b@e2box.co.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ebimu_publisher = ebimu_pkg.ebimu_publisher:main',
            'ebimu_subscriber = ebimu_pkg.ebimu_subscriber:main',
            'imu_pub = ebimu_pkg.imu_pub:main'
        ],
    },
)
