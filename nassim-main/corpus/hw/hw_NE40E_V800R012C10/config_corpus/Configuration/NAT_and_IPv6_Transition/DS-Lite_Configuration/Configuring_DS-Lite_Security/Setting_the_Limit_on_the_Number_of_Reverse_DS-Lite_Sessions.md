Setting the Limit on the Number of Reverse DS-Lite Sessions
===========================================================

A reverse session is established for packets transmitted from the network side to the user side. To prevent network-side devices from consuming excessive session table resources to cause connection failures of other network-side devices, enable the limit on the number of reverse DS-Lite sessions.

#### Context

If the number of established Transmission Control Protocol (TCP), User Datagram Protocol (UDP), Internet Control Message Protocol (ICMP) DS-Lite sessions, or the total number of DS-Lite sessions involving the same source or destination IP address exceeds a configured threshold, a device stops establishing such sessions. The limit helps prevent resource overconsumption from resulting in a failure to establish connections for other users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Select a mode to configure the limit on the number of reverse DS-Lite sessions:
   
   
   * Configure the limit on the number of reverse DS-Lite sessions in the DS-Lite instance view.
     
     1. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
        
        The DS-Lite instance view is displayed.
     2. (Optional) Run [**ds-lite reverse-session-limit enable**](cmdqueryname=ds-lite+reverse-session-limit+enable)
        
        The DS-Lite reverse IP session monitoring function is enabled.
   * Run [**ds-lite reverse-session-limit**](cmdqueryname=ds-lite+reverse-session-limit) { **tcp** | **udp** | **icmp** | **total** } *session-number*
     
     The maximum number of network-to-user sessions that can be established is set.
   * Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
   * Configure the limit on the number of reverse DS-Lite sessions in the NAT policy template view.
     
     1. Run [**nat-policy template**](cmdqueryname=nat-policy+template) *template-name*
        
        A NAT policy template is created.
     2. Run [**nat reverse-session-limit**](cmdqueryname=nat+reverse-session-limit) { **tcp** | **udp** | **icmp** | **total** } *session-number*
        
        The maximum number of user-based reverse NAT sessions that can be established is set.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The limit on the number of reverse DS-Lite sessions configured in the NAT policy template prevails. If a limit is set in the template, the setting takes effect. If no limit is set in the DS-Lite instance or the NAT policy template, the default value in the template takes effect. If a delivered NAT policy template is invalid, the setting in the DS-Lite instance takes effect.
     + The status of the limit on the number of reverse DS-Lite sessions is determined by the configuration in a DS-Lite instance. If the limit function is disabled in the DS-Lite instance, forward DS-Lite sessions can be established without restriction.