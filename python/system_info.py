import psutil
import platform

def get_system_info():
    print("=" * 50)
    print("        SYSTEM RESOURCE MONITOR")
    print("=" * 50)

    # RAM Info
    ram = psutil.virtual_memory()
    print("\n📦 RAM INFORMATION:")
    print(f"  Total     : {ram.total / (1024**3):.2f} GB")
    print(f"  Used      : {ram.used / (1024**3):.2f} GB")
    print(f"  Available : {ram.available / (1024**3):.2f} GB")
    print(f"  Usage     : {ram.percent}%")

    # Storage Info
    print("\n💾 STORAGE INFORMATION:")
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Drive     : {partition.device}")
            print(f"  Total     : {usage.total / (1024**3):.2f} GB")
            print(f"  Used      : {usage.used / (1024**3):.2f} GB")
            print(f"  Free      : {usage.free / (1024**3):.2f} GB")
            print(f"  Usage     : {usage.percent}%")
            print()
        except PermissionError:
            continue

    # CPU Info
    print("⚙️  CPU / PROCESSOR INFORMATION:")
    print(f"  Processor : {platform.processor()}")
    print(f"  Cores     : {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
    print(f"  Load      : {psutil.cpu_percent(interval=1)}%")

    per_core = psutil.cpu_percent(interval=1, percpu=True)
    for i, load in enumerate(per_core):
        print(f"  Core {i+1:<4} : {load}%")

    print("=" * 50)

if __name__ == "__main__":
    get_system_info()