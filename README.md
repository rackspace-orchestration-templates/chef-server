[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/chef-server/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/chef-server)
Description
===========

This is a template for deploying the open source [Chef
Server](http://docs.opscode.com/install_server.html) server on a single Linux
server.

Requirements
============
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the
[python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
  <TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
  stack-create Chef-Server-Stack -f chef-server.yaml \
  -P chef_username=bob
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as
the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these
values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `server_hostname`: Sets the hostname of the server. (Default: Chef-Server)
* `image`: Operating system to install (Default: Ubuntu 14.04 LTS (Trusty Tahr)
  (PVHVM))
* `flavor`: Cloud server size to use. (Default: 2 GB Performance)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value fo a specific output.

* `private_key`: SSH private that can be used to login as root to the server.
* `server_ip`: Public IP address of the cloud server

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
Once the deployment is up, you can navigate to the of the server using the
`chef_url` provided in the `output-list`. Users will need to be setup vai the
CLI.

Check out the [Manage the Chef
Server](http://docs.chef.io/server/#manage-the-chef-server)
documentation provided by OpsCode for more information about managing users,
keys, and clients. If this is your first time using Chef Server 12,
instructions for adding users and organizations via command line can be found
[here](http://docs.chef.io/server/server_orgs.html). For security purposes, we
have disabled user setup and signup via the web interface.

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
