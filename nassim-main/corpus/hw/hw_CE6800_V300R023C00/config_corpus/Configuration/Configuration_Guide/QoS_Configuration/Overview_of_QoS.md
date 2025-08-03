Overview of QoS
===============

Overview of QoS

#### Introduction to QoS

As networks grow in both scope and service diversity, the resulting sharp increase in traffic exacerbates network congestion and increases the forwarding delay, while in some cases even causing packet loss. Any one of these situations will cause services to experience deterioration in quality or even total interruption. To support increasingly diversified services such as gaming, video, and live streaming, it is critical that network congestion be resolved. One answer is to increase network bandwidth, but this comes with increased costs. A better, more cost-effective solution is to use an "assured" policy to manage traffic.

Quality of service (QoS) is able to offer such a solution. It does this by providing end-to-end (E2E) service quality guarantee to meet diversified service requirements. It is important to note that QoS does not increase the network bandwidth. Instead, it improves network resource utilization and allows different types of traffic to compete for network resources based on their priorities, so that voice, video, and important data applications are processed preferentially on network devices. QoS is now widely used on, and vital to, Internet applications.


#### DiffServ

QoS is an overall solution, instead of being merely a single function. When two hosts on a network communicate with each other, traffic between them may traverse a large number of devices. QoS can guarantee E2E service quality only when all devices on the network use a unified QoS service model, of which Differentiated Services (DiffServ) is the most commonly used.

DiffServ classifies packets on a network into multiple classes and provides differentiated processing for each class. In this way, when congestion occurs, classes with a higher priority are given preference. Packets of the same class are aggregated and sent as a whole to ensure the same delay, jitter, and packet loss rate.

In the DiffServ model, a device can flexibly classify packets based on a combination of conditions and re-mark packets with different priorities. The other devices simply need to identify the priorities carried in packets to allocate resources and control traffic.

QoS technologies supported by the device are based on the DiffServ service model. In this chapter, we describe QoS technologies in terms of packet classification methods and QoS service technologies.


#### QoS Packet Classification Methods

DiffServ classifies packets on a network into multiple classes and provides differentiated processing for each class. The device supports behavior aggregate (BA) classification and multi-field (MF) classification.

**MF classification: MQC-based traffic classification**

MF classification refers to the process of classifying packets in a refined manner based on complex rules, such as 5-tuple (source IP address, source port number, protocol number, destination IP address, and destination port number). Using MF classification, the device classifies packets with the same characteristics into the same type, and assigns them the same QoS level. MF classification can be implemented through traffic classifiers in the Modular QoS Command-Line Interface (MQC), which involves three elements: traffic classifier, traffic behavior, and traffic policy.

1. Traffic classifier: Defines matching rules.
2. Traffic behavior: Specifies actions to be taken for packets. Different QoS functions can be implemented based on traffic behaviors. This document provides guidance for configuring MQC-based traffic statistics collection, packet re-marking, and packet filtering.
3. Traffic policy: Binds the configured traffic classifier and traffic behavior into a traffic policy, which is then applied in a specified view.

**BA classification: QoS priority-based classification**

BA classification refers to the process of classifying packets based on simple rules â a certain priority field in packets, to identify traffic with different priorities. Priorities are described as follows:

* External priority
  
  The external priority is also known as the packet priority or QoS priority. QoS information is recorded by using certain fields in packets, such as the 802.1p value of VLAN packets and the Differentiated Services Code Point (DSCP) value of IP packets. A device can process received packets only based on internal priorities to provide differentiated QoS levels for different services. As such, external priorities are mapped to internal priorities after packets enter the device.
* Internal priority
  
  The internal priority is also known as the class of service (CoS), per-hop behavior (PHB), or local priority. Internal priority values are CS7, CS6, EF, AF4, AF3, AF2, AF1, and BE (in descending order of priority), and correspond to queues 7, 6, 5, 4, 3, 2, 1, and 0, respectively. The internal priority determines the queue into which packets are placed. When QoS services are configured for a queue, the same QoS level is configured for all the packets forwarded through that queue.
* Drop priority
  
  The drop priority is also known as a color. It determines the sequence in which packets are dropped when congestion occurs in a queue, without affecting the mapping between internal priorities and queues. The drop priorities defined by Institute of Electrical and Electronics Engineers (IEEE) are green, yellow, and red in ascending order. By default, the device first discards packets with a higher drop priority when congestion occurs in a queue.
  
  Whether packets are discarded first is determined by QoS parameter settings. For example, in a weighted random early detection (WRED) drop profile, if green packets can use a maximum of 50% of the buffer and red packets can use the entire buffer, the device first discards green packets when congestion occurs in a queue.

When processing QoS services, in the inbound direction, the device maps external priorities of packets to internal and drop priorities, while in the outbound direction, it maps internal and drop priorities to external priorities. To centrally schedule packets, you can use the following methods to adjust the mapping between external priorities and internal priorities:

* Packet re-marking: Based on MQC, the re-marking action defined in a traffic behavior is used to set the priority or fields of packets and re-define the external priority of packets.
* Priority mapping: In the DiffServ model, the device defines DiffServ domains to manage and record the mapping between external priorities and internal or drop priorities, which can vary between multiple DiffServ domains. In this way, differentiated QoS services are provided.

**Relationship between MF classification and BA classification**

MF classification can also be used to identify packets with specific QoS priorities, and this is implemented through MQC. In summary, MF classification classifies packets based on MQC traffic classifiers; BA classification classifies packets based on the internal and drop priorities that the external priorities of packets are mapped to, without using MQC traffic classifiers.


#### QoS Service Technologies

After packets are classified, differentiated QoS services can be provided for different types of packets. Here, we describe the following QoS service technologies:

**Traffic policing, traffic shaping, and interface-based rate limiting**

In order to ensure services remain stable even in scenarios where network resources are limited, user traffic rates must be limited. This can be achieved by using traffic policing, traffic shaping, and interface-based rate limiting, which define basic bandwidth (rate limiting) of different services passing through network devices and monitor the rate of services entering network devices (speed testing). When the volume of service traffic exceeds the basic bandwidth (speeding), excess traffic is discarded or buffered (punishment). In this way, traffic is limited and resource utilization is improved, resulting in more stable services for users.

* Traffic policing controls the traffic rate within a bandwidth limit. It does this by discarding excess traffic when the service traffic exceeds the rate limit. This prevents individual services or users from consuming excessive bandwidth resources.
* Traffic shaping adjusts the rate of outgoing traffic to stabilize the rate at which it is transmitted, thereby avoiding unnecessary packet loss and congestion. Unlike traffic policing, which discards packets exceeding the rate limit, traffic shaping buffers such packets and sends them out at an even rate.
* Interface-based rate limiting limits the total rate of packets sent or received on an interface and can be implemented through either traffic policing or traffic shaping.

**Congestion avoidance**

Congestion avoidance is a congestion control mechanism that monitors network resources such as queues and memory buffers, as well as discarding packets when congestion occurs or worsens.

**Congestion management**

Congestion management is a queue-based technology that works by buffering packets in queues upon network congestion occurs. Congestion management schedules the packets based on a scheduling algorithm, ensuring that QoS-demanding services, such as latency-sensitive services, are preferentially scheduled.


#### QoS Service Process

To sum up, traffic classification is the basis of differentiated services. Traffic policing, traffic shaping, interface-based rate limiting, congestion avoidance, and congestion management are techniques for controlling network traffic and resource allocation, and ultimately implementing differentiated services.

[Figure 1](#EN-US_CONCEPT_0000001513029806__dc_s_whp_QoS_000402) shows the QoS service process on network devices.**Figure 1** QoS service process  
![](figure/en-us_image_0000001513149770.png)