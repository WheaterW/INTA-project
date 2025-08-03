Configuring a Share-Group and Binding it to an MTI
==================================================

After configuring an IPv4 multicast VPN, configure a Share-Group address and a multicast tunnel interface (MTI) to be bound to the VPN instance.

#### Context

A multicast domain (MD) is a group of VPN instances that can transmit and receive multicast packets between PEs. Different VPN instances belong to different MDs. An MD serves a specific VPN. All private multicast data transmitted in the VPN is transmitted in the MD. All VPN instances on the PEs that belong to an MD need to join the same multicast group, which is called the Share-Group. A share-MDT is set up on the public network to transmit PIM and multicast data packets between PEs in the MD.

MTIs are the ingress and egress of the MDT on the public network. Local and remote PEs in a VPN transmit private network data through MTIs. MTIs allow interaction between the public network instance and VPN instances on PEs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The same Share-Group address cannot be configured for different VPN instances on a PE.

In an MD VPN, the value range of a Share-Group address is the same as that of an Any-Source Multicast (ASM) group address.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
4. Run [**multicast-domain share-group**](cmdqueryname=multicast-domain+share-group) *group-address* **binding mtunnel** *mtunnel-number*
   
   
   
   A Share-Group is configured and bound to a specified MTI. The system automatically binds the MTI to the VPN instance IPv4 address family.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After an MTI is created using the command in this step, the system automatically configures PIM on the MTI. You do not need to configure PIM on this MTI.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.