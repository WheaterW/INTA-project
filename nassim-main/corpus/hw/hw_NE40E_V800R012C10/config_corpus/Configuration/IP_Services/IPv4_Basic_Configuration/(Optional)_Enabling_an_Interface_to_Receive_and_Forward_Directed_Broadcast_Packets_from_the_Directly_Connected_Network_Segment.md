(Optional) Enabling an Interface to Receive and Forward Directed Broadcast Packets from the Directly Connected Network Segment
==============================================================================================================================

In scenarios in which an interface needs to receive and forward directed broadcast packets from the directly connected network segment, enable this function.

#### Usage Scenario

A directed broadcast packet is broadcast to a specific network. In the destination IP address of such a packet, the network ID field contains the network ID of a specific network, and the host ID field contains all 1s.

Directed broadcast packets can be used by attackers to attack the network system, posing security risks. However, a device interface may need to receive or forward directed broadcast packets in some scenarios. When this is the case, enable the interface to receive or forward directed broadcast packets from the directly connected network segment.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip forward-broadcast**](cmdqueryname=ip+forward-broadcast+acl+name) [ **acl** { *acl-number* | **name** *acl-name* } ]
   
   
   
   The device is enabled to receive and forward directed broadcast packets from the directly connected network segment.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.