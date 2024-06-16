from setuptools import find_packages, setup

package_name = 'robot_controller'

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
    maintainer='adarsh',
    maintainer_email='adarsh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = robot_controller.first_node:main",
            "test_node2 = robot_controller.second_node:main",
            "pos_node = robot_controller.pose_sub:main",
            "ctt_node = robot_controller.ctt:main"
        ],
    },
)
