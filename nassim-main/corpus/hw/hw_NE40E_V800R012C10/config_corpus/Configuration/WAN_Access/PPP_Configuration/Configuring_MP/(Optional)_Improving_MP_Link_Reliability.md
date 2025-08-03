(Optional) Improving MP Link Reliability
========================================

This section describes how to configure flapping damping and the minimum number of Point-to-Point-Protocol (PPP) links allowed for a Multilink Point-to-Point Protocol (MP) link to improve MP link reliability.

#### Context

The flapping status of an MP link reflects the bandwidth stability of the MP link. In a specified monitoring period, if the number of flapping times of an MP member link exceeds the specified maximum number of flapping times, configure flapping damping for MP member links. ![](../../../../public_sys-resources/note_3.0-en-us.png) 

After an MP member link is dampened, the interfaces on the two ends of the member link enter the damping state. The data link layer status of the end interfaces for the member link
is **DOWN (damping)** in the [**display interface mp-group**](cmdqueryname=display+interface+mp-group) command output.


The minimum number of PPP links allowed for an MP link determines the minimum bandwidth of the MP link. To meet bandwidth requirements, you can configure the minimum number of PPP links allowed for an MP link.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface mp-group**](cmdqueryname=interface+mp-group) *number*
   
   
   
   An MP-Group interface is created, and the MP-Group interface view is displayed.
3. Run [**ppp mp damping**](cmdqueryname=ppp+mp+damping) [ **detect-time** *detect-time* **flapping-count** *flapping-count* **damping-time** *damping-time* ]
   
   
   
   Flapping damping is configured for the member links of the MP link.
4. Run [**ppp mp threshold-least**](cmdqueryname=ppp+mp+threshold-least) *number*
   
   
   
   The minimum number of PPP links allowed for the MP link is set.
5. Restart the MP-Group interface.
   1. Run [**shutdown**](cmdqueryname=shutdown)
      
      
      
      The interface is shut down.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
      
      
      
      The interface is restarted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.