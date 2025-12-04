"""
Staff Module
Equivalent to StaffModule.tsx
Admin Only
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class StaffModule(QWidget):
    """Staff module - manages staff members (Admin only)"""
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        
        title = QLabel("Staff Management")
        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)
        
        subtitle = QLabel("🔒 Admin Only")
        subtitle.setStyleSheet("QLabel { color: #4fb3d4; font-size: 16px; font-weight: bold; }")
        layout.addWidget(subtitle)
        
        info = QLabel("Staff module - Employee management and scheduling")
        info.setStyleSheet("QLabel { color: white; font-size: 16px; margin-top: 20px; }")
        layout.addWidget(info)
        
        layout.addStretch()
