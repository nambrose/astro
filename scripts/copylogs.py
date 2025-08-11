import subprocess

src_path_prefix = "c:\\users\\nicka\\"
dest_path_prefix= src_path_prefix + "astro\\"

robocopy_options = "/S /XO /W:3 /R:3 /FFT /MT"  # Example Robocopy options

def copyFiles(src, dest):
    try:
        # Construct the command as a list of arguments for better handling of spaces
        command = ["robocopy", src, dest] + robocopy_options.split()
        
        print(command)
        

        # Execute the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print("Robocopy successful:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Robocopy failed with error code {e.returncode}:")
        print(e.stderr)
    except FileNotFoundError:
        print("Error: 'robocopy.exe' not found. Ensure Robocopy is in your system's PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Copy NINA logs
copyFiles(src_path_prefix + "AppData\\local\\NINA\\logs" , dest_path_prefix + "NINA\\logs\\")

#Copy NINA Auto Focus
copyFiles(src_path_prefix + "AppData\\local\\NINA\\AutoFocus" , dest_path_prefix + "NINA\\AutoFocus\\")

#Copy Plate Solve failures
copyFiles(src_path_prefix + "AppData\\local\\NINA\\PlateSolver\\Failed" , dest_path_prefix + "NINA\\PlateSolveFailed\\")
