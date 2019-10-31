import cv2
import sys
import utils


if __name__ == '__main__':

    if sys.argv[1] and sys.argv[2]:

        image1 = cv2.imread(sys.argv[1])
        image2 = cv2.imread(sys.argv[2])
        stitch_match = utils.FindKeyPointsAndMatching()
        kp1, kp2 = stitch_match.get_key_points(img1=image1, img2=image2)
        homo_matrix = stitch_match.match(kp1, kp2)
        stitch_merge = utils.PasteTwoImages()
        merge_image = stitch_merge(image1, image2, homo_matrix)
        cv2.namedWindow('output', 0)
        cv2.imshow('output', merge_image)
        if cv2.waitKey() == 27:
            cv2.destroyAllWindows()
        cv2.imwrite(sys.argv[1][0] + '-output.JPG', merge_image)
        print('\n=======>Output saved!')
    else:
        print('input images location!')
