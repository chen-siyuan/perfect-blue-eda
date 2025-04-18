import pathlib

import cv2 as cv

from video import Video


def main():
    base_dir = pathlib.Path(__file__).parent
    input_dir = base_dir / "input"

    video = Video(input_dir / "anime.mp4")

    frame = video[117538 // 2]
    cv.imshow("frame", frame)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
