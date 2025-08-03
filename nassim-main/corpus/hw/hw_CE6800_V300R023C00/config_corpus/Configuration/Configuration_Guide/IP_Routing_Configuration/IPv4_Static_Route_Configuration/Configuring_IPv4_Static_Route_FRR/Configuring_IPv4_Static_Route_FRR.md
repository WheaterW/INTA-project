Configuring IPv4 Static Route FRR
=================================

Configuring IPv4 Static Route FRR

#### Prerequisites

Before configuring IPv4 static route FRR, you have completed the following tasks:

* Set data link layer protocol parameters and IP addresses for interfaces to ensure that the data link layer protocol status of each interface is up.
* Configure two or more IPv4 static routes with the same prefix and mask and different preference values.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable FRR for IPv4 static routes.
   
   
   ```
   [ip route-static frr](cmdqueryname=ip+route-static+frr) [ vpn-instance vpn-instance-name ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Before enabling FRR for static routes to implement route backup, set different preference values for these static routes.
   
   In a scenario where FRR for static route and BFD for static route are both configured, if you need FRR to be implemented between a static route with an Ethernet outbound interface specified and another static route, you must ensure that the two routes have both an outbound interface and a next-hop IP address specified.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```