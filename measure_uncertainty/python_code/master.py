import glob,os

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Run all scripts in the directory
os.chdir(directory)  # locate ourselves in the directory
for script in sorted(glob.glob("*.py")):
    with open(script) as f:
       contents = f.read()
    exec(contents)