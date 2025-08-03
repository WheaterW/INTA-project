Configuring a Limit on the Maximum Number of Network-to-User NAT Sessions
=========================================================================

A reverse session is established for packets transmitted from the network side to the user side. To prevent individual users from consuming excessive session resources to cause failures to establish connections for other users, you can set a limit on the maximum number of network-to-user NAT sessions that can be established for a specific user.

#### Context

If the number of established Transmission Control Protocol (TCP), User Datagram Protocol (UDP), Internet Control Message Protocol (ICMP) NAT sessions, or the total number of NAT sessions involving the same destination IP address exceeds a configured threshold, a device stops establishing such sessions. The limit helps prevent resource overconsumption from resulting in a failure to establish connections for other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. (Optional) Run [**nat reverse-session-limit enable**](cmdqueryname=nat+reverse-session-limit+enable)
   
   
   
   The device is enabled to monitor the number of established user-specific network-to-user NAT sessions.
4. Run [**nat reverse-session-limit**](cmdqueryname=nat+reverse-session-limit) { **tcp** | **udp** | **icmp** | **total** } *session-number*
   
   
   
   The maximum number of network-to-user NAT sessions that can be established is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.