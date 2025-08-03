Configuring Intelligent Monitoring
==================================

Intelligent monitoring identifies device exceptions and predicts resource trends.

#### Context

A device that works at the aggregation or core layer of a carrier network plays an important role and transmits many services. Exceptions on the device may impact these services. Intelligent exception identification and intelligent log exception detection can quickly perceive and detect exceptions for fault locating. And intelligent resource trend prediction can predict network resource trends for resource allocation.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**eai**](cmdqueryname=eai)
   
   
   
   The EAI view is displayed.
3. Run any of the following commands as required:
   
   
   * To enable intelligent exception identification, run the [**intelligent-anomaly-identify enable**](cmdqueryname=intelligent-anomaly-identify+enable) command.
   * To enable intelligent log exception detection, run the [**intelligent-logrecord-detection enable**](cmdqueryname=intelligent-logrecord-detection+enable) command.
   * To enable intelligent resource trend prediction, run the [**intelligent-resource-prediction enable**](cmdqueryname=intelligent-resource-prediction+enable) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.