(Optional) Configuring the Layer 2 Loop Detection Threshold
===========================================================

If the Layer 2 loop detection threshold is not properly set, Layer 2 loop detection may be unexpectedly enabled or display incorrect loop levels, affecting Layer 2 loop detection results. As a result, some services may be affected.

#### Context

The system calculates the default Layer 2 loop detection threshold based on the packet loss detection and default algorithm. If the Layer 2 loop detection threshold is not properly set, Layer 2 loop detection may not be enabled or be unexpectedly enabled. To resolve this problem, perform the following operations to modify the Layer 2 loop detection threshold:![](../../../../public_sys-resources/notice_3.0-en-us.png) 

It is recommended that you run this command with assistance from Huawei engineers. Before performing the operation, obtain experience values of packet loss statistics on the specified board.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**l2-loop-detect packets-drop-threshold**](cmdqueryname=l2-loop-detect+packets-drop-threshold) *packets-drop-threshold*
   
   
   
   The Layer 2 loop detection threshold is configured.
4. (Optional) Run [**l2-loop-detect loop-level-threshold**](cmdqueryname=l2-loop-detect+loop-level-threshold+main-interface+determined) **main-interface** **determined** *determined-threshold* **suspect** *suspect-threshold* **notification** *notification-threshold*
   
   
   
   The loop level threshold is configured on a detected main interface.
5. (Optional) Run [**l2-loop-detect loop-level-threshold**](cmdqueryname=l2-loop-detect+loop-level-threshold+sub-interface+determined) **sub-interface** **determined** *determined-threshold* **suspect** *suspect-threshold* **notification** *notification-threshold*
   
   
   
   The loop level threshold is configured on a detected sub-interface.
   
   The loop level threshold on a main interface must be greater than that on a sub-interface. If the loop level threshold on a main interface is smaller than that on a sub-interface and a loop occurs on the sub-interface, the system considers that the loop occurs on the main interface, and detection on the sub-interface does not take effect.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.