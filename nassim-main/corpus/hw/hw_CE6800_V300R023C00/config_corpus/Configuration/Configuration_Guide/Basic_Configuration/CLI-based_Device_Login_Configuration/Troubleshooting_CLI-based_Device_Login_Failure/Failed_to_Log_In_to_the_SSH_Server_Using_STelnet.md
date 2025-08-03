Failed to Log In to the SSH Server Using STelnet
================================================

Failed to Log In to the SSH Server Using STelnet

#### Fault Description

A user fails to log in to the SSH server using STelnet.


#### Procedure

1. Log in to the SSH server through the console port or Telnet. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Check whether the SSH service is enabled on the SSH server.
   
   
   1. Check the configuration of the SSH server.
      ```
      [display ssh server status](cmdqueryname=display+ssh+server+status)
      ```
      * If STelnet is not enabled, go to step b.
      * If STelnet is enabled, go to step 3.
   2. Enable the STelnet service on the SSH server.
      ```
      [stelnet server enable](cmdqueryname=stelnet+server+enable)
      ```
3. Check the protocol configuration in the VTY user interface view of the SSH server.
   
   
   1. Check whether the protocol supported by the VTY user interface is SSH or all.
      ```
      [user-interface vty](cmdqueryname=user-interface+vty) first-ui-number [ last-ui-number ]
      [display this](cmdqueryname=display+this)
      ```
      * If not, go to step b.
      * If so, go to step 4.
   2. Set the protocol supported by the user interface to SSH.
      ```
      [protocol inbound](cmdqueryname=protocol+inbound) { ssh | all }
      [quit](cmdqueryname=quit)
      ```
4. Check whether an SSH user is configured on the SSH server.
   
   
   1. Check the configuration of the SSH user.
      ```
      [display ssh user-information](cmdqueryname=display+ssh+user-information)
      ```
      * If no configuration information exists, go to step b.
      * If configuration information exists, go to step 5.
   2. Create an SSH user, and configure the authentication mode and service type for the SSH user.
      ```
      [ssh user](cmdqueryname=ssh+user) user-name   //Create an SSH user.
      [ssh user](cmdqueryname=ssh+user) user-name authentication-type { password | rsa | password-rsa | all | dsa | password-dsa | ecc | password-ecc | sm2 | password-sm2 | password-x509v3-rsa | x509v3-rsa } // Configure the authentication mode for the SSH user.
      [ssh user](cmdqueryname=ssh+user) user-name service-type { all |  stelnet }  //Configure the service type for the SSH user.
      ```
5. Check whether the number of users who have logged in to the SSH server reaches the upper limit.
   
   
   1. Check whether all VTY channels are occupied.
      ```
      [display users](cmdqueryname=display+users)
      ```
      * If all VTY channels are occupied, go to step b.
      * If not all VTY channels are occupied, go to step 6.
   2. Check the maximum number of users allowed by the current VTY channel.
      ```
      [display user-interface maximum-vty](cmdqueryname=display+user-interface+maximum-vty)
      ```
   3. Set the maximum number of users allowed by the VTY channel to 21.
      ```
      [user-interface maximum-vty](cmdqueryname=user-interface+maximum-vty) 21
      ```
6. Check whether an ACL is bound to the VTY user interface of the SSH server.
   
   
   1. Check whether an ACL is configured on the VTY user interface.
      ```
      [user-interface vty](cmdqueryname=user-interface+vty) first-ui-number [ last-ui-number ]
      [display this](cmdqueryname=display+this)
      [quit](cmdqueryname=quit)
      ```
      * If an ACL is configured, record the ACL number and go to step b.
      * If no ACL is configured, go to step 7.
   2. Check whether ACL denies the IP address of the STelnet client.
      ```
      [display acl](cmdqueryname=display+acl) acl-number
      ```
      * If so, go to step c.
      * If not, go to step 7.
   3. Delete the **deny** rule.
      ```
      [undo rule](cmdqueryname=undo+rule) rule-id
      ```
   4. Modify the ACL to allow access from the IP address of the client.
      ```
      [rule](cmdqueryname=rule) permit source source-ip-address source-wildcard
      ```
7. Check whether the SSH version on the SSH server matches that on the SSH client.
   
   
   1. Check the SSH version.
      ```
      [display ssh server status](cmdqueryname=display+ssh+server+status)
      ```
      * If the SSH client and SSH server have different SSH versions and **SSH version 1.x compatibility** of the SSH server is **Disable**, go to step b.
      * If the SSH client and SSH server have the same SSH version, go to step 8.
   2. Enable the capability with earlier versions for the SSH server.
      ```
      [ssh server compatible-ssh1x enable](cmdqueryname=ssh+server+compatible-ssh1x+enable)
      ```
8. Check whether the first login function is enabled for the SSH client.
   
   
   
   If the first login function is not enabled on an SSH client, the first login from the STelnet client to the SSH server fails because validity check on the RSA public key of the SSH server fails.
   
   
   
   1. Check whether the first login function is enabled for the SSH client.
      ```
      [display this](cmdqueryname=display+this)
      ```
   2. Enable first login for the SSH client.
      ```
      [ssh client first-time enable](cmdqueryname=ssh+client+first-time+enable)
      ```