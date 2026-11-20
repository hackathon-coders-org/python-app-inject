def greet(name: str = "inject") -> str:
    return f"Hello from {name}"


if __name__ == "__main__":
    print(greet())
