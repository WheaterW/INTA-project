Overview of Traffic Policing and Traffic Shaping
================================================

Traffic policing and traffic shaping are key factors for QoS to ensure service quality and provide basic QoS functions for network stability.

#### Overview of Traffic Policing

Traffic policing controls the rate of incoming packets to ensure that network resources are properly allocated. If the traffic rate of a connection exceeds the specifications on an interface, traffic policing allows the interface to drop excess packets or re-mark the packet priority to maximize network resource usage and protect carriers' profits. An example of this process is restricting the rate of HTTP packets to 50% of the network bandwidth.

Traffic policing implements the QoS requirements defined in the service level agreement (SLA). The SLA contains parameters, such as the committed information rate (CIR), peak information rate (PIR), committed burst size (CBS), and peak burst size (PBS) to monitor and control incoming traffic. The device performs Pass, Drop, or Markdown actions for the traffic exceeding the specified limit. Markdown means that packets are marked with a lower service class or a higher drop precedence so that these packets are preferentially dropped when traffic congestion occurs. This measure ensures that the packets conforming to the SLA can have the services specified in the SLA.

Traffic policing uses committed access rate (CAR) to control traffic. CAR uses token buckets to meter the traffic rate. Then preset actions are implemented based on the metering result. These actions include:

* Pass: forwards the packets conforming to the SLA.
* Discard: drops the packets exceeding the specified limit.
* Re-mark: re-marks the packets whose traffic rate is between the CIR and PIR with a lower priority and allows these packets to be forwarded.


#### Overview of Traffic Shaping

Traffic shaping controls the rate of outgoing packets to allow the traffic rate to match that on the downstream device. When traffic is transmitted from a high-speed link to a low-speed link or a traffic burst occurs, the inbound interface of the low-speed link is prone to severe data loss. To prevent this problem, configure traffic shaping on the outbound interface of the device connecting to the low-speed link, as shown in [Figure 1](feature_0021577570.html#EN-US_CONCEPT_0172356883__fig_qos_feature_03501).

**Figure 1** Data transmission from the high-speed link to the low-speed link  
![](figure/en-us_image_0000001352513185.png)

As shown in [Figure 2](feature_0021577570.html#EN-US_CONCEPT_0172356883__fig_qos_feature_03502), traffic shaping can be configured on the outbound interface of an upstream device to make irregular traffic transmitted at an even rate, preventing traffic congestion on the downstream device.

**Figure 2** Effect of traffic shaping  
![](images/fig_feature_image_0021580435.png)