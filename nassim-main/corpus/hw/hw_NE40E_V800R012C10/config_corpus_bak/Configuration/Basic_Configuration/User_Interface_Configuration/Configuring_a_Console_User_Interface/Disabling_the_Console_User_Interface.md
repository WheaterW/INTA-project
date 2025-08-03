Disabling the Console User Interface
====================================

The console user interface can be disabled if it is abnormal or needs to be paused due to some reasons.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface**](cmdqueryname=user-interface){ *ui-type* | **console***first-ui-number* }
   
   
   
   The console user interface view is displayed.
3. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The console user interface is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.