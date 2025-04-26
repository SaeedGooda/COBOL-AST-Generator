# COBOL AST Generator

A Python tool to generate an Abstract Syntax Tree (AST) from COBOL `.cbl` files using ANTLR4. It removes comments by default (optional) and saves the AST as a text file in the same directory. Works on Windows, Linux, and macOS.

## Features
- Parses COBOL `.cbl` files
- Removes full-line (`*` in column 7), inline (` *> `), and metadata comments (e.g., `MO1624* ... *`)
- Saves AST as `<input_filename> AST.txt`
- Simple command-line interface

## Prerequisites
- Python 3.6+ ([python.org](https://www.python.org/downloads/))
- A `.cbl` file (e.g., `ICMM3DDC.cbl`)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SaeedGooda/COBOL-AST-Generator.git
   cd COBOL-AST-Generator
   ```

2. **Install Python**:
   - **Windows**: Download and install Python from [python.org](https://www.python.org/downloads/windows/). Check "Add Python to PATH" during setup. Verify: `python --version`
   - **Linux**: Install via package manager:
     ```bash
     sudo apt-get install python3 python3-pip  # Ubuntu/Debian
     sudo yum install python3 python3-pip      # CentOS/RHEL
     ```
     Verify: `python3 --version`
   - **macOS**: Install via Homebrew (if not pre-installed):
     ```bash
     brew install python
     ```
     Verify: `python3 --version`

3. **Run Requirements and Use**:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
     This installs `antlr4-python3-runtime`.
   - The repository includes `CobolLexer.py` and `CobolParser.py`.
   - Proceed to [Usage](#usage) to run the tool.

## Usage
Run the script to generate an AST:
```bash
python app.py <input_file.cbl> [--comments enable|disable]
```
- `<input_file.cbl>`: Path to your COBOL file
- `--comments disable`: Keeps comments (default)
- `--comments enable`: Removes comments

**Output**:
- Saves AST to `<input_filename> AST.txt` in the same directory
- Shows: `AST generated successfully: <output_file>`

**Examples**:
- Remove comments: `python app.py HelloWorld.cbl`
- Keep comments: `python app.py HelloWorld.cbl --comments enable`

## Platform Notes
- **Windows**: Use `python` (e.g., `python app.py HelloWorld.cbl`)
- **Linux/macOS**: Use `python3` (e.g., `python3 app.py HelloWorld.cbl`)

## Contact
- **Email**: [saeedgooda219@gmail.com](mailto:saeedgooda219@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/saeed-gooda-bbaa091a3/](https://www.linkedin.com/in/saeed-gooda-bbaa091a3/)