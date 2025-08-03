Enabling CU-106 on an Interface
===============================

After enabling CU-106 in the system view, you need to enable CU-106 in the interface view.

#### Context

Perform the following steps on the T-BC and T-TC:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ptp enable**](cmdqueryname=ptp+enable)
   
   
   
   PTP is enabled on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.