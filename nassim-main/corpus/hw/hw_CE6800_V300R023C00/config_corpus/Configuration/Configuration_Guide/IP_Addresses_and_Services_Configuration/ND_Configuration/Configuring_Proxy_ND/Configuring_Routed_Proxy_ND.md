Configuring Routed Proxy ND
===========================

Configuring Routed Proxy ND

#### Context

Hosts that belong to the same network segment but different physical networks are unable to communicate with each other if the gateways connected to them have different IPv6 addresses. In this case, you can enable routed proxy ND on a device's interface connected to the hosts to allow them to communicate.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure a global unicast address for the interface.
   
   
   ```
   [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ] [ tag tag-value ]
   ```
6. Configure routed proxy ND.
   
   
   ```
   [ipv6 nd proxy route enable](cmdqueryname=ipv6+nd+proxy+route+enable) 
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```