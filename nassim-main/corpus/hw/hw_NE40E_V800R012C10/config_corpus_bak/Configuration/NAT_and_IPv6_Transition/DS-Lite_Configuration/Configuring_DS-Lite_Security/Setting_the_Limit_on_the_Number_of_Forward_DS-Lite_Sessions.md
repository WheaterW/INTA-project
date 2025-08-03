Setting the Limit on the Number of Forward DS-Lite Sessions
===========================================================

A forward session is established for packets transmitted from the user side to the network side. To prevent individual users from consuming excessive session table resources to cause connection failures of other users, enable the limit on the number of forward DS-Lite sessions.

#### Context

If the number of established Transmission Control Protocol (TCP), User Datagram Protocol (UDP), Internet Control Message Protocol (ICMP) DS-Lite sessions, or the total number of DS-Lite sessions involving the same source or destination IP address exceeds a configured threshold, a device stops establishing such sessions. The limit helps prevent resource overconsumption from resulting in a failure to establish connections for other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform one of the following operations:
   1. Set the limit on the number of forward DS-Lite sessions that can be established in the DS-Lite instance view.
      
      
      1. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
         
         The DS-Lite instance view is displayed.
      2. (Optional) Run [**ds-lite session-limit enable**](cmdqueryname=ds-lite+session-limit+enable)
         
         The user-based DS-Lite session number limit function is enabled.
      3. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
   2. Set the limit on the number of forward DS-Lite sessions that can be established in the NAT policy template view.
      
      
      1. Run [**nat-policy template**](cmdqueryname=nat-policy+template) *template-name*
         
         A NAT policy template is created.
      2. Run [**nat session-limit**](cmdqueryname=nat+session-limit) { **tcp** | **udp** | **icmp** | **total** } *session-number*
         
         The limit on the number of forward DS-Lite sessions that can be established is set.
      3. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The limit on the number of forward DS-Lite sessions configured in the NAT policy template prevails. If a limit is set in the template, the setting takes effect. If no limit is set in the DS-Lite instance or the NAT policy template, the default value in the template takes effect. If a delivered NAT policy template is invalid, the setting in the DS-Lite instance takes effect.
      * The status of the limit on the number of forward DS-Lite sessions is determined by the configuration in a DS-Lite instance. If the limit function is disabled in the DS-Lite instance, forward DS-Lite sessions can be established without restriction.