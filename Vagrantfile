# -*- mode: ruby -*-
# vi: set ft=ruby :
$script = <<SCRIPT
    apt-get update
    apt-get -y install mc
    apt-get -y install nginx
    apt-get install python
    apt-get install libsqlite3-dev
    apt-get install -y python-pip
    pip install gunicorn
    pip install django==1.6.1
SCRIPT

Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    config.vm.network "private_network", ip: "192.168.100.220"

    config.vm.synced_folder ".", "/home/box/web"

    config.vm.provider "virtualbox" do |v|
      v.name = "stepic"
    end

    # provisioner config
    config.vm.provision "shell", inline: $script
end