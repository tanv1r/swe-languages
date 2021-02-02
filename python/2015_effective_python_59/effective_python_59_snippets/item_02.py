# For more guidelines read https://www.python.org/dev/peps/pep-0008/
# 
# Whitespace:
# 
# 01. Use spaces instead of tabs for indentiation.
# 02. Use 4 spaces for each level of syntactically significant indenting.
# 03. Lines should be 79 characters in length or less.
# 04. Continuations of long expressions onto additional lines should be indented
#     by 4 extra spaces from their normal indentation level
# 05. In a file, functions and classes should be separated by 2 blank lines.
# 06. In a calss, methods should be separated by 1 blank line.
# 07. Do not put spaces around list indexes, function calls, or keyword
#     assignments.
# 08. Put one---and only one---space before and after variable assignments.
# 
# Naming:
# 
# 01. Functions, variables, and attributes should in lowercase_underscore 
#     format.
# 02. Protected instance attributes should in _leading_underscore format.
# 03. Private instance attributes should be __double_underscore format.
# 04. Classes and exceptions should in CapitalizedWord format.
# 05. Module-level constants should be in ALL_CAPS format.
# 06. Instance methods in classes should use self as the name of the first 
#     parameter (which refers to the object).
# 07. Class methods should use cls as the name of the first parameter (which 
#     refers to the class).
#
# Expressions and Statements:
#
# 01. Use inline negation (if a is not b) instead of negation of positive 
#     expressions (if not a is b)
# 02. Do not check for empty values (like [] or '') by checking the length (if 
#     len(somelist) == 0). Use 'if not somelist' and assume empty values 
#     implicitly evaluate to False.
# 03. The same thing goes for non-empty values like ([1] or 'hi'). The 
#     statement 'if somelist' is implicitly True for non-empty values.
# 04. Avoid single-line if statements, for and while loops, and except compound 
#     statements. Spread these over multiple lines for clarify.
# 05. Always put import statements at the top of the file.
# 06. Always use absolute names for modules when importing them, not names 
#     relative to current module's own path. For example, to import the foo 
#     module from the bar package you should do 'from bar import foo', not just 
#     'import foo'.
# 07. If you must do relative imports, use the explicit syntax 'from . import 
#     foo'.
# 08. Imports should be in sections in the following order:
#         a. Standard library modules.
#         b. Third-party modules.
#         c. Your own modules.
#     Each subsection should have imports in alphabetic order.
#
# Pylint is a popular static analyzer to enforce PEP 8 style guide.
#