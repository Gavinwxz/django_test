from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/Gavinwxz/django_test"

env.user = 'gavin'
env.password = 'xiaozhu110'

env.hosts = ['bixiaoyao.shop']

env.port = '27488'


def deploy():
    source_folder = '/home/gavin/sites/bixiaoyao.shop/django_test'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart wode')
    sudo('service nginx reload')