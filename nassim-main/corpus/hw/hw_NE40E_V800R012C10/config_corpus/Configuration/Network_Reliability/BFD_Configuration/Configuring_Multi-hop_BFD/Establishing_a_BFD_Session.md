Establishing a BFD Session
==========================

You can establish a BFD session on both ends of a multi-hop link to rapidly detect link faults.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the scenario:
   
   
   * BFD for IPv4 session
     
     Run the [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] [ **source-ip** *source-ip* ]  [ **track-interface** { **interface** | **controller** } *interface-type* *interface-number* ]  command to create the binding information about a BFD for IPv4 session.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a BFD for IPv4 session is created for the first time, a peer IPv4 address must be specified for the BFD session, and the BFD session must be bound to the local interface. The binding cannot be modified after being created.
     + When a BFD for IPv4 session is created, the system checks only the validity of the IPv4 address format. Binding the BFD for IPv4 session to an incorrect remote or local IPv4 address results in a failure in establishing the BFD for IPv4 session.
     + If BFD and unicast reverse path forwarding (URPF) are used together, **source-ip** must be configured correctly before a BFD session is bound to the IPv4 address to prevent BFD packets from being discarded. URPF checks the format of the source IPv4 addresses in received packets and discards the packets whose source IPv4 addresses are incorrect.
   * BFD for IPv6 session
     
     To create the binding information about a BFD for IPv6 session, run the [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ] [ **source-ipv6** *source-ipv6* ] [ **track-interface** { **interface** | **controller** } *interface-type* *interface-number* ] command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a multi-hop BFD for IPv6 session is created for the first time, a peer IPv6 address must be specified for the BFD session, and the BFD session must be bound to the local interface. The binding cannot be modified after being created.
     + When a BFD for IPv6 session is created, the system checks only the validity of the IPv6 address format. Binding the BFD for IPv6 session to an incorrect remote or local IPv6 address results in a failure in establishing the BFD for IPv6 session.
     + If BFD and URPF are used together, **source-ipv6** must be configured correctly before a BFD session is bound to the IPv6 address to prevent BFD packets from being discarded. URPF checks the format of the source IPv6 addresses in received packets and discards the packets whose source IPv6 addresses are incorrect.
3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
   
   
   
   The local discriminator of the BFD session is created.
4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
   
   
   
   The remote discriminator of the BFD session is created.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator of the local device and the remote discriminator of the remote device must be the same. The remote discriminator of the local device and the local discriminator of the remote device must be the same. A discriminator inconsistency causes the BFD session to fail to be established.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.