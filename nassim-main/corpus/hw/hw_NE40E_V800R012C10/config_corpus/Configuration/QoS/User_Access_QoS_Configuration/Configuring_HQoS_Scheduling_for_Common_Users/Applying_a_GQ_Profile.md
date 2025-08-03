Applying a GQ Profile
=====================

For a user VLAN or a BAS interface through which users go online, you can apply a GQ profile to it in order to schedule traffic based on GQs.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Apply a GQ profile in the user VLAN view to schedule user traffic.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the sub-interface view.
   2. Run the [**user-vlan**](cmdqueryname=user-vlan) { { *start-vlan-id* [ *end-vlan-id* ] [ **qinq** *start-pe-vlan* [ *end-pe-vlan* ] ] } | **any-other** } command to enter the user VLAN view.
   3. Run the [**user-group-queue**](cmdqueryname=user-group-queue) *user-group-queue-name* [ **identifier** *identifier* ] { **inbound** | **outbound** } [ **group** *groupname* ] command to allocate a GQ to users in the user VLAN view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the sub-interface view.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   7. Run the [**interface**](cmdqueryname=interface) **Eth-trunk** *trunk-number* command to enter the Eth-Trunk interface view.
   8. (Optional) Run the [**bas-load-balance exclude user-group-queue outbound**](cmdqueryname=bas-load-balance+exclude+user-group-queue+outbound) command to configure the device not to perform route selection for users' downstream traffic based on GQs.
      
      
      
      If users go online through an Eth-Trunk interface, the device performs route selection for downstream traffic of users in a given GQ based on that GQ by default. This means that downstream traffic of all users in the GQ is forwarded through the same Eth-Trunk member interface. Consequently, traffic load imbalance may occur among Eth-Trunk member interfaces. To load-balance users' downstream traffic among Eth-Trunk member interfaces, run this command.
   9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Apply a GQ profile in the BAS view, and configure the device to schedule users' downstream traffic based on parent GQs.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   3. Run the [**bas**](cmdqueryname=bas) command to enter the BAS view.
   4. Run the **[**user-group-queue**](cmdqueryname=user-group-queue)** **user-group-queue-name** ****outbound**** [ ****group**** **group** ] command to apply a GQ profile in the BAS view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the interface view.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   8. Run the [**interface**](cmdqueryname=interface) **Eth-trunk** *trunk-number* command to enter the Eth-Trunk interface view.
   9. (Optional) Run the [**bas-load-balance exclude sub-port-queue outbound**](cmdqueryname=bas-load-balance+exclude+sub-port-queue+outbound) command to configure the device not to perform route selection for users' downstream traffic based on parent GQs.
      
      
      
      If users go online through an Eth-Trunk interface, the device performs route selection for downstream traffic of users in a given parent GQ based on that GQ by default. This means that downstream traffic of all users in the parent GQ is forwarded through the same Eth-Trunk member interface. Consequently, traffic load imbalance may occur among Eth-Trunk member interfaces. To load-balance users' downstream traffic among Eth-Trunk member interfaces, run this command.
   10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.