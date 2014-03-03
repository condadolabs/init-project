from fabric.api import local, env

def init(vagrant=True):
    "Prepare a local machine for development."
    os = local('uname -s', capture=True)
    if os == 'Darwin': #OSX
        env.installer = 'brew cask install'
    elif os == 'Linux':
        env.installer = 'apt-get install'
    else:
        print "Error: Your operating system (%s) is not supported yet" % os
        exit
    if vagrant:
        local('%(installer)s virtualbox vagrant' % env)
        local('vagrant plugin install vagrant-vbguest')
    local('sudo pip install ansible')


def configure():
