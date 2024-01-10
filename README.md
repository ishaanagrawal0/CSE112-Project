# CSE112-Project: Assembler Clone

## Overview
This repository contains the group project undertaken for the CSE112 Course at IIIT-D. The goal of this project was to create an assembler clone capable of converting assembly instructions into machine code. The project was divided among team members Aditya Gupta, Ishaan Agrawal, Debjit Banerji, and Himang Chandra Garg.

## Contributors
- Aditya Gupta
- Ishaan Agrawal
- Debjit Banerji
- Himang Chandra Garg

## Project Structure
### Functionality
- The assembler reads assembly instructions from a text file (`f1` globally defined in the code) and generates output into another file (`f2` globally).
- Different functions such as `MoveImmediate`, `MoveRegister`, `Addition`, `Subtraction`, etc., have been implemented to handle the conversion of assembly instructions into corresponding machine code. Each function is tailored to manage the machine code outputs for their respective commands.
- The assembler also handles flag adjustments after every statement, as specified in the requirements. Additionally, it supports 8 registers as provided in the question.
- Error handling has been implemented comprehensively within the codebase, ensuring that errors are identified and addressed effectively.
- Careful consideration has been given to whitespace handling within the input file to maintain accuracy during the conversion process.
- Utilization of separate loops aids in identifying and managing all labels present in the assembly code, facilitating error handling and ensuring smoother program execution.

## Usage
1. **Input File:** The assembly instructions are provided in a text file named `f1`.
2. **Output File:** The generated machine code is stored in the file `f2`.

## Implementation Details
The assembler functions by analyzing the assembly instructions provided in `f1`, using a set of predefined functions to convert these instructions into machine code. The program's design adheres to the provided ISA, ensuring accurate conversion and flag adjustments. The error handling mechanisms and whitespace considerations contribute to the robustness of the assembler, enabling reliable output generation.

## How to Run
[Include specific instructions or commands on how to compile/run the assembler, if applicable.]

## Future Enhancements
Potential improvements and enhancements that could be incorporated in future iterations of the assembler could include:
- Optimizations for efficiency in handling larger assembly code files.
- Enhanced error reporting and debugging functionalities.
- Expansion of supported ISA instructions for broader compatibility.

