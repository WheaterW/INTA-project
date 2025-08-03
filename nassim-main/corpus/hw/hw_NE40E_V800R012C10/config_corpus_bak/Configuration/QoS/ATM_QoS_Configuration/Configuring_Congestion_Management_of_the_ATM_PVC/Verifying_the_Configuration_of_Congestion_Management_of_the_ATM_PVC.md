Verifying the Configuration of Congestion Management of the ATM PVC
===================================================================

After congestion management is configured for ATM PVCs,
you can view information about queues and packet statistics on ATM
interfaces.

#### Procedure

* Use the [**display atm pvc-queue**](cmdqueryname=display+atm+pvc-queue) [ **interface** *interface-type* *interface-number* [.*sub-interface* ] [ **pvc** *vpi/vci* ] ] command to check queue scheduling
  information on all PVCs or one PVC on an ATM interface.
* Use the [**display atm pvc-info**](cmdqueryname=display+atm+pvc-info) [ **interface** **atm** *interface-number* [ **pvc** { *pvc-name* [ *vpi*/*vci* ] | *vpi*/*vci* } ] ] command to check information of PVCs on an ATM
  interface.