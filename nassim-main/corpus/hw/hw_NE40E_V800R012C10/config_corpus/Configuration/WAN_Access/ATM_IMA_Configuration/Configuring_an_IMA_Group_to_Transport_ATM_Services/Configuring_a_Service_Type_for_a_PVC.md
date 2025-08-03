Configuring a Service Type for a PVC
====================================

To implement ATM traffic shaping, configure a service type for a PVC.

#### Context

To prevent the impact of heavy burst ATM traffic and ensure efficient use of network resources, you can configure a service type for a PVC to implement ATM traffic shaping. Doing so can limit the outgoing traffic on an ATM network within a proper range. To configure a service type for a PVC, you must create a service type in the system view and apply the service type to the PVC.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **[**atm service**](cmdqueryname=atm+service)** **svcName** { { ****cbr**** **pcr** **cdvt** } | { { **nrt-vbr** | **rt-vbr** } *pcr* *scr* *mbs* *cdvt* } | { **ubr** *pcr* [ *cdvt* ] } | { **ubr-plus** *pcr* *mcr* *cdvt* } }
   
   
   
   A service type is created and its value is set.
3. Run [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number*[.*subinterface* ]
   
   
   
   The IMA group interface (sub-interface) view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the view of the IMA group interface or sub-interface is displayed, you can perform the following operations:
   
   * Run the [**atm-link check**](cmdqueryname=atm-link+check) command to enable OAM on an IMA group sub-interface. If the PVC/PVP status of the IMA group sub-interface goes Down, the protocol status of the sub-interface also goes Down.
   * Run the [**pvc max-number**](cmdqueryname=pvc+max-number) command to set the maximum number of PVCs on an IMA group interface. If the number of PVC on the IMA group interface reaches the upper limit, no PVC can be created.
4. Run [**pvc**](cmdqueryname=pvc) [ *pvc-name* ] *vpi/vci*
   
   
   
   A PVC is created, and the ATM-PVC view is displayed.
5. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the PVC.
6. Run [**service**](cmdqueryname=service) { **output** | **input** } *service-name*
   
   
   
   A specified service type is applied to the PVC.