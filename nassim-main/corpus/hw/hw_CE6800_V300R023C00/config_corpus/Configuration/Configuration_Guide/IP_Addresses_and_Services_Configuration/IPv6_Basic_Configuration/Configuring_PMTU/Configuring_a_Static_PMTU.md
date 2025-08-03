Configuring a Static PMTU
=========================

Configuring a Static PMTU

#### Context

Generally, a PMTU is dynamically negotiated based on the IPv6 MTU of an interface. To protect a device against attacks from jumbo packets in special situations, manually configure a PMTU for a specified destination node to control the maximum length of packets forwarded from the device to the destination node.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a PMTU for a specified IPv6 address.
   
   
   ```
   [ipv6 pathmtu](cmdqueryname=ipv6+pathmtu+vpn-instance) ipv6-address [ [ vpn-instance vpn-instance-name ] path-mtu ]
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```