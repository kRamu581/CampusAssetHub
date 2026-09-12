
import glob
import re

files = [
    "sp_widget_53238a8493cfc750929a7c5efaba100d.xml", # Quick Actions
    "sp_widget_687382c493cfc750929a7c5efaba1091.xml", # How It Works
    "sp_widget_b3934ac493cfc750929a7c5efaba10c9.xml", # Key Features
    "sp_widget_79e3c20893cfc750929a7c5efaba10fb.xml", # Impact Stats
    "sp_widget_d314c60893cfc750929a7c5efaba10fd.xml"  # Footer
]

def dark_mode_css(css):
    # Colors
    css = re.sub(r"(background(?:-color)?:\s*)#ffffff", r"\1#1F1F1F", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#f3f4f6", r"\1#181818", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#f8fafc", r"\1#181818", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#eff6ff", r"\1rgba(83,186,0,0.1)", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#dbeafe", r"\1rgba(83,186,0,0.15)", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)white", r"\1#1F1F1F", css, flags=re.IGNORECASE)
    
    # Text colors
    css = re.sub(r"(color:\s*)#111827", r"\1#FFFFFF", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#0F172A", r"\1#FFFFFF", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#1E293B", r"\1#FFFFFF", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#1f2937", r"\1#FFFFFF", css, flags=re.IGNORECASE)
    
    css = re.sub(r"(color:\s*)#4b5563", r"\1#B0B0B0", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#6b7280", r"\1#B0B0B0", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#475569", r"\1#B0B0B0", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#64748B", r"\1#B0B0B0", css, flags=re.IGNORECASE)
    
    # Accents (Blue -> Green)
    css = re.sub(r"(color:\s*)#2563eb", r"\1#53BA00", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#4F46E5", r"\1#53BA00", css, flags=re.IGNORECASE)
    css = re.sub(r"(color:\s*)#3b82f6", r"\1#53BA00", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#2563eb", r"\1#53BA00", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#4F46E5", r"\1#53BA00", css, flags=re.IGNORECASE)
    css = re.sub(r"(background(?:-color)?:\s*)#3b82f6", r"\1#53BA00", css, flags=re.IGNORECASE)
    css = re.sub(r"(border-color:\s*)#2563eb", r"\1#53BA00", css, flags=re.IGNORECASE)
    
    # Borders
    css = re.sub(r"(border.*?(?:solid|px)\s*)#e5e7eb", r"\1rgba(255,255,255,0.08)", css, flags=re.IGNORECASE)
    css = re.sub(r"(border.*?(?:solid|px)\s*)#e2e8f0", r"\1rgba(255,255,255,0.08)", css, flags=re.IGNORECASE)
    css = re.sub(r"(border.*?(?:solid|px)\s*)#f1f5f9", r"\1rgba(255,255,255,0.08)", css, flags=re.IGNORECASE)
    css = re.sub(r"(border.*?(?:solid|px)\s*)#f3f4f6", r"\1rgba(255,255,255,0.08)", css, flags=re.IGNORECASE)
    
    return css

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    def replacer(match):
        css_content = match.group(1)
        new_css = dark_mode_css(css_content)
        return "<css>" + new_css + "</css>"
        
    new_content = re.sub(r"<css>(.*?)</css>", replacer, content, flags=re.DOTALL)
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(new_content)
    print("Updated", f)

