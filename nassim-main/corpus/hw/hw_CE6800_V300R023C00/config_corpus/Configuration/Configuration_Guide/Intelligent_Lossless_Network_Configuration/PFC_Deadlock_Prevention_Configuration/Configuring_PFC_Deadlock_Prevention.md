Configuring PFC Deadlock Prevention
===================================

Configuring PFC Deadlock Prevention

#### Context

PFC deadlock prevention preemptively avoids PFC deadlocks for Clos networks. The PFC-enabled device identifies a service flow (hook-shaped flow) that may cause a PFC deadlock, and modifies the queue priority of the hook-shaped flow to prevent a PFC deadlock.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a PFC uplink interface group and enter the PFC uplink interface group view.
   
   
   ```
   [dcb pfc uplink group](cmdqueryname=dcb+pfc+uplink+group) groupname
   ```
   
   By default, no PFC uplink interface group exists in the system.
3. Add interfaces to the PFC uplink interface group.
   
   
   ```
   [group-member interface](cmdqueryname=group-member+interface) { interface-name | interface-type interface-number } [ to { interface-name | interface-type interface-number } ] &<1-32>
   ```
   
   By default, no interface is added to a PFC uplink interface group.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Only physical interfaces can be added to a PFC uplink interface group.
   * A maximum of one PFC uplink interface group can be created. If two PFC uplink interface groups exist before the upgrade, the two PFC uplink interface groups still take effect after the upgrade.
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
   
   * The PFC deadlock prevention function takes effect only when the physical interfaces added to the PFC uplink interface group have no logical interface configuration or when they are main interfaces or member interfaces of an Eth-Trunk. Logical interfaces such as sub-interfaces, VLANIF interfaces, and VBDIF interfaces cannot be configured on such physical interfaces.
   * If you add a physical interface that has been added to an Eth-Trunk to a PFC uplink interface group, PFC deadlock prevention takes effect on the Eth-Trunk.
   
   For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
   
   PFC deadlock prevention takes effect on physical interfaces.
4. Adjust the queue priority and DSCP value of packets in a hook-shaped flow matching a PFC uplink interface group.
   
   
   ```
   [adjust](cmdqueryname=adjust) original-dscp original-dscpvalue to priority prioritynumber dscp dscpvalue
   ```
   
   By default, there is no configuration for a hook-shaped flow matching a PFC uplink interface group.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can adjust the DSCP value of packets in a hook-shaped flow by referring to the table that lists the mappings of IP packet DSCP values to internal priorities or drop priorities in the inbound direction in [Default Settings for Priority Mapping](galaxy_qos_priority_mapping_cfg_0005.html). This ensures that the packets are still forwarded through the specified queue on the downstream device.
   * The [**adjust**](cmdqueryname=adjust) command can be configured at most twice in a PFC uplink interface group, and the settings of the *original-dscpvalue*, *prioritynumber*, and *dscpvalue* parameters must be different in the two command configurations. If the configuration needs to be modified, run the [**undo adjust**](cmdqueryname=undo+adjust) **original-dscp** *original-dscpvalue* **to** **priority** *prioritynumber* **dscp** *dscpvalue* command to delete the original configuration first.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```