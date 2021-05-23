from fabric.api import run, sudo, task, put, get

def show_dir():
    run('ls -la')

def create_folder(folder):
    run(f'mkdir {folder}')

def delete_folder(folder):
    sudo(f'rm -rf {folder}')

def hello_world():
    print('Hello worlf from Fabric!')

def bye():
    print('Bye Frabic!')

@task
def upload_txt_file():
    put(
        local_path="./example.txt",
        remote_path="./python-web"
    )

@task
def get_txt_file(file):
    get(
        local_path="./download",
        remote_path=f"./python-web/{file}"
    )

@task
def pull():
    run('cd ./python-web && git pull')