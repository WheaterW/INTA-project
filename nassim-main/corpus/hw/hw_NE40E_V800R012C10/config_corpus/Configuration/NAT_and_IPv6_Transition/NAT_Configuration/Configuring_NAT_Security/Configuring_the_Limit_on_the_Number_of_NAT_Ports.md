Configuring the Limit on the Number of NAT Ports
================================================

To prevent individual users from occupying excessive port resources to cause the connection failure of other users, you can enable the NAT port number limit function.

#### Context

By checking whether the total number of TCP/UDP/ICMP/TOTAL ports used for connections involving the same source or destination address exceeds the configured threshold, the system can determine whether to restrict the initiation of new connections in the direction, preventing individual users from occupying excessive port resources and causing the connection failure of other users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only dedicated boards support this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**nat port-limit enable**](cmdqueryname=nat+port-limit+enable)
   
   
   
   The user-based port number limit function is enabled.
4. Run [**nat port-limit**](cmdqueryname=nat+port-limit) { **tcp** | **udp** | **icmp** | **total** } *limit-value*
   
   
   
   The limit on the number of user-based ports is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.