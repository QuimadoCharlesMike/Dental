"""
Login Window
Equivalent to LoginPage.tsx
Updated with complete design system implementation
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QComboBox
)
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot, QSize
from PyQt6.QtGui import QPixmap, QIcon, QCursor
from typing import Dict, List

# Mock users - equivalent to mockUsers in LoginPage.tsx
MOCK_USERS = [
    {
        'id': '1',
        'username': 'admin',
        'password': 'admin123',
        'role': 'Admin',
        'full_name': 'Dr. Admin User'
    },
    {
        'id': '2',
        'username': 'employee',
        'password': 'emp123',
        'role': 'Employee',
        'full_name': 'Staff Member'
    }
]


class LoginWindow(QWidget):
    """
    Login window widget
    Equivalent to LoginPage component
    
    Features:
    - Account type selector (Admin/Employee)
    - Username and password fields with icons
    - Password visibility toggle
    - Secure connection badge
    - Forgot password link
    - Error message display
    - Full design system styling
    """
    
    # Signal emitted when login is successful
    login_successful = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.password_visible = False
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Set window background
        self.setStyleSheet("QWidget#LoginWindow { background-color: #2d3e50; }")
        self.setObjectName("LoginWindow")
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Login card container
        self.login_card = QFrame()
        self.login_card.setObjectName("loginCard")
        self.login_card.setMinimumWidth(600)
        self.login_card.setMaximumWidth(600)
        self.login_card.setStyleSheet("""
            QFrame#loginCard {
                background-color: rgba(26, 45, 63, 0.95);
                border: 4px solid #4fb3d4;
                border-radius: 12px;
            }
        """)
        
        card_layout = QVBoxLayout(self.login_card)
        card_layout.setContentsMargins(32, 32, 32, 32)
        card_layout.setSpacing(0)
        
        # === LOGO SECTION ===
        self.create_logo_section(card_layout)
        
        # === TITLE SECTION ===
        self.create_title_section(card_layout)
        
        # === FORM SECTION ===
        self.create_form_section(card_layout)
        
        # === SECURITY BADGE ===
        self.create_security_badge(card_layout)
        
        # === BUTTON SECTION ===
        self.create_button_section(card_layout)
        
        main_layout.addWidget(self.login_card)
    
    def create_logo_section(self, parent_layout):
        """Create logo section"""
        logo_container = QWidget()
        logo_container.setObjectName("logoContainer")
        logo_container.setMinimumHeight(220)
        logo_container.setMaximumHeight(220)
        
        logo_layout = QVBoxLayout(logo_container)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        logo_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        # Logo label
        self.logo_label = QLabel()
        self.logo_label.setObjectName("logoLabel")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setMinimumSize(80, 80)
        self.logo_label.setMaximumSize(80, 80)
        self.logo_label.setStyleSheet("""
            QLabel#logoLabel {
                background-color: #3a4f5f;
                border-radius: 16px;
                color: #4fb3d4;
                font-size: 14px;
            }
        """)
        
        # Try to load logo, fallback to placeholder
        try:
            logo_pixmap = QPixmap("assets/logo.png")
            if not logo_pixmap.isNull():
                scaled_pixmap = logo_pixmap.scaled(
                    64, 64, 
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.logo_label.setPixmap(scaled_pixmap)
            else:
                self.logo_label.setText("🦷")
                self.logo_label.setStyleSheet("""
                    QLabel#logoLabel {
                        background-color: #3a4f5f;
                        border-radius: 16px;
                        color: #4fb3d4;
                        font-size: 40px;
                    }
                """)
        except:
            self.logo_label.setText("🦷")
            self.logo_label.setStyleSheet("""
                QLabel#logoLabel {
                    background-color: #3a4f5f;
                    border-radius: 16px;
                    color: #4fb3d4;
                    font-size: 40px;
                }
            """)
        
        logo_layout.addWidget(self.logo_label)
        parent_layout.addWidget(logo_container)
    
    def create_title_section(self, parent_layout):
        """Create title section"""
        title_container = QWidget()
        title_container.setObjectName("titleContainer")
        
        title_layout = QVBoxLayout(title_container)
        title_layout.setContentsMargins(0, 0, 0, 24)
        title_layout.setSpacing(4)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        # Welcome label
        welcome_label = QLabel("WELCOME BACK")
        welcome_label.setObjectName("welcomeLabel")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("""
            QLabel#welcomeLabel {
                color: white;
                font-size: 32px;
                font-weight: bold;
            }
        """)
        title_layout.addWidget(welcome_label)
        
        # Subtitle
        subtitle_label = QLabel("Sign in to Smiley Dental Clinic")
        subtitle_label.setObjectName("subtitleLabel")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet("""
            QLabel#subtitleLabel {
                color: #4fb3d4;
                font-size: 20px;
                font-weight: 600;
            }
        """)
        title_layout.addWidget(subtitle_label)
        
        parent_layout.addWidget(title_container)
    
    def create_form_section(self, parent_layout):
        """Create form section"""
        form_container = QWidget()
        form_container.setObjectName("formContainer")
        
        form_layout = QVBoxLayout(form_container)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(16)
        
        # === ACCOUNT TYPE FIELD ===
        self.create_account_type_field(form_layout)
        
        # === USERNAME FIELD ===
        self.create_username_field(form_layout)
        
        # === PASSWORD FIELD ===
        self.create_password_field(form_layout)
        
        # === ERROR LABEL ===
        self.error_label = QLabel()
        self.error_label.setObjectName("errorLabel")
        self.error_label.setWordWrap(True)
        self.error_label.setStyleSheet("""
            QLabel#errorLabel {
                background-color: #cc0000;
                color: white;
                border: 2px solid #ff3333;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        self.error_label.hide()
        form_layout.addWidget(self.error_label)
        
        parent_layout.addWidget(form_container)
    
    def create_account_type_field(self, parent_layout):
        """Create account type dropdown"""
        container = QWidget()
        container.setObjectName("accountTypeContainer")
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        
        # Label
        label = QLabel("Account Type")
        label.setObjectName("accountTypeLabel")
        label.setStyleSheet("""
            QLabel#accountTypeLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        layout.addWidget(label)
        
        # ComboBox
        self.account_type_combo = QComboBox()
        self.account_type_combo.setObjectName("accountTypeComboBox")
        self.account_type_combo.addItems(["Admin", "Employee"])
        self.account_type_combo.setMinimumHeight(44)
        self.account_type_combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.account_type_combo.setStyleSheet("""
            QComboBox#accountTypeComboBox {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
            }
            QComboBox#accountTypeComboBox:hover {
                border-color: #5dd9c1;
            }
            QComboBox#accountTypeComboBox:focus {
                border-color: #4fb3d4;
            }
            QComboBox#accountTypeComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox#accountTypeComboBox QAbstractItemView {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                selection-background-color: #4fb3d4;
                selection-color: white;
                padding: 4px;
            }
        """)
        layout.addWidget(self.account_type_combo)
        
        parent_layout.addWidget(container)
    
    def create_username_field(self, parent_layout):
        """Create username input field"""
        container = QWidget()
        container.setObjectName("usernameContainer")
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        
        # Label
        label = QLabel("Username")
        label.setObjectName("usernameLabel")
        label.setStyleSheet("""
            QLabel#usernameLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        layout.addWidget(label)
        
        # Input field
        self.username_input = QLineEdit()
        self.username_input.setObjectName("usernameLineEdit")
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMinimumHeight(44)
        self.username_input.setStyleSheet("""
            QLineEdit#usernameLineEdit {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                padding: 12px;
                padding-left: 40px;
                font-size: 16px;
            }
            QLineEdit#usernameLineEdit:hover {
                border-color: #5dd9c1;
            }
            QLineEdit#usernameLineEdit:focus {
                border-color: #4fb3d4;
            }
        """)
        
        # Connect Enter key to move to password field
        self.username_input.returnPressed.connect(self.password_input.setFocus)
        
        layout.addWidget(self.username_input)
        
        # Add icon overlay
        icon_label = QLabel(self.username_input)
        icon_label.setObjectName("usernameIcon")
        icon_label.setText("👤")
        icon_label.setStyleSheet("""
            QLabel#usernameIcon {
                background: transparent;
                border: none;
                color: #4fb3d4;
                font-size: 16px;
            }
        """)
        icon_label.setGeometry(12, 12, 20, 20)
        
        parent_layout.addWidget(container)
    
    def create_password_field(self, parent_layout):
        """Create password input field with toggle"""
        container = QWidget()
        container.setObjectName("passwordContainer")
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        
        # Label
        label = QLabel("Password")
        label.setObjectName("passwordLabel")
        label.setStyleSheet("""
            QLabel#passwordLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        layout.addWidget(label)
        
        # Password input container (for input + toggle button)
        input_container = QWidget()
        input_container.setObjectName("passwordInputContainer")
        input_layout = QHBoxLayout(input_container)
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(0)
        
        # Input field
        self.password_input = QLineEdit()
        self.password_input.setObjectName("passwordLineEdit")
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumHeight(44)
        self.password_input.setStyleSheet("""
            QLineEdit#passwordLineEdit {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                border-top-left-radius: 8px;
                border-bottom-left-radius: 8px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
                padding: 12px;
                padding-left: 40px;
                padding-right: 12px;
                font-size: 16px;
            }
            QLineEdit#passwordLineEdit:hover {
                border-color: #5dd9c1;
            }
            QLineEdit#passwordLineEdit:focus {
                border-color: #4fb3d4;
            }
        """)
        self.password_input.returnPressed.connect(self.handle_login)
        input_layout.addWidget(self.password_input)
        
        # Toggle button
        self.toggle_password_btn = QPushButton()
        self.toggle_password_btn.setObjectName("togglePasswordButton")
        self.toggle_password_btn.setText("👁")
        self.toggle_password_btn.setMinimumSize(44, 44)
        self.toggle_password_btn.setMaximumSize(44, 44)
        self.toggle_password_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggle_password_btn.setStyleSheet("""
            QPushButton#togglePasswordButton {
                background-color: #2d3e50;
                border: 2px solid #4fb3d4;
                border-left: none;
                border-top-right-radius: 8px;
                border-bottom-right-radius: 8px;
                padding: 12px;
                font-size: 16px;
            }
            QPushButton#togglePasswordButton:hover {
                background-color: #3a4f5f;
                border-color: #5dd9c1;
            }
            QPushButton#togglePasswordButton:pressed {
                background-color: #1a2d3f;
            }
        """)
        self.toggle_password_btn.clicked.connect(self.toggle_password_visibility)
        input_layout.addWidget(self.toggle_password_btn)
        
        layout.addWidget(input_container)
        
        # Add lock icon overlay
        lock_icon = QLabel(self.password_input)
        lock_icon.setObjectName("passwordIcon")
        lock_icon.setText("🔒")
        lock_icon.setStyleSheet("""
            QLabel#passwordIcon {
                background: transparent;
                border: none;
                color: #4fb3d4;
                font-size: 16px;
            }
        """)
        lock_icon.setGeometry(12, 12, 20, 20)
        
        parent_layout.addWidget(container)
    
    def create_security_badge(self, parent_layout):
        """Create security connection badge"""
        security_container = QWidget()
        security_container.setObjectName("securityContainer")
        security_container.setMinimumHeight(30)
        security_container.setMaximumHeight(30)
        
        security_layout = QHBoxLayout(security_container)
        security_layout.setContentsMargins(0, 0, 0, 0)
        security_layout.setSpacing(6)
        security_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        # Shield icon
        shield_icon = QLabel("🛡️")
        shield_icon.setObjectName("securityIcon")
        shield_icon.setStyleSheet("""
            QLabel#securityIcon {
                color: #4fb3d4;
                font-size: 14px;
            }
        """)
        security_layout.addWidget(shield_icon)
        
        # Security label
        security_label = QLabel("Secure Connection")
        security_label.setObjectName("securityLabel")
        security_label.setStyleSheet("""
            QLabel#securityLabel {
                color: #4fb3d4;
                font-size: 12px;
            }
        """)
        security_layout.addWidget(security_label)
        
        parent_layout.addWidget(security_container)
    
    def create_button_section(self, parent_layout):
        """Create button section"""
        button_container = QWidget()
        button_container.setObjectName("buttonContainer")
        
        button_layout = QVBoxLayout(button_container)
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(12)
        
        # Sign In button
        self.sign_in_btn = QPushButton("Sign In")
        self.sign_in_btn.setObjectName("signInButton")
        self.sign_in_btn.setMinimumHeight(48)
        self.sign_in_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sign_in_btn.setDefault(True)
        self.sign_in_btn.setStyleSheet("""
            QPushButton#signInButton {
                background-color: #4fb3d4;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 16px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton#signInButton:hover {
                background-color: #3a9cb8;
            }
            QPushButton#signInButton:pressed {
                background-color: #2d8aa3;
            }
            QPushButton#signInButton:disabled {
                background-color: #6b7280;
                color: #9ca3af;
            }
        """)
        self.sign_in_btn.clicked.connect(self.handle_login)
        button_layout.addWidget(self.sign_in_btn)
        
        # Forgot Password button
        forgot_password_btn = QPushButton("Forgot Password?")
        forgot_password_btn.setObjectName("forgotPasswordButton")
        forgot_password_btn.setMinimumHeight(32)
        forgot_password_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        forgot_password_btn.setFlat(True)
        forgot_password_btn.setStyleSheet("""
            QPushButton#forgotPasswordButton {
                background-color: transparent;
                color: #4fb3d4;
                border: none;
                font-size: 14px;
                text-decoration: underline;
            }
            QPushButton#forgotPasswordButton:hover {
                color: #5dd9c1;
            }
            QPushButton#forgotPasswordButton:pressed {
                color: #3a9cb8;
            }
        """)
        forgot_password_btn.clicked.connect(self.handle_forgot_password)
        button_layout.addWidget(forgot_password_btn)
        
        parent_layout.addWidget(button_container)
    
    @pyqtSlot()
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if self.password_visible:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_password_btn.setText("👁")
            self.password_visible = False
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_password_btn.setText("👁‍🗨")
            self.password_visible = True
    
    @pyqtSlot()
    def handle_forgot_password(self):
        """Handle forgot password click"""
        # TODO: Implement forgot password dialog
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(
            self,
            "Forgot Password",
            "Please contact your system administrator to reset your password.\n\n" +
            "Admin Email: admin@smileydental.com\n" +
            "Phone: (555) 123-4567",
            QMessageBox.StandardButton.Ok
        )
    
    @pyqtSlot()
    def handle_login(self):
        """
        Handle login button click
        Equivalent to handleSubmit in LoginPage.tsx
        """
        username = self.username_input.text().strip()
        password = self.password_input.text()
        account_type = self.account_type_combo.currentText()
        
        # Hide previous error
        self.error_label.hide()
        
        # Basic validation
        if not username or not password:
            self.show_error("Please enter both username and password")
            return
        
        # Validate credentials
        user = None
        for mock_user in MOCK_USERS:
            if (mock_user['username'] == username and 
                mock_user['password'] == password and
                mock_user['role'] == account_type):
                user = mock_user
                break
        
        if user:
            # Successful login
            self.login_successful.emit({
                'id': user['id'],
                'username': user['username'],
                'role': user['role'],
                'full_name': user['full_name']
            })
        else:
            # Failed login
            self.show_error("❌ Invalid username, password, or account type")
            self.password_input.clear()
            self.password_input.setFocus()
    
    def show_error(self, message: str):
        """Show error message"""
        self.error_label.setText(message)
        self.error_label.show()
