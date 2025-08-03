Configuring Binding Authentication
==================================

In addition to web authentication, users can also be authenticated using binding authentication.

#### Context

In addition to web authentication, users can also be authenticated using binding authentication.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber**
   
   
   
   The user access type is set to Layer 2 subscriber access.
5. Run [**default-domain**](cmdqueryname=default-domain) **pre-authentication** *domain-name*
   
   
   
   The default pre-authentication domain is specified.
6. Run [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name*
   
   
   
   The default authentication domain is specified.
7. Run [**authentication-method**](cmdqueryname=authentication-method) **bind**
   
   
   
   PPP authentication, 802.1X authentication, or binding authentication is configured.
   
   You can set authentication methods for only Layer 2 users on a BAS interface. Multiple authentication modes can be configured on an interface but you should note the following:
   
   * Web authentication conflicts with fast authentication.
   * Binding authentication conflicts with the other authentication modes.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.