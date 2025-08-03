Setting a Limit on the Number of NAT64 Reverse Sessions
=======================================================

A reverse session refers to a session initiated from the IPv4 side to the IPv6 side. If individual users consume excessive session table resources, other users may fail to establish connections. To address this problem, set a limit on the maximum number of IPv4-to-IPv6 reverse NAT64 sessions that can be established for a specific user.

#### Context

A NAT device checks whether the number of established Transmission Control Protocol (TCP), User Datagram Protocol (UDP), or Internet Control Message Protocol (ICMP) sessions or the total number of sessions involving the same source or destination IP address exceeds the configured threshold. Then the NAT device determines whether to restrict the initiation of new connections from the source or destination IP address. This prevents individual users from consuming excessive session table resources and causing the connection failure of other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT64 instance view is displayed.
3. (Optional) Run [**nat64 reverse-session-limit enable**](cmdqueryname=nat64+reverse-session-limit+enable)
   
   
   
   The limitation on the number of NAT64 reverse sessions that can be established is enabled.
   
   If this function is not enabled, run the [**nat64 reverse-session-limit enable**](cmdqueryname=nat64+reverse-session-limit+enable) command to enable it.
4. Run [**nat64 reverse-session-limit**](cmdqueryname=nat64+reverse-session-limit) { **icmp** | **tcp** | **udp** | **total** } *limit-number*
   
   
   
   The maximum number of NAT64 sessions that can be established is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.