"""
Patients Module
Equivalent to PatientsModule.tsx
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QDialog, QFormLayout, QMessageBox, QHeaderView
)
from PyQt6.QtCore import Qt
from typing import List, Dict, Optional
from datetime import datetime


class Patient:
    """Patient data model"""
    def __init__(self, id: str, name: str, age: int, gender: str, 
                 contact: str, email: str, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.email = email
        self.address = address
        self.registered_date = datetime.now().strftime("%Y-%m-%d")


class PatientDialog(QDialog):
    """Dialog for adding/editing patients"""
    
    def __init__(self, parent=None, patient: Optional[Patient] = None):
        super().__init__(parent)
        self.patient = patient
        self.is_edit = patient is not None
        
        self.setWindowTitle("Edit Patient" if self.is_edit else "Add New Patient")
        self.setModal(True)
        self.setMinimumWidth(500)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up dialog UI"""
        layout = QFormLayout(self)
        layout.setSpacing(16)
        
        # Create input fields
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.gender_input = QLineEdit()
        self.contact_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()
        
        # Set placeholders
        self.name_input.setPlaceholderText("Full name")
        self.age_input.setPlaceholderText("Age")
        self.gender_input.setPlaceholderText("Male/Female/Other")
        self.contact_input.setPlaceholderText("Phone number")
        self.email_input.setPlaceholderText("Email address")
        self.address_input.setPlaceholderText("Full address")
        
        # If editing, populate fields
        if self.is_edit:
            self.name_input.setText(self.patient.name)
            self.age_input.setText(str(self.patient.age))
            self.gender_input.setText(self.patient.gender)
            self.contact_input.setText(self.patient.contact)
            self.email_input.setText(self.patient.email)
            self.address_input.setText(self.patient.address)
        
        # Add fields to form
        layout.addRow("Name:", self.name_input)
        layout.addRow("Age:", self.age_input)
        layout.addRow("Gender:", self.gender_input)
        layout.addRow("Contact:", self.contact_input)
        layout.addRow("Email:", self.email_input)
        layout.addRow("Address:", self.address_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #4fb3d4;
                padding: 12px 32px;
            }
        """)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                padding: 12px 32px;
            }
        """)
        
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        layout.addRow("", button_layout)
    
    def get_data(self) -> Dict:
        """Get form data"""
        return {
            'name': self.name_input.text(),
            'age': int(self.age_input.text()) if self.age_input.text() else 0,
            'gender': self.gender_input.text(),
            'contact': self.contact_input.text(),
            'email': self.email_input.text(),
            'address': self.address_input.text(),
        }


class PatientsModule(QWidget):
    """
    Patients module widget
    Equivalent to PatientsModule component
    """
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.patients: List[Patient] = []
        self.next_id = 1
        
        # Initialize with some mock data
        self.init_mock_data()
        
        self.setup_ui()
    
    def init_mock_data(self):
        """Initialize with mock patient data"""
        # Empty by default - can add mock data here if needed
        pass
    
    def setup_ui(self):
        """Set up the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        
        # Header section
        header_layout = QHBoxLayout()
        
        title = QLabel("Patients Management")
        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        header_layout.addWidget(title)
        header_layout.addStretch()
        
        # Search box
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search patients...")
        self.search_input.setFixedWidth(300)
        self.search_input.textChanged.connect(self.filter_patients)
        header_layout.addWidget(self.search_input)
        
        # Add button
        add_button = QPushButton("+ Add New Patient")
        add_button.clicked.connect(self.add_patient)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4fb3d4;
                padding: 12px 24px;
                font-size: 16px;
            }
        """)
        header_layout.addWidget(add_button)
        
        layout.addLayout(header_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Age", "Gender", "Contact", 
            "Email", "Registered", "Actions"
        ])
        
        # Style table
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #2d3e50;
                color: white;
                border: 2px solid #4fb3d4;
                border-radius: 8px;
                font-size: 16px;
            }
            QTableWidget::item {
                padding: 12px;
            }
            QHeaderView::section {
                background-color: #1a2d3f;
                color: white;
                padding: 12px;
                font-weight: bold;
                border: none;
            }
        """)
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(7, 200)
        
        layout.addWidget(self.table)
        
        self.refresh_table()
    
    def refresh_table(self):
        """Refresh table with current patient data"""
        self.table.setRowCount(0)
        
        search_query = self.search_input.text().lower() if hasattr(self, 'search_input') else ""
        
        for patient in self.patients:
            # Filter by search query
            if search_query and search_query not in patient.name.lower():
                continue
            
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            # Add data
            self.table.setItem(row, 0, QTableWidgetItem(patient.id))
            self.table.setItem(row, 1, QTableWidgetItem(patient.name))
            self.table.setItem(row, 2, QTableWidgetItem(str(patient.age)))
            self.table.setItem(row, 3, QTableWidgetItem(patient.gender))
            self.table.setItem(row, 4, QTableWidgetItem(patient.contact))
            self.table.setItem(row, 5, QTableWidgetItem(patient.email))
            self.table.setItem(row, 6, QTableWidgetItem(patient.registered_date))
            
            # Action buttons
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(4, 4, 4, 4)
            
            edit_btn = QPushButton("Edit")
            edit_btn.clicked.connect(lambda checked, p=patient: self.edit_patient(p))
            edit_btn.setStyleSheet("QPushButton { background-color: #4fb3d4; padding: 6px 12px; }")
            
            delete_btn = QPushButton("Delete")
            delete_btn.clicked.connect(lambda checked, p=patient: self.delete_patient(p))
            delete_btn.setStyleSheet("QPushButton { background-color: #cc0000; padding: 6px 12px; }")
            
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            
            self.table.setCellWidget(row, 7, action_widget)
    
    def filter_patients(self):
        """Filter patients based on search"""
        self.refresh_table()
    
    def add_patient(self):
        """Add new patient"""
        dialog = PatientDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            patient = Patient(
                id=f"P{self.next_id:04d}",
                name=data['name'],
                age=data['age'],
                gender=data['gender'],
                contact=data['contact'],
                email=data['email'],
                address=data['address']
            )
            self.patients.append(patient)
            self.next_id += 1
            self.refresh_table()
    
    def edit_patient(self, patient: Patient):
        """Edit existing patient"""
        dialog = PatientDialog(self, patient)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            patient.name = data['name']
            patient.age = data['age']
            patient.gender = data['gender']
            patient.contact = data['contact']
            patient.email = data['email']
            patient.address = data['address']
            self.refresh_table()
    
    def delete_patient(self, patient: Patient):
        """Delete patient"""
        reply = QMessageBox.question(
            self,
            "Delete Patient",
            f"Are you sure you want to delete patient '{patient.name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.patients.remove(patient)
            self.refresh_table()
