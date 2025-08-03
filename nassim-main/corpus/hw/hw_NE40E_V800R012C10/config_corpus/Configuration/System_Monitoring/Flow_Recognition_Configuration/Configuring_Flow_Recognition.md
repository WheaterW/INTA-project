Configuring Flow Recognition
============================

To allow a device to send the septuple information (source and destination MAC addresses, source and destination IP addresses, source and destination port numbers, and protocol type) of traffic to a controller for flow identification, enable flow recognition.

#### Context

[Figure 1](#EN-US_TASK_0172373417__fig_dc_ne_flow-recognition_cfg_00001) shows the typical networking of flow recognition. Target flows enter the transport network from the multimedia terminal and then reach the device through Interface 1. After flow recognition is enabled on the device, the device collects data and then sends the data to the controller over telemetry.

**Figure 1** Flow recognition networking  
![](figure/en-us_image_0244937411.png)

#### Pre-configuration Tasks

Before configuring flow recognition, complete the following tasks:

* Configure a dynamic routing protocol or static routes so that nodes are reachable at the network layer.
* Configure telemetry subscription to ensure that data is promptly reported to the controller.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**flow-recognition inbound**](cmdqueryname=flow-recognition+inbound)
   
   
   
   Flow recognition is enabled on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.