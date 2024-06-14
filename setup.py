from setuptools import setup, find_packages

setup(
    name="video_subtitle_remover",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'albumentations==0.5.2',
        'filesplit==3.0.2',
        'opencv-python==4.8.1.78',
        #'scikit-image==0.17.2',
        'imgaug==0.4.0',
        'kornia==0.5.0',
        'pyclipper==1.3.0.post5',
        'lmdb==1.4.1',
        'PyYAML==6.0.1',
        'omegaconf==2.1.2',
        'tqdm==4.66.1',
        'easydict==1.9',
        #'scikit-learn==0.24.2',
        'pandas==2.0.3',
        'webdataset==0.2.57',
        'pytorch-lightning==1.2.9',
        'numpy==1.23.1',
        'protobuf==3.20.0',
        'av==11.0.0',
        'einops==0.7.0'
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts if needed
            # e.g., 'remove_subtitles=backend.main:main_function'
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for removing hard-coded subtitles from videos",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/idrisrupt/video-subtitle-remover",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)