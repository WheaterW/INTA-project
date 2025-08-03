Configuring Parameters for Eth-Trunk Member Interfaces
======================================================

To ensure reliable communication between Eth-Trunk interfaces, configure proper parameters for Eth-Trunk member interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The Eth-Trunk member interface view is displayed.
3. Run [**distribute-weight**](cmdqueryname=distribute-weight) *weight-value*
   
   
   
   A load-balancing weight is configured for the Eth-Trunk member interface.
   
   
   
   The number of member interfaces of an Eth-Trunk interfaces cannot exceed the maximum number of member interfaces allowed.
   
   An Eth-Trunk interface performs load balancing based on the weights of its member interfaces. The greater the weight of an Eth-Trunk member interface, the heavier the load carried by the member interface.
4. Run [**lacp priority**](cmdqueryname=lacp+priority) *priority*
   
   
   
   The LACP priority is configured for the member interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The LACP priority indicates the preference of an interface to become active. The smaller the value, the higher the priority.
5. (Optional) Run [**lacp force-up**](cmdqueryname=lacp+force-up)
   
   
   
   The Eth-Trunk member interface is configured to stay in the force-up state.
   
   
   
   After this [**lacp force-up**](cmdqueryname=lacp+force-up) command is run, the force-up state takes effect only when all the member interfaces of the Eth-Trunk interface in static LACP mode time out in receipt of LACPDUs.
   
   When all the Eth-Trunk member interfaces' force-up state takes effect, the minimum number of active member links configured using the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command still takes effect, but the maximum number of active member links configured using the [**max active-linknumber**](cmdqueryname=max+active-linknumber) *link-number* command stops taking effect.
6. (Optional) Run [**lacp port-role**](cmdqueryname=lacp+port-role) { **master** | **slave** | **none** }
   
   
   
   By default, the role is set to **none** for the member interfaces of an Eth-Trunk interface in static LACP mode, indicating that no role is set.
   
   If not all interfaces to be added to an Eth-Trunk interface in static LACP mode reside on the same traffic manager (TM) but you want those on the same TM to negotiate first, run the [**lacp backup-mode enable**](cmdqueryname=lacp+backup-mode+enable) command in the Eth-Trunk interface view to enable the Eth-Trunk interface to work in static LACP master/backup negotiation mode and then perform this step to set the master role for each interface on the same TM.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.