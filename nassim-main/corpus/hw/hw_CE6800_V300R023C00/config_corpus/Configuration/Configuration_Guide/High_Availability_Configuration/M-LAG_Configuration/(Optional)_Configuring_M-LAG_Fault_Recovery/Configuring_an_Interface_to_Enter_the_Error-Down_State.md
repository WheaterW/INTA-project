Configuring an Interface to Enter the Error-Down State
======================================================

Configuring an Interface to Enter the Error-Down State

#### Context

On a network with a device dual-homed to an M-LAG, if the peer-link between M-LAG member devices fails but the DAD status remains normal, interfaces except the Ethernet management interface and peer-link interface on one M-LAG member device will enter the error-down state by default. In actual application, uplink interfaces running a routing protocol or interfaces at both ends of the DAD link should not enter the error-down state, which can be achieved by proper configurations.


#### Procedure

* Disable or delay the action of changing interfaces except the Ethernet management interface and peer-link interface on one M-LAG member device to the error-down state if the peer-link between fails but the DAD status remains normal.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the DFS group view.
     
     
     ```
     [dfs-group](cmdqueryname=dfs-group) dfs-group-id
     ```
  3. Disable or delay the action of changing interfaces except the Ethernet management interface and peer-link interface on one M-LAG member device to the error-down state if the peer-link between fails but the DAD status is normal.
     
     
     ```
     [dual-active detection error-down](cmdqueryname=dual-active+detection+error-down) { disable | delay delaytime }
     ```
     By default, interfaces except the Ethernet management interface and peer-link interface on one M-LAG member device change to the error-down state if the peer-link fails but the DAD status remains normal.![](../public_sys-resources/note_3.0-en-us.png) 
     
     When an access device is single-homed to M-LAG master and backup devices at Layer 3, traffic forwarding is not affected even if the peer-link fails but the DAD status remains normal. To disable interfaces except the Ethernet management interface and peer-link interface on one M-LAG member device from entering the error-down state or delay this action to prevent unnecessary packet loss, you can run the [**dual-active detection error-down**](cmdqueryname=dual-active+detection+error-down) command. When an access device is dual-homed to M-LAG master and backup devices or single-homed to M-LAG master and backup devices at Layer 2, you cannot disable or delay the error-down action.
* Configure logical interfaces on the M-LAG backup device to enter the error-down state if the peer-link fails but the DAD status remains normal.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the DFS group view.
     
     
     ```
     [dfs-group](cmdqueryname=dfs-group) dfs-group-id
     ```
  3. Configure logical interfaces on the M-LAG backup device to enter the error-down state if the peer-link fails but the DAD status remains normal.
     
     
     ```
     [dual-active detection error-down mode routing-switch](cmdqueryname=dual-active+detection+error-down+mode+routing-switch)
     ```
     By default, logical interfaces are not triggered to enter the error-down state if the peer-link fails but the DAD status is normal.![](../public_sys-resources/note_3.0-en-us.png) 
     
     On a network with an M-LAG that connects to an IP network or a VXLAN, when logical interfaces on one M-LAG member device are configured to enter the error-down state if the peer-link fails but the DAD status remains normal, only VLANIF interfaces, VBDIF interfaces, loopback interfaces, and the M-LAG member interface on one M-LAG member device will go error-down if conditions are met. If a faulty peer-link interface in the M-LAG recovers, the M-LAG member device restores VLANIF interfaces, VBDIF interfaces, and loopback interfaces to the up state after a delay of 6 seconds upon successful DFS group pairing. This delay leaves time for ARP entry synchronization on a large number of VLANIF interfaces. If such a logical interface has been configured to change its Layer 3 protocol status to up after a certain delay, it will do so after this delay plus an additional 6 seconds.
     
     To improve the switchover convergence performance in a scenario where the peer-link fails and two master devices exist, you are advised to configure the **[**port-status fast-detect enable**](cmdqueryname=port-status+fast-detect+enable)** command on the interfaces connecting M-LAG member devices to upstream and downstream devices and on the connected interfaces on these devices to enable the chip to quickly detect the physical status change of interfaces.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure interfaces not to enter the error-down state if the peer-link fails but the DAD status remains normal.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure interfaces not to enter the error-down state if the peer-link fails but the DAD status remains normal.
     
     
     ```
     [m-lag unpaired-port reserved](cmdqueryname=m-lag+unpaired-port+reserved)
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     It is recommended that you configure this command on interfaces on both the M-LAG master and backup devices to ensure that the interfaces in error-down state on the two devices are consistent after a master/backup switchover.
     
     You are advised to configure this command on the underlay outbound interface of a static bypass VXLAN tunnel in a virtual peer-link scenario to prevent the interface from entering the error-down state.
     
     This command cannot be configured on peer-link interfaces or M-LAG member interfaces.
     
     This command cannot be configured on a physical interface that has been added to an Eth-Trunk interface.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure interfaces to enter the error-down state automatically if the peer-link fails but the DAD status remains normal.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure interfaces to enter the error-down state automatically if the peer-link fails but the DAD status remains normal.
     
     
     ```
     [m-lag unpaired-port suspend](cmdqueryname=m-lag+unpaired-port+suspend)
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     It is recommended that you configure this command on interfaces on both the M-LAG master and backup devices to ensure that the interfaces in error-down state on the two devices are consistent after a master/backup switchover.
     
     This command cannot be configured on peer-link interfaces or M-LAG member interfaces.
     
     This command cannot be configured on a physical interface that has been added to an Eth-Trunk interface.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the interfaces that transmit uplink traffic as uplink interfaces. When the peer-link fails but the DAD status is normal, if all uplink interfaces of one M-LAG member device are down and the other M-LAG member device has uplink interfaces in the up state, the error-down action is triggered on the M-LAG member device whose uplink interfaces are all down. For details about the range of interfaces that enter the error-down state, see the interface error-down rules described in this section.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the interface that transmits uplink traffic as an uplink interface.
     
     
     ```
     uplink-port enable
     ```
     
     By default, an interface is not an uplink interface.
     
     
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     A maximum of 256 uplink interfaces can be configured on a device.
     
     If no uplink interface is configured on a device, uplink interfaces on the device are considered up.
     
     An uplink interface transmits uplink traffic. Do not configure an interface that does not transmit uplink traffic as an uplink interface.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```