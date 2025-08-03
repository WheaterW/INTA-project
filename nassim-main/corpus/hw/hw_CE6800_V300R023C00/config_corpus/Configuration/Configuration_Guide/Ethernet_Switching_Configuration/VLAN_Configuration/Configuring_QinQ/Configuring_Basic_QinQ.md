Configuring Basic QinQ
======================

Configuring Basic QinQ

#### Context

After basic QinQ is configured on an interface, packets received by the interface are tagged with the default VLAN ID of the interface.

* Single-tagged packets change into double-tagged packets.
* Untagged packets change into single-tagged packets with the default VLAN tag of the interface.

For example, to separate private and public networks, you can configure basic QinQ on devices. The inner VLAN tag (private VLAN tag) is used on the private network, and outer VLAN tag (public VLAN tag) is used on the public network. In this manner, the packets of the same VLAN can be transparently transmitted between users of different private networks.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VLAN.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
6. Configure the interface type to **dot1q-tunnel**.
   
   
   ```
   [port link-type](cmdqueryname=port+link-type) dot1q-tunnel
   ```
   
   The CE6885-LL (low latency mode) does not support this command.
7. Configure the default VLAN of the interface.
   
   
   ```
   [port default vlan](cmdqueryname=port+default+vlan) vlan-id
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration interface**](cmdqueryname=display+current-configuration+interface) *interface-type* *interface-number* command to check the QinQ configuration of an interface.