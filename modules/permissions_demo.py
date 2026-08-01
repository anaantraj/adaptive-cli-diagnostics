# simulates unix-style rwx permission flags using bitwise ops
READ = 0b100
WRITE = 0b010
EXECUTE = 0b001


def build_permission(read=False, write=False, execute=False):
    perm = 0
    if read:
        perm |= READ
    if write:
        perm |= WRITE
    if execute:
        perm |= EXECUTE
    return perm


def describe_permission(perm):
    r = "r" if perm & READ else "-"
    w = "w" if perm & WRITE else "-"
    x = "x" if perm & EXECUTE else "-"
    return r + w + x


def combine_permissions(perm1, perm2):
    return perm1 | perm2


def intersect_permissions(perm1, perm2):
    return perm1 & perm2


def flip_permission(perm):
    return perm ^ 0b111


def run_demo():
    print("\n--- Permissions Demo (bitwise ops) ---")
    read = input("Allow read? (y/n): ").strip().lower() == "y"
    write = input("Allow write? (y/n): ").strip().lower() == "y"
    execute = input("Allow execute? (y/n): ").strip().lower() == "y"

    perm = build_permission(read, write, execute)
    print(f"Permission value: {perm} (binary: {bin(perm)})")
    print(f"Permission string: {describe_permission(perm)}")

    flipped = flip_permission(perm)
    print(f"Flipped (XOR with 111): {describe_permission(flipped)}")
