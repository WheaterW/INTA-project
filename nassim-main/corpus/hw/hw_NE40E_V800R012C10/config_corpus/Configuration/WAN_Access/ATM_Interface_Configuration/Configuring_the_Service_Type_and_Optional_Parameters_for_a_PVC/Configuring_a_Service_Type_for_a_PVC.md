Configuring a Service Type for a PVC
====================================

PVC services are classified as CBR, NRT-VBR, RT-VBR, UBR, or UBR-plus.

#### Context

To configure a service type for a PVC, you must create a service type in the system view and apply the service type to the PVC.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**atm service**](cmdqueryname=atm+service) *service-name* { **cbr** *output-pcr* *cdvt-value* | **nrt-vbr** *output-pcr* *output-scr* *output-mbs* *cdvt-value* | **rt-vbr** *output-pcr* *output-scr* *output-mbs* *cdvt-value* | **ubr** *output-pcr* [ *cdvt-value* ] | **ubr-plus** *output-pcr* *output-mcr* *cdvt-value* }
   
   
   
   A service type template is created, and parameters are configured.
   
   The service type can be configured as CBR, NRT-VBR, UBR, UBR-plus, or RT-VBR.
3. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number* [ *.subinterface* ]
   
   
   
   The ATM interface or sub-interface view is displayed.
4. Run [**atm cell transfer**](cmdqueryname=atm+cell+transfer)
   
   
   
   The ATM cell transport mode is configured.
5. Run [**pvc**](cmdqueryname=pvc) [ *pvc-name* ] *vpi/vci*
   
   
   
   A PVC is created, and the PVC view is displayed.
6. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The PVC is shut down.
7. Run [**service**](cmdqueryname=service) { **output** | **input** } *service-name*
   
   
   
   A service type template is configured for the PVC.
8. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   The PVC is started.