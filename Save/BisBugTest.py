import sublime
import sublime_plugin
import os
import shutil
from time import sleep

class BisBugCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        full_name = self.view.file_name()
        file_name = os.path.split(full_name)
        current_user = os.environ.get("USERNAME")
        print full_name
        print file_name



        self.view.window().run_command("exec", {
            "cmd": ['C:\Unisys\Clients\MPC$1\GIScriptMaker.exe WINDOWS BisBug mapperguest E WINNE 7 BisBug Workstation arthur2 3986 map bass 0 N'],
            "shell": True
        })

        #  Start for loop the check if the script file was created
        #  we should only need to wait for 5 seconds if it doesn't complete before that bail out
        for secs in range(5):
            if os.path.exists("C:\Unisys\Clients\MPC$1\Scripts\BisBug.ATR"):

                print "File Exists!"
                shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisBug.ATR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisBug.ATR")
                shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisBug.SCR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisBug.SCR")

                print "Writing BisBug command file"
                with open("S:\Bis-Files\Site-E\Winne\IT220-255\BisBug.bis", "w") as textfile:
                    textfile.write("24d102")

                self.view.window().run_command("exec", {
                  "cmd": ['C:\Unisys\Clients\MPC$1\mpcapi32.exe -cBisBug -dMAPPER.MSF'],
                  "shell": True
                })
                break

            else:
                sleep(1)
                if secs == 4:
                    print "Could not create or find BisBug.ATR in 5 seconds..."