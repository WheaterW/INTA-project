Configuring a BFD Session for IPv4 with Automatically Negotiated Discriminators
===============================================================================

Configuring a BFD Session for IPv4 with Automatically Negotiated Discriminators

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
   2. Create a static BFD session for IPv4 with automatically negotiated discriminators.
      
      
      ```
      [bfd](cmdqueryname=bfd) session-name bind peer-ip peer-ip [ vpn-instance vpn-name ] [ interface { interface-name | interface-type interface-number } ] { source-ip source-ip [ select-board slot-id1  [ slot-id2 ] ] | [ select-board slot-id1 [ slot-id2 ] ] source-ip source-ip } auto
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      * The source address must be specified.
      * The peer IPv4 address must be specified and cannot be a multicast IPv4 address.
      * If both *slot-id1* and *slot-id2* are configured in **select-board** *slot-id1* [ *slot-id2* ], preference is given to *slot-id1*. If the board specified by *slot-id1* cannot be selected, the board specified by *slot-id2* is then selected. If neither board is selected, board selection stops.
   3. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** [ **for-ip** ] | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **static** [ **for-ip** ] | **static-auto** } [ **verbose** ] command to check BFD session information.