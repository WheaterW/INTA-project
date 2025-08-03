Configuring MCheck to Switch to RSTP/MSTP
=========================================

Configuring MCheck to Switch to RSTP/MSTP

#### Context

If a port on an RSTP/MSTP-enabled device is connected to an STP-enabled device, the port switches to the STP mode.

If the STP-enabled device is powered off or disconnected from the RSTP/MSTP-enabled device, the port does not automatically switch back to the RSTP/MSTP mode.

In any of the following cases, perform the MCheck operation to switch the port to the RSTP/MSTP mode:

* The STP-enabled device is powered off or disconnected from the RSTP/MSTP-enabled device.
* The STP-enabled device is switched to the RSTP mode.
* The STP-enabled device is switched to the MSTP mode.

#### Procedure

* Switch the port to the RSTP/MSTP mode in the interface view.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [stp mcheck](cmdqueryname=stp+mcheck)
  ```
* Switch the port to the RSTP/MSTP mode in the system view.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [stp mcheck](cmdqueryname=stp+mcheck)
  ```
* Switch the port in an MSTP process to the MSTP mode in the MSTP process view.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [stp process](cmdqueryname=stp+process) process-id
  [stp mcheck](cmdqueryname=stp+mcheck)
  ```