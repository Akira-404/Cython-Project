import time

import numpy as np
import cv2
import copy


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


def cpu_soft_nms(boxes: np.ndarray,
                 sigma: float = 0.5,
                 Nt: float = 0.3,
                 threshold: float = 0.001,
                 method: int = 0) -> list:

    N = boxes.shape[0]
    for i in range(N):
        maxscore = boxes[i, 4]
        maxpos = i

        tx1 = boxes[i, 0]
        ty1 = boxes[i, 1]
        tx2 = boxes[i, 2]
        ty2 = boxes[i, 3]
        ts = boxes[i, 4]

        pos = i + 1
        # get max box
        while pos < N:
            if maxscore < boxes[pos, 4]:
                maxscore = boxes[pos, 4]
                maxpos = pos
            pos += 1

        # add max box as a detection
        boxes[i, 0] = boxes[maxpos, 0]
        boxes[i, 1] = boxes[maxpos, 1]
        boxes[i, 2] = boxes[maxpos, 2]
        boxes[i, 3] = boxes[maxpos, 3]
        boxes[i, 4] = boxes[maxpos, 4]

        # swap ith box with position fo max box
        boxes[maxpos, 0] = tx1
        boxes[maxpos, 1] = ty1
        boxes[maxpos, 2] = tx2
        boxes[maxpos, 3] = ty2
        boxes[maxpos, 4] = ts

        tx1 = boxes[i, 0]
        ty1 = boxes[i, 1]
        tx2 = boxes[i, 2]
        ty2 = boxes[i, 3]
        ts = boxes[i, 4]

        # NMS iterations ,not that N changes if detection boxes fall below threshold
        while pos < N:
            x1 = boxes[pos, 0]
            y1 = boxes[pos, 1]
            x2 = boxes[pos, 2]
            y2 = boxes[pos, 3]
            s = boxes[pos, 4]

            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            iw = (min(tx2, x2) - max(tx1, x1) + 1)
            if iw > 0:
                ih = (min(ty2, y2) - max(ty1, y1) + 1)
                if ih > 0:
                    ua = float((tx2 - tx1 + 1) * (ty2 - ty1 + 1) + area - iw * ih)
                    ov = iw * ih / ua  # iou between max box and detection box

                    if method == 1:  # linear
                        weight = (1 - ov) if ov > Nt else 1
                    elif method == 2:  # gaussian
                        weight = np.exp(-(ov * ov) / sigma)
                    else:  # original NMS
                        weight = 0 if ov > Nt else 1

                    boxes[pos, 4] = weight * boxes[pos, 4]
            # if box score falls below threshold, discard the box by swapping with last box
            # update N
            if boxes[pos, 4] < threshold:
                boxes[pos, 0] = boxes[N - 1, 0]
                boxes[pos, 1] = boxes[N - 1, 1]
                boxes[pos, 2] = boxes[N - 1, 2]
                boxes[pos, 3] = boxes[N - 1, 3]
                boxes[pos, 4] = boxes[N - 1, 4]
                N = N - 1
                pos = pos - 1

            pos = pos + 1

    keep = [i for i in range(N)]
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
    cv2.imwrite('imgs/cpu_soft_nms_result_1.jpg', img1)

    t1 = time.time()
    keep = cpu_soft_nms(boxes)
    t2 = time.time()
    print(f'time:{t2 - t1}s')

    img2 = copy.deepcopy(canvas)
    for item in keep:
        x1, y1, x2, y2, score = boxes[item]
        cv2.rectangle(img2, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)
        # cv2.putText(img2, str(score), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imwrite('imgs/cpu_soft_nms_result_2.jpg', img2)
    cv2.waitKey(0)
