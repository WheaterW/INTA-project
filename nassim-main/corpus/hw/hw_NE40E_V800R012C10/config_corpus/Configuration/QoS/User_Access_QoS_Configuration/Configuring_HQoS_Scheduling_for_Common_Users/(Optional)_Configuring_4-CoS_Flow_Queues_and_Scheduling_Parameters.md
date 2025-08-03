(Optional) Configuring 4-CoS Flow Queues and Scheduling Parameters
==================================================================

You can configure parameters for a 4-CoS flow queue profile, which reduces the configuration workload required by an 8-CoS flow queue profile.

#### Context

There are 8-CoS (BE/AF1/AF2/AF3/AF4/EF/CS6/CS7) and 4-CoS (cos0/cos1/cos2/cos3) priority modes. The 8-CoS priority mode is used by default. The 4-CoS priority mode allows you to implement rate limiting for eight flow queues by configuring rate limiting only for four flow queues, reducing the configuration workload.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration task is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flow-queue**](cmdqueryname=flow-queue) *flow-queue-name* **4cos-mode**
   
   
   
   The 4-CoS flow queue view is displayed.
3. Run [**queue**](cmdqueryname=queue) *cos-value* { { **pq** | **wfq** **weight** *weight-value* | **lpq** } | **shaping** { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ] | **flow-wred** *wred-name* }\*
   
   
   
   A scheduling policy is configured for a queue of a specific priority.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.