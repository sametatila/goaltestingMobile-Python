import subprocess
import re

def discover_bluetooth_devices():
    try:
        # PowerShell komutunu çalıştır
        result = subprocess.run(
            ["powershell", "-Command", "Get-PnpDevice -Class Bluetooth | Format-Table -Property Name, InstanceId"],
            capture_output=True,
            text=True
        )

        devices_output = result.stdout
        print(devices_output)

        # MAC adreslerini ayıklamak için düzenli ifade kullanma
        device_lines = devices_output.splitlines()
        devices = []
        for line in device_lines:
            match = re.search(r'(\w+)\s+(BTHENUM\\DEV_([\w]+)\\)', line)
            if match:
                name = match.group(1).strip()
                instance_id = match.group(3)
                mac_address = ':'.join(instance_id[i:i+2] for i in range(0, len(instance_id), 2))
                devices.append((name, mac_address))

        # Bulunan cihazları listeleme
        for name, mac_address in devices:
            print(f"Adı: {name}, MAC Adresi: {mac_address}")

    except subprocess.CalledProcessError as e:
        print(f"Tarama sırasında bir hata oluştu: {e}")

if __name__ == "__main__":
    discover_bluetooth_devices()
