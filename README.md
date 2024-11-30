# Swift Strings to XCStrings Converter

## Introduction
In Swift, strings and localization are crucial for building apps that support multiple languages and regions. This converter is a tool designed to transform the conventional .strings files used in Swift projects into the newer .xcstrings format, which offers enhanced functionality and better organization.


## What are .strings in Swift?

<code>.strings</code> files are key-value pairs used for localizing text in iOS and macOS applications. Each entry in a .strings file represents a localized string associated with a unique key.

Example <code>.strings</code> File:
```
"add_reminder" = "Add Reminder";
"medicine_name" = "Medicine Name";
```

- Key: "add_reminder" or "medicine_name", used in the code.
- Value: The actual localized text, such as "Add Reminder".

## What are .xcstrings?
<code>.xcstrings</code> is a newer JSON-based format introduced by Apple for managing localized strings. It provides several advantages over .strings files:
- Organized structure for managing multiple languages.
- Built-in support for metadata, such as the translation state.
- Integrated support in Xcode for better handling of translations.

Example <code>.xcstrings</code> File:
```
{
  "sourceLanguage": "en",
  "strings": {
    "add_reminder": {
      "extractionState": "manual",
      "localizations": {
        "en": {
          "stringUnit": {
            "state": "translated",
            "value": "Add Reminder"
          }
        },
        "de": {
          "stringUnit": {
            "state": "translated",
            "value": "Erinnerung hinzufügen"
          }
        }
      }
    }
  },
  "version": "1.0"
}
```
- Language Support: The localizations section supports multiple languages.
- Metadata: States like translated, pending, or unverified can be tracked.

## What Does This Converter Do?
- This Python-based converter automates the transformation of <code>.strings</code> files into .xcstrings format. It supports:
- Multiple Languages: You can provide <code>.strings</code> files for different languages, and the tool merges them into a single <code>.xcstrings</code> file.
- Structured Output: The resulting <code>.xcstrings</code> file is well-organized and ready to be used in Xcode.

### Features:
1. Parse .strings Files: Extracts key-value pairs from <code>.strings</code> files.
2. Supports Multiple Languages: Combines translations from <code>.strings</code> files for different languages.
3. Output to <code>.xcstrings</code> Format: Produces a valid <code>.xcstrings</code> file compliant with Apple standards.

## Usage
### Prerequisites:
- Python 3.x installed on your system.
- <code>.strings</code> files for the languages you want to convert.

### Steps:
1. Clone this repository.
2.	Place your .strings files in the same directory.
3.	Update the file paths in the script:
```
input_strings_files = {
    "en": "Localizable_en.strings",
    "de": "Localizable_de.strings",
    "fr": "Localizable_fr.strings"
}
```
4.	Run the script:
```
python convert_strings_to_xcstrings.py
```

5.	The output <code>.xcstrings</code> file will be saved in the same directory.

## Example

Input .strings Files:

<b><code>Localizable_en.strings:</code></b>
```
"add_reminder" = "Add Reminder";
```
<b><code>Localizable_de.strings:</code></b>
```
"add_reminder" = "Erinnerung hinzufügen";
```

<b>Output <code>.xcstrings</code> File:</b>
```
{
  "sourceLanguage": "en",
  "strings": {
    "add_reminder": {
      "extractionState": "manual",
      "localizations": {
        "en": {
          "stringUnit": {
            "state": "translated",
            "value": "Add Reminder"
          }
        },
        "de": {
          "stringUnit": {
            "state": "translated",
            "value": "Erinnerung hinzufügen"
          }
        }
      }
    }
  },
  "version": "1.0"
}
```

## Advantages of .xcstrings

1.	Improved Organization: Supports managing multiple languages within a single file.
2.	Rich Metadata: Tracks translation states for better collaboration with translators.
3.	Xcode Integration: Native support in Xcode for easier localization workflows.

