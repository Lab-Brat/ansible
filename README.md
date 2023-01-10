### Ansible
Repository with `site.yaml` that launches all of my other Ansible roles.

#### Roles
* ansible_flask: install and configure [flask_masque](https://github.com/Lab-Brat/flask_masque)
* ansible_jenkins: deploy Jenkins server in a Docker container.
* ansible_personal: configure personal installation of Arch or Arch based distros.
* ansible_server: install different infrascructure components, such as Docker, Nginx etc.

#### Initialization
Clone the repository:
```bash
git clone https://github.com/Lab-Brat/ansible.git
cd ansible
```  

and instantiate available roles as submodules, and pull the latest versions:
```bash
git submodule init
git submodule update --recursive --remote
```

#### Test with Vagrant
There is a Vagrant config file in `vagrant` directory that will deploy an AlmaLinux server.
Navigate to it, create SSH keys and run Vagrant:
```bash
cd vagrant
ssh-keygen -P '' -q -f vg_box
vagrant up
```

#### Playbook
`inventory` file and `ansible.cfg` has neccessary information to run the playbook 
on the default Vagrant AlmaLinux box. If the default box was not used, just update
inventory file as you see fit.  

All roles and most of the tasks are tagged, and can be invoked with `-t` flag.  
For example, to install Nginx and disable SElinux:
```bash
ansible-playbook site.yaml -t 'server,nginx,selinux_off' 
```
this will use `server` role, and from it will call `nginx` and `selinux_off` tasks.
