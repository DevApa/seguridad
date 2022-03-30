
#python, nginx, pip
"""
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo apt install python3-pip
sudo apt install python3-dev
sudo apt install libpq-dev
sudo apt install nginx
"""
#postgresql
"""
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql-14
sudo systemctl enable postgresql
sudo apt install vim
"""
"""
#pgadmin

sudo apt-get install --reinstall python3-apt
sudo apt install curl
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/focal pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'
sudo apt update
sudo apt install pgadmin4
sudo /usr/pgadmin4/bin/setup-web.sh

"""
"""
#gocd
sudo apt install git
git clone --branch branchInventario https://github.com/DevApa/seguridad.git
sudo apt install python3.10-venv
"""
