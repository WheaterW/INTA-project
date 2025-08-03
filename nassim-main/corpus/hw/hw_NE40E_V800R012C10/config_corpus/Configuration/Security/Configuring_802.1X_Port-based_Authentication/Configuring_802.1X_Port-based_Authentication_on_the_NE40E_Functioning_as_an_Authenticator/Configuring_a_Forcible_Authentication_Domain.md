Configuring a Forcible Authentication Domain
============================================

After a forcible authentication domain is configured, the NE40E uses the authentication policy configured in this domain to authenticate users.

#### Prerequisites

* Configure an authentication scheme (RADIUS authentication).
* Configure a RADIUS server group.

#### Context

To ensure that users go online from the configured domain for authentication and accounting, you need to configure a forcible authentication domain so that all 802.1X users accessing the interface are authenticated in this domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *scheme-name*
   
   
   
   An authentication scheme is specified for the domain.
5. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *accounting-scheme-name*
   
   
   
   An accounting scheme is specified for the domain.
6. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   A RADIUS server group is specified for the domain.
7. Run [**dot1x-template**](cmdqueryname=dot1x-template) *dot1x-template-number*
   
   
   
   An 802.1X template is bound to the domain.