ssh authentication-type default password
========================================

ssh authentication-type default password

Function
--------



The **ssh authentication-type default password** command configures password authentication as the default authentication mode for users who request to log in to a device using SSH.

The **undo ssh authentication-type default password** command cancels the configuration.



By default, password authentication is used.


Format
------

**ssh authentication-type default password**

**undo ssh authentication-type default password**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When users request to log in to a device using SSH, if no SSH user is created using the ssh user, ssh user authentication-type, and ssh user service-type commands, successful user login depends on whether the **ssh authentication-type default password** command is run.

* If the **ssh authentication-type default password** command is run, users log in through AAA authentication.
* If the **ssh authentication-type default password** command is not run, users cannot log in.If an SSH user has been created using the ssh user, ssh user authentication-type, and ssh user service-type commands, authentication of the SSH user depends on whether the **ssh user authentication-type** command is run. If the **ssh user authentication-type** command is run, the user is authenticated using the authentication mode specified in this command. If the **ssh user authentication-type** command is not run, the user cannot log in to the device.This command takes effect for both IPv4 and IPv6 users.

Example
-------

# Configure password authentication as the default authentication mode for an SSH user.
```
<HUAWEI> system-view
[~HUAWEI] ssh authentication-type default password

```