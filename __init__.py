# Copyright (c) OpenMMLab. All rights reserved.
import mmengine
import mmcv
import mmcls
import mmseg
import mmdet
import mmdet3d
from mmengine.utils import digit_version

from .point.version import __version__, version_info

mmengine_minimum_version = '0.5.0'
mmengine_maximum_version = '0.5.1'
mmengine_version = digit_version(mmengine.__version__)

mmcv_minimum_version = '2.0.0rc4'
mmcv_maximum_version = '2.0.0rc5'
mmcv_version = digit_version(mmcv.__version__)

mmcls_minimum_version = '1.0.0rc5'
mmcls_maximum_version = '1.0.0rc6'
mmcls_version = digit_version(mmcls.__version__)

mmdet_minimum_version = '3.0.0rc5'
mmdet_maximum_version = '3.0.0rc6'
mmdet_version = digit_version(mmdet.__version__)

mmseg_minimum_version = '1.0.0rc5'
mmseg_maximum_version = '1.0.0rc6'
mmseg_version = digit_version(mmseg.__version__)

mmdet3d_minimum_version = '1.1.0rc3'
mmdet3d_maximum_version = '1.1.0rc4'
mmdet3d_version = digit_version(mmdet3d.__version__)

assert (mmengine_version >= digit_version(mmengine_minimum_version)
        and mmengine_version < digit_version(mmengine_maximum_version)), \
    f'MMEngine=={mmengine.__version__} is used but incompatible. ' \
    f'Please install mmengine>={mmengine_minimum_version}, ' \
    f'<{mmengine_maximum_version}.'

assert (mmcv_version >= digit_version(mmcv_minimum_version)
        and mmcv_version < digit_version(mmcv_maximum_version)), \
    f'MMCV=={mmcv.__version__} is used but incompatible. ' \
    f'Please install mmcv>={mmcv_minimum_version}, <{mmcv_maximum_version}.'

assert (mmcls_version >= digit_version(mmcls_minimum_version)
        and mmcls_version < digit_version(mmcls_maximum_version)), \
    f'MMCLS=={mmcls.__version__} is used but incompatible. ' \
    f'Please install mmcls>={mmcls_minimum_version}, <{mmcls_maximum_version}.'

assert (mmdet_version >= digit_version(mmdet_minimum_version)
        and mmdet_version < digit_version(mmdet_maximum_version)), \
    f'MMDET=={mmdet.__version__} is used but incompatible. ' \
    f'Please install mmdet>={mmdet_minimum_version}, ' \
    f'<{mmdet_maximum_version}.'

assert (mmseg_version >= digit_version(mmseg_minimum_version)
        and mmseg_version < digit_version(mmseg_maximum_version)), \
    f'MMSEG=={mmseg.__version__} is used but incompatible. ' \
    f'Please install mmseg>={mmseg_minimum_version}, <{mmseg_maximum_version}.'

assert (mmdet3d_version >= digit_version(mmdet3d_minimum_version)
        and mmdet3d_version < digit_version(mmdet3d_maximum_version)), \
    f'MMDET3D=={mmdet3d.__version__} is used but incompatible. ' \
    f'Please install mmdet3d>={mmdet3d_minimum_version}, ' \
    f'<{mmdet3d_maximum_version}.'


__all__ = ['__version__', 'version_info', 'digit_version']
