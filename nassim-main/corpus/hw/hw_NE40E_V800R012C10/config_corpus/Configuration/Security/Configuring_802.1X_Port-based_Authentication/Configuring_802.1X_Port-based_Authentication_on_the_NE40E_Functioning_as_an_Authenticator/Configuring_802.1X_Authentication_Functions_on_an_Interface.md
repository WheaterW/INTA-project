Configuring 802.1X Authentication Functions on an Interface
===========================================================

After 802.1X authentication is enabled on an interface, a user device connected to the interface can access the network only after being authenticated. If authentication fails, the user device cannot access the network.

#### Context

802.1X authentication supports two access control types:

* Interface-based access control: After the first user is authenticated, subsequent users can use network resources without being authenticated. If the first user goes offline, the other users can no longer access the network.
* MAC-based access control: Every user accessing an interface is authenticated. If a user goes offline, other authenticated users can still access the network. If the supplicant does not support 802.1X port-based authentication, MAC address bypass authentication can be used.

An 802.1X authentication-enabled interface supports the following authorization modes:

* Authorized: **authorized-force** is configured to allow users to access the network without being authenticated.
* Auto: **auto** is configured to allow only EAPOL packets to pass through and prohibit users from accessing network resources. If authentication succeeds, the interface enters the authorized state and allows users to access the network.
* Unauthorized: **unauthorized-force** is configured to prohibit user authentication. The authenticator does not provide authentication services for access users on this interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the access control type or authorization state of an interface is changed when 802.1X users are accessing the network through this interface, the users may be logged out.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**dot1x enable**](cmdqueryname=dot1x+enable)
   
   
   
   802.1X authentication is enabled on the interface.
4. Run [**dot1x force-domain**](cmdqueryname=dot1x+force-domain) *domain-name*
   
   
   
   A forcible authentication domain is configured for 802.1X authentication on the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The domain specified in the [**dot1x force-domain**](cmdqueryname=dot1x+force-domain) command is the forcible authentication domain configured for 802.1X authentication on the interface.
5. (Optional) Run [**dot1x port-method**](cmdqueryname=dot1x+port-method) { **port** | **mac** }
   
   
   
   An access control type is configured on the interface.
   
   
   
   * If a supplicant does not support 802.1X port-based authentication after the [**dot1x port-method mac**](cmdqueryname=dot1x+port-method+mac) command is run, run the [**dot1x mac-bypass**](cmdqueryname=dot1x+mac-bypass) command to enable MAC address bypass authentication.
   * After MAC address bypass authentication is enabled on an interface, to separately manage the traffic of users who pass the authentication and who fail the authentication, run the [**dot1x vlan-tagged**](cmdqueryname=dot1x+vlan-tagged) command to configure redirection parameters for a specified VLAN.
6. (Optional) Run [**dot1x port-control**](cmdqueryname=dot1x+port-control) { **authorized-force** | **auto** | **unauthorized-force** }
   
   
   
   An authorization mode for 802.1X authentication on the interface is configured.
7. (Optional) Run [**dot1x max-user**](cmdqueryname=dot1x+max-user) *number*
   
   
   
   The maximum number of access users allowed to access the 802.1X authentication-enabled interface is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the number of access users on an interface reaches the configured upper limit, no more users can access the network through this interface.
8. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. (Optional) Run **[**radius-attribute nas-identifier max-length unlimited**](cmdqueryname=radius-attribute+nas-identifier+max-length+unlimited)**
   
   
   
   The length limit of the RADIUS attribute NAS-Identifier is canceled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The NE40E-M2E does not support the **radius-attribute nas-identifier max-length unlimited** command.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.