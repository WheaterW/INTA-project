(Optional) Enabling Proactive NETCONF Registration
==================================================

Proactive NETCONF registration enables a device to send a NETCONF connection request to the NMS when the device goes online.

#### Context

If an NMS does not support automatic device discovery, the NMS cannot manage devices in a timely manner. To address this problem, you can configure proactive NETCONF registration for a device to send a NETCONF connection request to the NMS when the device goes online so that the NMS can manage the device in a timely manner.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**netconf**](cmdqueryname=netconf)
   
   
   
   The NETCONF user interface view is displayed.
3. Run [**callhome**](cmdqueryname=callhome) *callhome-name*
   
   
   
   A callhome template is created, and the callhome template view is displayed.
4. (Optional) Run [**reconnection interval**](cmdqueryname=reconnection+interval) *interval*
   
   
   
   The interval at which the device firstly sends NETCONF connection requests to the NMS is set.
5. Run [**endpoint**](cmdqueryname=endpoint) *endpoint-name*
   
   
   
   A NETCONF connection instance is created, and the NETCONF connection instance view is displayed.
6. Set a callhome keepalive interval.
   
   
   * Run [**keepalive-interval**](cmdqueryname=keepalive-interval) *intervalTime*
     
     A callhome keepalive interval is set.
   * Run [**keepalive-maxcount**](cmdqueryname=keepalive-maxcount) *maxcount*
     
     The maximum number of callhome keepalive times is set.
   
   When the number of consecutive failures to exchange keepalive packets between the device and NMS exceeds the maximum number of callhome keepalive times, the device disconnects from the NMS.
7. Run [**peer-ip**](cmdqueryname=peer-ip) *ip-address* **port** *port-number* { [ **local-address** *source-ip* | [ **vpn-instance** *vpn-instance* | **public-net** ] ] \* | [ **source-interface** { *interface-name* | *interface-type* *interface-num* } ] }
   
   
   
   The IP address and TCP port number of the NMS with which the device is to establish a NETCONF connection, and the device source IP address and VPN instance or the source interface are configured.
   
   
   
   The *ip-address* parameter can be set to an IPv4 or IPv6 address.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.