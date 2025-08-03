Setting an Aging Time for NAT Sessions
======================================

To accelerate aging of expired NAT sessions of a protocol, set an aging time. After the aging time elapses, NAT sessions age, and system resources are released.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**nat session long-link**](cmdqueryname=nat+session+long-link) [ **inbound** | **outbound** ] **tcp** { **source-ip** *ip-address* { *ip-mask* | *mask-length* } [ **source-port** *port-number* ] [ **vpn-instance** *vpn-instance-name* ] | { **destination-ip** *ip-address* { *ip-mask* | *mask-length* } [ **destination-port** *port-number* ] | **destination-port** *port-number* } [ **vpn-instance** *vpn-instance-name* ] } \*
   
   
   
   A policy for establishing a persistent NAT TCP connection is configured.
   
   After this policy is configured, the aging time of the TCP connection of the specified session is changed to 200 hours by default. To reset the aging time of the persistent TCP connection, run the [**nat session aging-time**](cmdqueryname=nat+session+aging-time) command.
3. Run [**nat session aging-time**](cmdqueryname=nat+session+aging-time) { **tcp** | **udp** | **icmp** | **fin-rst** | **syn** | **fragment** | **dns** | **ftp** | **http** | **rtsp** | **sip** | **pptp** | **tcp** **long-link** | **ip** } *aging-time*
   
   
   
   An aging time is set for the sessions of a specified type.
   
   
   
   The changed aging time takes effect on new rather than existing NAT sessions.
4. (Optional) Set the fast aging time for DNS sessions.
   
   
   
   You are advised to configure this function when DNS traffic is heavy. After the fast aging function for DNS sessions is enabled, if the device receives DNS request and response packets at the same time, the DNS sessions age according to the configured fast aging time to save system resources.
   
   
   
   1. Run **[**nat session dns fast-aging enable**](cmdqueryname=nat+session+dns+fast-aging+enable)**
      
      The fast aging function is enabled for DNS sessions.
   2. Run **[**nat session dns fast-aging-time**](cmdqueryname=nat+session+dns+fast-aging-time)** *aging-time*
      
      A fast aging time is set for DNS sessions.
5. (Optional) Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
6. Run [**nat session aging-time**](cmdqueryname=nat+session+aging-time) { **ip** | **fin-rst** | **fragment** | **ftp** | **icmp** | **pptp** | **rtsp** | **sip** | **syn** | **tcp** | **udp** | **dns** | **http**} *aging-time*
   
   
   
   An aging time is set for the sessions of a specified type. If an aging time is set for a NAT instance, the aging time is used when a session is established in the instance. If no aging time is set for a NAT instance, the aging time set in the system view is used when a session is established in the instance.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.