Enabling DHCPv4
===============

Enabling DHCPv4

#### Context

Before configuring the DHCPv4 server function, you must enable DHCPv4 in the system view.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DHCPv4.
   
   
   ```
   [dhcp enable](cmdqueryname=dhcp+enable) [ ipv4 | ipv6 ]
   ```
   
   If **ipv4** is specified, only DHCPv4 is enabled. If **ipv6** is specified, only DHCPv6 is enabled. If no parameter is specified, both DHCPv4 and DHCPv6 are enabled.
   
   The CE6885-LL supports the **ipv4** and **ipv6** parameters only in standard forwarding mode.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```