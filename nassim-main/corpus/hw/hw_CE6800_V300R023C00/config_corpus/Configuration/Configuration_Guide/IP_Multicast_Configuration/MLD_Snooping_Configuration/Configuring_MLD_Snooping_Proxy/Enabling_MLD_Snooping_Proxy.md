Enabling MLD Snooping Proxy
===========================

Enabling MLD Snooping Proxy

#### Context

When MLD is disabled on Layer 3 devices (for example, when only a static multicast group is configured), no MLD querier is available on the network to maintain multicast group memberships. In this case, you can configure MLD snooping proxy on the Layer 2 device so that it functions as an MLD querier and sends Query messages.

Conversely, when MLD is enabled on the network, you can also configure MLD snooping proxy on a Layer 2 device. In this case, the device sends MLD Report/Done messages to its upstream Layer 3 device on behalf of user hosts. This helps reduce the number of such messages sent to the Layer 3 device.

![](../public_sys-resources/note_3.0-en-us.png) 

* MLD snooping proxy and the following functions cannot be configured in the same VLAN:
  + MLD snooping querier
  + Report and Done message suppression
* The MLD snooping proxy function cannot be enabled in a VLAN if the corresponding Layer 3 VLANIF interface has Layer 3 multicast functions (such as MLD and PIM) enabled.
* When configuring MLD snooping in an M-LAG scenario, ensure that the MLD snooping proxy configuration is consistent on the active and standby M-LAG devices.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Enable MLD snooping proxy.
   
   
   ```
   [mld snooping proxy](cmdqueryname=mld+snooping+proxy)
   ```
4. (Optional) Configure the device to transparently transmit protocol messages in a VLAN.
   
   
   ```
   [mld snooping proxy router-protocol-pass](cmdqueryname=mld+snooping+proxy+router-protocol-pass)
   ```
   
   By default, an MLD snooping proxy device terminates received protocol messages and learns multicast forwarding entries from these messages. If MLD snooping proxy is enabled on both the upstream and downstream devices, you can run this command so that the device transparently forwards the protocol messages it receives on a router port to other router ports, without learning the entries from the messages. In this way, the upstream and downstream devices do not learn entries from each other, which would otherwise cause entry aging problems.
5. (Optional) Disable the device from forwarding MLD Query messages to the upstream router.
   1. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   3. Switch the interface working mode from Layer 3 to Layer 2.
      
      
      ```
      [portswitch](cmdqueryname=portswitch)
      ```
      
      Determine whether to perform this step based on the current interface working mode.
   4. Disable the device from forwarding MLD Query messages to the upstream router.
      
      
      ```
      [mld snooping proxy-uplink-port](cmdqueryname=mld+snooping+proxy-uplink-port) vlan vlan-id
      ```
      
      
      
      After MLD snooping proxy is enabled on a device, it periodically broadcasts MLD Query messages to all the interfaces (including router ports) in a VLAN. This may result in reelection of the MLD querier. To prevent such reelection if MLD is enabled on the upstream device, run this command to disable forwarding of MLD messages to router ports.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```