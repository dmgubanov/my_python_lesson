import subprocess

# Определяем функцию git_config_list
def git_config_list():
    # Выполняем команду `git config --global --list`
    result = subprocess.run(['git', 'config', '--global', '--list'], capture_output=True, text=True)
    
    # Проверяем, успешно ли выполнена команда
    if result.returncode == 0:
        # Выводим результат выполнения команды
        print(result.stdout)
    else:
        # Выводим ошибку, если команда завершилась с ошибкой
        print(f"Ошибка: {result.stderr}")

# Вызываем функцию
git_config_list()

