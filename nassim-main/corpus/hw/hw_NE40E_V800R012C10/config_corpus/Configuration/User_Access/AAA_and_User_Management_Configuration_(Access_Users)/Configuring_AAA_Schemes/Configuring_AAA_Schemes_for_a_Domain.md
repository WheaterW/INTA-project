Configuring AAA Schemes for a Domain
====================================

Configure AAA schemes for a domain before you can perform AAA on users in this domain.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Specify the domain in which user authentication, authorization, and accounting need to be performed.
4. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *scheme-name*
   
   
   
   An authentication scheme is specified for the domain.
   
   
   
   You can run the [**display authentication-scheme**](cmdqueryname=display+authentication-scheme) command to check detailed information about the default authentication schemes.
5. (Optional) Run [**authening authen-fail online authen-domain**](cmdqueryname=authening+authen-fail+online+authen-domain) *domain-name*
   
   
   
   A domain is set for redirection upon a RADIUS authentication failure.
6. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *scheme-name*
   
   
   
   An accounting scheme is specified for the domain.
7. (Optional) Run [**accounting dual-stack**](cmdqueryname=accounting+dual-stack) { **separate** | **identical** }
   
   
   
   The accounting mode for IPv4/IPv6 dual-stack users is configured.
   
   If **separate** is specified, traffic of IPv4 and IPv6 users is sent to the server separately; if **identical** is configured, traffic of IPv4 and IPv6 users is sent to the server together.
8. Run [**authorization-scheme**](cmdqueryname=authorization-scheme) *authorization-scheme-name*
   
   
   
   An authorization scheme is specified for the domain.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.