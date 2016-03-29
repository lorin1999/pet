from setuptools import setup


setup(
    name='memes',
    install_requires=[
        'kivy',
        'flask',
        'requests[security]',
        'slugify',
    ],
    packages=['memes'],
    entry_points={'console_scripts': [
        'kivy = memes.kivy_viewer:main',
        'flask = memes.flask_viewer:main'
    ]},
)
