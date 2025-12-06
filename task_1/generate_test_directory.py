import os

def create_file(path, content="test"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_test_structure(base="test_src"):
    if os.path.exists(base):
        import shutil
        shutil.rmtree(base)

    os.makedirs(os.path.join(base, "subfolder", "nested"), exist_ok=True)

    create_file(os.path.join(base, "file1.txt"))
    create_file(os.path.join(base, "file2.jpg"))
    create_file(os.path.join(base, "file3"))

    create_file(os.path.join(base, "subfolder", "file4.txt"))
    create_file(os.path.join(base, "subfolder", "file5.png"))

    create_file(os.path.join(base, "subfolder", "nested", "file6.mp3"))
    create_file(os.path.join(base, "subfolder", "nested", "file7.docx"))

    print(f"✅ Test directory '{base}' successfully created!")

if __name__ == "__main__":
    generate_test_structure()
