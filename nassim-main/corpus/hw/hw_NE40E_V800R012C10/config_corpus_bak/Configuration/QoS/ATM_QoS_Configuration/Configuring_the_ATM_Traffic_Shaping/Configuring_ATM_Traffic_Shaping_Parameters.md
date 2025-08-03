Configuring ATM Traffic Shaping Parameters
==========================================

You must specify the service type and parameters related to the service type for PVCs or PVPs to limit the volume of outgoing traffic on an ATM network.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**atm service**](cmdqueryname=atm+service) *service-name* { **cbr** *output-pcr* *cdvt-value* | **nrt-vbr** *output-pcr* *output-scr* *output-mbs* *cdvt-value* | **rt-vbr** *output-pcr* *output-scr* *output-mbs* *cdvt-value* | **ubr** *output-pcr* [ *cdvt-value* ] | **ubr-plus** *output-pcr* *output-mcr* *cdvt-value* }
   
   
   
   The PVC or PVP service types and related parameters are configured.
   
   To configure PVC service types, you need to create service types in the system view; then, apply the service types to specific PVCs.