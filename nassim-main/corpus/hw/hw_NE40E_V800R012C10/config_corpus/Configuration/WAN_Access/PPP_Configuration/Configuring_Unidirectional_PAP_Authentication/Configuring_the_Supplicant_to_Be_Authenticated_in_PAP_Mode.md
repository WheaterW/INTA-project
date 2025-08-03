Configuring the Supplicant to Be Authenticated in PAP Mode
==========================================================

This section describes how to configure the supplicant to be authenticated in PAP mode.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view of the supplicant is displayed.
3. Run [**ppp pap local-user**](cmdqueryname=ppp+pap+local-user) *user-name* **password** { [**simple**](cmdqueryname=simple) *password2* | **cipher** { *password1* | *password2* } }
   
   
   
   The interface is configured to send the local PAP username and password to the authenticator when the local end is authenticated by the authenticator in PAP mode.
4. Perform the following steps to restart the interface:
   1. Run the [**shutdown**](cmdqueryname=shutdown) command to shut down the interface.
   2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restart the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After completing the configuration, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands to restart the interface for the configuration to take effect.
   
   After running the [**shutdown**](cmdqueryname=shutdown) command during an interface restart, run the [**commit**](cmdqueryname=commit) command to commit the configuration. Otherwise, the configuration does not take effect.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.