### Ansible Scripts

#### Basics
Cheatsheets on how to get Ansible up and running can be found [here](https://github.com/Lab-Brat/cheatsheets/tree/main/ansible).

#### Playbooks
* configs
  * docker-compose.yaml: docker compose instructions that install Jenkins server
* flask_app_forms
  * app_forms.yaml: install flask-masque web app on Fedora
  * vars.yaml: variables for `app_forms.yaml`
* personal_setup
  * setup.yaml: personal configuration setup.
* docker.yaml: install Docker on Fedora.
* init_config.yaml: inistial OS configuration.
* jenkins.yaml: install Jenkins as a Docker container on Fedora (requires `docker-compose.yaml` file in `configs` directory)
* modern_commands.yaml: install modern alternative to classic linux commands, likr `lsd` for `ls` `bat` for `cat` etc.
