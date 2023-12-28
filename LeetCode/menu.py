import os
import subprocess
import importlib.util

def load_module(file_path):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    print("Welcome to the LeetCode problem solver!")
    problem_dir = './LeetCode'  # specify your problem directory here
    while True:
        print("\nAvailable problems:")
        problem_files = [f for f in os.listdir(problem_dir) if f.startswith('problem_') and f.endswith('.py')]
        for i, file in enumerate(problem_files):
            print(f"{i+1}. {file}")
        print(f"{len(problem_files)+1}. Exit")
        
        choice = int(input("\nEnter the number of the problem you want to solve or 'Exit': "))
        if 1 <= choice <= len(problem_files):
            problem_file = os.path.join(problem_dir, problem_files[choice-1])
            try:
                # Try to import the module and call the main function
                problem_module = load_module(problem_file)
                problem_module.main()
            except AttributeError:
                # If that fails, run the file as a script
                subprocess.run(['python', problem_file])
        elif choice == len(problem_files) + 1:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()