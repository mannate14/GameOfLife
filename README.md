<<<<<<< HEAD
# Hexagonal Game of Life

A Python implementation of Conway's Game of Life on a hexagonal grid, extended with custom rules for aging, random resurrection, and no-repeat death causes.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Controls](#controls)
6. [Theory](#theory)

   * [Hexagonal Cellular Automaton](#hexagonal-cellular-automaton)
   * [Custom Rules](#custom-rules)
7. [Visualization](#visualization)
8. [File Structure](#file-structure)
9. [Contributing](#contributing)
10. [License](#license)

---

## Introduction

This project implements a variant of Conway's Game of Life on a **hexagonal grid**, adding mechanics for cell aging, periodic random revivals, and preventing consecutive deaths for the same cause. The simulation is built with **Pygame** for rendering and **NumPy** for efficient array operations.

## Prerequisites

* Python 3.8 or higher
* NumPy == 2.2.5
* Pygame == 2.6.1

Ensure you have the required packages installed. See [Installation](#installation).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hex-life
   cd hex-life
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
python hex_life.py
```

* **Draw** initial live cells by **clicking and dragging** with the mouse.
* Press **Space** to **start/pause** the simulation.
* Generated frames will be saved as `output1.png`, `output2.png`, etc.

## Controls

* **Left Mouse Button**: Toggle cells between alive/dead during the initial setup phase.
* **Space Bar**: Start or pause the simulation.
* **Close Window**: Exit the simulation.

## Theory

### Hexagonal Cellular Automaton

Unlike the standard square-grid Life, each cell here is a **hexagon** with six neighbors. The neighbor counting and placement use trigonometry to draw and detect hexagonal tiles.

### Custom Rules

1. **Underpopulation**

   * A live cell with fewer than 2 neighbors dies (underpopulation), subject to Rule 7.

2. **Overpopulation**

   * A live cell with more than 3 neighbors dies (overpopulation), subject to Rule 7.

3. **Survival**

   * A live cell with 2 or 3 neighbors survives.

4. **Reproduction**

   * A dead cell with exactly 3 neighbors becomes alive.

5. **Revival by Aging**

   * A dead cell that has been dead for exactly 6 generations becomes alive regardless of neighbor count.

6. **Random Resurrection**

   * Every 4th generation, one random dead cell is resurrected.

7. **No Repeat Death**

   * A cell’s two successive death events may not share the same cause (underpopulation vs. overpopulation), regardless of how many generations—or births—occur in between.

## Visualization

Below are sample frames from the simulation:

**Generation 7:**

![Gen7](images/output7.png)

**Generation 8:**

![Gen8](images/output8.png)

![](/images/rules-diagram.png)

*(Place additional illustrative images in the `images/` folder.)*

## File Structure

```
hex-life/
├── hex_life.py       # Main simulation script
├── requirements.txt  # Pinned dependencies
├── README.md         # Project documentation
└── images/           # Sample frames and diagrams
    ├── output7.png
    ├── output8.png
    └── rules-diagram.png
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

=======
# Hexagonal Game of Life

A Python implementation of Conway's Game of Life on a hexagonal grid, extended with custom rules for aging, random resurrection, and no-repeat death causes.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Controls](#controls)
6. [Theory](#theory)

   * [Hexagonal Cellular Automaton](#hexagonal-cellular-automaton)
   * [Custom Rules](#custom-rules)
7. [Visualization](#visualization)
8. [File Structure](#file-structure)
9. [Contributing](#contributing)
10. [License](#license)

---

## Introduction

This project implements a variant of Conway's Game of Life on a **hexagonal grid**, adding mechanics for cell aging, periodic random revivals, and preventing consecutive deaths for the same cause. The simulation is built with **Pygame** for rendering and **NumPy** for efficient array operations.

## Prerequisites

* Python 3.8 or higher
* NumPy == 2.2.5
* Pygame == 2.6.1

Ensure you have the required packages installed. See [Installation](#installation).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hex-life
   cd hex-life
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
python hex_life.py
```

* **Draw** initial live cells by **clicking and dragging** with the mouse.
* Press **Space** to **start/pause** the simulation.
* Generated frames will be saved as `output1.png`, `output2.png`, etc.

## Controls

* **Left Mouse Button**: Toggle cells between alive/dead during the initial setup phase.
* **Space Bar**: Start or pause the simulation.
* **Close Window**: Exit the simulation.

## Theory

### Hexagonal Cellular Automaton

Unlike the standard square-grid Life, each cell here is a **hexagon** with six neighbors. The neighbor counting and placement use trigonometry to draw and detect hexagonal tiles.

### Custom Rules

1. **Underpopulation**

   * A live cell with fewer than 2 neighbors dies (underpopulation), subject to Rule 7.

2. **Overpopulation**

   * A live cell with more than 3 neighbors dies (overpopulation), subject to Rule 7.

3. **Survival**

   * A live cell with 2 or 3 neighbors survives.

4. **Reproduction**

   * A dead cell with exactly 3 neighbors becomes alive.

5. **Revival by Aging**

   * A dead cell that has been dead for exactly 6 generations becomes alive regardless of neighbor count.

6. **Random Resurrection**

   * Every 4th generation, one random dead cell is resurrected.

7. **No Repeat Death**

   * A cell’s two successive death events may not share the same cause (underpopulation vs. overpopulation), regardless of how many generations—or births—occur in between.

## Visualization

Below are sample frames from the simulation:

**Generation 7:**

![Gen7](images/output7.png)

**Generation 8:**

![Gen8](images/output8.png)

![](/images/rules-diagram.png)

*(Place additional illustrative images in the `images/` folder.)*

## File Structure

```
hex-life/
├── hex_life.py       # Main simulation script
├── requirements.txt  # Pinned dependencies
├── README.md         # Project documentation
└── images/           # Sample frames and diagrams
    ├── output7.png
    ├── output8.png
    └── rules-diagram.png
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

>>>>>>> 4210afd6a713a21ba395c6f7a1b846cd70240fac
