Configuring the MEL Value for an ERPS Ring
==========================================

Configuring the MEL Value for an ERPS Ring

#### Context

On a Layer 2 network running ERPS, if another fault detection protocol is configured, the MEL field in R-APS PDUs can be used to determine whether the R-APS PDUs can be forwarded. If the MEL value configured for an ERPS ring is smaller than the MEL value in packets of the fault detection protocol, the R-APS PDUs cannot be forwarded. Otherwise, the R-APS PDUs can be forwarded. The MEL value can also be used for communication with non-Huawei devices. The same MEL value ensures smooth communication between devices.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created ERPS ring.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Configure the MEL value for the ERPS ring.
   
   
   ```
   [raps-mel](cmdqueryname=raps-mel) level-id  
   ```
   
   
   
   By default, the value of the MEL field in R-APS PDUs is 7.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```