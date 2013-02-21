import sublime
import sublime_plugin
import os
import shutil
from time import sleep

class BisCtrlCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("MAPPER Control Line:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        if self.window.active_view():
            self.window.active_view().run_command("bis_exec", {"text": text} )

class BisExecCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):

        path      = self.view.file_name()
        directory = os.path.dirname(path)
        file_name = os.path.basename(path)
        directory = directory + "\BisCmd.bis"
        output    = path + "|" + file_name + "|" + text
        current_user = os.environ.get("USERNAME")

        #  Check if BisCmd script is registered
        if os.path.exists("C:\Unisys\Clients\MPC\Scripts\BisCmd.ATR"):

            # shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.ATR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisCmd.ATR")
            # shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.SCR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisCmd.SCR")

            print "Writing BisCmd file"
            with open(directory, "w") as textfile:
                textfile.write(output)

            self.view.window().run_command("exec", {
              "cmd": ['C:\Unisys\Clients\MPC\mpcapi32.exe -cBisCmd -dMAPPER.MSF'],
              "shell": True
            })

        #  Check if BisCmd script is registered
        elif os.path.exists("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.ATR"):

            # shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.ATR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisCmd.ATR")
            # shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.SCR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisCmd.SCR")

            print "Writing BisCmd file"
            with open(directory, "w") as textfile:
                textfile.write(output)

            self.view.window().run_command("exec", {
              "cmd": ['C:\Unisys\Clients\MPC$1\mpcapi32.exe -cBisCmd -dMAPPER.MSF'],
              "shell": True
            })

        else:
            print "Could not find BisExec script in current directory"
            # print "Now creating it..."

            # self.view.window().run_command("exec", {
            #     "cmd": ['C:\Unisys\Clients\MPC$1\GIScriptMaker.exe WINDOWS BisCmd mapperguest E WINNE 14 BisCmd Workstation arthur2 3986 map '' 0 N'],
            #     "shell": True
            # })

            # for secs in range(5):
            #     if os.path.exists("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.ATR"):

            #         print "File Exists!"
            #         shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.ATR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisCmd.ATR")
            #         shutil.copy("C:\Unisys\Clients\MPC$1\Scripts\BisCmd.SCR", "C:\Documents and Settings\winne\Application Data\Unisys\Clients\MPC5.4\Scripts\BisCmd.SCR")

            #         print "Writing BisCmd file"
            #         with open(directory, "w") as textfile:
            #             textfile.write(output)

            #         self.view.window().run_command("exec", {
            #           "cmd": ['C:\Unisys\Clients\MPC$1\mpcapi32.exe -cBisCmd -dMAPPER.MSF'],
            #           "shell": False
            #         })
            #         break

            #     else:
            #         sleep(1)
            #         if secs == 4:
            #             print "Could not create or find BisCmd.ATR in 5 seconds..."