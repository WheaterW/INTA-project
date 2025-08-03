Configuring the Authenticator to Authenticate Its Peer in PAP Mode
==================================================================

This section describes how to configure PAP authentication on the authenticator. PAP performs two-way handshake authentication only in the initial link establishment phase.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
   
   
   
   The user name and password of the supplicant are added to the local user list.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the interface of the authenticator is displayed.
6. Run [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) **pap**
   
   
   
   The local end is configured to authenticate the peer in PAP mode.
7. Perform the following steps to restart the interface:
   1. Run the [**shutdown**](cmdqueryname=shutdown) command to shut down the interface.
   2. Run the [**commit**](cmdqueryname=commit) command to make the configuration take effect.
   3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restart the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.