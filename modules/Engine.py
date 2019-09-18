import os, shutil, zipfile, signal, sys
from modules.Docker import Docker

app_images_path = os.path.abspath(os.path.join(os.getcwd(), "apps"))

class Engine():

    def __init__(self, app_name, guest_port=8888, host_port=80):
        self.docker_guest_port = guest_port
        self.docker_host_port = host_port
        self.docker = Docker()
        self.app_name = app_name


    def run(self):
        container_id = None
        try:
            self.setup_the_app(self.app_name)
            container_id = self.docker.run_container(self.app_name, guest_port=self.docker_guest_port, host_port=self.docker_host_port)
            signal.signal(signal.SIGINT, self.signal_handler)
            print("\n[*] Press Ctr+C to kill the container.")
            signal.pause()
        except Exception as ex:
            raise Exception(ex)
        finally:
            if (container_id != None):
                self.docker.remove_container(container_id)


    def signal_handler(self, signal, frame):
        try:
            sys.exit(0)
        except:
            pass


    def setup_the_app(self, app_name):
        app_path = os.path.join(app_images_path, app_name)
        temp_path = os.path.join(app_path, "temp")

        if self.docker.image_exists(app_name):
            print("[!] The image for \'{}\' has been already built, skipping".format(app_name))
            return self.docker.get_image_id(app_name)

        # unzip the application files
        _zip = zipfile.ZipFile(os.path.join(app_path, app_name + ".zip"), "r")
        _zip.extractall(temp_path)
        _zip.close()

        # copy temp files to the app folder (e.g., Dockerfile)
        shutil.copy(os.path.join(app_path, "Dockerfile"), temp_path)
        shutil.copy(os.path.join(app_path, "run.sh"), temp_path)

        self.docker.build_image(app_name, temp_path)
        shutil.rmtree(temp_path)
