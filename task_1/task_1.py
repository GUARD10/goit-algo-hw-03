import argparse
import os
import shutil


def _copy_file(item: str, dst_path: str, full_item_path: str) -> None:
    ext = os.path.splitext(item)[1].lower().replace(".", "")
    ext = ext if ext else "no_extension"

    target_folder = os.path.join(dst_path, ext)
    os.makedirs(target_folder, exist_ok=True)

    shutil.copy2(full_item_path, os.path.join(target_folder, item))

def copy_and_sort_files(src_path: str, dst_path: str) -> None:
    try:
        for item in os.listdir(src_path):
            full_item_path = os.path.join(src_path, item)

            if os.path.isdir(full_item_path):
                copy_and_sort_files(full_item_path, dst_path)

            else:
                _copy_file(item, dst_path, full_item_path)

    except PermissionError:
        print(f"⚠️ No access to file: {src_path}")
    except Exception as e:
        print(f"❌ Error: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Recursive file sorter")
    parser.add_argument("src", help="Source directory path")
    parser.add_argument("dst", nargs="?", default="dist", help="Destination directory path")

    args = parser.parse_args()

    if not os.path.exists(args.src):
        print("❌ Directory does not exist")
        return

    os.makedirs(args.dst, exist_ok=True)
    copy_and_sort_files(args.src, args.dst)

    print(f"✅ File successfully saved in '{args.dst}'")


if __name__ == "__main__":
    main()
