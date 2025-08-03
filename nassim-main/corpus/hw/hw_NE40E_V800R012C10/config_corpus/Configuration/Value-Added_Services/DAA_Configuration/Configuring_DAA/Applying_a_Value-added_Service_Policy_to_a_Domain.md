Applying a Value-added Service Policy to a Domain
=================================================

If a policy server does not deliver any service policy, the service policy configured in a domain is used.

#### Context

After a value-added service policy is applied to a domain, all users in the domain use this policy as the default value-added service policy. The service policy sent by a policy server takes precedence over the service policy configured in a domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**value-added-service policy**](cmdqueryname=value-added-service+policy) *service-policy-name*
   
   
   
   A value-added service policy is bound to the domain.
5. (Optional) Run [**accounting-service-policy**](cmdqueryname=accounting-service-policy) { **inbound** | **outbound** } { **disable** | **enable** }
   
   
   
   The device is enabled to determine whether to match the upstream or downstream traffic of users that go online through an AAA domain against DAA services.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.