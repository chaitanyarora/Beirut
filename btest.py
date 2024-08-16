import subprocess
import os

cwd = os.path.dirname(os.path.abspath(__file__))
print(cwd)

blender_executable = r"/blender_only/blender.exe"
blend_file_paths = "path_to_your_file.blend"
test_script_paths = "path_to_your_script.py"

def test():
    for x in range(len(test_script_paths)):

        blender_command = [blender_executable, blend_file_paths[x],'-b', '-P', test_script_paths[x]]

        try:
            #To read the console output
            result = subprocess.run(blender_command, stdout=subprocess.PIPE, text=True, check=True)
            print(f'Started testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        print(f'Done testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')

if __name__ == '__main__':
    test()