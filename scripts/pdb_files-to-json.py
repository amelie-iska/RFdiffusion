# import os
# import json
# import argparse
# import re
# from pathlib import Path

# def find_pdb_files(input_folder, script_path):
#     pdb_files = {}
#     input_folder = Path(input_folder).resolve()
#     script_dir = Path(script_path).resolve().parent.parent  # Go up one more level
    
#     print(f"Input folder: {input_folder}")
#     print(f"Script directory: {script_dir}")

#     # Find the common base path (should be the Workspace directory)
#     common_base = Path(os.path.commonpath([input_folder, script_dir]))
#     print(f"Common base path: {common_base}")

#     # Compile a regular expression pattern for the desired file names
#     file_pattern = re.compile(r'run-\d+_\d+\.pdb$')

#     for root, dirs, files in os.walk(input_folder):
#         # Skip the 'traj' subdirectory
#         if 'traj' in dirs:
#             dirs.remove('traj')
        
#         for file in files:
#             if file.endswith('.pdb') and file_pattern.match(file):
#                 full_path = Path(root) / file
#                 relative_path = full_path.relative_to(common_base)
#                 rel_path_str = '../' + str(relative_path)
#                 rel_path_str = rel_path_str.replace('\\', '/')
#                 pdb_files[rel_path_str] = ""
#                 print(f"Found PDB file: {rel_path_str}")
    
#     print(f"Total PDB files found: {len(pdb_files)}")
#     return pdb_files

# def main():
#     parser = argparse.ArgumentParser(description="Find PDB files and create a JSON file")
#     parser.add_argument('--input_folder', required=True, help="Path to the input folder")
#     parser.add_argument('--output_file', default='pdb_files.json', help="Path to the output JSON file")
#     args = parser.parse_args()

#     input_folder = Path(args.input_folder).resolve()
#     if not input_folder.exists():
#         print(f"Error: Input folder does not exist: {input_folder}")
#         return

#     pdb_files = find_pdb_files(args.input_folder, __file__)

#     with open(args.output_file, 'w') as f:
#         json.dump(pdb_files, f, indent=4)

#     print(f"JSON file created: {args.output_file}")

# if __name__ == "__main__":
#     main()

# # Example usage:
# # python pdb_files2json.py --input_folder ../RFdiffusion/example_outputs/design_ppi/5era-chainDI --output_file ./runs/5era-DI_1100.json

import os
import json
import argparse
from pathlib import Path

def find_pdb_files(input_folder):
    pdb_files = {}
    input_folder = Path(input_folder).resolve()
    
    print(f"Input folder: {input_folder}")

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.pdb') and 'traj' not in file:
                full_path = Path(root) / file
                abs_path_str = str(full_path)
                pdb_files[abs_path_str] = ""
                print(f"Found PDB file: {abs_path_str}")
    
    print(f"Total PDB files found: {len(pdb_files)}")
    return pdb_files

def main():
    parser = argparse.ArgumentParser(description="Find PDB files and create a JSON file")
    parser.add_argument('--input_folder', required=True, help="Path to the input folder")
    parser.add_argument('--output_file', required=True, help="Path to the output JSON file")
    args = parser.parse_args()

    input_folder = Path(args.input_folder).resolve()
    if not input_folder.exists():
        print(f"Error: Input folder does not exist: {input_folder}")
        return

    pdb_files = find_pdb_files(args.input_folder)

    output_file = Path(args.output_file).resolve()

    print("Contents of pdb_files dictionary:")
    print(json.dumps(pdb_files, indent=4))
    
    with open(output_file, 'w') as f:
        json.dump(pdb_files, f, indent=4)

    print(f"JSON file created: {output_file}")

if __name__ == "__main__":
    main()

# Example usage:
# python3 /home/lily/amelie/Workspace/RFdiffusion/scripts/pdb_files-to-json.py --input_folder /home/lily/amelie/Workspace/RFdiffusion/outputs/motifscaffolding --output_file /home/lily/amelie/Workspace/RFdiffusion/outputs/motifscaffolding/5TPN_run1.json

