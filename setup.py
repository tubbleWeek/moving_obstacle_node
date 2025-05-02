from setuptools import find_packages, setup

package_name = 'moving_obstacle_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/moving_obstacle.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/obstacle.urdf']),
        ('share/' + package_name + '/worlds', ['worlds/world.world'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='will',
    maintainer_email='will@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'obstacles = moving_obstacle_node.obstacles:main'
        ],
    },
)
