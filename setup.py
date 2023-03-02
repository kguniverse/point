import os
from setuptools import find_packages, setup

import torch
from torch.utils.cpp_extension import (BuildExtension, CppExtension,
                                       CUDAExtension)

def make_cuda_ext(name,
                  module,
                  sources,
                  sources_cuda=[],
                  extra_args=[],
                  extra_include_path=[]):

    define_macros = []
    extra_compile_args = {'cxx': [] + extra_args}

    if torch.cuda.is_available() or os.getenv('FORCE_CUDA', '0') == '1':
        define_macros += [('WITH_CUDA', None)]
        extension = CUDAExtension
        extra_compile_args['nvcc'] = extra_args + [
            '-D__CUDA_NO_HALF_OPERATORS__',
            '-D__CUDA_NO_HALF_CONVERSIONS__',
            '-D__CUDA_NO_HALF2_OPERATORS__',
        ]
        sources += sources_cuda
    else:
        print(f'Compiling {name} without CUDA')
        extension = CppExtension
        raise EnvironmentError('CUDA is required to compile bev_detection!')

    return extension(
        name=f'{module}.{name}',
        sources=[os.path.join(*module.split('.'), p) for p in sources],
        include_dirs=extra_include_path,
        define_macros=define_macros,
        extra_compile_args=extra_compile_args)

setup(
    name='point',
    version='1.0.0rc0',
    author='Cambricon',
    description='A algorithm repositry for Point-cloud perception.',
    packages=find_packages(),
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    ext_modules=[
        make_cuda_ext(
            name='voxel_pool_bevfusion_ext',
            module='bev/ops/voxel_pool_bevfusion',
            sources=['src/voxel_pool_bevfusion.cpp'],
            sources_cuda=['src/voxel_pool_bevfusion_cuda.cu']
        )
    ],
    cmdclass={'build_ext': BuildExtension},
)
