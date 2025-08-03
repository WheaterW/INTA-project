(Optional) Configuring a Basic Protocol Stack for IPoE Dual-stack Users
=======================================================================

This section describes how to configure a basic protocol stack for IPoE dual-stack users so that the device allows user access from the other stack only after it detects that the users have been online from the basic protocol stack.

#### Context

In cold standby scenarios, to implement load balancing among multiple BRASs, run the [**ipoe-service-type**](cmdqueryname=ipoe-service-type) command to configure a basic protocol stack for IPoE dual-stack users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber**
   
   
   
   The access type of the BAS interface is set to Layer 2 subscriber access.
5. Run [**default-domain**](cmdqueryname=default-domain) **pre-authentication** *domain-name*
   
   
   
   The default pre-authentication domain is configured on the BAS interface.
6. Run [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name*
   
   
   
   The default authentication domain is configured on the BAS interface.
7. Run either of the following command:
   1. To configure binding authentication on the BAS interface for IPv4 users, run the [**authentication-method**](cmdqueryname=authentication-method) **bind** command.
   2. To configure binding authentication on the BAS interface for IPv6 users, run the [**authentication-method-ipv6**](cmdqueryname=authentication-method-ipv6) **bind** command.
   
   
   
   You can configure authentication methods for only Layer 2 users on BAS interfaces. Multiple authentication methods can be configured on an interface but you should note the following:
   
   * Web authentication conflicts with fast authentication.
   * Bind authentication conflicts with the other authentication modes.
8. Run [**ipoe-service-type**](cmdqueryname=ipoe-service-type) { **ipv4** | **ipv6** }
   
   
   
   A basic protocol stack is configured for IPoE dual-stack users.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.