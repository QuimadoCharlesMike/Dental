"""
Appointments Module
Equivalent to AppointmentsModule.tsx
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class AppointmentsModule(QWidget):
    """Appointments module - manages appointment scheduling"""
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        
        title = QLabel("Appointments Management")
        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)
        
        # TODO: Implement appointments table, calendar, forms
        # Similar structure to PatientsModule
        info = QLabel("Appointments module - Calendar view and appointment management")
        info.setStyleSheet("QLabel { color: white; font-size: 16px; margin-top: 20px; }")
        layout.addWidget(info)
        
        layout.addStretch()
