from setuptools import setup

package_name = 'asbir_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aralab',
    maintainer_email='trichnak72399@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'potentialField = asbir_navigation.potentialField:main',
            'frameTest = asbir_navigation.frameTest:main',
            'modelTest = asbir_navigation.modelTest:main',
            'graphTest = asbir_navigation.graphTest:main',
            'buildBestPath = asbir_navigation.buildBestPath:main',
            'pointPub = asbir_navigation.pointPub:main',
            'odomFrame = asbir_navigation.odomFrame:main',
            'compressImage = asbir_navigation.imageCompression:main',
            'processMesh = asbir_navigation.processMesh:main',
            'pathController = asbir_navigation.pathController:main',
            'serialComm = asbir_navigation.serialComm:main',
            'setZero = asbir_navigation.servoSetZero:main',
            'cameraLink = asbir_navigation.cameraLinkFrame:main'
        ],
    },
)
