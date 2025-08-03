Setting the Limit on the Number of DS-Lite Ports
================================================

To prevent individual users from consuming excessive port resources to cause the connection failure of other users, you can enable the limit on the number of DS-Lite ports.

#### Context

By checking whether the total number of TCP/UDP/ICMP/TOTAL ports used for connections involving the same source or destination address exceeds the configured threshold, the system can determine whether to restrict the initiation of new connections in the direction, preventing individual users from consuming excessive port resources and causing the connection failure of other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. Run [**ds-lite port-limit enable**](cmdqueryname=ds-lite+port-limit+enable)
   
   
   
   The user-based port number limit function is enabled.
4. Run [**ds-lite port-limit**](cmdqueryname=ds-lite+port-limit) { **tcp** | **udp** | **icmp** | **total** } *port-number*
   
   
   
   The maximum number of user-based ports that can be assigned to each user is set.