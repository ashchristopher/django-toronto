from fabric.api import env, cd, run

env.environment_set = False


def vmfarms():
    env.environment_set = True


def install():
    """ Installs the django-toronto app. """
    pass


def deploy(tag):
    """ Deploys a specified `tag`. """
    print "Deploying {0}".format(tag)
    with cd(env.code_dir):
        pass


try:
    import local_fab_settings
except ImportError:
    pass
else:
    if getattr(local_fab_settings, 'USERNAME', None):
        env.user = local_fab_settings.USERNAME

    if getattr(local_fab_settings, 'KEY', None):
        env.key_filename = local_fab_settings.KEY

    if getattr(local_fab_settings, 'HOSTS', None):
        env.hosts = local_fab_settings.HOSTS
