# Hexagonal Game of Life

A Python implementation of Conway's Game of Life on a hexagonal grid, extended with custom rules for aging, random resurrection and no-repeat death causes.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Theory](#theory)
5. [Visualization](#visualization)
6. [File Structure](#file-structure)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

This project implements a variant of Conway's Game of Life on a **hexagonal grid**, adding mechanics for cell aging, periodic random revivals, and preventing consecutive deaths for the same cause. The simulation is built with **Pygame** for rendering and **NumPy** for efficient array operations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/its-adityagoyal/Game-of-Life-HexagonalGrid.git
   cd Game-of-Life-HexagonalGrid
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the simulation:

```bash
python main.py
```

* **Draw** initial live cells by **clicking and dragging** with the mouse.
* Press **S** to **Start** the simulation and **E** to **Exit**.
* Generated frames will be saved as `output1.png`, `output2.png`, etc.

## Theory

### Hexagonal Grid to Array Mapping

In our implementation, each hexagon in the grid is mapped to a 2D array index by projecting its center onto Cartesian coordinates. By computing the row and column offsets (using the hexagon’s radius and the √3/2 vertical spacing), we can translate any hex cell into a (row, col) pair in a regular 2D array.

### Neighbour Positioning

Neighbours of a hex cell “shift” differently depending on whether the cell sits in an even‑numbered or odd‑numbered row. In the illustration below, you can see:

**Even rows**: neighbours on one side are pushed slightly right  
**Odd rows**: neighbours on the opposite side are pushed slightly left  

![Hex Grid to Array Mapping](images/hex_to_array_mapping.png)

### Rules

All of the custom rules for this hexagonal automaton are defined in [rules.txt](rules.txt)

## Visualization

Below are sample frames from the simulation:

<p float="left">
  <img src="Output/output5.png" alt="Generation 2" width="45%" />
  <img src="Output/output6.png" alt="Generation 3" width="45%" />
</p>

*(Place additional illustrative images in the `Output/` folder.)*

## File Structure

```
Game-of-Life-HexagonalGrid/
├── main.py           # Main simulation script
├── requirements.txt  # Pinned dependencies
├── rules.txt         # Custom rules 
├── README.md         # Project documentation
├── Output/           # Sample frames and diagrams
|   ├── output1.png
|   ├── output2.png
|   .
└── images/           # Images for theory purpose
    ├── hex_to_array_mapping.png
```

## Contributions

Thank you for your interest in improving **Game‑of‑Life‑HexagonalGrid**! To contribute:

1. Fork the repository
2. Create a new branch
   ```bash
   git checkout -b feature/YourFeatureName
   ```
4. Make your changes and commit
5. Push to your fork
   ```bash
   git push origin feature/YourFeatureName
   ```
7. Open a Pull Request against main in this repo

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

