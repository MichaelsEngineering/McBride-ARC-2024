# ARC Prize Program

The ARC Prize Program is a comprehensive artificial intelligence system designed to solve novel reasoning tasks in the Abstraction and Reasoning Corpus (ARC) challenge. The approach I am building employs a 3-D pyramid-inspired, multi-faced architecture that combines boolean algebra, language models, and visual pattern recognition to tackle previously unseen problems.

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development Status](#development-status)
- [Contributing](#contributing)
- [License](#license)

## Features

- Multi-faced AI architecture for diverse problem-solving approaches
- Boolean algebra operations for logical pattern recognition
- LLM integration for natural language understanding of patterns
- GPU optimization for dual T4 setups
- Automated test case generation
- Confidence-based solution selection
- Extensible face system for future enhancements

## Architecture

### Task Feature Analyzer & Router

- Grid characteristic analysis
- Pattern type identification
- Multi-face routing capabilities
- Learning-based routing mechanism
- Task complexity assessment

### Boolean Algebra Face

- Truth table analysis for 2x2 patterns
- Multiple boolean operators (AND, OR, XOR, NAND, NOR, NOT, XNOR)
- Pattern caching system
- Confidence scoring
- Learning rate adaptation
- Dynamic rule application

### LLM Face

- LLaMA 3B model integration
- Optimized GPU utilization
- Pattern description generation
- Rule extraction from demonstrations
- Memory-efficient processing

### DAAG Face (Diffusion-Augmented Abstract Generation)

- Visual pattern transformation
- Experience augmentation
- Synthetic data generation
- Pattern complexity handling
- Diffusion-based solution generation

### Solution Aggregator & Selector

- Multi-face solution combination
- Confidence-based ranking
- Ensemble methods
- Cross-validation
- Multiple attempt generation

## Installation

1. Clone the repository:

   ```bash
   gh repo clone yourusername/arc-prize-program
   cd arc-prize-program
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Download required models:
   ```bash
   python scripts/download_models.py
   ```

## Usage

### Running the System

1. Process a single task:

   ```python
   from arc_processor import ARCProcessor

   processor = ARCProcessor()
   results = processor.process_single_task(task_data)
   ```

2. Process multiple tasks:
   ```python
   results = processor.process_tasks(tasks)
   processor.save_submission(results, 'submission.json')
   ```

### Running Tests

```bash
python -m unittest tests/test_boolean_face.py
python -m unittest tests/test_llm_face.py
python -m unittest tests/test_integration.py
```

## Project Structure

```text
MCBRIDE-ARC-2024/
├── src/
│   ├── faces/
│   │   ├── boolean_face.py
│   │   ├── llm_face.py
│   │   └── daag_face.py
│   ├── core/
│   │   ├── processor.py
│   │   ├── router.py
│   │   └── aggregator.py
│   └── utils/
│       ├── grid_ops.py
│       └── visualization.py
├── tests/
│   ├── test_boolean_face.py
│   ├── test_llm_face.py
│   └── test_integration.py
├── notebooks/
│   └── development.ipynb
├── data/
│   ├── training/
│   └── evaluation/
├── configs/
│   └── model_config.yaml
├── README.md
├── requirements.txt
└── LICENSE
```

## Development Status

### Currently Implemented

- Basic data loading and JSON handling
- Boolean operations using numpy
- LLaMA 3B integration
- Truth table analysis
- Basic submission formatting
- GPU optimization
- Logging system

### Under Development

- Program synthesis capabilities
- Pattern recognition system
- Router implementation
- DAAG face development
- Solution aggregation enhancement
- Cross-face validation

### Planned Features

- Test-time adaptation
- Advanced program synthesis
- Enhanced confidence scoring
- Complex ensemble methods
- Improved face integration

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Write unit tests for new features
- Follow PEP 8 style guidelines
- Document new functionality
- Maintain GPU optimization
- Consider memory efficiency

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- François Chollet for the ARC challenge
- Kaggle for hosting the competition
- LLaMA team for the base model
- The open-source AI community
