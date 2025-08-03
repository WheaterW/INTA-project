Verifying the Configuration of Logging In to the System Through the Console Port
================================================================================

After logging in to a router through a console port, you can view information about the console user interface, such as the usage, physical attributes and configurations, local user list, and online users.

#### Prerequisites

Login through a console port has been configured.
#### Procedure

* Run the [**display users**](cmdqueryname=display+users) [ **all** ] command to check user login information about user interfaces.
* Run the [**display user-interface**](cmdqueryname=display+user-interface) **console 0** command to check physical attributes and configurations of the user interface.
  
  
  
  In VS mode, this command is supported only by the admin VS.
* Run the [**display local-user**](cmdqueryname=display+local-user) command to check the local user list.
* Run the [**display access-user**](cmdqueryname=display+access-user) command to check information about users that pass AAA authentication.