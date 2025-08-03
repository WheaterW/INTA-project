Configuring IPv6 FRR
====================

Configuring IPv6 FRR

#### Prerequisites

Before configuring IPv6 FRR, you have completed the following tasks:

* Set data link layer protocol parameters and IPv6 addresses for interfaces to ensure that the data link layer protocol status on each interface is up.
* Configure routes of different routing protocols but destined for the same destination address.

#### Context

Public network IPv6 FRR is applicable to services that are sensitive to the delay or packet loss on an IPv6 public network.

After IPv6 FRR is configured, if a link fault is detected, the fault is reported to the route management module. Then, packets are switched to a standby link, which minimizes the impact of the link fault on ongoing services.

![](public_sys-resources/notice_3.0-en-us.png) 

IPv6 FRR enables routes of different types to back up each other, which may result in loops. Exercise caution when enabling this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IPv6 FRR.
   
   
   ```
   [ipv6 frr](cmdqueryname=ipv6+frr)
   ```
   
   If FRR is configured both in the system view and a routing protocol view, the FRR that is configured in the routing protocol view preferentially takes effect.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **verbose** command to check detailed information about the backup outbound interface and backup next hop in the routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] **verbose** command to check destination-specific information about the backup outbound interface and backup next hop in the routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address1* { *prefix-length1* } *ipv6-address2* { *prefix-length2* } **verbose** command to check prefix-specific information about the backup outbound interface and backup next hop in the routing table.