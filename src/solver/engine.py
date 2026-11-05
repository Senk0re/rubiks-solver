"""Engine module to interface with the Kociemba two-phase algorithm."""

from dataclasses import dataclass
from typing import Optional
import kociemba


@dataclass
class SolutionResult:
    is_valid: bool
    solution: Optional[str] = None
    error_message: Optional[str] = None


class CubeSolver:
    """Handles cube string validation and solution generation."""

    REQUIRED_LENGTH = 54
    FACES = ("U", "R", "F", "D", "L", "B")
    SOLVED_STATE = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

    @classmethod
    def validate_cube_string(cls, cube_str) -> tuple[bool, Optional[str]]:
        """Validate string length and ensure exaclty 9 stickers per color."""
        if len(cube_str) != cls.REQUIRED_LENGTH:
            return (
                False,
                f"Expected {cls.REQUIRED_LENGTH} characters, got {len(cube_str)}.",
            )

        for face in cls.FACES:
            count = cube_str.count(face)
            if count != 9:
                return (
                    False,
                    f"Face '{face}' must appear exactly 9 times, found {count}.",
                )

        return True, None

    @classmethod
    def solve(cls, cube_str: str) -> SolutionResult:
        """Solve cube state string using Kociemba algorithm."""
        is_valid, error = cls.validate_cube_string(cube_str)
        if not is_valid:
            return SolutionResult(is_valid=False, error_message=error)

        if cube_str == cls.SOLVED_STATE:
            return SolutionResult(is_valid=True, solution="")

        try:
            raw_solution = kociemba.solve(cube_str)
            return SolutionResult(is_valid=True, solution=raw_solution)
        except ValueError as err:
            return SolutionResult(
                is_valid=False, error_message=f"Impossible state: {str(err)}"
            )
