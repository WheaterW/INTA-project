Configuring Congestion Monitoring
=================================

Configuring Congestion Monitoring

#### Context

On an enterprise network, congestion mainly affects network performance, leading to transmission delay and signal loss. Performing congestion monitoring on each interface queue on a network device helps you to learn the buffer usage of queues. It also provides information about packets that cause congestion, guiding planning and adjusting network traffic.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
3. Enable queue-based congestion monitoring.
   
   
   ```
   [qos](cmdqueryname=qos) [ queue queue-index ] buffer-monitoring enable
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When queue-based congestion monitoring is enabled, the lower buffer threshold is 10% of the queue buffer space and the upper buffer threshold is 90% of the queue buffer space by default.
4. (Optional) Configure the upper and lower buffer thresholds.
   
   
   ```
   [qos](cmdqueryname=qos) [ queue queue-index ] buffer-monitoring percent low low-percent high high-percent
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display qos buffer-monitoring result**](cmdqueryname=display+qos+buffer-monitoring+result) **interface** { *interface-type* *interface-number* | *interface-name* } command to check the real-time buffer usage of queues.
* Run the [**display qos buffer-monitoring result history**](cmdqueryname=display+qos+buffer-monitoring+result+history) **interface** { *interface-type* *interface-number* | *interface-name* } [ **queue** *queue-index* ] [ **record-number** *record-number* ] command to check historical congestion monitoring information about queues.