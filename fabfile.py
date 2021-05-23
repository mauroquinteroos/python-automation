from fabric.api import run, sudo, task, put, get, cd, prefix, local, env

env.hosts = ['165.22.47.187']
env.user = 'mauro'
env.key_filename = '~/.ssh/id_ed25519.pub'

def deploy_pull():
    run('git pull')

def install():
    run('pip install -r requirements.txt')

@task
def deploy():
    with cd('python-web'):
        deploy_pull()
        with prefix('source env/bin/activate'):
            install()
        sudo('systemctl restart nginx')


@task
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
    # run('cd ./python-web && git pull')
    with cd('python-web'):
        run('git pull')

@task
def install_requirements():
    with cd('python-web'):
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')

@task
def show_local_dir():
    local('ls -la')