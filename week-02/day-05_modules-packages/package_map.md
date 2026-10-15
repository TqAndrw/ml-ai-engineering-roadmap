# Package Map

myapp
├── __init__.py
│   └── Re-exports public API: add, multiply
│
├── main.py
│   └── Application entry point
│
└── utils
    ├── __init__.py
    │   └── Re-exports utility functions
    │
    └── math_utils.py
        ├── add()
        └── multiply()

## Import Flow

main.py
→ myapp/__init__.py
→ myapp/utils/__init__.py
→ myapp/utils/math_utils.py

## Public API

External code can use:

```python
from myapp import add, multiply
