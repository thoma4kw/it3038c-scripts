import os
import psutil

def get_disk_info(path='/'):
    try:
        disk_usage = psutil.disk_usage(path)
        return disk_usage.total, disk_usage.used, disk_usage.free, disk_usage.percent
    except Exception as e:
        return f"Error: {str(e)}"

def get_largest_files(directory='.', num_files=5):
    try:
        files = [(file, os.path.getsize(os.path.join(directory, file))) for file in os.listdir(directory)]
        largest_files = sorted(files, key=lambda x: x[1], reverse=True)[:num_files]
        return largest_files
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    path = '/'  # You can specify a different path if needed, e.g., '/home' for your home directory
    total_space, used_space, free_space, usage_percent = get_disk_info(path)

    if (
        isinstance(total_space, int)
        and isinstance(used_space, int)
        and isinstance(free_space, int)
        and isinstance(usage_percent, int)
    ):
        total_space_gb = round(total_space / (1024 ** 3), 2)
        used_space_gb = round(used_space / (1024 ** 3), 2)
        free_space_gb = round(free_space / (1024 ** 3), 2)
        
        print(f"Total hard drive space on '{path}': {total_space_gb} GB")
        print(f"Used hard drive space on '{path}': {used_space_gb} GB")
        print(f"Free hard drive space on '{path}': {free_space_gb} GB")
        print(f"Percentage of used space on '{path}': {usage_percent}%")

        # Get and display the top 5 largest files in the specified directory
        largest_files = get_largest_files(path, num_files=5)
        print("\nTop 5 Largest Files:")
        for file, size in largest_files:
            size_gb = round(size / (1024 ** 3), 2)
            print(f"{file}: {size_gb} GB")
    else:
        print(f"Failed to retrieve disk information: {total_space}, {used_space}, {free_space}, {usage_percent}")
        if isinstance(total_space, Exception):
            # Print the exception details for troubleshooting
            print(f"Exception details: {total_space}")
