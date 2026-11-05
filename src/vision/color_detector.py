"""Module for color classification in HSV and CIELAB spaces."""

import cv2
import numpy as np


class ColorClassifier:
    """Classifies an average BGR color into one of standard Rubik's cube colors."""

    Color_Names = {
        "U": "White (U)",
        "R": "Red (R)",
        "F": "Green (F)",
        "D": "Yellow (D)",
        "L": "Orange (L)",
        "B": "BLUE (B)",
    }

    DEFAULT_CENTERS_BGR = {
        "U": np.array([230, 230, 230], dtype=np.float32),
        "R": np.array([30, 30, 190], dtype=np.float32),
        "F": np.array([35, 160, 45], dtype=np.float32),
        "D": np.array([30, 210, 220], dtype=np.float32),
        "L": np.array([20, 110, 230], dtype=np.float32),
        "B": np.array([170, 70, 30], dtype=np.float32),
    }

    @staticmethod
    def _bgr_to_lab(bgr: np.ndarray) -> np.ndarray:
        """Convert a BGR pixel vector + CIELAB space."""
        mat = np.clip(bgr, 0, 255).astype(np.uint8).reshape((1, 1, 3))
        lab = cv2.cvtColor(mat, cv2.COLOR_BGR2LAB)
        return lab[0, 0].astype(np.float32)

    @staticmethod
    def _bgr_to_hsv(bgr: np.ndarray) -> tuple[float, float, float]:
        mat = np.clip(bgr, 0, 255).astype(np.uint8).reshape((1, 1, 3))
        hsv = cv2.cvtColor(mat, cv2.COLOR_BGR2HSV)[0, 0]
        return float(hsv[0]), float(hsv[1]), float(hsv[2])

    @staticmethod
    def _hue_distance(h1: float, h2: float) -> float:
        """Calculate circular distance between who hues on 0...179 scale."""
        diff = abs(h1 - h2)
        return min(diff, 180.0 - diff)

    @classmethod
    def classify_bgr(cls, bgr_pixel: np.ndarray) -> str:
        """Classify a BGR pixel using adaptive saturation and hue ranges."""
        h, s, v = cls._bgr_to_hsv(bgr_pixel)

        # White
        if (s < 75 and v > 50) or (s < 95 and v > 160):
            return "U"

        # Yellow
        if 21 <= h <= 43:
            return "D"

        # Green
        if 44 <= h <= 84:
            return "F"

        # Blue
        if 85 <= h <= 132:
            return "B"

        # Orange
        if 9 <= h <= 20 and s > 80:
            return "L"

        # Red
        if h < 9 or h >= 145:
            return "R"

        return "U" if v > 130 else "R"
