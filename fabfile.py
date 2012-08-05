from datetime import datetime
from fabric.api import env, cd, run, task, prefix
from fabric.contrib.files import exists

import local_fab_settings

env.environment_set = False


def setup_env():
    env.user = local_fab_settings.USER
    env.key_filename = local_fab_settings.KEY_FILENAME
    env.hosts = local_fab_settings.HOSTS
    env.code_dir = local_fab_settings.VMFARMS_CODE_DIR
    env.forward_agent = True
    env.virtualenv = local_fab_settings.VMFARMS_VIRTUAL_ENV_DIR

    env.environment_set = True


def archive_installation_if_exists():
    with cd(env.code_dir):
        if exists('django-toronto'):
            dir_postfix = datetime.now().isoformat()
            new_dir_name = 'django-toronto-{0}'.format(dir_postfix)
            print "Moving old install to {0}".format(new_dir_name)
            run("mv -f django-toronto {0}".format(new_dir_name))


def check_if_installation_exists():
    with cd(env.code_dir):
        if exists('django-toronto'):
            raise Exception("Application is already installed.")


def setup_installation():
    with cd(env.code_dir):
        # checkout the code
        run('git clone git@github.com:ashchristopher/django-toronto.git django-toronto')


def install_requirements():
    with cd(env.code_dir):
        # install the requirements in the virtualenv
        with prefix('source {0}bin/activate'.format(env.virtualenv)):
            run('pip install -r django-toronto/requirements.txt')


def update_code_from_github(tag):
    with cd(env.code_dir):
        with cd('django-toronto'):
            run('git fetch')
            run('git checkout {0}'.format(tag))
            run('git pull --rebase origin {0}'.format(tag))


def update_database():
    with cd(env.code_dir):
        with cd('django-toronto'):
            run('python ./manage.py syncdb')
            run('python ./manage.py migrate')


@task
def provision():
    """ Installs the django-toronto app. """
    check_if_installation_exists()
    setup_installation()


@task
def deploy(tag):
    """ Deploys a specified `tag`. """
    print "Deploying {0}".format(tag)

    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        update_code_from_github(tag)
        install_requirements()
        update_database()

        # collect static

        # restart app servers


@task
def archive():
    """ Archives the current installation to a timestamped folder. """
    archive_installation_if_exists()

setup_env()
