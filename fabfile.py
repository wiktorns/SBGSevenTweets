from fabric.api import local, run, env

env.hosts = ["if.sedamcvrkuta.com"]
env.user = "root"

repository = "viktorbek/seventweets"
network = "radionica"
hostPort = 80
appPort = 8000
name = "test"


def list_containers():
    run("docker ps -a")


def build_image(tag=""):
    if tag is not "":
        tag = ":" + tag
    local(f"docker build -t{repository}{tag} .")


def push_image(tag=""):
    if tag is not "":
        tag = ":" + tag
    local(f"docker push {repository}{tag}")


def pull_image(tag=""):
    if tag is not "":
        tag = ":" + tag
    run(f"docker pull {repository}{tag}")


def create_network():
    run(f"docker network create {network}")


def run_container(tag=""):
    if tag is not "":
        tag = ":" + tag
    run(f"""
    docker run -d \
        --name {name} \
        --net {network} \
        -p {hostPort}:{appPort} \
    {repository}{tag}
    """)


def stop_container():
    run(f"docker stop {name}")
    run(f"docker rm {name}")


def restart_container():
    stop_container()
    run_container()


def deploy(tag=""):
    build_image(tag)
    push_image(tag)
    stop_container()
    #create_network()
    pull_image(tag)
    run_container(tag)