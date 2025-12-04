"""
Header Component
Equivalent to Header.tsx
"""

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal


class Header(QWidget):
    """
    Header widget with clinic name, user info, and logout button
    Equivalent to Header component
    """
    
    # Signal emitted when logout is clicked
    logout_clicked = pyqtSignal()
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(26, 45, 63, 0.95);
                border-bottom: 4px solid #4fb3d4;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(16)
        
        # Clinic name
        clinic_name = QLabel("SMILEY DENTAL CLINIC AND SERVICES")
        clinic_name.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)
        layout.addWidget(clinic_name)
        
        layout.addStretch()
        
        # User info card
        user_info_frame = QFrame()
        user_info_frame.setStyleSheet("""
            QFrame {
                background-color: #2d3e50;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                padding: 8px 16px;
            }
        """)
        user_info_layout = QHBoxLayout(user_info_frame)
        user_info_layout.setContentsMargins(8, 8, 8, 8)
        user_info_layout.setSpacing(12)
        
        # User icon
        user_icon = QLabel("👤")
        user_icon.setStyleSheet("""
            QLabel {
                color: #4fb3d4;
                font-size: 20px;
            }
        """)
        user_info_layout.addWidget(user_icon)
        
        # User details
        user_details_widget = QWidget()
        user_details_layout = QVBoxLayout(user_details_widget)
        user_details_layout.setContentsMargins(0, 0, 0, 0)
        user_details_layout.setSpacing(2)
        
        user_name_label = QLabel(self.user.full_name)
        user_name_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        user_details_layout.addWidget(user_name_label)
        
        user_role_label = QLabel(self.user.role)
        user_role_label.setStyleSheet("""
            QLabel {
                color: #4fb3d4;
                font-size: 12px;
                font-weight: 600;
            }
        """)
        user_details_layout.addWidget(user_role_label)
        
        user_info_layout.addWidget(user_details_widget)
        layout.addWidget(user_info_frame)
        
        # Logout button
        logout_button = QPushButton("Logout")
        logout_button.setCursor(Qt.CursorShape.PointingHandCursor)
        logout_button.setStyleSheet("""
            QPushButton {
                background-color: #cc0000;
                color: white;
                border: 2px solid #ff3333;
                border-radius: 8px;
                padding: 8px 24px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff3333;
            }
            QPushButton:pressed {
                background-color: #aa0000;
            }
        """)
        logout_button.clicked.connect(self.logout_clicked.emit)
        layout.addWidget(logout_button)
