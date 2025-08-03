A VLANIF Interface Goes Down
============================

A VLANIF Interface Goes Down

#### Fault Symptom

The [**display interface vlanif**](cmdqueryname=display+interface+vlanif) [ *vlan-id* ] command output shows that the VLANIF interface of the specified VLAN goes down.

#### Possible Causes

* No interface is added to the VLAN.
* The physical status of all interfaces added to the VLAN is down.
* The VLANIF interface does not have an IP address configured.
* The VLANIF interface is shut down.


#### Procedure

* Check whether any interface is added to the target VLAN.
  1. Check detailed information about the VLAN.
     
     
     ```
     [display vlan](cmdqueryname=display+vlan) vlan-id [ verbose | to vlan-id2 ]
     ```
     
     
     
     The [**port trunk pvid vlan**](cmdqueryname=port+trunk+pvid+vlan)*vlan-id* command only configures the PVID for a trunk interface but does not add this interface to the target VLAN. The [**port hybrid pvid vlan**](cmdqueryname=port+hybrid+pvid+vlan)*vlan-id* command only configures the PVID for a hybrid interface but does not add this interface to the target VLAN.
  2. Add interfaces to the target VLAN if no interface is added to the VLAN. For details, see [Add interfaces to VLANs](vrp_vlan_cfg_0018.html#EN-US_TASK_0000001130622850__cmd159334395817).
* Check whether the physical status of all interfaces added to the VLAN is down.
  
  
  
  If so, check why all interfaces added to the VLAN are down. The VLANIF interface goes up when at least one interface in the VLAN is up.
* Check whether the VLANIF interface has an IP address configured.
  1. Check the IP address of the VLANIF interface.
     
     
     ```
     [display interface vlanif](cmdqueryname=display+interface+vlanif) [ vlan-id ]
     ```
  2. Configure an IP address for the VLANIF interface if the VLANIF interface has no IP address configured.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     [interface](cmdqueryname=interface) vlanif vlan-id
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     [commit](cmdqueryname=commit)
     ```
* Check whether the VLANIF interface is shut down.
  1. Check the status of the VLANIF interface.
     
     
     ```
     [display interface vlanif](cmdqueryname=display+interface+vlanif) [ vlan-id ]
     ```
  2. Enable the VLANIF interface if it is shut down.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     [interface](cmdqueryname=interface) vlanif vlan-id
     [undo shutdown](cmdqueryname=undo+shutdown)
     [commit](cmdqueryname=commit)
     ```