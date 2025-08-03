(Optional) Configuring OAM End-to-End Loopback Detection
========================================================

You can configure end-to-end loopback detection to detect link status and report faults in real time without service interruption.

#### Context

Perform either of the following operations on the Router to implement end-to-end loopback detection:

* Run the **ping atm** command in the system view.
* Run the **oam-loopback** command in the ATM OAM view.

When configuring the function of end-to-end loopback detection in the ATM OAM view, note the following:

* The attribute of the OAM connection point of the PVP/PVC must be end-point.
* The CC function and the loopback function cannot be configured on the same PVP/PVC.
* During fault recovery, the [**undo oam-loopback**](cmdqueryname=undo+oam-loopback) command cannot be run.
* Before deleting OAM connections, run the [**undo oam-loopback**](cmdqueryname=undo+oam-loopback) command to disable the function of OAM end-to-end loopback detection if no faults occur on the board.

Perform the following steps on the Router:


#### Procedure

* Implement end-to-end loopback detection in the system view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ping atm**](cmdqueryname=ping+atm) **interface** **atm** *interface-number* *vpi/vci* **end-to-end** [ *times* ]
     
     
     
     End-to-end loopback detection is configured.
* Implement end-to-end loopback detection in the ATM OAM view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [.*subinterface* ]
     
     
     
     The ATM interface view is displayed.
  3. Run [**oam**](cmdqueryname=oam)
     
     
     
     The OAM interface view is displayed.
  4. Run [**attribute**](cmdqueryname=attribute) { *start*-*vpi* [ *end-vpi* ] | *vpi/start-vci* [ *vpi/end-vci* ] } **end-point**
     
     
     
     The OAM attributes of the connection point are configured.
  5. Run [**oam-loopback**](cmdqueryname=oam-loopback) *vpi/start-vci* [ *vpi/end-vci* ] **end-to-end**
     
     
     
     The function of OAM end-to-end loopback detection of the PVP/PVC is enabled.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     Before enabling OAM end-to-end loopback detection on an interface that is transmitting traffic, ensure that the OAM attribute of the connection point is end-point. Otherwise, traffic on the local interface will be interrupted.
  6. (Optional) Run [**oam-loopback**](cmdqueryname=oam-loopback) *vpi/start-vci* [ *vpi/end-vci* ] **up-cycle** *up-cycle-number* **down-cycle** *down-cycle-number*
     
     
     
     The number of delayed intervals for responding after the PVP/PVC status changes is configured.
     
     After the function of OAM end-to-end loopback detection is enabled, to prevent PVP/PVC flapping, the system does not immediately respond when the PVP/PVC status changes. When the PVP/PVC remains Down or Up for specified consecutive intervals, the system responds to the change.