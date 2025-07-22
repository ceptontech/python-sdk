# Cepton Python SDK2 wrapper
**CURRENTLY NOT IN ACTIVE DEVELOPMENT**

Provides the Cepton SDK version 2.x to a Python API

## Designed scopes
- Python3 only.
- Support python 3.7 or later due to the use of asyncio native coroutines
- Module itself is arch independent, but the FFI part loads from dynamic libraries

## Acquire source libraries
- Option 1: Copy from jenkins server eg `ct2/jenkins/sdk/`
- Option 2: Build source locally. See root `README.md`. In short:
```bash
mkdir build-{linux,win32,darwin}
cd build-{linux,win32,darwin}
cmake .. -DINSTALL_INPLACE=ON -DINPLACE_PYTHON=ON
cmake --build . --config Release
cmake --install . --config Release
```

## Install
```bash
pip install cepton-sdk2
```

## Usage
```
import cepton_sdk2
```
