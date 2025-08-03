(Optional) Configuring the Renewal Time and Rebinding Time of an Address Pool
=============================================================================

(Optional)_Configuring_the_Renewal_Time_and_Rebinding_Time_of_an_Address_Pool

#### Context

When you need to set the renewal time and rebinding time of an IPv6 address pool, specify the percentage of the renewal time to the preferred lifetime and the percentage of the rebinding time to the preferred lifetime. If the specified renewal time and rebinding time are too short, the lease period (T1) and renewal time (T2) of the IPv6 addresses assigned by the DHCPv6 server is also too short, causing the clients to frequently send Renew messages. Set the renewal time and rebinding time as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name*
   
   
   
   An IPv6 address pool is created, and its view is displayed.
3. Run [**renew-time-percent**](cmdqueryname=renew-time-percent) *renew-time-percent* **rebind-time-percent** *rebind-time-percent*
   
   
   
   The percentage of the renewal time to the preferred lifetime and the percentage of the rebinding time to the preferred lifetime are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.