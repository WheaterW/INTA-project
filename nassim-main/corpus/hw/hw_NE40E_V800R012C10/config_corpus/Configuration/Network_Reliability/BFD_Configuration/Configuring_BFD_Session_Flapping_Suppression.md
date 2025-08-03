Configuring BFD Session Flapping Suppression
============================================

You can configure BFD session flapping suppression to reduce the number of BFD session flappings.

#### Usage Scenario

If link quality is poor, BFD results in frequent service switchovers. You can configure a link flapping time to prevent frequent service switchovers, protecting link resources and reducing link resource consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD session view is displayed.
3. Run [**dampening timer-interval**](cmdqueryname=dampening+timer-interval) **maximum** *maximum-milliseconds* **initial** *initial-milliseconds* **secondary** *secondary-milliseconds*
   
   
   
   A flapping suppression time is configured for the BFD session.
   
   
   
   It is recommended that the secondary flapping suppression time be greater than the initial flapping suppression time and less than the maximum flapping suppression time.
4. (Optional) Run [**dampening timer-interval**](cmdqueryname=dampening+timer-interval) **bundle-member** **maximum** *bundle-maximum-milliseconds* **initial** *bundle-initial-milliseconds* **secondary** *bundle-secondary-milliseconds*
   
   
   
   A flapping suppression time is configured for the BFD for link-bundle session.
   
   
   
   It is recommended that the secondary flapping suppression time be greater than the initial flapping suppression time and less than the maximum flapping suppression time.
5. (Optional) Run [**dampening timer-interval**](cmdqueryname=dampening+timer-interval) **bundle-member** **l3-only-mode**
   
   
   
   The flapping suppression time is configured to take effect only for the main BFD for link-bundle session.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.