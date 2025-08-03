Binding a 802.1X Template to a Domain
=====================================

When 802.1X authentication is used for users in a domain, authentication negotiation is performed based on parameters defined in a dot1x template.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**dot1x-template**](cmdqueryname=dot1x-template) *dot1x-template-number*
   
   
   
   A dot1x template is bound to a domain.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.