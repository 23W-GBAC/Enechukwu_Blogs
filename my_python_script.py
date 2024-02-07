import psutil
import speedtest
import time
import smtplib
from email.mime.text import MIMEText

def get_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    return download_speed, upload_speed

def send_email(to_email, subject, message):
    # Replace these with your email details
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    
    # Set up the email server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email message
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    # Send the email
    server.sendmail(sender_email, to_email, msg.as_string())

    # Close the connection
    server.quit()

def monitor_and_output():
    while True:
        download_speed, upload_speed = get_speed()

        print(f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")

        if download_speed < 5 or upload_speed < 5:
            # Internet speed is below 5 Mbps, send an email
            to_email = "provider_email@example.com"
            subject = "Internet Speed Alert"
            message = "Dear Internet Provider,\n\nMy internet speed is below 5 Mbps. Please check and resolve the issue.\n\nBest regards,\nYour Name"
            
            send_email(to_email, subject, message)

        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

if __name__ == "__main__":
    monitor_and_output()
