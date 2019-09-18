from os import path
import subprocess, shlex, shutil, os
import zipfile

class Docker():

    FNULL = open(os.devnull, 'w')

    def image_exists(self, image_name):
        return self.get_image_id(image_name) != ""


    def get_image_id(self, image_name):
        out = subprocess.check_output(shlex.split("docker images -q {}".format(image_name)), encoding="UTF-8")
        return out.replace("\n", "")


    def get_container_ids(self, image_name, running_only=False):
        image_id = self.get_image_id(image_name)
        running_filter = "" if not running_only else "--filter \"status=running\""
        command = "docker ps -aq --filter \"ancestor={}\" {}".format(image_id, running_filter)
        out = subprocess.check_output(shlex.split(command), encoding="UTF-8")
        return out.replace("\n", " ").split()


    def build_image(self, image_name, dockerfile_path):
        dockerfile = path.join(dockerfile_path, "Dockerfile")
        if (path.isdir(dockerfile_path) and path.exists(dockerfile)):
            print("[*] Building the '%s' image..." % image_name)        
            try:
                p = subprocess.Popen(shlex.split("docker build -t {} .".format(image_name)), cwd=dockerfile_path)
                p.wait()
            except Exception as ex:
                print("[ERROR]: failure while building '{}': \n\t{}".format(image_name, ex))
                raise Exception(ex)
        else:
            print("[!] Could not find Dockerfile for '{}'".format(image_name))
        return self.get_image_id(image_name)


    def run_container(self, image_name, guest_port, host_port):
        if self.get_container_ids(image_name, True):
            print("[!] The container is already running")
        else:
            command = "docker run -d -p {}:{} {}".format(host_port, guest_port, image_name)
            p = subprocess.Popen(shlex.split(command), stdout=self.FNULL)
            p.wait()
        return self.get_container_ids(image_name, True)[0]


    def remove_container(self, container_id):
        try:
            p = subprocess.Popen(shlex.split("docker rm -f {}".format(container_id)), stdout=self.FNULL)
            p.wait()
        except Exception as ex:
            print("[ERROR]: failure while removing a container")
