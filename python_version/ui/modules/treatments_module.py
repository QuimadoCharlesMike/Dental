"""
Treatments Module
Equivalent to TreatmentsModule.tsx
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class TreatmentsModule(QWidget):
    """Treatments module - manages treatment records"""
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        
        title = QLabel("Treatments Management")
        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)
        
        info = QLabel("Treatments module - Patient treatment records and procedures")
        info.setStyleSheet("QLabel { color: white; font-size: 16px; margin-top: 20px; }")
        layout.addWidget(info)
        
        layout.addStretch()
