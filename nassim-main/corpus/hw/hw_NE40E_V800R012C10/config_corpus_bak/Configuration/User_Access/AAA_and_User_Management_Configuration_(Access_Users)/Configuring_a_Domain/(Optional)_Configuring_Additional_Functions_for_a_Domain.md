(Optional) Configuring Additional Functions for a Domain
========================================================

Many additional functions, such as time-based control, policy-based routing, traffic statistics, and IP address usage alarms, can be configured for a domain.

#### Context

Additional functions that can be configured for a domain include:

* Time-based control
  
  Time-based control means that a domain is automatically blocked in a specified period. During this period, the users of this domain cannot access the network, and the online users are disconnected. After the time period expires, the domain automatically enters the activated state, and users in the domain can go online.
* Idle cut
  
  Idle cut enables the NE40E to consider a user idle and disconnect the user if the traffic volume of the user keeps being lower than a threshold in a period. Idle cut takes effect based on the specified idle period and traffic volume threshold.
  
  The idle cut function configured for a domain controls only the basic traffic of a user. The multicast traffic and the VAS traffic that is not configured with the summary feature are not included in the basic traffic. Therefore, the idle cut function is invalid for them.
* Mandatory PPP authentication
  
  Generally, the authentication mode (PAP, CHAP, or MSCHAP) of a PPP user is negotiated by the PPP client and the virtual template interface. After the mandatory authentication mode of PPP users is configured for a domain, the users in the domain are authenticated in the configured mode.
* Policy-based routing
  
  With policy-based routing configured for a domain, the NE40E determines a forwarding egress according to the address specified for the user domain, not a packet destination address.
* IP address usage alarm
  
  After the alarm threshold for the usage (in percentage) of IP addresses is set in a domain, the NE40E sends an alarm to the network management system (NMS) when the usage of IP addresses exceeds the threshold. If no alarm threshold is set, the NE40E does not send any alarm to the NMS, regardless of the usage of IP addresses.
* Traffic statistics collection
  
  The traffic statistics function collects the total traffic of a domain and the upstream and downstream traffic of users.
* Accounting packet copy
  
  The accounting packet copy function allows the device to send accounting information to two RADIUS server groups at the same time and waits for their responses. If no response is received, the NE40E retransmits accounting information after 5s. If the NE40E does not receive any accounting response for three consecutive times, the NE40E sends an accounting stop packet to the RADIUS copy server and does not send accounting packets to this server any more.
  
  The function is used when original accounting information needs to be stored on multiple devices (for example, the multi-carrier networking scenario). In this case, accounting packet copies need to be sent to two RADIUS server groups at the same time, and will be used as the original accounting information in future settlement.
* Function to stop sending real-time accounting packets to accounting copy servers
  
  If an accounting copy server cannot process a large number of real-time accounting packets due to limited performance, configure the device to stop sending real-time accounting packets to the server.
* Re-authentication timeout
  
  The re-authentication timeout function allows the NE40E to disconnect a Layer 3 pre-authentication user if the user fails to pass the authentication within the maximum re-authentication time.
* Policy for online users when their quotas are used up
  
  The NE40E uses a policy on an online user after the user's quota (traffic or session time) is used up. It may log out the user, keep the user online, and forcibly redirect the user.
* Host route tagging
  
  The host route tagging function allows the device to import route tags based on routing policies and advertise different IPv4 host routes to different networks by setting and categorizing route tags for host routes of IPv4 users.
* Function to stop accounting within a specified time period
  
  This function enables a device to stop accounting for traffic from users in a domain within a specified time period. After the specified period elapses, the device starts accounting for the users again.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**time-range domain-block**](cmdqueryname=time-range+domain-block) { [**name**](cmdqueryname=name) *range-name* | **enable** }
   
   
   
   Time-based control is configured.
   
   You can configure up to four time ranges. All of them can take effect.
5. Run [**idle-cut**](cmdqueryname=idle-cut) *idle-time* { *idle-data* | **zero-rate** } [ **inbound** | **outbound** ]
   
   
   
   The idle cut function is configured for the domain.
   
   
   
   This command is used when some users cannot access the Internet due to an exception but can access the Internet after being logged out once. The idle-cut function can take effect on upstream traffic, downstream traffic, or both according to the parameter you specify. If you do not specify the **inbound** parameter or the **outbound** parameter, the idle-cut function takes effect on both upstream and downstream traffic.
6. Run [**ppp-force-authtype**](cmdqueryname=ppp-force-authtype) { **chap** | **mschap\_v1** | **mschap\_v2** | **pap** }
   
   
   
   Mandatory PPP authentication is configured for the domain.
7. Run [**policy-route**](cmdqueryname=policy-route) { *next-hop-ip-address* | *next-hop-ipv6-address* }
   
   
   
   The policy-based routing function is configured for the domain.
8. Run [**ip-warning-threshold**](cmdqueryname=ip-warning-threshold) { *upper-limit-value* | **lower-limit** *lower-limit-value* }
   
   
   
   The IP address usage alarm function is configured for the domain.
9. Run [**flow-bill**](cmdqueryname=flow-bill)
   
   
   
   The function to collect the total traffic statistics is enabled for the domain.
10. Run [**flow-statistic**](cmdqueryname=flow-statistic) { **down** | **up** } \*
    
    
    
    The function to collect the user traffic statistics is enabled for the domain.
11. Run [**accounting-copy radius-server**](cmdqueryname=accounting-copy+radius-server) *group-name*
    
    
    
    The accounting packet copy function is enabled for the domain.
12. Run [**radius-server accounting-copy realtime disable**](cmdqueryname=radius-server+accounting-copy+realtime+disable)
    
    
    
    The device is configured to stop sending real-time accounting packets to RADIUS accounting copy servers.
    
    
    
    After this command is run, the device will not send real-time accounting packets to copy servers, regardless of whether the servers have been configured in the domain.
13. Run [**max-ipuser-reauthtime**](cmdqueryname=max-ipuser-reauthtime) *time-value*
    
    
    
    The re-authentication timeout function is configured.
14. Run [**quota-out**](cmdqueryname=quota-out) { **offline** | **online** | **redirect** **url** *url-string* [ **redirect-stop-accounting** ] | **send-realtime-accounting** }
    
    
    
    A policy is set for online users after the user quota is used up.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This command takes effect only when a user's quota is used up and the user is in the specified domain. If the user domain is changed by a CoA packet sent from a policy server and the [**quota-out**](cmdqueryname=quota-out) command is not configured in the new domain, the user will be logged out when the quota is used up.
    
    * If the RADIUS protocol type is set to **non-standard**, a real-time accounting packet is sent to the RADIUS server to apply for a new quota when a user's quota is used up. If the RADIUS server responds with zero quota, the user is redirected based on the **quota-out** **redirect** **url** *url-string* [ **redirect-stop-accounting** ] command configuration.
    * If you want a user to be directly redirected when the user's quota is used up, you must set the RADIUS protocol type to **standard** and run the [**quota-out**](cmdqueryname=quota-out) **redirect** **url** *url-string* [ **redirect-stop-accounting** ] command.
15. Run [**radius-no-response lease-time**](cmdqueryname=radius-no-response+lease-time) *time*
    
    
    
    The lease time is set for DHCP users when the RADIUS server does not respond.
16. Run [**redirect-domain effect-attribute**](cmdqueryname=redirect-domain+effect-attribute) { **user-group** | **web-url** | **qos-profile** | **accounting-scheme** | **ip-unr-tag** }
    
    
    
    The fields that are allowed to take effect in the CoA delivery domain or quota exhaustion redirection domain are configured.
17. Run [**ip unr tag**](cmdqueryname=ip+unr+tag) *tag-value* **route-type** **host-route** **framed-route**
    
    
    
    A route tag is set for host routes of IPv4 users and network segment routes generated based on the RADIUS-delivered Framed-Route attribute.
18. (Optional) Run [**reallocate-ip-address**](cmdqueryname=reallocate-ip-address)
    
    
    
    The device is configured to reallocate IP addresses during authentication in the post-authentication domain.
    
    
    
    This command takes effect only for web users.
19. Run [**time-range non-accounting**](cmdqueryname=time-range+non-accounting) *time-range-name*
    
    
    
    The device is enabled to stop accounting in a domain within a specified time period.
20. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.