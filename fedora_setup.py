import subprocess
import logging
import os


def confirm_root_status():
    if os.getuid() != 0:
        raise Exception("Please run it with sudo")

def update_dnf_config():
    confirm_root_status()
    logging.info("updating file: /etc/dnf/dnf.conf")
    logging.info("updating download speed of dnf")
    file = open("/etc/dnf/dnf.conf", "a")
    file.writelines(["fastestmirror=True\n",
                      "defaultyes=True\n", 
                      "max_parallel_downloads=10\n"
                      ])
    file.close()
    logging.info("added three line ")
    logging.info("\n".join(["fastestmirror=True\n",
                      "defaultyes=True\n", 
                      "max_parallel_downloads=10\n"
                      ]))
    
    command = ["sudo", "dnf", "update", "-y"]
    subprocess.run(command)
    logging.info("dnf package update succesfully")


def install_rpm_fusion():
    logging.info("adding rpmfusion repo")
    command = [
        "sudo"
        "dnf",
        "install",
        "https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm",
        "https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
        "-y"
    ]
    subprocess.run(command)
    logging.info("Sccessfully added rpmfusion repo")
    command = [
        "sudo", "dnf", "update", "-y"
    ]
    subprocess.run(command)
    logging.info("cache update successfull")
    


command = ["ls", "-l"]
subprocess.run(command)