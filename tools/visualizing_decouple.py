from visualizer import Visualizer
import numpy as np
from os import path as osp
import argparse

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


if __name__ == '__main__':
    main()
