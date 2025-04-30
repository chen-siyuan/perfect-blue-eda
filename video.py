import cv2 as cv


class Video:
    """Encapsulate video file as an array of frames."""

    def __init__(self, path, *, verbose=False):
        self._cap = cv.VideoCapture(path)

        if not self._cap.isOpened():
            raise ValueError("Invalid path for video capture")

        self.num_frames = int(self._cap.get(cv.CAP_PROP_FRAME_COUNT))
        self.height = int(self._cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        self.width = int(self._cap.get(cv.CAP_PROP_FRAME_WIDTH))

        self.fps = self._cap.get(cv.CAP_PROP_FPS)
        self.num_secs = self.num_frames / self.fps

        if verbose:
            print(f"num_frames = {self.num_frames}")
            print(f"height = {self.height}")
            print(f"width = {self.width}")
            print(f"fps = {self.fps:.4f}")
            print(f"num_secs = {self.num_secs:.4f}")
            print(f"num_mins = {self.num_secs / 60:.4f}")

    def __getitem__(self, idx):
        if not 0 <= idx < self.num_frames:
            raise ValueError("Invalid frame index")

        self._cap.set(cv.CAP_PROP_POS_FRAMES, idx)

        ret, frame = self._cap.read()

        if not ret:
            raise RuntimeError("Invalid frame read")

        return frame

    def __del__(self):
        self._cap.release()
