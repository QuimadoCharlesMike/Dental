"""
Sidebar Navigation
Equivalent to Sidebar.tsx
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon
from typing import List, Dict


class Sidebar(QWidget):
    """
    Sidebar navigation widget
    Equivalent to Sidebar component
    """
    
    # Signal emitted when module changes
    module_changed = pyqtSignal(str)
    
    def __init__(self, user_role: str):
        super().__init__()
        self.user_role = user_role
        self.current_module = 'patients'
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        self.setFixedWidth(256)
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(26, 45, 63, 0.95);
                border-right: 4px solid #4fb3d4;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Menu header
        menu_header = QFrame()
        menu_header.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border-bottom: 2px solid #4fb3d4;
                padding: 12px;
            }
        """)
        menu_header_layout = QVBoxLayout(menu_header)
        
        menu_label = QLabel("Menu")
        menu_label.setStyleSheet("""
            QLabel {
                color: #4fb3d4;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        menu_header_layout.addWidget(menu_label)
        layout.addWidget(menu_header)
        
        # Menu items
        menu_items = [
            {'id': 'patients', 'label': 'Patients', 'icon': '👥'},
            {'id': 'appointments', 'label': 'Appointments', 'icon': '📅'},
            {'id': 'treatments', 'label': 'Treatments', 'icon': '💊'},
            {'id': 'billing', 'label': 'Billing', 'icon': '💰'},
            {'id': 'staff', 'label': 'Staff', 'icon': '👨‍⚕️', 'admin_only': True},
            {'id': 'reports', 'label': 'Reports', 'icon': '📊', 'admin_only': True},
        ]
        
        # Filter menu items by role
        filtered_items = [
            item for item in menu_items
            if not item.get('admin_only') or self.user_role == 'Admin'
        ]
        
        # Create menu container
        menu_container = QWidget()
        menu_layout = QVBoxLayout(menu_container)
        menu_layout.setContentsMargins(8, 8, 8, 8)
        menu_layout.setSpacing(8)
        
        self.menu_buttons = {}
        
        for item in filtered_items:
            button = QPushButton(f"{item['icon']}  {item['label']}")
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setStyleSheet(self.get_button_style(False))
            button.clicked.connect(lambda checked, module_id=item['id']: self.change_module(module_id))
            
            self.menu_buttons[item['id']] = button
            menu_layout.addWidget(button)
        
        menu_layout.addStretch()
        layout.addWidget(menu_container)
        
        # Set initial active module
        self.update_active_button('patients')
    
    def get_button_style(self, active: bool) -> str:
        """Get button stylesheet based on active state"""
        if active:
            return """
                QPushButton {
                    background-color: #4fb3d4;
                    color: white;
                    border: 2px solid #4fb3d4;
                    border-radius: 8px;
                    padding: 12px;
                    font-size: 16px;
                    font-weight: bold;
                    text-align: left;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: transparent;
                    color: white;
                    border: 2px solid transparent;
                    border-radius: 8px;
                    padding: 12px;
                    font-size: 16px;
                    font-weight: bold;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #2d3e50;
                    border-color: #4fb3d4;
                }
            """
    
    def change_module(self, module_id: str):
        """Change active module"""
        self.current_module = module_id
        self.update_active_button(module_id)
        self.module_changed.emit(module_id)
    
    def update_active_button(self, module_id: str):
        """Update button styles to show active module"""
        for btn_id, button in self.menu_buttons.items():
            button.setStyleSheet(self.get_button_style(btn_id == module_id))
