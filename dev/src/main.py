import platform
import distro
import sys
import requests
import json

from collections import namedtuple

argv = sys.argv
cmd = namedtuple("Command", ["name", "desc"])

class app:
    current_ver = "0.0.1"

commands = (

cmd("install", " - Installs a package which is gived in arg."),
cmd("help", " - Shows help menu (btw this menu)"),
cmd("update", " - Will update the program"),
cmd("info", " - Shows info about the package manager")

)

#get_os look the distro main /for example: Current os is Ubuntu but ubuntu based on debian./
def get_os():
    if platform.system() == "Darwin":
        return "Mac OS"
    if platform.system() == "Linux":
        package_manager = None
        distroN = distro.linux_distribution()
        if distro.like() in ["ubuntu", "debian"]:
            package_manager = "apt"
        if distro.like() == "arch":
            package_manager = "pacman"
        if distro.like() == "rhel":
            package_manager = "rpm"
        if distro.like() == "fedora":
            package_manager = "yum"
        if distro.like() == "sles":
            package_manager = "zypper"
        elif package_manager == None:
            package_manager = "\aDont supported or can't find\a"
        return (distroN, distro.id(), distro.like(), package_manager)

OSINFO = get_os()

def make_info(os):

    print("-" * 75)
    print("OS info:")
    print("     OS dist: ", os[0])
    print("     OS name: ", os[1])
    print("     OS like: ", os[2])
    print("     OS Package Manager: ", os[3])

    print("-"*33, "APP INFO", "-"*32)
    #App info section
    print("App info:")
    print("     APP version: ", app.current_ver)

    print("-" * 75)

    if os[3] == "\aDont supported or can't find\a":
        print("[ERROR] - Can't find (or) Dont supported package manager.")
        print("[INFO] - Exiting")
        exit()

def help_menu():
    print("-"*33, "HELP", "-"*38)
    for command in commands:
        print("     ", command.name, end=" ")
        print("     ", command.desc)

    print("-" * 75)

def handle_argv(arg):
    pass

def check_updates(req, current_ver):
    url = "https://api.github.com/repos/MendeburMarul/SPM/contents/req/latest-app-data.spmdata"
    req = requests.get(url)
    print(req.json())



make_info(OSINFO)
help_menu()
job = handle_argv(argv)  #arg handling so program can understand what type job need to be done. Returns Job types and some params if job type is installing
check_updates(requests, app.current_ver)  #check update in network.
