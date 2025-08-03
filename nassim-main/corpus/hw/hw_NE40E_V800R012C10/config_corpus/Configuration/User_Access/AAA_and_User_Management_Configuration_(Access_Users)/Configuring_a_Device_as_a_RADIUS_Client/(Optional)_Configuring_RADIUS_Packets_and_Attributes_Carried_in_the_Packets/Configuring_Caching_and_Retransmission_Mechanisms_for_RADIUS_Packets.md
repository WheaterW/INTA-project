Configuring Caching and Retransmission Mechanisms for RADIUS Packets
====================================================================

Configuring Caching and Retransmission Mechanisms for RADIUS Packets

#### Context

To ensure that factors such as network faults or delay do not prevent the device from receiving response packets sent by the RADIUS server, configure the caching and retransmission mechanisms for request packets to be sent to the RADIUS server. Perform configurations based on site requirements.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
3. Run [**radius-server**](cmdqueryname=radius-server) { **authentication** | **accounting** } **retransmit** *retry-times* **timeout** *second*
   
   
   
   The number of transmissions and the retransmission timeout period are configured for request packets to be sent to the RADIUS server.
   
   
   
   When you run this command:
   
   * If neither the **authentication** nor the **accounting** parameter is specified, the configuration takes effect for all RADIUS authentication and accounting servers in the RADIUS server group.
   * If only the **authentication** parameter is specified, the configuration takes effect for all RADIUS authentication servers in the RADIUS server group.
   * If only the **accounting** parameter is specified, the configuration takes effect for all RADIUS accounting servers in the RADIUS server group.
4. Configure the caching and retransmission of accounting packets as required.
   
   
   
   **Table 1** Configuring the caching and retransmission of accounting packets
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the caching and retransmission of Accounting Start packets. | [**radius-server accounting-start-packet resend**](cmdqueryname=radius-server+accounting-start-packet+resend) [ *resend-times* ] | Run this command to specify the number of retransmissions for Accounting Start packets entering a cache queue. |
   | Configure the caching and retransmission of Accounting Stop packets. | [**radius-server accounting-stop-packet resend**](cmdqueryname=radius-server+accounting-stop-packet+resend) [ *resend-times* ] | Run this command to specify the number of retransmissions for Accounting Stop packets entering a cache queue. |
   | Configure the caching and retransmission of real-time accounting packets. | [**radius-server accounting-interim-packet resend**](cmdqueryname=radius-server+accounting-interim-packet+resend) [ *resend-times* ] | Run this command to enable RADIUS real-time accounting packet caching and to specify the number of retransmissions for real-time accounting packets entering a cache queue. |
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**radius-server accounting cache**](cmdqueryname=radius-server+accounting+cache) *max-packet-number*
   
   
   
   The maximum number of accounting packets that can be cached is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the value specified by *max-packet-number* is not 8192, the system limits the maximum number of accounting packets that can be cached based on the specified value but no longer limits the number of users whose accounting packets can be cached.
7. Run [**radius-server accounting cache-warning-threshold**](cmdqueryname=radius-server+accounting+cache-warning-threshold) **upper-limit** *upper-limit* **lower-limit** *lower-limit*
   
   
   
   The accounting packet cache alarm function is enabled, and alarm thresholds for caching accounting packets are configured.
   
   
   
   Accounting packet cache usage = Number of cached accounting packets/Maximum number of accounting packets that can be cached
8. Run [**radius-server accounting cache retransmit**](cmdqueryname=radius-server+accounting+cache+retransmit) *retransmit* **timeout** *timeout*
   
   
   
   The interval for retransmitting cached RADIUS accounting packets and the number of users for each retransmission are configured.
9. Run [**radius-server accounting cache memory-threshold**](cmdqueryname=radius-server+accounting+cache+memory-threshold) *memory-threshold-value*
   
   
   
   A memory usage threshold is configured for the main control board.
10. Run [**radius-server cache keep packet**](cmdqueryname=radius-server+cache+keep+packet)
    
    
    
    The device is configured not to delete cached packets when the number of retransmissions reaches the specified threshold.
11. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the user view.
12. Run [**radius-server cache resend packet**](cmdqueryname=radius-server+cache+resend+packet)
    
    
    
    The function to retransmit cached packets is manually triggered.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.