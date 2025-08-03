Configuring the Limit on the Number of User-to-Network NAT64 Sessions
=====================================================================

To prevent individual users from consuming excessive session table resources to cause connection failures of other users, enable the NAT64 session number limit function.

#### Context

If the number of established Transmission Control Protocol (TCP), User Datagram Protocol (UDP), Internet Control Message Protocol (ICMP) NAT64 sessions, or the total number of NAT64 sessions of a user exceeds a configured threshold, a device stops establishing such sessions. The limit helps prevent resource overconsumption from resulting in a failure to establish connections for other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. (Optional) Run [**nat64 session-limit enable**](cmdqueryname=nat64+session-limit+enable)
   
   
   
   The NAT64 session number limit function is enabled.
   
   
   
   To enable this function, run the [**nat64 session-limit enable**](cmdqueryname=nat64+session-limit+enable) command.
4. Run [**nat64 session-limit**](cmdqueryname=nat64+session-limit) { **icmp** | **tcp** | **udp** | **total** } *session-number*
   
   
   
   The limit on the number of NAT64 sessions is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.