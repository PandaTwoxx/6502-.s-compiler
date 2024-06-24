import os
import time
from dotenv import load_dotenv
load_dotenv()
directory = os.getenv("DIRECTORY")
print(f"Pulling .s file from{directory}")
def out_to_bin(source_file, destination_file):
  try:
    with open(source_file, "rb") as source, open(destination_file, "wb") as destination:
      data = source.read(1024)
      while data:
        destination.write(data)
        data = source.read(1024)
    print(f"Successfully moved contents of {source_file} to {destination_file}")
  except FileNotFoundError:
    print(f"Compiling failed: File not found - {source_file} or {destination_file}")
  except PermissionError:
    print(f"Compiling failed: Insufficient permissions to access files.")
  except Exception as e:
    print(f"Compiling failed {e}")

def compile(file):
    if not(os.path.exists(f"{file}")):
       print('Compiling failed: file not found')
       return 0
    print('Compiling')
    os.system(f"./vasm6502_oldstyle -Fbin -dotdir {file}")
    print('Converting to .bin')
    if not(os.path.exists("a.out")):
       print('Compiling failed: a.out file not fount')
       return 0
    out_to_bin('a.out','rom.bin')
    if not(os.path.exists('rom.bin')):
        print('Compiling failed: Unable to create rom.bin file')
        return 0
    print('Removing .out file')
    os.remove('a.out')
    if os.path.exists('a.out'):
       print('Compiling failed: Unable to remove a.out')
       return 0
    print('Compiled successfully')
    return 1

def build():
    print('Starting build')

    start = time.time()

    file = ''
        
    for filename in os.listdir(directory):
        print(filename)
        if filename.endswith('.s'):
            file = filename

    if file == '':
        print('Compiling failed: .s file not found')
        end = time.time()
        print(f'Executed failed in {end-start}')
        return 0
    else:
        status = compile(file)
        end = time.time()
        if(status == 0):
            print(f'Execution failed in {end-start}')
            return 0
        else:
            print(f'Execution completed in {end-start}')
            return 1

build()