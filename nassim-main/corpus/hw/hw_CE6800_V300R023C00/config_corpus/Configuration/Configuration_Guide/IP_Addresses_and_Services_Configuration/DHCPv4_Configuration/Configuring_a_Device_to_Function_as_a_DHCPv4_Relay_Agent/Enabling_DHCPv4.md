Enabling DHCPv4
===============

Enabling DHCPv4

#### Context

Before configuring DHCPv4 relay, you must enable DHCPv4 in the system view.

When both the DHCPv4 server and relay functions are enabled on a device's interface, the device preferentially performs the DHCPv4 server process. That is, the device preferentially uses the local DHCPv4 server (that is, the DHCPv4 server on the same network segment as the IPv4 address of the interface) to allocate IPv4 addresses. If the local server cannot allocate IPv4 addresses, the device uses DHCPv4 relay so that the remote server allocates IPv4 addresses.

![](public_sys-resources/note_3.0-en-us.png) 

When configuring DHCPv4 relay on a Multichassis Link Aggregation Group (M-LAG), you must configure DHCPv4 relay on the two devices that constitute the M-LAG.



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