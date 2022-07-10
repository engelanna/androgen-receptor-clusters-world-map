import os

just_the_nonhidden_files = lambda dir: [
    file
    for file in os.listdir(dir)
    if not file.startswith(".") and not os.path.isdir(file)
]
