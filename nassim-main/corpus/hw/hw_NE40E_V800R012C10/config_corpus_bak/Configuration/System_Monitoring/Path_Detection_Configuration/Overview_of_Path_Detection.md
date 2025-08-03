Overview of Path Detection
==========================

The path detection function restores service traffic paths by constructing detection packets.

#### Definition

Path detection restores the forwarding path of service traffic on a VXLAN network by constructing detection packets.


#### Purpose

With the fast development of network services, networks grow significantly. Understanding the forwarding path of a specific flow or the path between two network devices will help you locate network faults quickly.

Path detection can be used to determine the forwarding path of a specific flow or the path between two network devices. To provide this function, the path detection-capable device must work with the controller. You can configure the path detection function on the device through the CLI or NMS and enable the inbound interface of the device to construct and forward a 5-tuple packet. The devices along the path can identify the packet and obtain the packet information based on the detection flag, and sends the packet information as well as the inbound and outbound interface information to the controller. The controller computes the entire path through which the flow passes based on the information reported by the devices.


#### Benefits

Path detection helps O&M personnel quickly locate the faulty device when traffic is interrupted on the network.