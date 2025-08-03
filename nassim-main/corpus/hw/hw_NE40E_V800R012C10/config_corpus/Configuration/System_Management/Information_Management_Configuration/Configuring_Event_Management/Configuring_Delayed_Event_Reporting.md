Configuring Delayed Event Reporting
===================================

To control the event reporting frequency, you can enable delayed event reporting by specifying a delay.

#### Context

If an event is repeatedly reported, you can enable delayed event reporting to prevent a large number of invalid events from being reported to the NMS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**event**](cmdqueryname=event)
   
   
   
   The event view is displayed.
3. Run [**delay-suppression enable**](cmdqueryname=delay-suppression+enable)
   
   
   
   Delayed event reporting is enabled.
4. Run [**suppression event-name**](cmdqueryname=suppression+event-name) *event-name* **period** *seconds*
   
   
   
   A delay after which a generated event is reported is configured.