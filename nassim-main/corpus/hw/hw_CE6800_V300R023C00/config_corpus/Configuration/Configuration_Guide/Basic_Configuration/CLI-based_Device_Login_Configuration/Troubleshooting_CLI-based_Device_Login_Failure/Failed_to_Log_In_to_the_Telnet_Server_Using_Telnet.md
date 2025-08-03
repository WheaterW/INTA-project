Failed to Log In to the Telnet Server Using Telnet
==================================================

Failed to Log In to the Telnet Server Using Telnet

#### Fault Description

A user fails to log in to the Telnet server using Telnet.


#### Procedure

1. Log in to the device through the console port. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Check whether the number of users who have logged in to the Telnet server reaches the upper limit.
   
   
   1. Check whether all VTY channels are occupied.
      ```
      [display users](cmdqueryname=display+users)
      ```
      * If all VTY channels are occupied, go to step b.
      * If not all VTY channels are occupied, go to step 3.
   2. Check the maximum number of users allowed by the current VTY channel.
      ```
      [display user-interface maximum-vty](cmdqueryname=display+user-interface+maximum-vty)
      ```
   3. Set the maximum number of users allowed by the VTY channel to 21.
      ```
      [user-interface maximum-vty](cmdqueryname=user-interface+maximum-vty) 21
      ```
3. Check whether an ACL has been configured on the VTY user interface of the Telnet server.
   
   
   1. Check whether an ACL is configured on the VTY user interface.
      ```
      [user-interface vty](cmdqueryname=user-interface+vty) first-ui-number [ last-ui-number ]
      [display this](cmdqueryname=display+this)
      [quit](cmdqueryname=quit)
      ```
      * If an ACL is configured, record the ACL number and go to step b.
      * If no ACL is configured, go to step 4.
   2. Check whether the IP address of the Telnet client is denied in the ACL.
      ```
      [display acl](cmdqueryname=display+acl) acl-number
      ```
      * If the IP address of the Telnet client is denied, go to step c.
      * If the IP address of the Telnet client is not denied, go to step 4.
   3. Delete the **deny** rule.
      ```
      [undo rule](cmdqueryname=undo+rule) rule-id
      ```
   4. Modify the ACL to allow access from the IP address of the client.
      ```
      [rule](cmdqueryname=rule) permit source source-ip-address source-wildcard
      ```
4. Check the protocol configuration in the VTY user interface view of the Telnet server.
   
   
   1. Check whether the protocol supported by the VTY user interface is Telnet or all.
      ```
      [user-interface vty](cmdqueryname=user-interface+vty) first-ui-number [ last-ui-number ]
      [display this](cmdqueryname=display+this)
      ```
      * If not, go to step b.
      * If so, go to step 5.
   2. Set the protocol supported by the user interface to Telnet.
      ```
      [protocol inbound](cmdqueryname=protocol+inbound) { telnet | all }
      [quit](cmdqueryname=quit)
      ```
5. Check whether the login authentication mode is configured in the user interface view of the Telnet server.
   
   
   ```
   [user-interface vty](cmdqueryname=user-interface+vty) first-ui-number [ last-ui-number ]
   [display this](cmdqueryname=display+this)
   [quit](cmdqueryname=quit)
   ```
   
   
   * If password authentication is configured using the [**authentication-mode**](cmdqueryname=authentication-mode) **password** command, you must set the local authentication password and enter the password upon login.
   * If AAA authentication is configured using the [**authentication-mode**](cmdqueryname=authentication-mode) **aaa** command, you must run the [**local-user**](cmdqueryname=local-user) *user-name* **password** command to create a local AAA user and set the user service type to Telnet.