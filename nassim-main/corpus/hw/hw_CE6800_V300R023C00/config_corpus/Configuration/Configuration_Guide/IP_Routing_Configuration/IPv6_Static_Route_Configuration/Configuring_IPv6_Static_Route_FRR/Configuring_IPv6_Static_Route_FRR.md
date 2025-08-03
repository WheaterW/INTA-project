Configuring IPv6 Static Route FRR
=================================

Configuring IPv6 Static Route FRR

#### Prerequisites

Before configuring IPv6 static route FRR, you have completed the following tasks:

* Set data link layer protocol parameters and IPv6 addresses for interfaces to ensure that the data link layer protocol status of each interface is up.
* To speed up fault detection, configure dynamic BFD for IPv6 static route or static BFD for IPv6 static route.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IPv6 static route FRR.
   
   
   ```
   [ipv6 route-static frr](cmdqueryname=ipv6+route-static+frr) [ vpn-instance vpn-instance-name ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Before FRR is enabled to perform static route backup, set different preference values for these static routes.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```