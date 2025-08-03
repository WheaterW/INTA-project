Verifying the Configuration of VTY User Interfaces
==================================================

After configuring a VTY user interface, verify the configuration.

#### Prerequisites

A VTY user interface has been configured.


#### Procedure

* Run the [**display users**](cmdqueryname=display+users) [ **all** ] command to check user login information about user interfaces.
* Run the [**display user-interface maximum-vty**](cmdqueryname=display+user-interface+maximum-vty) command to check the configured maximum number of VTY user interfaces.
* Run the [**display user-interface**](cmdqueryname=display+user-interface) **vty** *ui-number* command to check physical attributes and configuration of the user interface.
* Run the [**display local-user**](cmdqueryname=display+local-user) command to check the local user list.
* Run the [**display access-user**](cmdqueryname=display+access-user) command to check information about users that pass AAA authentication.
* Run the [**display vty mode**](cmdqueryname=display+vty+mode) command to check the VTY mode.