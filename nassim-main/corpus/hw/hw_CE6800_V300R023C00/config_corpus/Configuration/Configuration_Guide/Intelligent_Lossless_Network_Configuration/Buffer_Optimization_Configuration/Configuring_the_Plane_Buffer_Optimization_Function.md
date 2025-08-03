Configuring the Plane Buffer Optimization Function
==================================================

Configuring the Plane Buffer Optimization Function

#### Context

Plane buffer optimization can intelligently allocate buffer spaces for different planes based on the service mode of the live network, reducing the buffer space of the plane where interfaces with low usage reside and ensuring that the interfaces where lossless queues reside can obtain sufficient buffer space. Currently, the plane buffer optimization function supports only the long-distance mode. This function can be configured when lossless services on the live network have a long communication distance, for example, storage services deployed across multiple data centers.

![](public_sys-resources/note_3.0-en-us.png) 

Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM support the plane buffer optimization function.



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
3. Configure the plane buffer optimization mode and enable the plane buffer optimization function. (Only the CE6860-SAN and CE8850-SAN support the **enhanced-long-distance** parameter.)
   
   
   ```
   [buffer optimization mode](cmdqueryname=buffer+optimization+mode) { long-distance | enhanced-long-distance }
   ```
   
   By default, the plane buffer optimization function is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The plane buffer optimization function and the burst traffic buffering mode are mutually exclusive.
   * The new plane buffer optimization mode setting takes effect after the device restarts.
   * The plane buffer optimization function takes effect only for lossless services. You can run the [**display buffer optimization configuration**](cmdqueryname=display+buffer+optimization+configuration) command to view the interfaces that support both PFC and the plane buffer optimization function in long-distance mode.
   * For the CE6860-SAN and CE8850-SAN, after the enhanced long-distance mode is configured, you can run the [**display buffer optimization configuration**](cmdqueryname=display+buffer+optimization+configuration) command to check the interfaces that support antilocking PFC.
4. Exit the AI service view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```