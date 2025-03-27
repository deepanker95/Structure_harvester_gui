# HarvestEase GUI

![HarvestEase GUI](https://github.com/deepanker95/Structure_harvester_gui/blob/main/Screenshot%202025-03-27%20174420.png)

## Overview
**HarvestEase GUI** is a standalone, cross-platform graphical user interface designed as an offline alternative to **STRUCTURE HARVESTER**. This tool automates the parsing, visualization, and interpretation of STRUCTURE output files, implementing the **Evanno method** for determining the optimal number of genetic clusters (*K*).

## Features
- **Offline functionality** – No internet required, works on Windows, macOS, and Linux.
- **User-friendly GUI** – No coding required, drag-and-drop support.
- **Batch processing** – Analyze multiple STRUCTURE output files simultaneously.
- **Real-time visualization** – Automatically generates likelihood and ΔK plots.
- **One-click export** – Compatible with CLUMPP, DISTRUCT, and other downstream tools.
- **Cross-platform support** – Bundled as standalone executables via PyInstaller.

## Installation
### Windows
1. Download the latest Windows executable from [Google Drive](https://drive.google.com/file/d/1f1zVreuQZfxuWebvic5MqiiiDFqrDQaR/view?usp=sharing).
2. Extract the ZIP file and double-click `HarvestEase.exe`.

### macOS
1. Download the macOS `.dmg` file from [Google Drive](https://drive.google.com/file/d/1qeyeX_UsghTd8a1HzCeVX7DLaLJTKPTj/view?usp=sharing).
2. Open the `.dmg` and drag `HarvestEase` to the Applications folder.

### Linux
1. Download the Linux AppImage from [Google Drive](https://drive.google.com/file/d/1JId-5rqwZ2wgApoht3iyB1KUQDUbMKTj/view?usp=sharing).
2. Run `chmod +x HarvestEase.AppImage` and execute.

## Usage
1. Launch the application.
2. Load your STRUCTURE output files (`.log`, `.out` formats supported).
3. Select *K* range for Evanno method calculations.
4. View plots and export processed results.

## License
```
Copyright (c) 2025, Deepanker Das, Dr. Devojit Sarma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contributors
- **Deepanker Das** (Developer)
- **Dr. Devojit Sarma** (Advisor)

## Contact
For issues, suggestions, or contributions, please open an issue on [GitHub](https://github.com/deepanker95/Structure_harvester_gui) or contact [deepankernireh@gmail.com].
