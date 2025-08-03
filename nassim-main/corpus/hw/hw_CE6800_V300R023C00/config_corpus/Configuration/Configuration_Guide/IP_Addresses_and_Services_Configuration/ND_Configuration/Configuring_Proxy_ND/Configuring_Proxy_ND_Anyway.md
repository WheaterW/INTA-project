Configuring Proxy ND Anyway
===========================

Configuring Proxy ND Anyway

#### Context

In scenarios where servers are partitioned into VMs, the flexible deployment and migration of VMs on multiple servers or gateways can be achieved by configuring Layer 2 interconnection between multiple gateways. However, this approach may lead to larger Layer 2 domains on the network and the risk of broadcast storms. To resolve this issue, enable proxy ND anyway on a VM gateway. In this way, the gateway sends its interface MAC address to a source VM and communication between VMs is implemented through route forwarding.


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
6. Configure proxy ND anyway.
   
   
   ```
   [ipv6 nd proxy anyway enable](cmdqueryname=ipv6+nd+proxy+anyway+enable) 
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```