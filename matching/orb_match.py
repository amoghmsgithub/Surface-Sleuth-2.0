import cv2

def orb_match(img1, img2):
    orb = cv2.ORB_create(nfeatures=2000)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return 0

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    score = len(matches) / min(len(kp1), len(kp2)) * 100
    return score