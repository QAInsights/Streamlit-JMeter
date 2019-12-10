import os
fname = []
for file in os.listdir("."):
    if file.endswith(".csv"):
        fname.append((os.path.join(".", file)))
print(fname)