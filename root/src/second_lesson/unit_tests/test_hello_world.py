from hello_world import hello

def main():
    test_arg()
    test_default()

def test_arg():
    try:
        assert hello("Andrea Edson") == "Hello, Andrea Edson"
        print("Test with input passed")
    except Exception as e:
        print("Test with input failed: ", e)

def test_default():
    try:
        assert hello() == "Hello, world"
        print("Test with default passed")
    except Exception as e:
        print("Default test failed: ", e)


if __name__ == "__main__":
    main()
