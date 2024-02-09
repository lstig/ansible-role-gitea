Ansible Role `lstig.gitea`
=========

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/lstig/ansible-role-gitea/blob/main/LICENSE)

Install and manage gitea.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

[defaults](defaults/main.yml)

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

```yaml
---
- hosts: servers
  roles:
    - role: lstig.gitea
```
