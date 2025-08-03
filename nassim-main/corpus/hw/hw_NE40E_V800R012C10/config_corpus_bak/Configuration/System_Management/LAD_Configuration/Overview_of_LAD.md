Overview of LAD
===============

Link Automatic Discovery (LAD) allows a device to issue link discovery requests as triggered by the NMS or command lines. After the device receives link discovery replies, the device generates neighbor information and saves it in the local MIB. The NMS can query neighbor information in the MIB and generate the topology of the entire network.

#### Definition

Link Automatic Discovery (LAD) is a Huawei proprietary protocol
that discovers neighbors at the link layer. LAD allows a device to
issue link discovery requests as triggered by the NMS or command lines.
After the device receives link discovery replies, the device generates
neighbor information and saves it in the local MIB. The NMS can then
query neighbor information in the MIB and generate the topology of
the entire network.


#### Purpose

Large-scale networks demand increased NMS capabilities, such as
obtaining the topology status of connected devices automatically and
detecting configuration conflicts between devices. Currently, most
NMSs use an automated discovery function to trace changes in the network
topology but can only analyze the network-layer topology. Network-layer
topology information notifies you of basic events like the addition
or deletion of devices, but gives you no information about the interfaces
used by one device to connect to other devices or the location or
network operation mode of a device.

LAD is developed to resolve
these problems. LAD can identify the interfaces on a network device
and provide detailed information about connections between devices.
LAD can also display paths between clients, switches, routers, application
servers, and network servers. The detailed information provided by
LAD can help efficiently locate network faults.


#### Benefits

LAD helps network administrators promptly obtain detailed network
topology and changes in the topology and monitor the network status
in real time, improving security and stability for network communication.