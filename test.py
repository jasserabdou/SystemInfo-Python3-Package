import unittest
from Systeminfo.system_Info import SystemInfo


class TestSystemInfo(unittest.TestCase):
    def setUp(self):
        self.system_info = SystemInfo()

    def test_get_system_info(self):
        system_info = self.system_info.get_system_info()
        self.assertIsInstance(system_info, dict)
        self.assertIn("System", system_info)
        self.assertIn("Node Name", system_info)
        self.assertIn("Machine", system_info)
        self.assertIn("Processor", system_info)
        self.assertIn("Total RAM", system_info)
        self.assertIn("CPU Usage", system_info)
        self.assertIn("Available CPU Cores", system_info)

    def test_get_cpu_info(self):
        cpu_info = self.system_info.get_cpu_info()
        self.assertIsInstance(cpu_info, dict)
        self.assertIn("CPU", cpu_info)
        self.assertIn("Architecture", cpu_info)

    def test_get_gpu_info(self):
        gpu_info = self.system_info.get_gpu_info()
        if isinstance(gpu_info, list):
            for gpu in gpu_info:
                self.assertIsInstance(gpu, dict)
                self.assertIn("GPU", gpu)
                self.assertIn("Memory Total", gpu)
                self.assertIn("Memory Free", gpu)
                self.assertIn("Memory Used", gpu)
                self.assertIn("GPU Load", gpu)
                self.assertIn("GPU Temperature", gpu)
        else:
            self.assertIsInstance(gpu_info, str)

    def test_get_disk_info(self):
        disk_info = self.system_info.get_disk_info()
        for disk in disk_info:
            self.assertIsInstance(disk, dict)
            self.assertIn("Device", disk)
            self.assertIn("Mount Point", disk)
            self.assertIn("Total Space", disk)
            self.assertIn("Free Space", disk)
            self.assertIn("Used Space", disk)
            self.assertIn("Disk Usage", disk)

    def test_get_all_info(self):
        all_info = self.system_info.get_all_info()
        self.assertIsInstance(all_info, dict)
        self.assertIn("System Information", all_info)
        self.assertIn("CPU Information", all_info)
        self.assertIn("GPU Information", all_info)
        self.assertIn("Disk Information", all_info)


if __name__ == "__main__":
    unittest.main()
