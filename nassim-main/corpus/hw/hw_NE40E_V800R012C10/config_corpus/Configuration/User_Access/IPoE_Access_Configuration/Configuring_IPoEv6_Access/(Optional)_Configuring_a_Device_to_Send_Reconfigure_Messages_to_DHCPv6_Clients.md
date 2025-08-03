(Optional) Configuring a Device to Send Reconfigure Messages to DHCPv6 Clients
==============================================================================

(Optional) Configuring a Device to Send Reconfigure Messages to DHCPv6 Clients

#### Context

In a Layer 2 user access scenario where a BRAS is required to log out online DHCPv6 users, to allow clients to detect user logouts immediately after users are offline so that the clients can re-dial up for login, configure the BRAS to send Reconfigure messages to DHCPv6 clients. This greatly reduces the duration of IPv6 service interruption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access dhcpv6-reconfigure**](cmdqueryname=access+dhcpv6-reconfigure)
   
   
   
   The device is enabled to send Reconfigure messages to DHCPv6 clients, and the access-side Reconfigure view is displayed.
3. (Optional) Run [**retransmit times**](cmdqueryname=retransmit+times) *retransmit-times*
   
   
   
   The number of retransmissions of Reconfigure messages to DHCPv6 clients is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
7. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
8. Run [**dhcp coa-zero-lease dhcpv6-enhance layer2**](cmdqueryname=dhcp+coa-zero-lease+dhcpv6-enhance+layer2)
   
   
   
   In Layer 2 access scenarios, the lease time delivered by the RADIUS server in a CoA message with the value 0 takes effect for both DHCPv4 and DHCPv6 users.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.