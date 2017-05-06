from fabric.api import local, run, env, settings

env.hosts = ["if.sedamcvrkuta.com"]
env.user = "root"

repository = "viktorbek/seventweets"
network = "radionica"
hostPort = 80
appPort = 8000
name = "test"

pg_user = "radionica"
pg_pass = "P4ss"
pg_port = 5432
pg_version = "9.6.2"
pg_volume = "radionica-postgres-data"


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
    with settings(warn_only=True):
        run(f"docker network create {network}")


def create_volume():
    with settings(warn_only=True):
        run(f"docker volume create {pg_volume}")


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
    create_network()
    pull_image(tag)
    run_container(tag)


def db_start():
    with settings(warn_only=True):
        run(f"docker volume create {pg_volume}")

    run(f"""docker run -d \             
        --name radionica-postgres \             
        --net {network} \             
        --restart unless-stopped \             
        -e POSTGRES_USER={pg_user} \             
        -e POSTGRES_PASSWORD={pg_pass} \             
        -v {pg_volume}:/var/lib/postgresql/data \             
        -p 0.0.0.0:5432:5432 \             
        postgres:{pg_version}         
        """)


def db_stop():
    run("docker stop radionica-postgres")
    run("docker rm radionica-postgres")


def deploy_db():
    with settings(warn_only=True):
        create_volume()
        create_network()

    run(f"""docker run -d \
        --name radionica-postgres \
        --net {network} \
        --restart unless-stopped \
        -e POSTGRES_USER={pg_user} \
        -e POSTGRES_PASSWORD={pg_pass} \
        -v {pg_volume}:/var/lib/postgresql/data \
        postgres:{pg_version}
        """)