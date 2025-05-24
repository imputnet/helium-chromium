import argparse
from pathlib import Path

CHROME_VERSION_BASE = 136

def get_version_part(path):
    with open(path, "r") as file:
        return int(file.readline().split(".")[0].strip())

def append_version(file, name, version):
    file.write(f"{name}={version}\n")

def check_existing_version(path):
    with open(path, "r") as f:
        if "HELIUM" in f.read():
            raise Exception("file already contains helium versioning")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--platform-tree", type=Path, required=True)
    parser.add_argument("--chromium-tree", type=Path)
    parser.add_argument("--print", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    return (args.tree, args.platform_tree, args.chromium_tree, args.print)

def get_version_parts(tree, platform_tree):
    version_paths = {
        "HELIUM_MAJOR": tree / "version.txt",
        "HELIUM_MINOR": tree / "chromium_version.txt",
        "HELIUM_PATCH": tree / "revision.txt",
        "HELIUM_PLATFORM": platform_tree / "revision.txt",
    }
    
    version_parts = {}
    for name, path in version_paths.items():
        delta = 0 if name != "HELIUM_MINOR" else -CHROME_VERSION_BASE
        version_parts[name] = get_version_part(path) + delta
    return version_parts

def main():
    tree, platform_tree, chromium_tree, should_print = parse_args()

    version_parts = get_version_parts(tree, platform_tree)
    if should_print:
        print(f"{version_parts['HELIUM_MAJOR']}.{version_parts['HELIUM_MINOR']}." + \
              f"{version_parts['HELIUM_PATCH']}.{version_parts['HELIUM_PLATFORM']}")
    else:
        chrome_version_path = chromium_tree / "chrome/VERSION"
        check_existing_version(chrome_version_path)
        with open(chrome_version_path, "a") as f:
            for name, version in version_parts.items():
                append_version(f, name, version)

if __name__ == "__main__":
    main()
