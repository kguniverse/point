from visualizer import Visualizer, draw_lidar_bbox3d_on_img
import numpy as np
from os import path as osp
import argparse
import mmcv

def draw(points, 
         gt_bboxes = None, 
         pred_bboxes = None, 
         pred_labels = None):
    vis = Visualizer(points)
    if pred_bboxes is not None:
        if pred_labels is None:
            vis.add_bboxes(bbox3d=pred_bboxes)
        else:
            palette = np.random.randint(
                0, 255, size=(pred_labels.max() + 1, 3)) / 256
            labelDict = {}
            for j in range(len(pred_labels)):
                i = int(pred_labels[j])
                if labelDict.get(i) is None:
                    labelDict[i] = []
                labelDict[i].append(pred_bboxes[j])
            for i in labelDict:
                vis.add_bboxes(
                    bbox3d=np.array(labelDict[i]),
                    bbox_color=palette[i],
                    points_in_box_color=palette[i])
    if gt_bboxes is not None:
        vis.add_bboxes(bbox3d=gt_bboxes, bbox_color=(0, 0, 1))
    # show_path = osp.join(result_path,
    #                         f'{filename}_online.png') if snapshot else None
    vis.show()

def draw_multi_modality(imgs, lidar2img, pred_bboxes_mmdet3d, filename, img_shape):
    pred_bbox_color=(241, 101, 72)
    draw_bbox = draw_lidar_bbox3d_on_img
    canvas = np.zeros((img_shape[0] * 2, img_shape[1] * 3, 3), dtype=np.uint8)
    for i in range(len(imgs)):
        img = imgs[i]
        pred_img = draw_bbox(
            pred_bboxes_mmdet3d, img, lidar2img, None, color=pred_bbox_color)
        mmcv.imwrite(pred_img, osp.join('work_dirs/vis_result', f'{filename}_pred_{i}.png'))
        # canvas[img_shape[0] * (i // 3):img_shape[0] * (i // 3 + 1), img_shape[1] * (i % 3):img_shape[1] * (i % 3 + 1), :] = pred_img
    #TODO: rearrange the canvas

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('result_dir', help='result pkl files dir')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    result_dir = args.result_dir
    import glob
    import pickle
    for pkl_file in glob.glob(osp.join(result_dir, '*.pkl')):
        with open(pkl_file, 'rb') as f:
            data = pickle.load(f)
        for i in range(len(data)):
            draw(data[i]['points'], 
                 None,
                 data[i]['pred_bboxes'], 
                 data[i]['pred_labels'])
            draw_multi_modality(data[i]['imgs'],
                                data[i]['lidar2img'],
                                data[i]['pred_bboxes_mmdet3d'],
                                pkl_file)


if __name__ == '__main__':
    main()
