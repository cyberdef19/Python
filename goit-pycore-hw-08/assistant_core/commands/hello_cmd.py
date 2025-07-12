from assistant_core.utils.input_error import input_error
"""
Функція hello_cmd - виводить фразу 'How can I help you?'

return: str - повертає рядок з запитом про виконання дії
"""

@input_error
def hello_cmd():
    return "Як я можу допомогти тобі?"