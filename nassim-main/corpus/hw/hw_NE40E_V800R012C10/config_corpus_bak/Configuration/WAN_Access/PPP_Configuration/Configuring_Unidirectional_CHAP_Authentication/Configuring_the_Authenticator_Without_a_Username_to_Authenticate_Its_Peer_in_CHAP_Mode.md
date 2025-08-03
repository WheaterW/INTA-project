Configuring the Authenticator Without a Username to Authenticate Its Peer in CHAP Mode
======================================================================================

This section describes how to configure the authenticator without a username to authenticate its peer in CHAP mode.

#### Procedure

* Configure the authenticator.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     
     
     The peer username and password are added to the local user list.
     
     
     
     During authentication, the authenticator searches locally configured AAA usernames. If the peer username and password match those on the local end, authentication succeeds.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  6. Run [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) **chap** [ **pap** ]
     
     
     
     The local end is configured to authenticate the peer end in CHAP mode.
     
     
     
     The [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) **chap** [ **pap** ] command enables the local end to preferentially use the CHAP mode to authenticate the peer end during LCP negotiation. If the peer end does not support the CHAP mode, the PAP mode is used. If the peer end supports neither of the two negotiation modes, the negotiation fails.
  7. Run [**shutdown**](cmdqueryname=shutdown)
     
     
     
     The interface is shut down.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  9. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
     
     
     
     The interface is restarted.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the username or password is changed in the interface view, you must run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in the corresponding interface view for the configuration to take effect.
     
     After running the [**shutdown**](cmdqueryname=shutdown) command during an interface restart, run the [**commit**](cmdqueryname=commit) command to commit the configuration. Otherwise, the configuration does not take effect.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the supplicant.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ppp chap user**](cmdqueryname=ppp+chap+user) *user-name*
     
     
     
     A local username is configured.
  4. Run [**ppp chap password**](cmdqueryname=ppp+chap+password) { [**simple**](cmdqueryname=simple) *password2* | **cipher** { *password1* | *password2* } }
     
     
     
     A local CHAP password is configured.
     
     
     
     During authentication, the authenticator sends only a Challenge packet to the supplicant. Based on the locally configured password and the Challenge packet, the supplicant calculates a value using a specified encryption algorithm, and then sends the value and host name to the authenticator.
  5. Run [**shutdown**](cmdqueryname=shutdown)
     
     
     
     The interface is shut down.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  7. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
     
     
     
     The interface is restarted.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the username or password is changed in the interface view, you must run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in the corresponding interface view for the configuration to take effect.
     
     After running the [**shutdown**](cmdqueryname=shutdown) command during an interface restart, run the [**commit**](cmdqueryname=commit) command to commit the configuration. Otherwise, the configuration does not take effect.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.