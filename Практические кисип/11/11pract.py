import sys
import requests
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt


class GitHubInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('GitHub Repository Info - Вариант 4')
        self.setGeometry(100, 100, 500, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Заголовок
        title = QLabel('Получение информации о пользователе GitHub')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px;')
        layout.addWidget(title)

        # Поле ввода
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Имя пользователя:'))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Введите имя пользователя GitHub')
        self.username_input.setText('kubernetes')  # Пример
        input_layout.addWidget(self.username_input)
        layout.addLayout(input_layout)

        # Кнопка
        self.get_button = QPushButton('Получить информацию')
        self.get_button.clicked.connect(self.get_github_info)
        layout.addWidget(self.get_button)

        # Текстовое поле для вывода
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText('Здесь появится результат...')
        layout.addWidget(self.result_text)

        # Кнопка сохранения
        self.save_button = QPushButton('Сохранить в файл')
        self.save_button.clicked.connect(self.save_to_file)
        self.save_button.setEnabled(False)
        layout.addWidget(self.save_button)

        central_widget.setLayout(layout)
        self.current_data = None

    def get_github_info(self):
        username = self.username_input.text().strip()
        if not username:
            QMessageBox.warning(self, 'Ошибка', 'Введите имя пользователя!')
            return

        self.get_button.setEnabled(False)
        self.get_button.setText('Загрузка...')

        try:
            # Запрос к GitHub API
            url = f'https://api.github.com/users/{username}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # Извлекаем нужные поля
                self.current_data = {
                    'company': data.get('company'),
                    'created_at': data.get('created_at'),
                    'email': data.get('email'),
                    'id': data.get('id'),
                    'name': data.get('name'),
                    'url': data.get('url')
                }

                # Форматированный вывод
                formatted = json.dumps(self.current_data, indent=2, ensure_ascii=False)
                self.result_text.setText(formatted)
                self.save_button.setEnabled(True)

                QMessageBox.information(self, 'Успех', 'Данные получены!')
            else:
                QMessageBox.critical(self, 'Ошибка',
                                     f'Не удалось получить данные. Код ошибки: {response.status_code}\n'
                                     f'Проверьте правильность имени пользователя.')
                self.current_data = None
                self.save_button.setEnabled(False)

        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, 'Ошибка', 'Нет подключения к интернету!')
            self.current_data = None
            self.save_button.setEnabled(False)
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {str(e)}')
            self.current_data = None
            self.save_button.setEnabled(False)
        finally:
            self.get_button.setEnabled(True)
            self.get_button.setText('Получить информацию')

    def save_to_file(self):
        if not self.current_data:
            QMessageBox.warning(self, 'Ошибка', 'Нет данных для сохранения!')
            return

        username = self.username_input.text().strip()
        if not username:
            username = 'github_user'

        filename = f'{username}_info.json'

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.current_data, f, indent=2, ensure_ascii=False)
            QMessageBox.information(self, 'Успех', f'Данные сохранены в файл:\n{filename}')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Не удалось сохранить файл: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GitHubInfoApp()
    window.show()
    sys.exit(app.exec_())