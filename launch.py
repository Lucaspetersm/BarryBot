#!/usr/bin/env python3

import time, platform, sys
from os.path import isfile

launch_program = "_run.py"
relaunch_delay = 10

env = {}

def launch(program=launch_program):
    global env
    
    env_l = {}
    report = str()
    report_name = str()
    report_suffix = 1
    val_container = str()
    val_multiline = bool()
    
    try:
        with open(launch_program) as f:
            code = compile(f.read(), program, 'exec')
            exec(code, env_l)
    except Exception as e:
        env = env_l
        report_name = "crash_" + time.strftime("%Y-%m-%d-utc", time.gmtime())

        print("[ERROR] It looks like something broke! Generating crash report.")

        if isfile(report_name + ".txt"):
            while isfile(report_name + '_' + str(report_suffix) + ".txt"):
                report_suffix += 1

            report_name += '_' + str(report_suffix)

        report_name += ".txt"

        try:
            with open(report_name, 'w', encoding="utf-8") as report_file:
                report_file.write("It looks like something broke!\n\n")

                if "ver" in env_l:
                    report_file.write("ver: '" + str(env_l['ver']) + "'\n\n")
                else:
                    report_file.write("ver: undefined\n\n")

                report_file.write(
                    "platform.platform: '{}'\n".format(platform.platform()) +
                    "platform.python_version: '{}'\n".format(platform.python_version()) + 
                    "is_64bits: {}\n\n".format(sys.maxsize > 2**32) +
                    "e.__class__.__name__: {}\n".format(e.__class__.__name__) +
                    "e.args: {}\n\n".format(e.args)
                )

                for var in ("__builtins__", "ver", "reddit_pass", "discord_key"):
                    try:
                        del env_l[var]
                    except KeyError:
                        pass

                for var,val in env_l.items():
                    val_container = ''
                    val_multiline = False
                    report = str(var) + ': '
                    
                    if type(env_l[var]) is str:
                        if '\n' in env_l[var]:
                            val_container = "'''"
                            val_multiline = True
                        else:
                            val_container = "'"

                    report += "{0}{1}{0}\n".format(val_container, val)

                    if val_multiline:
                        report = '\n' + report + '\n'

                    report_file.write(report)
        except IOError:
            print ("[ERROR] Unable to save crash report.")
        else:
            print ("[INFO] Crash report saved as '" + report_name + "'")

if __name__ in ("__main__", "__builtins__"):
    while True:
        launch()
        if relaunch_delay > 0:
            time.sleep(relaunch_delay)
