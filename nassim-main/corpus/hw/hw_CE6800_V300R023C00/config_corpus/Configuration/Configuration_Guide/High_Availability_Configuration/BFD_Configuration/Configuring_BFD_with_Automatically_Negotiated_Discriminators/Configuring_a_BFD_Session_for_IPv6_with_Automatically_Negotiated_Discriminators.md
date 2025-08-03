Configuring a BFD Session for IPv6 with Automatically Negotiated Discriminators
===============================================================================

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
   2. Create a static BFD session for IPv6 with automatically negotiated discriminators.
      
      
      ```
      [bfd](cmdqueryname=bfd) sessname-value bind peer-ipv6 peerip6-value [ vpn-instance vpnname-value ] [ interface { interface-value | ifType ifNum } ] source-ipv6 sourceip6-value [ select-board slot-id [ slot-id2 ] ] auto
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      * The source address must be specified.
      * The peer IPv6 address must be specified and cannot be a multicast IPv6 address.
   3. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** **for-ipv6** | **discriminator** *discr-value* | **dynamic** | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** **for-ipv6** | **static-auto** } [ **verbose** ] command to check BFD session information.