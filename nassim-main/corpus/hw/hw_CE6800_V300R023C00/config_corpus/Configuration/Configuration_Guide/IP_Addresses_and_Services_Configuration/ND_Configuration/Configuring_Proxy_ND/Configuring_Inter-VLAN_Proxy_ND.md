Configuring Inter-VLAN Proxy ND
===============================

Configuring Inter-VLAN Proxy ND

#### Context

Hosts that belong to different VLANs on a physical network segment are unable to communicate with each other at Layer 3. In this case, you can enable inter-VLAN proxy ND on a device's interface associated with these VLANs to allow the hosts to communicate.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the VLANIF interface view.
   
   
   ```
   [interface vlanif](cmdqueryname=interface+vlanif) vlan-id
   ```
5. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
6. Configure a global unicast address for the interface.
   
   
   ```
   [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ] [ tag tag-value ]
   ```
7. Configure inter-VLAN proxy ND.
   
   
   ```
   [ipv6 nd proxy inter-access-vlan enable](cmdqueryname=ipv6+nd+proxy+inter-access-vlan+enable) 
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```