Telemetry System Architecture and Service Process
=================================================

Telemetry System Architecture and Service Process

#### System Architecture

Telemetry is a closed-loop automatic O&M system that consists of the device side (network devices) and OSS side including the collector, analyzer, and controller, as shown in [Figure 1](#EN-US_CONCEPT_0000001563994449__en-us_concept_0275777954_fig19792175763113).

**Figure 1** Telemetry system architecture  
![](figure/en-us_image_0000001563754589.png)

#### Service Process

Telemetry's OSS and device sides collaborate to complete the telemetry service process shown in [Figure 2](#EN-US_CONCEPT_0000001563994449__en-us_concept_0275777954_fig1647511855510).

1. Configuring a subscription: A subscription can be configured on network devices to subscribe to data sources for data collection.
   
   The device supports the following subscription modes:
   
   * Static subscription: You can run commands to configure subscription data sources to collect data from telemetry-capable devices. Static subscription is often used for coarse-grained data collection.
   * Dynamic subscription: You can run commands to configure the Google Remote Procedure Call (gRPC) service. The collector delivers dynamic configurations through gRPC to telemetry-capable devices in order to collect data.
2. Pushing sampled data: A network device reports sampled data to the collector based on controller configurations. The collector receives and stores the data.
3. Reading data: The analyzer reads the data stored in the collector.
4. Analyzing data: The analyzer analyzes the data and sends the results to the controller for network management and optimization.
5. Adjusting network parameters: The controller delivers network configurations to the network devices that need to be adjusted. After these configurations take effect, the devices report new sampled data to the collector. The telemetry OSS side analyzes whether the network optimization meets expectations. The service process is closed once optimization is complete.

![](public_sys-resources/note_3.0-en-us.png) 

Telemetry mentioned in this document refers to the telemetry OSS side unless otherwise specified.

If the connection between a device and the collector is interrupted, the device reconnects to the collector and resends the data. However, any data sampled while the connection is being re-established is lost.

After an active/standby switchover is performed, or when the system restarts after saving the telemetry service configuration, the device reloads the telemetry service configuration so that the service can run properly. However, the data sampled during the restart or active/standby switchover is lost.


**Figure 2** Telemetry service process  
![](figure/en-us_image_0000001563994489.png)