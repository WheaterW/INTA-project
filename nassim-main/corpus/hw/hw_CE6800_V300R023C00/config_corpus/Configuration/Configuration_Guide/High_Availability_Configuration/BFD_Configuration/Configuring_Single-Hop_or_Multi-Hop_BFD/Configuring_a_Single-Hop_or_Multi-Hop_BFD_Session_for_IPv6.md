Configuring a Single-Hop or Multi-Hop BFD Session for IPv6
==========================================================

The CE6885-LL in low-latency mode does not support IPv6 functions.

#### Procedure

1. Enable BFD globally.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable BFD globally and enter the global BFD view.
      
      
      ```
      [bfd](cmdqueryname=bfd)
      ```
      
      You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
2. Create a BFD session.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Configure a BFD for IPv6 binding relationship.
      
      
      ```
      [bfd](cmdqueryname=bfd) session-name bind peer-ipv6 peer-ipv6 [ vpn-instance vpn-name ] [ interface { interface-name | interface-type interface-number } ] [ source-ipv6 source-ipv6 ] [ select-board slot-id1 [ slot-id2 ] ]
      ```
      
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * If a single-hop BFD session for IPv6 is being created for the first time, a peer IPv6 address must be specified for the BFD session, and the BFD session must be bound to the local interface. The configuration of the BFD session cannot be modified after the session is created.
      * If a multi-hop BFD session for IPv6 is being created for the first time, a peer (destination device) IPv6 address must be specified for the BFD session. The configuration of the BFD session cannot be modified after the session is created.
      * When parameters of a BFD session for IPv6 are being configured, the system checks the validity of the specified IPv6 address. The BFD session for IPv6 cannot be established if an incorrect peer IPv6 address or source IPv6 address is specified.
      * If both *slot-id1* and *slot-id2* are configured in **select-board** *slot-id1* [ *slot-id2* ], preference is given to *slot-id1*. If the board specified by *slot-id1* cannot be selected, the board specified by *slot-id2* is then selected. If neither board is selected, board selection stops.
   3. Configure a local discriminator for the BFD session.
      
      
      ```
      [discriminator](cmdqueryname=discriminator) local discr-value
      ```
   4. Configure a remote discriminator for the BFD session.
      
      
      ```
      [discriminator](cmdqueryname=discriminator) remote discr-value
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator on one end must be the same as the remote discriminator on the other end. Otherwise, the BFD session cannot be established.