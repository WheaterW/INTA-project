(Optional) Specifying a Group for a Domain
==========================================

A domain can be specified to belong to a user group or
a VPN instance. This allows the domain to be flexibly associated with
various services.

#### Context

A domain can belong to any of the following groups:

* User group
  
  A user group is used to control the access
  right of users and implement ACLs. Up to 255 user groups can be configured
  on the NE40E.
* VPN instance

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run either of the following commands:
   
   
   * To specify a user group for the domain, run the [**user-group**](cmdqueryname=user-group) *group-name* command.
   * To specify a VPN instance for the domain, run the [**vpn-instance**](cmdqueryname=vpn-instance) *instance-name* command.
   * To specify an inbound VPN instance for the domain, run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* **inbound** command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Perform the instance configuration
     in hub and spoke networking scenarios. The VPN instances configured
     using the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* **inbound** command must be different from
     any of those configured using the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.