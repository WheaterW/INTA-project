(Optional) Configuring Prompt Response to Layer 2 Network Topology Changes
==========================================================================

Prompt response to Layer 2 network topology changes enables a device to correctly forward multicast data based on the new network topology, ensuring uninterrupted service forwarding.

#### Context

If a Layer 2 network topology changes, forwarding paths of multicast packets in the VLAN or VSI may change. After prompt response to Layer 2 network topology changes is configured on a device, the device will send an MLD Query message upon a link fault. After receiving the MLD Query message, hosts will reply with MLD Report messages if they need to the data. Based on the received MLD Report messages, the device updates information about multicast group member interfaces and switches multicast data traffic to the new forwarding path quickly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mld-snooping send-query enable**](cmdqueryname=mld-snooping+send-query+enable)
   
   
   
   Prompt response to Layer 2 network topology changes is configured.
   
   
   
   When the device detects a Layer 2 network topology change, it sends an MLD General Query message. This enables the device to quickly update port information and implement non-stop data forwarding for downstream user hosts.
3. (Optional) Run [**mld-snooping send-query source-address**](cmdqueryname=mld-snooping+send-query+source-address) *ip-address*
   
   
   
   A source IP address is set for MLD General Query messages.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.