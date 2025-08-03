Disabling the Pre-connection Function
=====================================

Disabling the Pre-connection Function

#### Context

After a user is connected to the interface of an NAC-enabled device, a pre-connection is established between the user and device. If the user fails the authentication, the device sets the user to the pre-connection state by default, and permits DHCP packets from the user. As a result, the user can still obtain an IP address though the user does not have any network access rights. This wastes IP addresses and brings security risks to the network.

If users do not need any network access rights before being authenticated successfully, disable the pre-connection function. Users will then not have any network access rights before being authenticated successfully and will not obtain IP addresses.

![](public_sys-resources/note_3.0-en-us.png) 

* The **undo authentication pre-authen-access enable** command does not take effect for users who have pre-connection authorization configured.
* The pre-connection function must be disabled during VLAN-based authorization (excluding pre-connection authorization).
* If a user in pre-connection state fails to go online using DHCP packets containing the Option 82 field, it is recommended that you disable the pre-connection function on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the pre-connection function.
   
   
   ```
   [undo authentication pre-authen-access enable](cmdqueryname=undo+authentication+pre-authen-access+enable)
   ```
   
   By default, the pre-connection function is enabled. That is, if a user does not have any network access rights before being authenticated successfully, the user is in pre-connection state.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```