Configuring an eMDI Detection Rate
==================================

This section describes how to configure detection only on the rate of video streams when two pieces of video traffic are detected on a node.

#### Context

On the NG MVPN network, if the transit and bud nodes overlap, two pieces of traffic will be detected on the same node, causing offset in the detection results of the packet loss rate, packet out-of-order rate, and jitter. To avoid detection offset when the transit and bud nodes overlap and ensure the accuracy of detection results, enable eMDI detection only on the rate of video streams that pass through the node instead of the packet loss rate, packet out-of-order rate, and jitter.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi monitor-rate-only**](cmdqueryname=emdi+monitor-rate-only)
   
   
   
   eMDI detection only on the rate of video streams is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.