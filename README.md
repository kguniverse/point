# mmopenlab 1.0 version

This is the branch for stable model training & visualization.

## train

```bash
./tools/dist_train.sh configs/pointpillars/hv_pointpillars_fpn_sbn-all_fp16_2x8_2x_nus-3d.py 8
```

## visualization

```bash
python tools/test.py configs/pointpillars/hv_pointpillars_fpn_sbn-all_fp16_2x8_2x_nus-3d.py work_dirs/hv_pointpillars_fpn_sbn-all_fp16_2x8_2x_nus-3d/latest.pth --show --show-dir vis
```

> Note: visualization only support for single gpu!

