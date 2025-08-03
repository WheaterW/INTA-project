Enabling Secondary Authentication
=================================

Enabling Secondary Authentication

#### Context

Misoperations of some commands cause the configurations of related features to be deleted, interrupting services and disconnecting the user network. To prevent misoperations, you can run the [**configuration re-authentication enable**](cmdqueryname=configuration+re-authentication+enable) command to enable secondary authentication.

After the secondary authentication function is enabled, you need to enter the login password for secondary authentication before running the following commands: [**reboot**](cmdqueryname=reboot), [**reset saved-configuration**](cmdqueryname=reset+saved-configuration), .

![](public_sys-resources/note_3.0-en-us.png) 

* To prevent some services from being unavailable due to misoperations, you are advised to enable secondary authentication.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable secondary authentication.
   
   
   ```
   [configuration re-authentication enable](cmdqueryname=configuration+re-authentication+enable)
   ```
   
   By default, secondary authentication is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```