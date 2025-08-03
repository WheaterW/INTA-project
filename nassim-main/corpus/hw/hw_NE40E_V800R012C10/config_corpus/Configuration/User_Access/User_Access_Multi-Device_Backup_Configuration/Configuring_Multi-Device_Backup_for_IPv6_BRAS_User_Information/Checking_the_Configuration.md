Checking the Configuration
==========================

After configuring multi-device backup, verify the configuration. You can view details about the remote server and the remote backup service type, which is BRAS.

#### Context

Run the following commands to verify the configuration.


#### Procedure

* Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) [ *profileName* ] command to check RBP information.
* Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) [ *service-name* [ **verbose** ] ] command to check RBS information.
* Run the [**display backup-user**](cmdqueryname=display+backup-user) [ **user-id** *id* | **username** [ **include** ] *user-name* ] command to check backup user information.
* Run the [**display access-user interface**](cmdqueryname=display+access-user+interface) *interface-type* *interface-number* [ **normal** | [ **rui-local** | **rui-remote** ] [ **master** | **slave** ] ] command to check information about the access users on a specified interface.