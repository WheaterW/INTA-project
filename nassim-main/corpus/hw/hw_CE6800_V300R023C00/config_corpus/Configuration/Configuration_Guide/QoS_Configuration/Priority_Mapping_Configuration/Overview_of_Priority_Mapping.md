Overview of Priority Mapping
============================

Overview of Priority Mapping

#### Definition

Priority mapping maps external priorities carried in packets into internal priorities on a device, and manages and records the mapping between external and internal priorities using DiffServ domains. In this way, the device provides differentiated services for packets based on internal priorities.

Common concepts of priorities are described as follows:

* External priority
  
  The external priority is also known as the packet priority or QoS priority. QoS information is recorded by using certain fields in packets, such as the 802.1p value of VLAN packets and the Differentiated Services Code Point (DSCP) value of IP packets. A device can process received packets only based on internal priorities to provide differentiated QoS levels for different services. As such, external priorities are mapped to internal priorities after packets enter the device.
* Internal priority
  
  The internal priority is also known as the class of service (CoS), per-hop behavior (PHB), or local priority. Internal priority values are CS7, CS6, EF, AF4, AF3, AF2, AF1, and BE (in descending order of priority), and correspond to queues 7, 6, 5, 4, 3, 2, 1, and 0, respectively. The internal priority determines the queue into which packets are placed. When QoS services are configured for a queue, the same QoS level is configured for all the packets forwarded through that queue.
* Drop priority
  
  The drop priority is also known as a color. It determines the sequence in which packets are dropped when congestion occurs in a queue, without affecting the mapping between internal priorities and queues. The drop priorities defined by Institute of Electrical and Electronics Engineers (IEEE) are green, yellow, and red in ascending order. By default, the device first discards packets with a higher drop priority when congestion occurs in a queue.
  
  Whether packets are discarded first is determined by QoS parameter settings. For example, in a weighted random early detection (WRED) drop profile, if green packets can use a maximum of 50% of the buffer and red packets can use the entire buffer, the device first discards green packets when congestion occurs in a queue.

#### Purpose

Packets transmitted over different networks carry different external priority fields. For example, the 802.1p value is used on a VLAN, and the DSCP value is used on an IP network. The device processes packets transmitted on the network as follows:

* For all incoming packets, the device maps external priorities (including 802.1p and DSCP values) to internal priorities, places the packets into specific queues based on the mapping, and applies traffic shaping, congestion avoidance, or congestion management to the queues.
* For outgoing packets, the device maps the internal priority to an external priority, and other devices can provide QoS services based on the external priority.