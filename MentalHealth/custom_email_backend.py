import smtplib
from django.core.mail.backends.smtp import EmailBackend

class CustomSSLEmailBackend(EmailBackend):
    def open(self):
        """
        Creates a secure SSL connection to the SMTP server.
        """
        if self.connection:
            return False
        
        try:
            self.connection = smtplib.SMTP_SSL(self.host, self.port, timeout=self.timeout)
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if not self.fail_silently:
                raise