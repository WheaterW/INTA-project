Creating an Eth-Trunk Interface and Configure a Link Aggregation Mode for It
============================================================================

Creating an Eth-Trunk Interface and Configure a Link Aggregation Mode for It

#### Prerequisites

Before configuring an Eth-Trunk, you have completed the following task:

Connect interfaces and ensure that they are physically up.


#### Context

Eth-Trunks in manual mode apply to scenarios where the peer device does not support LACP. Eth-Trunks in dynamic LACP mode apply only to scenarios where Huawei devices connect to servers. In other scenarios, you are advised to deploy Eth-Trunks in static LACP mode. If dynamic LACP is used, loops may occur on the network.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an Eth-Trunk interface and enter the Eth-Trunk interface view.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
3. (Optional) Switch the Eth-Trunk interface to work in Layer 2 or Layer 3 mode, depending on the current interface working mode.
   
   
   
   Switch the Eth-Trunk interface to work in Layer 2 mode.
   
   ```
   [portswitch](cmdqueryname=portswitch)   
   ```
   
   Switch the Eth-Trunk interface to work in Layer 3 mode.
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * An Eth-Trunk interface can either work in Layer 2 or Layer 3 mode. To add an Eth-Trunk interface to a VLAN or configure it to transmit Layer 2 data packets, you need to configure the Eth-Trunk interface to work in Layer 2 mode. In this case, all Layer 3 functions of the Eth-Trunk interface are disabled, and the Eth-Trunk interface uses the system MAC address. To use an Eth-Trunk interface to transmit Layer 3 data packets, configure the Eth-Trunk interface to work in Layer 3 mode. In this case, you can configure the IP address, MAC address, and MTU for the Eth-Trunk interface.
   * Physical interfaces can be added to an Eth-Trunk in either Layer 2 or Layer 3 mode.
4. Configure a link aggregation mode.
   
   
   ```
   [mode](cmdqueryname=mode) { manual load-balance | lacp-static | lacp-dynamic }
   ```
   
   By default, the link aggregation mode is **manual load-balance**.
   
   **manual load-balance** indicates that an Eth-Trunk interface works in manual mode. In this mode, traffic is balanced over all links. **lacp-static** indicates that an Eth-Trunk interface works in static LACP mode. **lacp-dynamic** indicates that an Eth-Trunk interface works in dynamic LACP mode.
5. (Optional) Disable the function to keep the selection status of interfaces stable for an Eth-Trunk interface in static LACP mode.
   
   
   ```
   [lacp stable-preferred disable](cmdqueryname=lacp+stable-preferred+disable)
   ```
   
   By default, the function to keep the selection status of interfaces stable is enabled for an Eth-Trunk interface in static LACP mode.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This function takes effect only on an Eth-Trunk interface in static LACP mode.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```