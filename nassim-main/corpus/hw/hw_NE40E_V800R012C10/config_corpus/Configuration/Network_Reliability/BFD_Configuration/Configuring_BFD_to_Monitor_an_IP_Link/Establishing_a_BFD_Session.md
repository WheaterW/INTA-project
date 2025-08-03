Establishing a BFD Session
==========================

You can establish a BFD session on both ends of a direct link to rapidly detect link faults.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. According to whether BFD detects an IPv4 or IPv6 link, perform either of the following operations:
   
   
   * Run either of the following commands to configure the binding information about a BFD for IPv4 session. The command you run will depend on whether the peer end is configured with an IP address.
     + For a Layer 3 interface with an IP address:
       
       To create the binding information about a BFD for IPv4 session, run the [**bfd**](cmdqueryname=bfd) *session-name* **[**bind**](cmdqueryname=bind)** **peer-ip** **peer-ip** [ **vpn-instance***vpn-name* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **source-ip** **source-ip** ] command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       - If a single-hop BFD for IPv4 session is created for the first time, a peer IPv4 address must be specified for the BFD session, and the BFD session must be bound to the local interface. The binding cannot be modified after being created.
       - When a BFD for IPv4 session is created, the system checks only the validity of the IPv4 address format. Binding the BFD for IPv4 session to an incorrect remote or local IPv4 address results in a failure in establishing the BFD for IPv4 session.
       - If BFD and unicast reverse path forwarding (URPF) are used together, **source-ip** must be configured correctly before a BFD session is bound to the IPv4 address to prevent BFD packets from being discarded. URPF checks the format of the source IPv4 addresses in received packets and discards the packets whose source IPv4 addresses are incorrect.
     + To bind a BFD for IPv4 session to a Layer 2 interface or a Layer 3 member interface without an IP address, run the [**bfd**](cmdqueryname=bfd) *session-name***bind** **peer-ip** **default-ip** **interface** *interface-type interface-number* [ **source-ip** *source-ip* ] command.
   * Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ] [ **interface** *interface-type* *interface-number* ] [ **source-ipv6** *source-ipv6* ]
     
     A BFD for IPv6 session is bound to an interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a single-hop BFD for IPv6 session is created for the first time, a peer IPv6 address must be specified for the BFD session, and the BFD session must be bound to the local interface. The binding cannot be modified after being created.
     + When a BFD for IPv6 session is created, the system checks only the validity of the IPv6 address format. Binding the BFD for IPv6 session to an incorrect remote or local IPv6 address results in a failure in establishing the BFD for IPv6 session.
     + If BFD and URPF are used together, **source-ipv6** must be configured correctly before a BFD session is bound to the IPv6 address to prevent BFD packets from being discarded. URPF checks the format of the source IPv6 addresses in received packets and discards the packets whose source IPv6 addresses are incorrect.
3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
   
   
   
   The local discriminator of the BFD session is created.
4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
   
   
   
   The remote discriminator of the BFD session is created.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local and remote discriminators on the two ends of a BFD session must be correctly associated. That is, the local discriminator of the local device must be the same as the remote discriminator of the remote device, and the remote discriminator of the local device must be the same as the local discriminator of the remote device. If the association is incorrect, a BFD session cannot be set up.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.