import os
import zipfile

source_dir = r".\\"

for root, dirs, files in os.walk(source_dir):
    for filename in files:

        # Skip files that are already zip archives
        if filename.lower().endswith(".zip"):
            print(f"Skipping already-zipped file: {filename}")
            continue

        filepath = os.path.join(root, filename)
        zip_path = os.path.join(root, os.path.splitext(filename)[0] + ".zip")

        # NEW LOGIC: if matching zip already exists, delete the file instead of compressing
        if os.path.exists(zip_path):
            print(f"Zip already exists for {filename}. Deleting original file.")
            try:
                os.remove(filepath)
            except Exception as e:
                print(f"Failed to delete {filepath}: {e}")
            continue

        try:
            with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
                z.write(filepath, arcname=filename)

            # verify zip exists before deleting
            if os.path.exists(zip_path):
                os.remove(filepath)
                print(f"Compressed and deleted: {filepath}")

        except Exception as e:
            print(f"Failed to process {filepath}: {e}")