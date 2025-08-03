Verifying the IPv6 GRE Tunnel Configuration
===========================================

After configuring an IPv6 GRE tunnel, you can check the
status of the tunnel interface and routing information.

#### Prerequisites

An IPv6 GRE tunnel has been configured.
#### Procedure

* Run the [**display ipv6 interface tunnel**](cmdqueryname=display+ipv6+interface+tunnel) command to
  check the status of a tunnel interface.
* Run either of the following commands to check related information:
  
  
  
  If an IPv4 address is configured for the tunnel interface:
  
  + Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check
    the IPv4 routing table.
  + Run the [**ping**](cmdqueryname=ping) **-a** *source-ip-address* *dest-ip-address* command to check tunnel connectivity.
  
  If an IPv6 address is configured for the tunnel interface:
  
  + Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check
    the IPv6 routing table.
  + Run the [**ping
    ipv6**](cmdqueryname=ping+ipv6) **-a** *source-ipv6-address* *dest-ipv6-address* command to check tunnel connectivity.