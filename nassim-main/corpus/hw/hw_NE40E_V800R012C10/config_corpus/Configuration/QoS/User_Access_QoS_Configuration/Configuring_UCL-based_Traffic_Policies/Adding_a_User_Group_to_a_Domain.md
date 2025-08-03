Adding a User Group to a Domain
===============================

Before applying a UCL-based traffic policy to users in a user group, add the user group to a domain.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**user-group**](cmdqueryname=user-group) *user-group-name*
   
   
   
   A specified user group is added to the domain.
5. (Optional) Run: [**traffic-policy ucl**](cmdqueryname=traffic-policy+ucl) **upstream match-source-ip** [ **ipv4** | **ipv6** ] [ **user-group-list** *user-group-list-name* ]
   
   
   
   MF classification based on user source IP addresses is configured.
   
   
   
   To perform MF classification based on user source IP addresses, perform this step.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.