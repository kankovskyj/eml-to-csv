import os
import csv
import email
from email import policy
from email.parser import BytesParser

# Directory containing .eml files
input_directory = "emails"

# Output CSV file
output_file = "emails.csv"

# Extract details from .eml file
def extract_from_eml(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
        
    subject = msg['subject']
    from_email = email.utils.parseaddr(msg['from'])[1]
    to_email = email.utils.parseaddr(msg['to'])[1]
    date = msg['date']
    
    body = ""  # Initialize body as an empty string
    
    # Extracting the body
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get_content_disposition())
            
            # Only consider text/plain parts
            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                body += part.get_payload(decode=True).decode(errors='replace')  # Use 'replace' to handle decoding errors
    else:
        # Directly get the payload if it's not multipart
        body = msg.get_payload(decode=True).decode(errors='replace')  # Use 'replace' to handle decoding errors
    
    return subject, from_email, to_email, date, body

    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
        
    subject = msg['subject']
    from_email = email.utils.parseaddr(msg['from'])[1]
    to_email = email.utils.parseaddr(msg['to'])[1]
    date = msg['date']
    
    body = ""  # Initialize body as an empty string
    
    # Extracting the body
    if msg.is_multipart():
        for part in msg.iter_parts():
            content_type = part.get_content_type()
            content_disposition = str(part.get_content_disposition())
            
            # Skip any text/plain (txt) attachments
            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                body = part.get_payload(decode=True).decode(errors='replace')  # Use 'replace' to handle decoding errors
                break
    else:
        # Directly get the payload if it's not multipart
        body = msg.get_payload(decode=True).decode(errors='replace')  # Use 'replace' to handle decoding errors
    
    return subject, from_email, to_email, date, body

# Write details to CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Subject', 'From', 'To', 'Date', 'Body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".eml"):
            subject, from_email, to_email, date, body = extract_from_eml(os.path.join(input_directory, filename))
            writer.writerow({'Subject': subject, 'From': from_email, 'To': to_email, 'Date': date, 'Body': body})

print(f"Data extracted to {output_file}")
