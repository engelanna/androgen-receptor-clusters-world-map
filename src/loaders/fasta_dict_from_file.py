from collections import defaultdict


class FastaDictFromFile:
    def __call__(self, file_path: str) -> dict:
        entries = defaultdict(lambda: "")

        for line in open(file_path, "r"):
            if line.startswith(">"):
                current_header = line.rstrip()
            else:
                entries[current_header] += line.rstrip()

        return entries
