Configuring IPv4 FRR
====================

Configuring IPv4 FRR

#### Prerequisites

Before configuring IPv4 FRR, you have completed the following tasks:

* Set data link layer protocol parameters and IPv4 addresses for interfaces to ensure that the data link layer protocol status on each interface is up.
* Configure routes of different routing protocols but destined for the same destination address.

#### Context

Public network IPv4 FRR is applicable to services that are sensitive to the delay or packet loss on an IPv4 public network.

After IPv4 FRR is configured, if a link fault is detected, the fault is reported to the route management module. Then, packets are switched to a standby link, which minimizes the impact of the link fault on ongoing services.

![](public_sys-resources/notice_3.0-en-us.png) 

IPv4 FRR enables routes of different types to back up each other, which may result in loops. Exercise caution when enabling this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IPv4 FRR.
   
   
   ```
   [ip frr](cmdqueryname=ip+frr)
   ```
   
   If FRR is configured both in the system view and a routing protocol view, the FRR that is configured in the routing protocol view preferentially takes effect.
   
   By default, IP FRR of the public network is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **verbose** command to check detailed information about the backup outbound interface and backup next hop in the routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *masklength* ] [ **longer-match** ] **verbose** command to check destination-specific information about the backup outbound interface and backup next hop in the routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *prefix* { *mask* | *masklength* } **verbose** command to check prefix-specific information about the backup outbound interface and backup next hop in the routing table.