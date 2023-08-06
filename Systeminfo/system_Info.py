import platform
import psutil
import socket
import cpuinfo
import GPUtil


class SystemInfo:
    def get_system_info(self):
        system = platform.uname()
        return {
            "System": f"{system.system} {system.release}",
            "Node Name": socket.gethostname(),
            "Machine": system.machine,
            "Processor": system.processor,
            "Total RAM": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
            "CPU Usage": f"{psutil.cpu_percent(interval=1):.2f}%",
            "Available CPU Cores": psutil.cpu_count(logical=False)
        }

    def get_cpu_info(self):
        info = cpuinfo.get_cpu_info()
        return {
            "CPU": info['brand_raw'],
            "Architecture": info['arch']
        }

    def get_gpu_info(self):
        try:
            gpus = GPUtil.getGPUs()
            gpu_info = []
            for i, gpu in enumerate(gpus):
                gpu_info.append({
                    "GPU": f"{gpu.name}",
                    "Memory Total": f"{gpu.memoryTotal / 1024:.2f} GB",
                    "Memory Free": f"{gpu.memoryFree / 1024:.2f} GB",
                    "Memory Used": f"{gpu.memoryUsed / 1024:.2f} GB",
                    "GPU Load": f"{gpu.load * 100:.2f}%",
                    "GPU Temperature": f"{gpu.temperature:.2f} °C"
                })
            return gpu_info
        except Exception as e:
            return f"GPU information not available: {e}"

    def get_disk_info(self):
        partitions = psutil.disk_partitions()
        disk_info = []
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append({
                    "Device": partition.device,
                    "Mount Point": partition.mountpoint,
                    "Total Space": f"{usage.total / (1024 ** 3):.2f} GB",
                    "Free Space": f"{usage.free / (1024 ** 3):.2f} GB",
                    "Used Space": f"{usage.used / (1024 ** 3):.2f} GB",
                    "Disk Usage": f"{usage.percent:.2f}%"
                })
            except Exception as e:
                disk_info.append({"Error": str(e)})
        return disk_info

    def get_all_info(self):
        all_info = {
            "System Information": self.get_system_info(),
            "CPU Information": self.get_cpu_info(),
            "GPU Information": self.get_gpu_info(),
            "Disk Information": self.get_disk_info()
        }
        return all_info


if __name__ == "__main__":
    system_info = SystemInfo()
    all_info = system_info.get_all_info()

    for category, info in all_info.items():
        print(f"\n===== {category} =====")
        if isinstance(info, list):
            for item in info:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("-------")
        else:
            for key, value in info.items():
                print(f"{key}: {value}")
