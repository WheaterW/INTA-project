Configuring Global Anycast RP
=============================

Configuring Global Anycast RP

#### Context

On the devices to be deployed with anycast RP in a PIM-SM domain, configure the address of the RP elected in the domain as their anycast RP address.

Either static or dynamic RPs can be used on a network. Using loopback interfaces as RPs is recommended. You need to configure the same RP address on the devices to be deployed with anycast RP.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IPv6 PIM view.
   
   
   ```
   [pim ipv6](cmdqueryname=pim+ipv6) [vpn-instance vpn-instance-name ]
   ```
3. Configure an anycast RP and enter its view.
   
   
   ```
   [anycast-rp](cmdqueryname=anycast-rp) rp-address
   ```
   
   
   
   The anycast RP address must be the same as the RP address on the network.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```