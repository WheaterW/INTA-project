(Optional) Configuring an Interface to Fill in DD Packets with Its Own MTU
==========================================================================

(Optional) Configuring an Interface to Fill in DD Packets with Its Own MTU

#### Context

To improve compatibility with a non-Huawei device, an OSPF-enabled Huawei device adds the MTU 0 in DD packets to be sent and does not check the MTUs in received DD packets, thereby allowing an OSPF neighbor relationship to be set up even if the two ends have different MTU settings.

However, under the default configuration, the non-Huawei device may discard a DD packet received from the Huawei device if the packet's actual MTU is greater than the MTU of the non-Huawei device. If an LSU is discarded, an OSPF neighbor relationship can still be set up, but the routing information carried in the LSU fails to be learned, causing service interruption.

To resolve this issue, you are advised to enable an interface to add its actual MTU in DD packets to be sent and check whether the MTU in a received DD packet is greater than the local MTU. If the interface MTU settings of the local and remote ends are different, an OSPF neighbor relationship cannot enter the Full state. By doing this, MTU inconsistency can be identified in a timely manner.

![](../public_sys-resources/notice_3.0-en-us.png) 

Enabling an interface to fill in DD Packets with its actual MTU will cause the involved neighbor relationship to be re-established.



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
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable the interface to fill in DD packets to be sent with its actual MTU and check whether the MTU in a DD packet received from a neighbor exceeds the local MTU.
   
   
   ```
   [ospf mtu-enable](cmdqueryname=ospf+mtu-enable)
   ```
   
   By default, the MTU value is 0 when an interface sends DD packets. That is, the actual MTU value of the interface is not filled in DD packets.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```