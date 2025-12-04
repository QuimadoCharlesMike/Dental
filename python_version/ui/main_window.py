"""
Main Window - Application Container
Equivalent to App.tsx and Dashboard.tsx
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QStackedWidget, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPalette, QColor
from typing import Optional, Dict

from .login_window import LoginWindow
from .header import Header
from .sidebar import Sidebar
from .modules.patients_module import PatientsModule
from .modules.appointments_module import AppointmentsModule
from .modules.treatments_module import TreatmentsModule
from .modules.billing_module import BillingModule
from .modules.staff_module import StaffModule
from .modules.reports_module import ReportsModule


class User:
    """User model - equivalent to TypeScript User interface"""
    def __init__(self, id: str, username: str, role: str, full_name: str):
        self.id = id
        self.username = username
        self.role = role  # 'Admin' or 'Employee'
        self.full_name = full_name


class MainWindow(QMainWindow):
    """
    Main application window
    Combines functionality of App.tsx and Dashboard.tsx
    """
    
    def __init__(self):
        super().__init__()
        self.current_user: Optional[User] = None
        self.current_module = 'patients'
        
        self.setWindowTitle("Smiley Dental Clinic and Services")
        self.setMinimumSize(1200, 800)
        
        # Apply dark theme
        self.apply_dark_theme()
        
        # Show login first
        self.show_login()
    
    def apply_dark_theme(self):
        """Apply dark theme colors matching React app"""
        palette = QPalette()
        
        # Background colors
        palette.setColor(QPalette.ColorRole.Window, QColor("#949494"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#2d3e50"))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#1a2d3f"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#1a2d3f"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#4fb3d4"))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
        
        self.setPalette(palette)
        
        # Apply stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #949494;
            }
            QWidget {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                font-size: 16px;
            }
            QPushButton {
                background-color: #4fb3d4;
                color: white;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                padding: 12px 24px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #3a9cb8;
            }
            QPushButton:pressed {
                background-color: #2d8aa3;
            }
            QPushButton[danger="true"] {
                background-color: #cc0000;
                border-color: #ff3333;
            }
            QPushButton[danger="true"]:hover {
                background-color: #ff3333;
            }
            QLineEdit {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #4fb3d4;
            }
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            QTableWidget {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                gridline-color: #1a2d3f;
            }
            QHeaderView::section {
                background-color: #1a2d3f;
                color: white;
                padding: 12px;
                border: none;
                font-weight: bold;
            }
        """)
    
    def show_login(self):
        """Show login window"""
        self.login_window = LoginWindow()
        self.login_window.login_successful.connect(self.handle_login)
        self.setCentralWidget(self.login_window)
    
    def handle_login(self, user_data: Dict[str, str]):
        """
        Handle successful login
        Equivalent to handleLogin in App.tsx
        """
        self.current_user = User(
            id=user_data['id'],
            username=user_data['username'],
            role=user_data['role'],
            full_name=user_data['full_name']
        )
        self.setup_dashboard()
    
    def setup_dashboard(self):
        """
        Set up main dashboard after login
        Equivalent to Dashboard.tsx
        """
        # Create central widget
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create sidebar
        self.sidebar = Sidebar(self.current_user.role)
        self.sidebar.module_changed.connect(self.change_module)
        main_layout.addWidget(self.sidebar)
        
        # Create right side (header + content)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        
        # Create header
        self.header = Header(self.current_user)
        self.header.logout_clicked.connect(self.handle_logout)
        right_layout.addWidget(self.header)
        
        # Create stacked widget for modules
        self.module_stack = QStackedWidget()
        self.module_stack.setStyleSheet("""
            QStackedWidget {
                background-color: transparent;
            }
        """)
        
        # Initialize modules
        self.modules = {
            'patients': PatientsModule(self.current_user),
            'appointments': AppointmentsModule(self.current_user),
            'treatments': TreatmentsModule(self.current_user),
            'billing': BillingModule(self.current_user),
        }
        
        # Add admin-only modules
        if self.current_user.role == 'Admin':
            self.modules['staff'] = StaffModule(self.current_user)
            self.modules['reports'] = ReportsModule(self.current_user)
        
        # Add modules to stack
        for module_name, module in self.modules.items():
            self.module_stack.addWidget(module)
        
        right_layout.addWidget(self.module_stack)
        main_layout.addWidget(right_widget, 1)
        
        # Set central widget
        self.setCentralWidget(central_widget)
        
        # Show default module (patients)
        self.change_module('patients')
    
    def change_module(self, module_name: str):
        """
        Switch active module
        Equivalent to setCurrentModule in Dashboard.tsx
        """
        if module_name in self.modules:
            self.current_module = module_name
            self.module_stack.setCurrentWidget(self.modules[module_name])
    
    def handle_logout(self):
        """
        Handle logout
        Equivalent to handleLogout in App.tsx
        """
        reply = QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to logout?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.current_user = None
            self.show_login()
