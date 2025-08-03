(Optional) Configuring the Time for Updating Configuration Parameters Assigned to Clients Through Stateless DHCPv6 Address Autoconfiguration
============================================================================================================================================

(Optional)_Configuring_the_Time_for_Updating_Configuration_Parameters_Assigned_to_Clients_Through_Stateless_DHCPv6_Address_Autoconfiguration

#### Context

When the DHCPv6 server assigns network configuration parameters (such as the DNS, NIS, and SNTP server addresses, but not IPv6 addresses) to DHCPv6 clients through stateless DHCPv6 address autoconfiguration, you can configure the time for updating these network configuration parameters. The clients then obtain the latest network configuration parameters from the server at the configured interval.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name*
   
   
   
   An IPv6 address pool is created, and its view is displayed.
3. Run [**information-refresh**](cmdqueryname=information-refresh) *time*
   
   
   
   The time for updating network configuration parameters assigned to clients through stateless DHCPv6 address autoconfiguration is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.