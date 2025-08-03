Configuring a Single-Hop or Multi-Hop BFD Session for IPv4
==========================================================

Configuring a Single-Hop or Multi-Hop BFD Session for IPv4

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
   3. (Optional) Configure the default multicast address for BFD.
      
      
      ```
      [default-ip-address](cmdqueryname=default-ip-address) default-ip-value
      ```
   4. (Optional) Disable the local and remote discriminators of a multicast BFD session from being set to the same value.
      
      
      ```
      [same discriminator disable](cmdqueryname=same+discriminator+disable)
      ```
2. Create a BFD session.
   1. Run either of the following commands to configure a BFD for IPv4 binding relationship. The command you run will depend on whether the peer end is configured with an IPv4 address.
      
      
      
      Configure a BFD for IPv4 binding relationship on a Layer 3 interface with an IPv4 address.
      
      ```
      [bfd](cmdqueryname=bfd) session-name bind peer-ip peer-ip [ vpn-instance vpn-name ] [ interface { interface-name | interface-type interface-number } ] [ [ source-ip source-ip ] [ select-board slot-id1 [ slot-id2 ] ] | [ select-board slot-id1 [ slot-id2 ] ] [ source-ip source-ip ] ]
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      * If a single-hop BFD session for IPv4 is being created for the first time, a peer IPv4 address must be specified for the BFD session, and the BFD session must be bound to the local interface. The configuration of the BFD session cannot be modified after the session is created.
      * If a multi-hop BFD session for IPv4 is being created for the first time, a peer (destination device) IPv4 address must be specified for the BFD session. The configuration of the BFD session cannot be modified after the session is created.
      * When parameters of a BFD session for IPv4 are being configured, the system checks the validity of the specified IPv4 address. The BFD session for IPv4 will not be established if an incorrect peer IPv4 address or source IPv4 address is specified.
      * If both *slot-id1* and *slot-id2* are configured in **select-board** *slot-id1* [ *slot-id2* ], preference is given to *slot-id1*. If the board specified by *slot-id1* cannot be selected, the board specified by *slot-id2* is then selected. If neither board is selected, board selection stops.
      
      Configure a BFD for IPv4 binding relationship on a Layer 2 interface or a Layer 3 physical member interface without an IPv4 address.
      
      ```
      [bfd](cmdqueryname=bfd) sessname-value bind peer-ip default-ip interface interface-type interface-number [ source-ip source-ip ]
      ```
   2. Configure a local discriminator for the BFD session.
      
      
      ```
      [discriminator](cmdqueryname=discriminator) local discr-value
      ```
   3. Configure a remote discriminator for the BFD session.
      
      
      ```
      [discriminator](cmdqueryname=discriminator) remote discr-value
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator on one end must be the same as the remote discriminator on the other end. Otherwise, the BFD session cannot be established.