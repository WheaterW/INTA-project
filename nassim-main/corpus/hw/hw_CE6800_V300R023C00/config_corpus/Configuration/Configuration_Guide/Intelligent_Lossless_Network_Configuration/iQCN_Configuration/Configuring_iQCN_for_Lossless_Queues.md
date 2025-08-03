Configuring iQCN for Lossless Queues
====================================

Configuring iQCN for Lossless Queues

#### Prerequisites

Before configuring iQCN for lossless queues, you have completed the following task:

* [Configure the PFC function.](galaxy_pfc_cfg_0001.html) A queue corresponding to the internal priority of a PFC-enabled device is a lossless queue.

#### Context

An iQCN-enabled forwarding device detects whether congestion occurs on the network. When detecting congestion, the forwarding device compares the interval at which CNPs are received with the interval between rate increase events of the sender's NIC. If the interval at which CNPs are received is longer, the forwarding device proactively sends CNPs to the sender's NIC to ensure that the NIC can reduce the packet sending rate in a timely manner.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enter the iQCN view and enable iQCN.
   
   
   ```
   [iqcn](cmdqueryname=iqcn)
   ```
   
   By default, iQCN is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   NPCC and iQCN cannot be enabled at the same time in the AI service view.
4. Specify a lossless queue for which the iQCN function is enabled.
   
   
   ```
   [assign queue](cmdqueryname=assign+queue) queue-id
   ```
   
   By default, no lossless queue is specified for enabling the iQCN function.
5. Enable the iQCN function globally.
   
   
   ```
   [iqcn enable](cmdqueryname=iqcn+enable)
   ```
   
   By default, the iQCN function is disabled globally.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When the iQCN function is disabled globally, you can modify settings of the parameters related to the function, but the function does not take effect. When the iQCN function is enabled globally again, the function takes effect based on the current parameter settings.
6. Set the interval between rate increase events of the NIC on a forwarding device.
   
   
   ```
   [rpg-time-reset](cmdqueryname=rpg-time-reset) timer
   ```
   
   By default, the interval between rate increase events of the NIC configured on a forwarding device is 300 µs.
7. Exit the iQCN view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Exit the AI service view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
10. Enable the iQCN function on the interface.
    
    
    ```
    [iqcn enable](cmdqueryname=iqcn+enable)
    ```
    
    By default, the iQCN function is disabled on an interface.
11. Exit the interface view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```