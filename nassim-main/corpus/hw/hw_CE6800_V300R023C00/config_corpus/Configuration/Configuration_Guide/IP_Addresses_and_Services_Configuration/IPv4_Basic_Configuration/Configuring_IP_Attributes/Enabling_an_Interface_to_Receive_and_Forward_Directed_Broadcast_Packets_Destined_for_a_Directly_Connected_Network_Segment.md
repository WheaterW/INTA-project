Enabling an Interface to Receive and Forward Directed Broadcast Packets Destined for a Directly Connected Network Segment
=========================================================================================================================

Enabling an Interface to Receive and Forward Directed Broadcast Packets Destined for a Directly Connected Network Segment

#### Context

A directed broadcast packet is sent to a specific network. In the destination IP address of such a packet, the network ID and host ID fields are comprised of a specific network's network ID and all 1s, respectively.

Attackers can use directed broadcast packets to attack network systems, posing security risks. In some scenarios, however, a device's interface may need to receive and forward such packets. To meet this need, enable the interface to receive and forward directed broadcast packets destined for the directly connected network segment.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number } 
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable the interface to receive and forward directed broadcast packets destined for a directly connected network segment.
   
   
   ```
   [ip forward-broadcast](cmdqueryname=ip+forward-broadcast+acl+name) [ acl { acl-number | name acl-name } ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```