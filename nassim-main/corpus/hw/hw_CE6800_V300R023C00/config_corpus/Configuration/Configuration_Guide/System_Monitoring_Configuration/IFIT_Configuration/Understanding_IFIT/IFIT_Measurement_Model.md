IFIT Measurement Model
======================

The IFIT measurement model is a general model used to directly measure the packet loss rate and delay of user service flows. From the perspective of measurement, a service flow is the target object of measurement. The purpose of measurement is to obtain the packet loss rate and delay data generated when the service flow passes through the transport network. That is, the measurement data on the ingress and egress of the transport network is summarized to obtain the performance indicators to be measured. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001564125281__fig16850152217156), the IFIT measurement model consists of four parts: measurement flow, transport network, measurement point, and measurement system.

**Figure 1** IFIT measurement model  
![](figure/en-us_image_0000001678979925.png)
#### Measurement Flow

A measurement flow is the key element in IFIT measurement, and must be specified before each measurement. You can bind ACL rules to IFIT traffic classifiers to define characteristics of measurement flows. Measurement flows are classified into static and dynamic flows, depending on the generation mode.

* Static flows that match ACL rules are analyzed based on flow IDs.
* Dynamic flows are analyzed based on aggregation source or destination port numbers to flexibly monitor service quality in real time.

#### Transport Network

The transport network transmits measurement flows, but does not generate or terminate them. Each node on the transport network must be reachable to each other. The transport network can carry different types of services over different tunnels. Currently, native IPv4/IPv6 networks and only VXLAN tunnels are supported, but GENEVE packets can be analyzed. For details, see [IFIT Application Scenarios](galaxy_ifit_cfg_ce_0007.html).


#### Measurement Point

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001564125281__fig16850152217156), IFIT measurement points are classified into ingress, transit, and egress based on the packet forwarding direction. Measurement points are defined as follows:

* Ingress: indicates the ingress measurement point of a measurement flow. On this measurement point, IFIT identifies service packets based on the packet characteristics, counts the service packets, adds IFIT packet headers to the packets, and sends the measurement result to the analyzer.
* Transit: indicates a transit measurement point of a measurement flow. On this measurement point, IFIT identifies the packets inserted with IFIT packet headers, counts the packets by flow ID, and sends the measurement result to the analyzer.
* Egress: indicates the egress measurement point of a measurement flow. On this measurement point, IFIT identifies the packets inserted with IFIT packet headers, counts the packets by flow ID, removes the IFIT packet headers when the packets leave the device, and sends the measurement result to the analyzer.

#### Measurement System

The measurement system consists of the ingress node (configured with IFIT) and multiple IFIT-enabled devices. IFIT supports the following two measurement indicators:

* Packet loss measurement: The number of lost packets is the difference between the number of packets entering a transport network and the number of packets leaving the transport network within a measurement interval.
* Delay measurement: The delay is the difference between the time a service flow enters the network and the time the service flow leaves the network within a measurement interval.

For details about the measurement indicators, see [IFIT Measurement Indicators](galaxy_ifit_cfg_ce_0006.html). The measurement results are sent to the NMS through telemetry for visualized display.