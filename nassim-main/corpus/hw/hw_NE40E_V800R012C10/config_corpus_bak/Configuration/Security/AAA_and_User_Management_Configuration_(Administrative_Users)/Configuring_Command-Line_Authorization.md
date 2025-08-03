Configuring Command-Line Authorization
======================================

Command-line authorization determines whether the user
has the right to run a command. Command-line authorization is classified
into level authorization and task authorization.

#### Usage Scenario

Command-line authorization
is used to implement the management and authorization for the command-line
rights of users.

![](../../../../public_sys-resources/note_3.0-en-us.png) The priority of
level authorization is higher than that of task authorization, that
is, if both the level authorization and task authorization are configured
on a local user, the level authorization takes effect. 

#### Pre-configuration Tasks

Before configuring
command-line authorization, configure link layer protocol parameters
and IP addresses for interfaces to ensure that link layer protocols
on each interface are Up.


[Configuring Level Authorization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1011.html)

Configuring level authorization involves configuring the level authorization mode, adjusting the level of the user or command line, and configuring the user level promotion authentication mode.

[Configuring Task Authorization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1012.html)

Compared with level authorization, task authorization supports the customization of the user group and task group according to the application scenario. Therefore, task authorization provides a more flexible right control granularity.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1014.html)

After command-line authorization is configured, you can view the information about the task group and the user group.