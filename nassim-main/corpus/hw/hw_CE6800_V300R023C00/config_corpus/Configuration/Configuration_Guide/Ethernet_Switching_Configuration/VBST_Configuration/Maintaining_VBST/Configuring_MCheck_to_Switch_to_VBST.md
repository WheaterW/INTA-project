Configuring MCheck to Switch to VBST
====================================

Configuring MCheck to Switch to VBST

#### Context

If a port of a VBST-enabled device is directly connected to an STP-enabled device, the port automatically switches to the STP mode and then sends BPDUs for proper communication between the two devices. However, if the STP-enabled device is powered off or disconnected from the VBST-enabled device, the port cannot automatically switch back to the original VBST mode. As a result, the VBST-enabled device cannot communicate with other VBST-enabled devices. In this case, you can run the [**stp vlan mcheck**](cmdqueryname=stp+vlan+mcheck) command to switch the port from the STP mode to VBST mode.


#### Procedure

* Switch the port from the STP mode to VBST mode in the interface view.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [portswitch](cmdqueryname=portswitch)
  [stp vlan](cmdqueryname=stp+vlan+mcheck) vlan-id mcheck
  ```
* Switch the port from the STP mode to VBST mode in the system view.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [stp vlan](cmdqueryname=stp+vlan+mcheck) vlan-id mcheck
  ```