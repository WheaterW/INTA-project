Enabling ATM Simple Traffic Classification
==========================================

ATM simple traffic classification can be enabled only on
ATM sub-interfaces or PVCs/PVPs.

#### Context

Perform the following steps on the Router on which ATM simple traffic classification is required:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform the following steps on the Router as required:
   
   
   * To create an ATM sub-interface and enter the view of the ATM
     sub-interface, run:
     
     ```
     [interface](cmdqueryname=interface) atm atm-number.sub-interface
     ```
   * To create a PVC or PVP and enter the PVC or PVP view, on the
     sub-interface view, run:
     
     ```
     [pvc](cmdqueryname=pvc) [ pvc-name ] vpi/vci
     ```
     
     or
     
     ```
     [pvp](cmdqueryname=pvp) vpi
     ```
3. Run [**trust upstream**](cmdqueryname=trust+upstream) *ds-domain-name* [ **inbound** | **outbound** ]
   
   
   
   The specified
   DS domain is bound to the interface and the simple traffic classification
   is enabled.