import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Domain references
DOMAIN = "https://YOUR_PRODUCTION_DOMAIN.com"

# 1. Update Title and Description in <head>
# Find the <title> tag
content = re.sub(r'<title>.*?</title>', '<title>AK Kidney Care Center | Kidney Specialist & Dialysis Care in Maharashtra</title>', content)
# Find name="title"
content = re.sub(r'<meta name="title" content=".*?">', '<meta name="title" content="AK Kidney Care Center | Kidney Specialist & Dialysis Care in Maharashtra">', content)
# Find description
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="AK Kidney Care Center provides kidney care, nephrology consultation, dialysis, CKD management and kidney health services in Karjat, Shrigonda and Daund, Maharashtra.">', content)

# 2. Open Graph tags
content = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="AK Kidney Care Center | Kidney Specialist & Dialysis Care in Maharashtra">', content)
content = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="AK Kidney Care Center provides kidney care, nephrology consultation, dialysis, CKD management and kidney health services in Karjat, Shrigonda and Daund, Maharashtra.">', content)
content = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{DOMAIN}/">', content)
content = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{DOMAIN}/images/og-image.jpg">\n    <meta property="og:image:width" content="1200">\n    <meta property="og:image:height" content="630">\n    <meta property="og:image:alt" content="AK Kidney Care Center">', content)
content = re.sub(r'<meta property="og:locale" content=".*?">', '<meta property="og:locale" content="en_IN">', content)

# 3. Twitter tags
content = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="AK Kidney Care Center | Kidney Specialist & Dialysis Care in Maharashtra">', content)
content = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="AK Kidney Care Center provides kidney care, nephrology consultation, dialysis, CKD management and kidney health services in Karjat, Shrigonda and Daund, Maharashtra.">', content)
content = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{DOMAIN}/images/og-image.jpg">', content)

# 4. Canonical
content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{DOMAIN}/">', content)

# 5. Replace fake JSON-LD
# We will remove the old JSON-LD scripts and inject the new ones before </head>
# First, remove existing ones (very crude but works for this structure)
content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)

# Now, prepare the new JSON-LD
new_json_ld = f"""
    <!-- Structured Data: Medical Business (Branches) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "MedicalClinic",
        "name": "AK Kidney Care Center - Karjat",
        "medicalSpecialty": "Nephrology",
        "url": "{DOMAIN}/",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "H223+MR3, Gaykarwadi",
          "addressLocality": "Karjat",
          "addressRegion": "Maharashtra",
          "postalCode": "414402",
          "addressCountry": "IN"
        }}
      }},
      {{
        "@context": "https://schema.org",
        "@type": "MedicalClinic",
        "name": "AK Kidney Care Center - Shrigonda",
        "medicalSpecialty": "Nephrology",
        "url": "{DOMAIN}/",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Wadali Rd, near BSNL Office",
          "addressLocality": "Shrigonda",
          "addressRegion": "Maharashtra",
          "postalCode": "413701",
          "addressCountry": "IN"
        }}
      }},
      {{
        "@context": "https://schema.org",
        "@type": "MedicalClinic",
        "name": "AK Kidney Care Center - Daund",
        "medicalSpecialty": "Nephrology",
        "url": "{DOMAIN}/",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "FH3P+GF6 Mission Human Park, Road, behind Kalpataru Developers, Lingali",
          "addressLocality": "Daund",
          "addressRegion": "Maharashtra",
          "postalCode": "413801",
          "addressCountry": "IN"
        }}
      }}
    ]
    </script>
"""
content = content.replace('</head>', new_json_ld + '</head>')

# Replace fake texts in the HTML body if any (we already did JSON, let's check for body text just in case)
content = content.replace('Springfield', 'Maharashtra')
content = content.replace('123 Medical Center Drive, Suite 200', 'Karjat, Maharashtra')
content = content.replace('+1-555-123-4567', '')
content = content.replace('info@akkidneycare.com', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
