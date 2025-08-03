Configuring STelnet for Device Login
====================================

Configuring STelnet for Device Login

#### Context

In order to remotely log in to the device from the terminal through STelnet when the IP address of a terminal and the management IP address of a device are Layer 3 reachable, an administrator must first create a login user on the device and configure STelnet.

![](public_sys-resources/note_3.0-en-us.png) 

By default, a new user needs to change the password at first login to the device. If the administrator resets the password, the user also needs to change the password at the first login to the device after password reset.

This section describes how to configure STelnet-based login in the password authentication mode.


#### Procedure

1. Set the VTY user authentication mode to AAA and configure the VTY user interface to support SSH.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   [user-interface](cmdqueryname=user-interface) [vty](cmdqueryname=vty) first-ui-number [ last-ui-number ]
   [authentication-mode](cmdqueryname=authentication-mode) [aaa](cmdqueryname=aaa)    //Set the VTY user authentication mode to AAA.
   [protocol inbound](cmdqueryname=protocol+inbound) [ssh](cmdqueryname=ssh)    //Configure the VTY user interface to support SSH.
   [quit](cmdqueryname=quit)
   [commit](cmdqueryname=commit)
   ```
2. Configure a local AAA user and its password.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   [local-user](cmdqueryname=local-user) user-name [password](cmdqueryname=password) irreversible-cipher irreversible-cipher-password    //Create a local user whose name is the same as the SSH user name and configure the local user's password.
   [local-user](cmdqueryname=local-user) user-name [service-type ssh](cmdqueryname=service-type+ssh)    //Set the service type of the local user to SSH.
   [local-user](cmdqueryname=local-user) user-name privilege level level   //Set the local user's level.
   [quit](cmdqueryname=quit)
   [commit](cmdqueryname=commit)
   ```
3. Create an SSH user and configure the authentication mode and service type.
   
   
   ```
   [ssh user](cmdqueryname=ssh+user) user-name   //Create an SSH user.
   [ssh user](cmdqueryname=ssh+user) user-name [authentication-type password](cmdqueryname=authentication-type+password)    //Set the authentication mode of the SSH user to password.
   [ssh user](cmdqueryname=ssh+user) user-name [service-type stelnet](cmdqueryname=service-type+stelnet)    //Set the service type of the SSH user to STelnet.
   [stelnet server enable](cmdqueryname=stelnet+server+enable)    //Enable the STelnet server function for the device.
   [ssh server-source](cmdqueryname=ssh+server-source) -i interface-type interface-number   //Configure the source interface for the SSH server. If IPv6 addresses are used for login, run the [ssh ipv6 server-source](cmdqueryname=ssh+ipv6+server-source) -a ipv6-address command to configure the source IP address for the SSH server.
   [commit](cmdqueryname=commit)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the SSH user name is the same as the local user name.
   
   The created user must change the password upon first login.