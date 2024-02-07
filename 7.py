'''
>>> 8.Explain what does django-admin.py make messages command is used
for?

The django-admin.py makemessages command is used in Django to handle the process of creating or updating translation files for internationalization (i18n) and localization (l10n) purposes. This command helps Django developers prepare their Django applications for translation into different languages.

Here's a breakdown of what makemessages does:

1. Scans the Codebase: 
    The makemessages command scans the entire codebase of your Django project, including Python code and templates, to identify strings that need to be translated. These strings typically include text displayed to users, such as labels, messages, and other static content.

2.Extracts Translatable Strings: 
    The command extracts these translatable strings and generates a message file (typically with a .po extension) for each language specified in your Django project settings. The message files contain pairs of original text and placeholders for translations.

3.Template and Code Comments:
    Additionally, makemessages is capable of extracting translatable strings from comments in templates and Python code, helping developers provide context for translators.

4.Creates or Updates Message Files: 
    If the message files for a particular language already exist, makemessages updates them with any new strings or changes in the codebase. If the message files do not exist, it creates them.

Once the message files are generated, developers or translators can open these files and replace the placeholders with the translated versions of the strings. After translation, the compilemessages command is used to compile these translations into machine-readable .mo files, which Django can then use to serve the application in the specified language.

In summary, makemessages is a crucial step in the internationalization process of a Django project, as it automates the extraction of translatable strings and prepares the groundwork for translation efforts.
'''