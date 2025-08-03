Enabling Adaptive Routing
=========================

Enabling Adaptive Routing

#### Context

To enable adaptive routing, enable it globally, enable it on an interface, and then configure the role of the interface in the direct topology.

The adaptive routing function can be configured only in the dragonfly topology and takes effect only when other devices in the topology are correctly configured.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable global adaptive routing.
   
   
   ```
   [adaptive-routing enable](cmdqueryname=adaptive-routing+enable)
   ```
   
   By default, global adaptive routing is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The interval between enabling and disabling global adaptive routing must be greater than 300 seconds.
   * The **[**adaptive-routing enable**](cmdqueryname=adaptive-routing+enable)** and **[**load-balance ecmp stateful enable**](cmdqueryname=load-balance+ecmp+stateful+enable)** commands cannot both be run on a device.
   * The **[**adaptive-routing enable**](cmdqueryname=adaptive-routing+enable)** and **[**vxlan-overlay local-preference enable**](cmdqueryname=vxlan-overlay+local-preference+enable)** commands cannot both be run on a device.
   * When global adaptive routing is disabled, adaptive routing is disabled on all interfaces that have the adaptive routing function enabled, and the role configurations on these interfaces are also deleted.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable adaptive routing on the interface and configure the role of the interface in the direct topology.
   
   
   ```
   [adaptive-routing enable dragonfly-role](cmdqueryname=adaptive-routing+enable+dragonfly-role) { global | local }
   ```
   
   
   
   By default, adaptive routing is disabled on an interface, and the role of the interface in the direct topology is not configured.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If adaptive routing is enabled globally on a device, an interface is added to a direct topology and participates in adaptive routing calculation only if the role of the interface is configured in the direct topology.
   * If PFC or antilocking PFC has been enabled on an interface, PFC resources on the interface are occupied. To release PFC resources on the interface, disable PFC or antilocking PFC on the interface and restart the device.
   * This command can be delivered only to physical interfaces. It cannot be delivered to split interfaces or logical interfaces such as sub-interfaces, Eth-Trunk interfaces, VLANIF interfaces, and VBDIF interfaces.
   
   For the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:
   
   * PFC and dragonfly antilocking PFC cannot be both enabled on an interface.
   * Antilocking PFC and dragonfly antilocking PFC cannot be both enabled on an interface.
   * On an interface, dragonfly antilocking PFC for priority queue 1 is mutually exclusive with differentiated flow scheduling for any queue.
   * In a priority queue of an interface, dragonfly antilocking PFC is mutually exclusive with differentiated flow scheduling.
   * Currently, PFC or antilocking PFC can be enabled on a maximum of 127 interfaces. If the accumulated number of interfaces where PFC or antilocking PFC has been enabled has reached 127, disable the delivered configurations to reduce the number of such interfaces and restart the device. Then you can enable PFC or antilocking PFC on more interfaces.
   
   For the CE8855 and CE8851-32CQ4BQ:
   
   If dragonfly deadlock prevention has been enabled, you must enable PFC for the priority queue corresponding to the deadlock prevention function on the interface before running this command to configure the role of the interface in the direct topology.
6. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```