# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------
import numpy as np
import cv2
import copy
import time


def init_canvas(width: int, height: int, color: tuple = (0, 0, 0)) -> np.ndarray:
    """
    docs:
        return a empty canvas of color.
    :param width: image width
    :param height: image height
    :param color: canvas color
    :return: a np.ndarry image
    """
    canvas = np.ones((height, width, 3), dtype='uint8')
    canvas[:] = color
    return canvas


def py_cpu_nms(boxes: np.ndarray, thresh: float) -> list:
    """
    docs:
        Pure Python NMS baseline
    :param boxes:boxes shape:[classes_numx5] eg:[[x1,y1,x2,y2,score],...]
    :param thresh:
    :return:
    """

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    scores = boxes[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]  # scores从大到小排序，获取下标

    keep = []  # 保持需要留下的box index
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        iou = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(iou <= thresh)[0]
        order = order[inds + 1]  # next one

    return keep


if __name__ == '__main__':
    canvas = init_canvas(800, 600)

    # test data
    np.random.seed(1)  # keep fixed
    num_rois = 60
    minxy = np.random.randint(50, 300, size=(num_rois, 2))
    maxxy = np.random.randint(300, 500, size=(num_rois, 2))
    score = 0.8 * np.random.random_sample((num_rois, 1)) + 0.2
    boxes = np.concatenate((minxy, maxxy, score), axis=1).astype(np.float32)
    print(f'boxes shape:{boxes.shape}')

    img1 = copy.deepcopy(canvas)
    for item in boxes:
        x1, y1, x2, y2, score = item
        cv2.rectangle(img1, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)
        # cv2.putText(img1, str(score), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imwrite('imgs/cpu_nms_result_1.jpg', img1)

    t1 = time.time()
    keep = py_cpu_nms(boxes, 0.3)
    t2 = time.time()
    print(f'time:{t2 - t1}s')

    img2 = copy.deepcopy(canvas)
    for item in keep:
        x1, y1, x2, y2, score = boxes[item]
        cv2.rectangle(img2, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)
        # cv2.putText(img2, str(score), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imwrite('imgs/cpu_nms_result_2.jpg', img2)
    cv2.waitKey(0)
