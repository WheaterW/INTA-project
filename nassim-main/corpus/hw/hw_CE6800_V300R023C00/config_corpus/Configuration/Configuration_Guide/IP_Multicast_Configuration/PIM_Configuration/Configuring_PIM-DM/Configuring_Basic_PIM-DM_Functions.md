Configuring Basic PIM-DM Functions
==================================

Configuring Basic PIM-DM Functions

#### Context

On a PIM-DM network, PIM-DM must be enabled on interfaces for the devices to set up PIM neighbor relationships with neighboring devices to process data from them.

PIM-DM and PIM-SM cannot be both configured in a public network instance. PIM Hello messages do not carry PIM mode information. Therefore, a PIM device cannot determine the PIM mode of its PIM neighbor. If an RPF interface and RPF neighbor run PIM with different modes, they cannot learn PIM routing information from each other. As a result, multicast forwarding entries cannot be correctly created.

![](public_sys-resources/note_3.0-en-us.png) 

To switch between PIM-DM and PIM-SM, you need to run the [**undo multicast routing-enable**](cmdqueryname=undo+multicast+routing-enable) command in the system view to disable multicast routing, run the [**multicast routing-enable**](cmdqueryname=multicast+routing-enable) command to enable multicast routing again, and then configure PIM-DM or PIM-SM.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IP multicast routing in the public network instance.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable PIM-DM.
   
   
   ```
   [pim dm](cmdqueryname=pim+dm)
   ```
   
   
   
   By default, PIM-DM is not enabled on interfaces.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If you run the [**undo pim dm**](cmdqueryname=undo+pim+dm) command, PIM neighbor and protocol status information on the interface will be deleted. If multicast services are running on the interface, the multicast services will be affected in this case.
   
   PIM-DM can only be configured in a public network instance, not in a VPN instance.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display pim**](cmdqueryname=display+pim) **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check PIM neighbor information.
* Run the [**display pim grafts**](cmdqueryname=display+pim+grafts) command to check unacknowledged PIM-DM Graft messages.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **interface** *interface-type interface-number* | **message-type** { **assert** | **hello** | **join-prune** | **graft** | **graft-ack** | **state-refresh** | **bsr** | **discovery** } ] \* command to check the statistics about sent and received PIM control messages.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** *interface-type* *interface-number* | **outgoing-interface** { **include** | **exclude** | **match** } *interface-type* *interface-number* | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] ââââcommand to check PIM routing entries.