Configuring Intra-VLAN Proxy ND
===============================

Configuring Intra-VLAN Proxy ND

#### Context

Hosts that belong to the same VLAN are unable to communicate with each other if Layer 2 interface isolation is configured in the VLAN. In this case, you can enable intra-VLAN proxy ND on a device's interface associated with the VLAN to allow the hosts to communicate.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLANIF interface or Layer 3 sub-interface view.
   
   
   * Enter the VLANIF interface view.
     ```
     [interface vlanif](cmdqueryname=interface+vlanif) vlan-id
     ```
   * Enter the Layer 3 sub-interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number.sub-number
     ```
3. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
4. Configure a global unicast address for the interface.
   
   
   ```
   [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ] [ tag tag-value ]
   ```
5. Configure intra-VLAN proxy ND.
   
   
   ```
   [ipv6 nd proxy inner-access-vlan enable](cmdqueryname=ipv6+nd+proxy+inner-access-vlan+enable) 
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```