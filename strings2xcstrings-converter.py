import json
import re

def convert_to_xcstrings(input_files, output_file):
    """
    Converts multiple .strings files to a single xcstrings JSON file.

    Args:
        input_files (dict): A dictionary with language codes as keys and file paths as values.
        output_file (str): The path to the output .xcstrings file.
    """
    xcstrings = {
        "sourceLanguage": "en",
        "strings": {},
        "version": "1.0"
    }

    # Regex pattern to match strings
    string_pattern = re.compile(r'"(.*?)"\s*=\s*"(.*?)";')

    # Process each language file
    for lang, file_path in input_files.items():
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            match = string_pattern.match(line)
            if match:
                key = match.group(1)
                value = match.group(2)

                # Ensure the key exists in the JSON structure
                if key not in xcstrings["strings"]:
                    xcstrings["strings"][key] = {
                        "extractionState": "manual",
                        "localizations": {}
                    }

                # Add the localized string for the current language
                xcstrings["strings"][key]["localizations"][lang] = {
                    "stringUnit": {
                        "state": "translated",
                        "value": value
                    }
                }

    # Write the output xcstrings file
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(xcstrings, file, indent=2, ensure_ascii=False)

    print(f"Conversion complete! Output saved to {output_file}")

# Usage example
input_strings_files = {
    "en": "Localizable_en.strings",
    "de": "Localizable_de.strings"
}
output_xcstrings_file = "Localizable.xcstrings"
convert_to_xcstrings(input_strings_files, output_xcstrings_file)