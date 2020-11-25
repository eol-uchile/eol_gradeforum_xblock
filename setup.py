"""Setup for eolgradediscussion XBlock."""


import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='eolgradediscussion',
    version='0.1',
    description='Eol Grade Forum Xblock',
    license='AGPL v3',
    packages=[
        'eolgradediscussion',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'eolgradediscussion = eolgradediscussion:EolGradeDiscussionXBlock',
        ],
        "lms.djangoapp": [
            "eolgradediscussion = eolgradediscussion.apps:EolGradeDiscussionConfig",
        ],
        "cms.djangoapp": [
            "eolgradediscussion = eolgradediscussion.apps:EolGradeDiscussionConfig",
        ]
    },
    package_data=package_data("eolgradediscussion", ["static", "public"]),
)
