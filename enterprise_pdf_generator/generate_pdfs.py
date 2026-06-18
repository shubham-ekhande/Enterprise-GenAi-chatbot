import os
import random
from faker import Faker

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


fake = Faker()
styles = getSampleStyleSheet()


OUTPUT_FOLDER = "generated_pdfs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
# COMPANY INFORMATION
# =====================================================

company_names = [
    "NextGen Technologies",
    "VisionAI Solutions",
    "CloudNova Pvt Ltd",
    "QuantumSoft Systems",
    "Apex Analytics"
]


departments = [
    "Human Resources",
    "Engineering",
    "AI Research",
    "Cybersecurity",
    "Finance",
    "Marketing"
]
policies = [
    "Remote work is allowed twice a week.",
    "Employees must maintain data confidentiality.",
    "All employees should follow cybersecurity guidelines.",
    "Passwords must be updated every 90 days.",
    "Annual performance reviews are mandatory.",
    "Employees receive health insurance benefits.",
    "VPN usage is mandatory for remote work.",
    "Workplace harassment is strictly prohibited."
]


products = [
    "AI Chatbot Platform",
    "Cloud Security Scanner",
    "Business Analytics Dashboard",
    "Smart Attendance System",
    "Customer Intelligence Platform"
]
# PDF CREATOR FUNCTION
# =====================================================


def create_pdf(file_name, title, content_lines):

    file_path = os.path.join(OUTPUT_FOLDER, file_name)

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )

    story = []

    title_style = styles['Heading1']
    normal_style = styles['BodyText']

    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 20))

    for line in content_lines:
        story.append(Paragraph(line, normal_style))
        story.append(Spacer(1, 10))

    doc.build(story)

    print(f"PDF Created: {file_path}")

# EMPLOYEE HANDBOOK
# =====================================================


def generate_employee_handbook():

    company = random.choice(company_names)

    content = [
        f"Welcome to {company}.",
        "Employees are expected to maintain professionalism at all times.",
        "Working hours are from 9 AM to 6 PM.",
        "Employees should adhere to the company dress code.",
        "Attendance above 90% is required.",
        "Performance reviews are conducted every six months.",
        random.choice(policies),
        random.choice(policies)
    ]

    create_pdf(
        "employee_handbook.pdf",
        "Employee Handbook",
        content
    )
    # LEAVE POLICY
# =====================================================


def generate_leave_policy():

    content = [
        "Employees receive 12 casual leaves annually.",
        "Employees receive 10 sick leaves annually.",
        "Emergency leave requests are prioritized.",
        "Paid leave requires manager approval.",
        "Maternity leave is provided according to company policy.",
        "Unused leaves can be carried forward based on HR rules."
    ]

    create_pdf(
        "leave_policy.pdf",
        "Leave Policy",
        content
    )
    # CYBERSECURITY POLICY
# =====================================================


def generate_cybersecurity_policy():

    content = [
        "Passwords must contain uppercase letters and numbers.",
        "Employees must not share confidential data externally.",
        "Company VPN is mandatory for remote access.",
        "Suspicious emails should be reported immediately.",
        "USB device usage is restricted.",
        "Multi-factor authentication is enabled for all accounts.",
        random.choice(policies),
        random.choice(policies)
    ]

    create_pdf(
        "cybersecurity_policy.pdf",
        "Cybersecurity Policy",
        content
    )
# COMPANY OVERVIEW
# =====================================================


def generate_company_overview():

    company = random.choice(company_names)

    content = [
        f"{company} is a global technology organization.",
        f"Headquarters: {fake.city()}, India",
        f"Founded: {random.randint(2010, 2022)}",
        "The company specializes in AI, Cloud, and Data Analytics.",
        "The mission is to deliver enterprise digital transformation.",
        "The vision is to become a leader in AI-powered business automation.",
        f"Main Department: {random.choice(departments)}"
    ]

    create_pdf(
        "company_overview.pdf",
        "Company Overview",
        content
    )
# PRODUCT MANUAL
# =====================================================


def generate_product_manual():

    product = random.choice(products)

    content = [
        f"Product Name: {product}",
        "This platform provides enterprise AI automation.",
        "Users can upload data and generate reports.",
        "The product supports cloud deployment.",
        "Security and encryption are enabled by default.",
        "The dashboard includes analytics visualization.",
        "The product integrates with enterprise APIs.",
        "Technical support is available 24/7."
    ]

    create_pdf(
        "product_manual.pdf",
        "Product Manual",
        content
    )
    # FINANCE REPORT
# =====================================================


def generate_finance_report():

    revenue = random.randint(10, 100)
    expenses = random.randint(5, 50)

    content = [
        f"Quarterly Revenue: ${revenue} Million",
        f"Quarterly Expenses: ${expenses} Million",
        f"Net Profit: ${revenue - expenses} Million",
        "AI division generated highest revenue growth.",
        "Cloud services adoption increased by 35%.",
        "Cybersecurity solutions expanded globally.",
        "Operational efficiency improved through automation."
    ]

    create_pdf(
        "finance_report.pdf",
        "Quarterly Finance Report",
        content
    )
# IT SUPPORT MANUAL
# =====================================================


def generate_it_support_manual():

    content = [
        "Employees should raise tickets through the IT portal.",
        "Password reset requests are handled within 24 hours.",
        "VPN issues should be reported immediately.",
        "System updates occur every Friday evening.",
        "Company laptops must use approved antivirus software.",
        "Unauthorized software installation is prohibited."
    ]

    create_pdf(
        "it_support_manual.pdf",
        "IT Support Manual",
        content
    )
    # CLIENT AGREEMENT
# =====================================================


def generate_client_agreement():

    client_name = fake.company()

    content = [
        f"Client Name: {client_name}",
        "This agreement defines service delivery responsibilities.",
        "Confidentiality must be maintained at all times.",
        "Payment terms are net 30 days.",
        "Project milestones should be completed on schedule.",
        "The agreement remains valid for one year.",
        "Termination conditions are defined by legal compliance."
    ]

    create_pdf(
        "client_agreement.pdf",
        "Client Service Agreement",
        content
    )
# GENERATE ALL PDFs
# =====================================================


def generate_all_pdfs():

    generate_employee_handbook()
    generate_leave_policy()
    generate_cybersecurity_policy()
    generate_company_overview()
    generate_product_manual()
    generate_finance_report()
    generate_it_support_manual()
    generate_client_agreement()

    print("\nAll enterprise PDFs generated successfully.")
# MAIN
# =====================================================

if __name__ == "__main__":
    generate_all_pdfs()