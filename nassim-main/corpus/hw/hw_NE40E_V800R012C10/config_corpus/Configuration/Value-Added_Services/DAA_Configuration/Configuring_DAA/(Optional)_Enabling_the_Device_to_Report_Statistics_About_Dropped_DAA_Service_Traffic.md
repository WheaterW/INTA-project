(Optional) Enabling the Device to Report Statistics About Dropped DAA Service Traffic
=====================================================================================

You can enable the device to report statistics about dropped DAA service traffic. This allows you to query information about users with such traffic.

#### Context

To query information about users with dropped DAA service traffic, enable the device to report statistics about dropped DAA service traffic. The information can be used to locate the device that dropped DAA service traffic.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**value-added-service daa report-dropped-flow enable**](cmdqueryname=value-added-service+daa+report-dropped-flow+enable)
   
   
   
   The device is enabled to report statistics about dropped DAA service traffic.

#### Result

After the preceding configurations are complete, run the [**display value-added-service user daa with-dropped-flow**](cmdqueryname=display+value-added-service+user+daa+with-dropped-flow) command to query information about users with dropped DAA service traffic. Then run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) command to query the number of dropped upstream and downstream DAA service packets.