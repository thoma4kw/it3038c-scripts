pip install psutil

import psutil

def get_free_space(path='/'):
    try:
        disk_usage = psutil.disk_usage(path)
        return disk_usage.free
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    path = '/'  # You can specify a different path if needed, e.g., '/home' for your home directory
    free_space_bytes = get_free_space(path)
    free_space_gb = round(free_space_bytes / (1024 ** 3), 2)  # Convert bytes to gigabytes

    if isinstance(free_space_bytes, int):
        print(f"Free hard drive space on '{path}': {free_space_gb} GB")
    else:
        print(f"Failed to retrieve free space: {free_space_bytes}")
