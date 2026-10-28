# Rubik's Cube Solver 

An interactive Computer Vision pipeline and solver for the Rubik's Cube. 
The system detects the state of a physical Rubik's cube using a webcam feed, validates the permutation, and computes near-optimal solutions in standard Singmaster notation (`U, D, R, L, F, B`) using Kociemba's Two-Phase Algorithm.

## Features
- **Real-Time Detection:** Color classification and state mapping via OpenCV.
- **State Validation:** Full permutation, parity, and orientation integrity checks.
- **Near-Optimal Solving:** Under 50ms computation time using the Two-Phase Algorithm ($\le 21$ moves).
- **Extensible Architecture:** Decoupled CV, engine, and interface layers.

## Tech Stack
- **Language:** Python 3.11+
- **Vision:** OpenCV, NumPy
- **Algorithm:** Kociemba Two-Phase Algorithm
- **Testing:** PyTest
- **CLI/Display:** Rich

## Getting Started

### Prerequisites
- Linux / macOS with webcam support (`v4l2` on Linux)
- Python 3.11+

### Installation
```bash
git clone [https://github.com/Senk0re/rubiks-solver.git](https://github.com/Senk0re/rubiks-solver.git)
cd rubiks-solver

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
