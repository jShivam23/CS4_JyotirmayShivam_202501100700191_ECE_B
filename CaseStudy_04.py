import os

def main():
    file_name = "CS4.txt"
    
    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found. Please create it with the log data.")
        return

    print("--- Task 1: Basic File Reading ---")
    
    with open(file_name, 'r') as file:
        # Using readlines() to get all lines
        lines = file.readlines()
        
        print(f"Total number of lines: {len(lines)}")
        
        print("\nFirst 2 lines:")
        for line in lines[:2]:
            print(line.strip())
            
        print("\nLast 2 lines:")
        for line in lines[-2:]:
            print(line.strip())
            
    with open(file_name, 'r') as file:
        print("\nUsing readline() to read the first line:")
        print(file.readline().strip())
        
        file.seek(0)
        print("\nUsing read() to print the first 50 characters:")
        print(file.read(50))

    print("\n--- Task 2: Log Classification ---")
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    with open(file_name, 'r') as file:
        for line in file:
            if "INFO" in line:
                log_counts["INFO"] += 1
            elif "WARNING" in line:
                log_counts["WARNING"] += 1
            elif "ERROR" in line:
                log_counts["ERROR"] += 1
                
    print(f"Log Keyword Counts: {log_counts}")


    print("\n--- Task 3: Write Filtered Files ---")
    info_lines = []
    warning_lines = []
    error_lines = []

    with open(file_name, 'r') as file:
        for line in file:
            if "INFO" in line:
                info_lines.append(line)
            elif "WARNING" in line:
                warning_lines.append(line)
            elif "ERROR" in line:
                error_lines.append(line)

    with open('info_logs.txt', 'w') as f:
        f.writelines(info_lines)

    with open('error_logs.txt', 'w') as f:
        f.writelines(error_lines)

    with open('warning_logs.txt', 'w') as f:
        for line in warning_lines:
            f.write(line)
            
    print("Filtered files created: info_logs.txt, warning_logs.txt, error_logs.txt")


    print("\n--- Task 4: Search Feature ---")
    search_keyword = input("Enter keyword to search (e.g., ERROR, INFO, WARNING): ").strip()
    
    search_results = []
    print(f"\nMatching lines for '{search_keyword}':")
    
    with open(file_name, 'r') as file:
        for line in file:
            if search_keyword in line:
                search_results.append(line)
                print(line.strip())

    with open('search_result.txt', 'w') as f:
        f.writelines(search_results)
        
    print(f"Search results saved in search_result.txt")

    print("\n--- File Pointer (seek) Operations ---")
    with open(file_name, 'rb') as file:
        
        file_length = file.seek(0, 2)
        file.seek(0)
        
        print("\nReading first 50 characters:")
        print(file.read(50).decode('utf-8'))
        
        file.seek(0)
        print("\nAfter seek(0) [Beginning] - Reading first 20 chars:")
        print(file.read(20).decode('utf-8'))
        
        mid_point = file_length // 2
        file.seek(mid_point)
        print(f"\nAfter seek(len(file)//2) [Middle: {mid_point}] - Reading 20 chars:")
        print(file.read(20).decode('utf-8'))
        
        if file_length >= 100:
            file.seek(-100, 2)
            print("\nAfter seek(-100, 2) [Last 100 chars] - Reading to end:")
            print(file.read().decode('utf-8'))
        else:
            print("\nFile is less than 100 characters long, skipping seek(-100, 2).")

if __name__ == "__main__":
    main()