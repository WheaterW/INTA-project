Understanding Packet Event
==========================

Understanding Packet Event

#### Packet Loss Visualization

**Figure 1** Network diagram of packet loss visualization  
![](figure/en-us_image_0000001563999441.png)

As shown in [Figure 1](#EN-US_CONCEPT_0000001564119213__fig_dc_cfg_qos_012902), packets sent from Host1 may be discarded by the devices due to the following reasons:

* A forwarding exception: Packets are discarded in abnormal scenarios such as chip entry loss, chip entry delivery error, and packet check error.
* Specified packet discarding rules: For example, port isolation is configured to discard packets between two specified ports; a punishment action such as traffic suppression associated with MAC address flapping is configured; and split horizon is configured on interfaces.
* A full buffer: The buffer of a port or queue is fully occupied, causing the excess packets to be discarded.
* ACL rule deny actions: Packets that match such ACL rules will be discarded.

After packet loss visualization is enabled on a forwarding device, corresponding flow entries will be generated in the device's CPU if packets are discarded on the device. The device periodically reports the flow entries in UDP packets of the NetStream V9 format to the collector. Then the analyzer reads packet loss data from the collector, and analyzes the data to quickly locate the fault.


#### Latency Visualization

**Figure 2** Network diagram of latency visualization  
![](figure/en-us_image_0000001512680014.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001564119213__fig1790941219442), after latency visualization is enabled on a forwarding device, corresponding flow entries will be generated in the device's CPU if the latency of packets sent from Host1 exceeds the threshold on the device. The device periodically reports the flow entries in UDP packets of the NetStream V9 format to the collector. The analyzer then reads data from the collector and analyzes the latency to detect the congested nodes that cause the high latency.