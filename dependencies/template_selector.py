import glob
import json
import os
from PyQt5.QtWidgets import QFrame, QLineEdit, QPushButton, QLabel, QHBoxLayout, QComboBox, QSizePolicy


class TemplateSelector(QFrame):
    def __init__(self, template_path=os.path.join("templates", "*.json")):
        super().__init__()
        self.template_path = template_path
        self._setup_ui()
        self._display_ui()
        self._set_templates()

    def _setup_ui(self):
        self.setLayout(QHBoxLayout())
        self.dropdown = QComboBox()
        self.label = QLabel("Template")

    def _display_ui(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.dropdown)

    def _find_templates(self):
        return glob.glob(os.path.join(self.template_path, "*.json"))

    def _set_templates(self):
        self.templates = self._find_templates()
        self.striped_templates = [os.path.basename(template.strip(".json")) for template in self.templates]
        self.templates = self.templates
        for striped_template in self.striped_templates:
            self.dropdown.addItem(striped_template)

    def get_selected_template(self):
        current_index = self.dropdown.currentIndex()
        selected_file = self.templates[current_index]
        if selected_file is None:
            return None
        with open(os.path.join(os.getcwd(), selected_file), 'r') as f:
            return_dict = json.load(f)
        return return_dict
