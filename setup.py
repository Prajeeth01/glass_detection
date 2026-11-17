from setuptools import find_packages, setup

package_name = "glass_detection"

setup(
    name=package_name,
    version="1.0.1",
    packages=find_packages(),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            [f"resource/{package_name}"],
        ),
        (
            f"share/{package_name}",
            ["package.xml"],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Prajeeth",
    maintainer_email="pra7805s@hs-coburg.de",
    description="ROS 2 package for detecting glass objects.",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "glass_detection_node=glass_detection.glass_detection_node:main",
        ],
    },
)
