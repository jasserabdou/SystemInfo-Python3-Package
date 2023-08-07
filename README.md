# SystemInfo Package

This Python package provides a simple and easy-to-use way to gather system information, including details about the operating system, CPU, GPU (if available), and disk usage. The package uses popular Python libraries such as `platform`, `psutil`, `socket`, `cpuinfo`, and `GPUtil` to retrieve and present the system data.

## Installation
```bash
pip install systeminfo-python3
```

## Usage

To use the package, you can follow these steps:

1. Import the `SystemInfo` class from the package:

```python
from Systeminfo.system_Info import SystemInfo
```

2. Create an instance of the `SystemInfo` class:

```python
system_info = SystemInfo()
```

3. Get all the information using the `get_all_info()` method:

```python
all_info = system_info.get_all_info()
```

4. Print the system information:

```python
print("===== System Information =====")
for key, value in all_info["System Information"].items():
    print(f"{key}: {value}")
```

5. Print the CPU information:

```python
print("\n===== CPU Information =====")
for key, value in all_info["CPU Information"].items():
    print(f"{key}: {value}")
```

6. Print the GPU information if available:

```python
if "GPU Information" in all_info:
    print("\n===== GPU Information =====")
    for gpu_info in all_info["GPU Information"]:
        for key, value in gpu_info.items():
            print(f"{key}: {value}")
```

7. Print the disk information:

```python
print("\n===== Disk Information =====")
for disk_info in all_info["Disk Information"]:
    for key, value in disk_info.items():
        print(f"{key}: {value}")
    print("-------")
```

### Example

Here's an example of how to use the package to retrieve and print system information:

```python
from Systeminfo.system_Info import SystemInfo

# Create an instance of the SystemInfo class
system_info = SystemInfo()

# Get all the information using the SystemInfo class
all_info = system_info.get_all_info()

# Print the system information
print("===== System Information =====")
for key, value in all_info["System Information"].items():
    print(f"{key}: {value}")

# Print the CPU information
print("\n===== CPU Information =====")
for key, value in all_info["CPU Information"].items():
    print(f"{key}: {value}")

# Print the GPU information if available
if "GPU Information" in all_info:
    print("\n===== GPU Information =====")
    for gpu_info in all_info["GPU Information"]:
        for key, value in gpu_info.items():
            print(f"{key}: {value}")

# Print the disk information
print("\n===== Disk Information =====")
for disk_info in all_info["Disk Information"]:
    for key, value in disk_info.items():
        print(f"{key}: {value}")
    print("-------")
```

## Dependencies

The package relies on the following external Python libraries:

- `platform`: Provides access to the underlying platform's identifying data.
- `psutil`: Offers system and process-related information.
- `socket`: Provides access to network communication capabilities.
- `cpuinfo`: Provides information about the CPU (Central Processing Unit).
- `GPUtil`: Allows retrieving GPU (Graphics Processing Unit) information (optional).

## Compatibility

The package is compatible with Python 3.9 and above.

## License

This package is released under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.
