from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['host']
env.user = 'USER'
env.password = 'PASS'

def update():
    sudo("cd /srv/www/greatjournalism.net/public_html/site && git pull")
    sudo("chown -R www-data:www-data /srv/www/greatjournalism.net/public_html/site")
    reboot()

def reboot():
    sudo("/etc/init.d/apache2 restart")