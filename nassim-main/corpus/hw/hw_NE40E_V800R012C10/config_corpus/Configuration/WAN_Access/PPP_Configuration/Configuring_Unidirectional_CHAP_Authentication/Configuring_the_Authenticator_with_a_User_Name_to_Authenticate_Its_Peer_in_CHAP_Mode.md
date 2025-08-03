Configuring the Authenticator with a User Name to Authenticate Its Peer in CHAP Mode
====================================================================================

Configuring the Authenticator with a User Name to Authenticate Its Peer in CHAP Mode

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.

You can configure the authenticator with a user name to authenticate its peer in CHAP mode.


#### Procedure

* Configure the authenticator.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     
     
     The user name and password of the supplicant are added to the local user list.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  6. Run [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) **chap** [ **pap** ]
     
     
     
     The local end is configured to authenticate the peer in CHAP mode.
     
     You can run the [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) **chap** [ **pap** ] command to perform CHAP authentication preferentially in LCP negotiation. If the peer does not support CHAP authentication, PAP authentication is performed. If the peer supports neither CHAP nor PAP, LCP negotiation fails. Either CHAP or PAP is involved in a PPP negotiation.
  7. Run [**ppp chap user**](cmdqueryname=ppp+chap+user) *user-name*
     
     
     
     A user name is specified.
  8. Perform the following steps to restart the interface:
     
     
     1. Run the [**shutdown**](cmdqueryname=shutdown) command to shut down the interface.
     2. Run the [**commit**](cmdqueryname=commit) command to make the configuration take effect.
     3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restart the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the supplicant.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     
     
     The user name and password of the supplicant are added to the local user list.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  6. Run [**ppp chap user**](cmdqueryname=ppp+chap+user) *user-name*
     
     
     
     A user name is configured.
  7. Perform the following steps to restart the interface:
     
     
     1. Run the [**shutdown**](cmdqueryname=shutdown) command to shut down the interface.
     2. Run the [**commit**](cmdqueryname=commit) command to make the configuration take effect.
     3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restart the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.