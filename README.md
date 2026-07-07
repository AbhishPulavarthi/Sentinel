# Sentinel

Sentinel is a Python-based digital forensics and file analysis toolkit built as a long-term cybersecurity learning project.

The goal of this project is to gradually develop a practical toolkit for inspecting files, verifying file integrity, extracting metadata, and exploring concepts used in digital forensics and cybersecurity.

Each version introduces new features while following good software engineering practices such as version control, documentation, and clean code organization.

---

## Current Features (v0.2)

- Graphical file selection using Tkinter
- Displays:
  - File name
  - File extension
  - File name without extension
  - File size (Bytes, KB, MB)
- Generates cryptographic hashes:
  - SHA-256
  - MD5
- Handles file selection cancellation gracefully

---

## Technologies Used

- Python 3
- pathlib
- tkinter
- hashlib

---

## Project Structure

```
Sentinel/
├── main.py
├── README.md
└── .gitignore
```

---

## Version History

### v0.1
- Added graphical file picker
- Displayed file information
- Displayed file size

### v0.2
- Added SHA-256 hashing
- Added MD5 hashing
- Improved console output
- Added project documentation

---

## Future Plans

- Extract file metadata
- Analyze file timestamps
- Scan directories
- Support additional hashing algorithms
- Compare files using hashes
- Generate forensic reports
- Improve the user interface

---

## Author

**Abhish Pulavarthi**

Computer Science Engineering (Cybersecurity)

---

> Sentinel is an actively developed project, and new features will be added through incremental version updates.