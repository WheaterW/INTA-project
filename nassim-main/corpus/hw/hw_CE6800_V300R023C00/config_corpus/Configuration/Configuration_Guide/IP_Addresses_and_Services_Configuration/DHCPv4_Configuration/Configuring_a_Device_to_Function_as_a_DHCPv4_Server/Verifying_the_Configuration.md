Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ip pool**](cmdqueryname=display+ip+pool) command to check the address allocation information of address pools.
  
  
  + Check all address pools.
    
    [**display ip pool**](cmdqueryname=display+ip+pool)
  + Check all address pools in a specified VPN instance.
    
    [**display ip pool**](cmdqueryname=display+ip+pool) **vpn-instance** *vpn-instance-name*
  + Check an interface address pool.
    
    [**display ip pool**](cmdqueryname=display+ip+pool) **interface** *interface-pool-name* [ *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** ]
  + Check a global address pool.
    
    [**display ip pool**](cmdqueryname=display+ip+pool) **name** *pool-name* [ *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** ]![](public_sys-resources/note_3.0-en-us.png) 
  
  If **conflict** is specified, information about conflicting IPv4 addresses in the address pool is displayed.
  
  If **expired** is specified, information about expired IPv4 addresses in the address pool is displayed.
  
  If **used** is specified, information about used IPv4 addresses in the address pool is displayed.
* Run the [**display dhcp server database**](cmdqueryname=display+dhcp+server+database) command to check the path for storing DHCPv4 data.
* Run the [**display dhcp server configuration**](cmdqueryname=display+dhcp+server+configuration) command to check the configuration of the DHCPv4 server.
* Run the [**display dhcp server statistics**](cmdqueryname=display+dhcp+server+statistics) command to check statistics about DHCPv4 messages sent and received on the DHCPv4 server.
* Run the [**display dhcp statistics**](cmdqueryname=display+dhcp+statistics) command to check statistics about DHCPv4 messages sent and received by the device.
* Run the [**display dhcp configuration**](cmdqueryname=display+dhcp+configuration) command to check the configuration of the DHCPv4 public module.