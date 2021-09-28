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
    :param width: image width
    :param height: image height
    :param color: canvas color
    :return: a np.ndarry image
    """
    canvas = np.ones((height, width, 3), dtype='uint8')
    canvas[:] = color
    return canvas


def py_cpu_nms(dets: np.ndarray, thresh: float):
    """Pure Python NMS baseline."""
    '''
    dets shape:[classes_numx5],5:[x1,y1,x2,y2,score]
    
    '''
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]

    keep = []
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
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]

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

    # test data
    # boxes = np.array([[100, 100, 210, 210, 0.72],
    #                   [250, 250, 420, 420, 0.8],
    #                   [220, 220, 320, 330, 0.92],
    #                   [100, 100, 210, 210, 0.72],
    #                   [230, 240, 325, 330, 0.81],
    #                   [220, 230, 315, 340, 0.9]])

    img1 = copy.deepcopy(canvas)
    for item in boxes:
        x1, y1, x2, y2, score = item
        cv2.rectangle(img1, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)
        # cv2.putText(img1, str(score), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imwrite('cpu_nms_result_1.jpg', img1)

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
    cv2.imwrite('cpu_nms_result_2.jpg', img2)
    cv2.waitKey(0)
