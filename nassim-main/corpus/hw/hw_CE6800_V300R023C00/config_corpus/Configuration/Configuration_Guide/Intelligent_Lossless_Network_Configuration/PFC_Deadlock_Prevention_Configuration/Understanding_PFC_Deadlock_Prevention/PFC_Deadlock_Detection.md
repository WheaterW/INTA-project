PFC Deadlock Detection
======================

PFC Deadlock Detection

#### PFC Deadlock

PFC deadlock is a network state that is caused by the following situation: congestion occurs on multiple switches simultaneously due to a loop or some other reason, the interface buffer usage of each switch exceeds the threshold, the switches wait for each other to release resources, and consequently data flows on all switches are permanently blocked.

Under normal circumstances, a PFC-enabled device only pauses traffic in one or several priority queues of an interface, rather than on the entire interface. Each queue can be paused or restarted individually, without affecting traffic in other queues. In this way, PFC enables traffic of various types to share one link. However, when a link or device fails, a temporary loop may occur on the network during route re-convergence, resulting in a cyclic buffer dependency. This then leads to the PFC thresholds being reached on the devices, such as the four switches in [Figure 1](#EN-US_CONCEPT_0000001564128557__en-us_concept_0000001512830090_fig1829710437420), which then send PFC frames to peer devices. In this case, all of the switches in the topology stop sending traffic, resulting in PFC deadlock.

**Figure 1** PFC deadlock  
![](figure/en-us_image_0000001513029706.png)

#### PFC Deadlock Detection Implementation

PFC deadlock detection allows a device to monitor a PFC deadlock through the following processes. Then, if the device continuously receives PFC frames during deadlock detection, the device does not respond.

1. **Deadlock detection**
   
   Once an interface of Device2 receives PFC frames from Device1, the internal scheduler of Device2 stops sending traffic in a specified priority queue, and Device2 starts a timer to detect PFC frames received by the queue according to the configured deadlock detection and precision.
   
   **Figure 2** Enabling deadlock detection  
   ![](figure/en-us_image_0000001563750009.png)
2. **Deadlock determination**
   
   If the queue is in the PFC-XOFF (flow-controlled) state throughout the specified PFC deadlock detection period, the system determines that a PFC deadlock occurs. In this case, the PFC deadlock recovery process needs to be performed.
   
   **Figure 3** Determining deadlock occurrence  
   ![](figure/en-us_image_0000001564109749.png)
3. **Deadlock recovery**
   
   During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending or discards traffic in the specified priority queue. After the recovery period expires, the normal flow control mechanism of PFC resumes. If the system still determines that a deadlock occurs in the next deadlock detection period, the deadlock recovery process starts again.
   
   **Figure 4** Entering the deadlock recovery process  
   ![](figure/en-us_image_0000001563989913.png)
4. **Deadlock control**
   
   If the deadlock recovery process does not work and PFC deadlocks persist, you can configure the system to forcibly enter the deadlock control process after a specified number of deadlocks occur in a period of time. In this case, the system considers that deadlocks occur frequently on the network, posing high risk. In response, the system enters the deadlock control process, and the PFC function is automatically disabled on the device. If you want to re-enable the PFC function, you must do so manually.
   
   **Figure 5** Disabling the PFC function upon frequent deadlocks  
   ![](figure/en-us_image_0000001563750013.png)