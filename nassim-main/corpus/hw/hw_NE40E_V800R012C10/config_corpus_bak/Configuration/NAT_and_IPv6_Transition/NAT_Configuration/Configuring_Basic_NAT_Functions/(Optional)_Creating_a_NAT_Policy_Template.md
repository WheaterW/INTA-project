(Optional) Creating a NAT Policy Template
=========================================

Configure NAT policy templates so that NAT configuration policies can be issued by a RADIUS server.

#### Context

To enable a RADIUS server to issue NAT configuration policies, configure a NAT template on a device and define some NAT configuration policies, such as a limit on the number of NAT sessions in the template. After the RADIUS server issues a template name to the device, the device finds the configured NAT policy template and applies it to a specified NAT instance.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in a NAT policy template take effect only after the NAT policy template is issued by a RADIUS server. The implementation is supported only in the distributed CGN scenario.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin-VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat-policy template**](cmdqueryname=nat-policy+template) *template-name*
   
   
   
   A NAT policy template is created, and its view is displayed.
3. Run [**nat session-limit**](cmdqueryname=nat+session-limit+tcp+udp+icmp+total) { **tcp** | **udp** | **icmp** | **total** } *session-number*
   
   
   
   The maximum number of NAT sessions that can be established is set.
4. Run [**nat reverse-session-limit**](cmdqueryname=nat+reverse-session-limit+tcp+udp+icmp+total) { **tcp** | **udp** | **icmp** | **total** } *session-number*
   
   
   
   The maximum number of reverse NAT sessions that can be established for each user IP address is set.
   
   
   
   The limit on the number of forward or reverse NAT sessions configured in the NAT policy template is used. If a limit is set in the template, the setting takes effect. If no limit is set in the NAT policy template, the default value in the template takes effect. If a delivered NAT policy template is invalid, the setting in the NAT instance takes effect.
   
   Whether the limit on the number of forward or reverse NAT sessions takes effect is determined by the configuration in a NAT instance. If the limit function is disabled in the NAT instance, forward or reverse NAT sessions can be established without restriction.
5. Run [**nat alg**](cmdqueryname=nat+alg+all+ftp+pptp+rtsp+sip) { **all** | **ftp** | **pptp** | **rtsp** | **sip** }
   
   
   
   The application protocol types that the NAT ALG detects are configured.
   
   
   
   If the [**nat alg**](cmdqueryname=nat+alg) command is run in both the NAT policy template and NAT instance views, both command instances take effect.
6. Run [**port-range**](cmdqueryname=port-range+extended-port-range+extended-times) *port-num* [  **extended-port-range** *extended-port-range* **extended-times** *extended-times* ]
   
   
   
   A port pre-allocation mode is configured.
   
   
   
   If the [**port-range**](cmdqueryname=port-range) command is run in both the NAT policy template view and NAT instance view, the configuration in the NAT policy template takes effect. If the command is not run in the NAT policy template view, the configuration in the NAT instance view takes effect.
   
   If the [**port-single enable**](cmdqueryname=port-single+enable) command is run in the NAT instance view, the per-port allocation mode configured in the instance takes effect, regardless of whether the [**port-range**](cmdqueryname=port-range) command is run in the NAT policy template view. If the [**port-single enable**](cmdqueryname=port-single+enable) command is not run in the NAT instance view, the [**port-range**](cmdqueryname=port-range) command run in the NAT policy template view takes effect.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.