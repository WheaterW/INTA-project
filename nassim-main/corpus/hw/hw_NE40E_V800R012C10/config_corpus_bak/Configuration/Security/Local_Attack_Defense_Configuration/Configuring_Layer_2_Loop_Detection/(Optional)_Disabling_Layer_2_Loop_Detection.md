(Optional) Disabling Layer 2 Loop Detection
===========================================

If you confirm that Layer 2 loops do not occur on a board, you can disable the Layer 2 loop detection function to improve the fault locating efficiency.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If you need to disable Layer 2 loop detection, contact Huawei technical support engineers.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**l2-loop-detect disable**](cmdqueryname=l2-loop-detect+disable)
   
   
   
   Layer 2 loop detection is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.