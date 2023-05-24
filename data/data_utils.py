import re


def clean_text(text: str) -> str:
    if text == None:
        return text
    pattern = r'[\r\t\n\s*?#"|]'
    cleaned_text = re.sub(pattern, " ", text)
    cleaned_text = cleaned_text.strip()
    cleaned_text = cleaned_text.encode("ascii", "ignore").decode("ascii")

    return cleaned_text


def correct_file_extension(filename: str, extension: str) -> str:
    """Checks for file extension and if not correct fixes it."""
    return (
        filename if filename.endswith(extension) else filename.split(".")[0] + extension
    )
