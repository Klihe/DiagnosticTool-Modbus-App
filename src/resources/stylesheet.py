def load_stylesheet() -> str:
    """Load the stylesheet from the stylesheet.css file

    Raises:
        FileNotFoundError: If the stylesheet.css file is not found

    Returns:
        str: The stylesheet from the stylesheet.css file
    """

    try:
        # Open the stylesheet.css file in read mode
        with open("src/resources/stylesheet.css", "r") as file:
            # Read the contents of the file and return it
            return file.read()
    except FileNotFoundError:
        # If the file is not found, raise an exception
        raise FileNotFoundError("src/resources/stylesheet.css not found")
