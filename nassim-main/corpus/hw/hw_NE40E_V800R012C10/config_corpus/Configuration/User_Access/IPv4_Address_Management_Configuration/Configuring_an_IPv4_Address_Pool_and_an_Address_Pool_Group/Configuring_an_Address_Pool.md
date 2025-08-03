Configuring an Address Pool
===========================

Configuring an Address Pool

#### Context

Configuring the type, name, gateway, and address segment of an address pool is mandatory. Configure either a dynamic or a non-dynamic address pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**access wait-request-time**](cmdqueryname=access+wait-request-time) **dhcpv4** *time-value*
   
   
   
   The timeout period for a router to wait for a Request message from a client in response to an Offer message sent to the client is configured.
3. Perform the corresponding steps according to the type of the address pool to be configured.
   
   
   * Configure a dynamic address pool.
     1. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* **bas** **dynamic**
        
        A dynamic address pool is created, and the corresponding address pool view is displayed.
     2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
        
        A RADIUS server group is configured for the address pool.
     3. Run [**authentication-name**](cmdqueryname=authentication-name) *authentication-name* **password** **cipher** *password*
        
        An authentication name and a password are configured for the device to apply for dynamic address segments.
     4. (Optional) Run [**ip used-threshold**](cmdqueryname=ip+used-threshold) **upper-limit** *upper-value* **lower-limit** *lower-value*
        
        The upper and lower address usage thresholds are configured for the dynamic address pool. The lower threshold for address segment release must be smaller than the upper threshold for address segment application.
        
        The BRAS checks the dynamic address pool usage every 10 minutes. If the BRAS detects that the dynamic address pool usage reaches the upper threshold, it applies to the RADIUS server for new address segments. If the BRAS detects that the dynamic address pool usage falls below the lower threshold, it applies to the RADIUS server for address segment release.
     5. (Optional) Run [**detect**](cmdqueryname=detect) **retransmit** *retransmit-value* **interval** *days* *hours* *minutes*
        
        The interval and time for detecting the RADIUS server is configured for a dynamic address pool.
   * Configure a non-dynamic address pool.
     1. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** { **local** | **remote** } [ **rui-slave** ] | **server** ]
        
        A non-dynamic address pool is configured, and its view is displayed.
        
        A maximum of 4096 address pools can be configured on a device, including access-side and network-side address pools. Each address pool must have a unique name.
     2. Run [**gateway**](cmdqueryname=gateway) *ip-address* { *mask* | *mask-length* }
        
        A gateway address and mask are configured for the address pool.
        
        The gateway address and subnet mask are used to verify if an address in the configured address segment resides on the same subnet as the gateway. Therefore, you must configure the gateway address and mask before configuring address segments.
     3. (Optional) Run [**gateway unnumbered**](cmdqueryname=gateway+unnumbered) **interface** *interface-type* *interface-number*
        
        The address pool is configured to borrow the interface gateway address.
        
        Before configuring a gateway for an IP address pool, ensure that the gateway address and user addresses are on the same subnet. However, the gateway address cannot be assigned to users. As a result, many IP addresses are wasted. The command makes the loopback address of the device as the gateway for the IP address of all users. This prevents IP addresses from being wasted in each address pool.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + The borrowed interface must be configured with an IP address.
        + Currently, the [**gateway unnumbered**](cmdqueryname=gateway+unnumbered) **interface** *interface-type* *interface-number* command can be configured only in the local IPv4 address pool view.
        + If an address pool is bound to a domain, you need to unbind the address pool from the domain first. Otherwise, you cannot configure, delete, or modify the unnumbered interface gateway.
        + The mask length of the gateway configured in a remote address pool must be the same as that in the corresponding server address pool on the DHCP server.
        + Only one [**gateway unnumbered**](cmdqueryname=gateway+unnumbered) **interface** *interface-type* *interface-number* command and one [**gateway ip-address**](cmdqueryname=gateway+ip-address) {*mask* | *mask-length* } command can be configured for an address pool.
        
        When you need to configure a loopback interface as the preferentially used gateway for PPP users who receive the Framed-IP-Address attribute from the RADIUS server, run the [**ppp-gateway unnumbered loopback**](cmdqueryname=ppp-gateway+unnumbered+loopback) command in the AAA view.
     4. Run [**section**](cmdqueryname=section) *section-number* *start-ip-address* [ *end-ip-address* ]
        
        An address segment is configured.
        
        A maximum of 256 address segments can be configured in an address pool. An address segment contains at most 65536 IP addresses. The address segments cannot overlap each other. [**section**](cmdqueryname=section) and [**gateway ip-address**](cmdqueryname=gateway+ip-address) { *mask* | *mask-length* } must be in the same network segment.
     5. (Optional) Run [**wait-request-time**](cmdqueryname=wait-request-time) *time-value*The timeout period for a router to wait for a Request message from a client in response to an Offer message sent to the client is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The [**wait-request-time**](cmdqueryname=wait-request-time) *time-value* command is run in the address pool view whereas the [**access wait-request-time**](cmdqueryname=access+wait-request-time) **dhcpv4** *time-value* command is run in the system view. If the two commands are both run, the command run in the address pool view takes effect.
     6. (Optional) Run [**weight**](cmdqueryname=weight) *weight-value*A weight is configured for the address pool.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + After a weight is configured for an address pool, you must run the [**ip-pool algorithm loading-share remote**](cmdqueryname=ip-pool+algorithm+loading-share+remote) command in the system view to configure the device to assign addresses from IPv4 remote address pools based on weights of the address pools.
        + This function applies only to remote address pools and local RUI-slave address pools.
     7. (Optional) Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     8. (Optional) Run [**ip-pool algorithm loading-share remote**](cmdqueryname=ip-pool+algorithm+loading-share+remote) [ **chasten** { **restrain-period** *period-value* | **timeout-threshold** *threshold-value* } \* ]
        
        A suppression threshold for the number of NAK packets and a suppression period are configured for the remote address pool.
4. (Optional) Run [**dhcp-server check-remote-ip loose**](cmdqueryname=dhcp-server+check-remote-ip+loose)
   
   
   
   The BRAS is disabled from checking whether IP addresses assigned by the DHCP server are on the subnet to which the gateway address of the remote address pool belongs. This command takes effect for remote address pools and remote RUI address pools only.
5. (Optional) Run [**ip-attribute public**](cmdqueryname=ip-attribute+public)
   
   
   
   The public network attribute is configured for the address pool or the address pool group.
   
   
   
   You also need to run the [**ip-pool usage-status threshold**](cmdqueryname=ip-pool+usage-status+threshold) command in the AAA view to configure upper and lower thresholds for public IP address pool usage so that the public IP address pool status can be calculated and sent to the RADIUS server.
   
   This command takes effect only for local address pools.
6. (Optional) Run [**lease**](cmdqueryname=lease) *days* [ *hours* [ *minutes* ] ]
   
   
   
   A lease is configured for the address pool.
   
   
   
   This command takes effect only in the local address pool.
7. (Optional) Run [**rebinding-time**](cmdqueryname=rebinding-time) *days* [ *hours* [ *minutes* ] ]
   
   
   
   The rebinding time is configured for IP addresses.
   
   
   
   This command takes effect only in the local address pool.
8. (Optional) Run [**renewal-time**](cmdqueryname=renewal-time) *days* [ *hours* [ *minutes* ] ]
   
   
   
   The renewal time is configured for IP addresses.
   
   
   
   This command takes effect only in the local address pool.
9. (Optional) Run [**recycle**](cmdqueryname=recycle) *start-ip-address* [ *end-ip-address* ]
   
   
   
   The IP address status is set to idle. When a user is not online, you can reclaim the occupied IP address manually by running this command.
10. (Optional) Run [**conflict auto-recycle**](cmdqueryname=conflict+auto-recycle) **interval** *interval-time*
    
    
    
    The interval at which conflicting addresses are automatically reclaimed is configured.
    
    
    
    If *interval-time* is set to 0, the function to automatically reclaim addresses is disabled, and conflicting addresses are isolated. In this case, you need to run the [**reset conflict-ip-address**](cmdqueryname=reset+conflict-ip-address) command to reclaim conflicting addresses.
    
    If *interval-time* is not set to 0, when the usage of IP addresses in the address pool exceeds the alarm threshold and the address conflict duration exceeds the *interval-time* value, the Router automatically reclaims some conflicting addresses and assigns them to users.
    
    This command takes effect only in the local or server address pool.
11. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
    
    
    
    The VPN instance to which the address pool belongs is configured.
12. (Optional) Run [**warning-threshold**](cmdqueryname=warning-threshold) *warning-threshold-value*
    
    
    
    An alarm threshold for the address usage of the address pool is configured. If the address usage exceeds the threshold, the Router generates an alarm.
13. (Optional) Set the alarm threshold for the address usage of the IPv4 address pool bound to the VPN instance.
    1. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
    2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
       
       
       
       The VPN instance view is displayed.
    3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
       
       
       
       The VPN instance IPv4 address family view is displayed.
    4. Run [**ip-pool warning-threshold**](cmdqueryname=ip-pool+warning-threshold) *threshold*
       
       
       
       An alarm threshold is set for the address usage of the address pool, so that the Router generates an alarm when the address usage exceeds the threshold.
    5. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the VPN instance view.
    6. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
14. (Optional) Run [**warning-exhaust**](cmdqueryname=warning-exhaust)
    
    
    
    The address exhaustion alarm function is enabled for the IP address pool.
    
    
    
    After this command is run, the system generates an address exhaustion alarm when addresses in the IP address pool are exhausted, prompting the administrator to plan IP addresses. When addresses are exhausted, users cannot go online.
    
    When the address usage of the IP address pool falls below 90%, the address exhaustion alarm is cleared.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
16. (Optional) Run [**frame-ip lease manage**](cmdqueryname=frame-ip+lease+manage)
    
    
    
    The lease management function of IP addresses delivered by the RADIUS server is enabled in the IP address pool.
17. (Optional) Run [**option33 route**](cmdqueryname=option33+route) *dest-ip* *gateway-ip*
    
    
    
    User routes are configured in the address pool.
18. (Optional) Run [**option router disable**](cmdqueryname=option+router+disable)
    
    
    
    The device is disabled from sending DHCP messages carrying Option 3 (network gateway address) to clients.
19. (Optional) Enable the function to automatically reclaim IP addresses assigned in RADIUS authentication responses.
    1. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
    2. Run [**aaa**](cmdqueryname=aaa)
       
       
       
       The AAA view is displayed.
    3. Run [**framed-ip conflict auto-recycle**](cmdqueryname=framed-ip+conflict+auto-recycle)
       
       
       
       The function to automatically reclaim IP addresses assigned in RADIUS authentication responses is enabled.
20. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.