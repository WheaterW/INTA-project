Configuring Centralized DS-Lite Providing Backup for Centralized DS-Lite Backup
===============================================================================

Centralized DS-Lite providing backup for centralized DS-Lite improves DS-Lite device reliability.

#### Context

In centralized DS-Lite providing backup for centralized DS-Lite, the master and backup DS-Lite devices are configured and both support centralized DS-Lite function. If a service board on the master DS-Lite device fails, the master DS-Lite device distributes traffic to the backup DS-Lite device for DS-Lite processing. After the service board on the master DS-Lite device recovers, user traffic switches back for DS-Lite switching.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The view in which license resources are assigned is displayed.
3. Run [**active nat session-table size**](cmdqueryname=active+nat+session-table+size) *table-size* [**slot**](cmdqueryname=slot) *slot-id* 
   
   
   
   The session resources are assigned to the specified service board and its CPU.
4. Run [**active ds-lite**](cmdqueryname=active+ds-lite+vsuf+slot) **vsuf slot** *slot-id*
   
   
   
   DS-Lite is enabled on the specified service board.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   A service-location group is created, and its view is displayed.
7. Run 
   
   
   
   A CPU on the service board is bound to the service-location group.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
   
   
   
   A service-instance group is created, and its view is displayed.
10. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
    
    
    
    A service-location group is bound to the service-instance group.
11. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
12. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance+id) *instance-name* **id** *id*
    
    
    
    The DS-Lite instance view is displayed.
13. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
    
    
    
    A service-instance group is bound to the DS-Lite instance.
14. Run [**ds-lite centralized-backup enable**](cmdqueryname=ds-lite+centralized-backup+enable)
    
    
    
    Centralized DS-Lite providing backup for centralized DS-Lite is enabled.
15. (Optional) Run [**ds-lite centralized-backup switch down-number**](cmdqueryname=ds-lite+centralized-backup+switch+down-number) *down-number*
    
    
    
    The maximum number of failed CPUs is set for the function of centralized DS-Lite providing backup for centralized DS-Lite.
16. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.