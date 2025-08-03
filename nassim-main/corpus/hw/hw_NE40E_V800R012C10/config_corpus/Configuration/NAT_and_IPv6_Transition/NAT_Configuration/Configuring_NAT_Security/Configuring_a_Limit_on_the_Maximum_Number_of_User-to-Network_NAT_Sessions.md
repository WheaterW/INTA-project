Configuring a Limit on the Maximum Number of User-to-Network NAT Sessions
=========================================================================

A forward session is established for packets transmitted from the user side to the network side. To prevent individual users from consuming excessive session resources to cause failures to establish connections for other users, you can set a limit on the maximum number of user-to-network NAT sessions that can be established for a specific user.

#### Context

If the number of established Transmission Control Protocol (TCP), User Datagram Protocol (UDP), Internet Control Message Protocol (ICMP) NAT sessions, or the total number of NAT sessions involving the same source IP address exceeds a configured threshold, a device stops establishing such sessions. The limit helps prevent resource overconsumption from resulting in a failure to establish connections for other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. (Optional) Run [**nat session-limit enable**](cmdqueryname=nat+session-limit+enable)
   
   
   
   The user-based NAT session number limit function is enabled.
4. Run [**nat session-limit**](cmdqueryname=nat+session-limit) { **tcp** | **udp** | **icmp** | **total** } *session-number*
   
   
   
   The maximum number of user-to-network NAT sessions that can be established is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.