{
    "name" : "HMS_AlaaAbouZied",
    "description" : "hmsalaa",
    "author" : "Alaa AbouZied",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_view.xml',
        'views/hms_department_view.xml',
        'views/hms_doctors_view.xml',
        'views/hms_log_history_view.xml',
        'views/crm_customer_view.xml',
        'reports/report.xml',
        'reports/template.xml',
    ],
    'depends': [
        'base', 
        'crm'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
