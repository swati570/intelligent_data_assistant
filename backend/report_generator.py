from reportlab.pdfgen import canvas

def generate_report(df, insights):
    c = canvas.Canvas("report.pdf")
    c.drawString(100, 800, "Intelligent Data Analysis Report")
    c.drawString(100, 780, f"Insights: {insights[:500]}")
    c.save()
