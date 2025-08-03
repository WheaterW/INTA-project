Enabling Packet Loss Visualization
==================================

Enabling Packet Loss Visualization

#### Context

After packet loss visualization is enabled, if a device discards packets due to reasons such as abnormal forwarding, specified packet discarding rules, a full buffer, or ACL rule deny actions, the device reports related flow entries to the collector.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the packet monitoring view.
   
   
   ```
   [packet event monitor](cmdqueryname=packet+event+monitor)
   ```
3. (Optional) Enable the NVMe packet parsing function. (Only the following models support this function: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.)
   
   
   ```
   [nvme enable](cmdqueryname=nvme+enable)
   ```
4. Enable the packet loss visualization function.
   1. Enter the packet loss visualization view.
      
      
      ```
      [capture drop-event](cmdqueryname=capture+drop-event)
      ```
   2. Enable the packet loss visualization function for the packets that are discarded due to:
      
      
      * a forwarding exception.
        ```
        [capture drop-packet forward-exception enable](cmdqueryname=capture+drop-packet+forward-exception+enable)
        ```
        
        By default, the packet loss visualization function for the packets that are discarded due to a forwarding exception is disabled.
      * specified packet discarding rules.
        ```
        [capture drop-packet forward-normal enable](cmdqueryname=capture+drop-packet+forward-normal+enable)
        ```
        
        By default, the packet loss visualization function for the packets that are discarded due to specified packet discarding rules is disabled.
      * a full buffer.
        ```
        [capture drop-packet buffer-overflow enable](cmdqueryname=capture+drop-packet+buffer-overflow+enable)
        ```
        
        By default, the packet loss visualization function for the packets that are discarded due to a full buffer is disabled.
      * ACL rule deny actions. (This command is supported only by the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.)
        ```
        [capture drop-packet acl-deny enable](cmdqueryname=capture+drop-packet+acl-deny+enable)
        ```
        
        By default, the packet loss visualization function for the packets that are discarded due to the ACL rule deny actions is disabled.![](public_sys-resources/note_3.0-en-us.png) 
      
      For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ: When the packet loss visualization function for the packets that are discarded due to a forwarding exception is enabled, the packet loss visualization function for the packets that are discarded due to the ACL rule deny actions also takes effect.
   3. Exit the packet loss visualization view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
5. Exit the packet monitoring view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```