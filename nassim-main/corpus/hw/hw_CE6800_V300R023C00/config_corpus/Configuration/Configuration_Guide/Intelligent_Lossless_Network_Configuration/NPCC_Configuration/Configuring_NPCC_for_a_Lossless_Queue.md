Configuring NPCC for a Lossless Queue
=====================================

Configuring NPCC for a Lossless Queue

#### Prerequisites

Before configuring NPCC for a lossless queue, [configure the PFC function](galaxy_pfc_cfg_0001.html). A queue corresponding to the internal priority for which PFC is enabled is known as a lossless queue.


#### Context

NPCC supports the high-throughput and low-latency modes. In high-throughput mode, the device focuses on improving the throughput of RoCEv2 traffic. In low-latency mode, the device aims to reduce the latency of RoCEv2 traffic. The high-throughput mode is recommended in storage scenarios.


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
3. Enable NPCC and enter the NPCC view.
   
   
   ```
   [npcc](cmdqueryname=npcc)
   ```
   
   By default, NPCC is disabled.
4. Specify a lossless queue for which the NPCC function is enabled.
   
   
   ```
   [assign queue](cmdqueryname=assign+queue) queue-id
   ```
   
   By default, the NPCC function is not enabled on any lossless queue.
5. Set the NPCC function to high-throughput or low-latency mode.
   
   
   ```
   [npcc mode](cmdqueryname=npcc+mode) { high-throughput | low-latency }
   ```
   
   By default, the NPCC function works in high-throughput mode.
6. Exit the NPCC view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Exit the AI service view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
9. Enable the NPCC function on the interface.
   
   
   * On an IPv4 network:
     ```
     [npcc enable](cmdqueryname=npcc+enable)
     ```
   * On an IPv6 network:
     ```
     [ipv6 npcc enable](cmdqueryname=ipv6+npcc+enable)
     ```
   
   By default, the NPCC function is disabled on an interface.
10. Exit the interface view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```