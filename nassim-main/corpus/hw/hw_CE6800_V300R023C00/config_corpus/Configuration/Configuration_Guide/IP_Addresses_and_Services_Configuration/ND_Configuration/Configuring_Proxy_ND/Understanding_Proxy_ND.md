Understanding Proxy ND
======================

ND applies only to communication between hosts that belong to the same physical network and network segment. After receiving an NS message from a host, a device checks whether the destination IPv6 address of the NS message is a local one to determine whether the requested MAC address is a local one. If yes, the device replies with an NA message. If no, the device discards the NS message.

If hosts on different physical networks belong to the same network segment, or hosts on the same physical network belong to the same network segment but cannot communicate at Layer 2, you can configure proxy ND on the device between them to implement communication. After proxy ND is configured, if the device receives an NS message and finds that the destination address of the NS message is not its own address, it uses its own MAC address and the IPv6 address of the destination host to reply to the source host with an NA message.

#### Routed Proxy ND

Hosts that belong to the same network segment but different physical networks are unable to communicate with each other if the gateways connected to them have different IPv6 addresses. In this case, you can enable routed proxy ND on a device's interface connected to the hosts to allow them to communicate.

As shown in [Figure 1](#EN-US_CONCEPT_0000001130622530__fig186751057113612), DeviceA and DeviceB are connected to different networks, and the IPv6 addresses of interfaces 1 and 2 belong to different network segments. Take HostA and HostB as an example. When HostA needs to communicate with HostB, it sends an NS message to request HostB's MAC address because the destination IPv6 address is on the same network segment as the local IPv6 address. However, as HostA and HostB are located on different physical networks, HostB cannot receive the NS message.

**Figure 1** Network diagram of routed proxy ND  
![](figure/en-us_image_0000001176742019.png)

To address the preceding issue, enable routed proxy ND on DeviceA's interface 1 and DeviceB's interface 2. The implementation process is as follows:

1. HostA sends an NS message for the MAC address of HostB.
2. After receiving the NS message, DeviceA checks the destination IPv6 address of the message and finds that this address is not its own IPv6 address. Therefore, DeviceA determines that the message does not request its own MAC address. DeviceA then checks whether there is any route to HostB.
   * If there is no route to HostB, DeviceA discards the NS message.
   * If a route to HostB is available, DeviceA checks whether routed proxy ND is enabled on the interface that receives the message.
     + If routed proxy ND is enabled, DeviceA sends the MAC address of interface 1 to HostA through an NA message.
       
       After receiving the NA message, HostA considers that this message is from HostB. HostA then learns the MAC address of interface 1 from the message and uses this MAC address to send data packets to HostB.
     + If routed proxy ND is not enabled, DeviceA discards the NS message.

#### Proxy ND Anyway

In scenarios where servers are partitioned into VMs, the flexible deployment and migration of VMs on multiple servers or gateways can be achieved by configuring Layer 2 interconnection between multiple gateways. However, this approach may lead to larger Layer 2 domains on the network and the risk of broadcast storms. To resolve this issue, enable proxy ND anyway on a VM gateway. In this way, the gateway sends its interface MAC address to a source VM and communication between VMs is implemented through route forwarding.

As shown in [Figure 2](#EN-US_CONCEPT_0000001130622530__fig12417825103810), the IPv6 addresses of VM1 and VM2 are 2001:db8:300:400::1/64 and 2001:db8:300:400::2/64, respectively. VM1 and VM2 are located on the same network segment. DeviceA and DeviceB are connected to VM1 and VM2, respectively. The interconnection interfaces (interface 1) have the same IPv6 and MAC addresses. When VM1 needs to communicate with VM2, it sends an NS message to request VM2's MAC address because the destination IPv6 address is on the same network segment as the local IPv6 address. However, as VM1 and VM2 are located on different physical networks, VM2 cannot receive the NS message and therefore does not respond.

**Figure 2** Typical network diagram of proxy ND anyway  
![](figure/en-us_image_0000001176742009.png)

To address the preceding issue, enable proxy ND anyway on interface 1 of DeviceA and DeviceB. The implementation process is as follows:

1. VM1 sends an NS message for the MAC address of VM2.
2. After receiving the NS message, DeviceA checks the destination IPv6 address of the message and finds that this address is not its own IPv6 address. Therefore, DeviceA determines that the message does not request its own MAC address. DeviceA then checks whether proxy ND anyway is enabled on the interface that receives the message.
   * If proxy ND anyway is enabled, DeviceA sends the MAC address of interface 1 to VM1 through an NA message.
     
     After receiving the NA message, VM1 considers that this message is from VM2. VM1 then learns the MAC address of interface 1 from the message and uses this MAC address to send data packets to VM2.
   * If proxy ND anyway is not enabled, DeviceA discards the NS message.


#### Intra-VLAN Proxy ND

Hosts that belong to the same VLAN are unable to communicate with each other if Layer 2 interface isolation is configured in the VLAN. In this case, you can enable intra-VLAN proxy ND on a device's interface associated with the VLAN to allow the hosts to communicate.

As shown in [Figure 3](#EN-US_CONCEPT_0000001130622530__fig134781934203714), HostA and HostB are connected to Device, whose interfaces connected to HostA and HostB belong to the same VLAN. HostA and HostB cannot communicate at Layer 2 because intra-VLAN Layer 2 interface isolation is configured on Device.

**Figure 3** Network diagram of intra-VLAN proxy ND  
![](figure/en-us_image_0000001130622564.png)

To address the preceding issue, enable intra-VLAN proxy ND on Device's interface 1. The implementation process is as follows:

1. HostA sends an NS message for the MAC address of HostB.
2. After receiving the NS message, Device checks the destination IPv6 address of the message and finds that this address is not its own IPv6 address. Therefore, Device determines that the message does not request its own MAC address. Device then checks whether there is any ND entry for HostB.
   * If there is an ND entry for HostB and VLAN information in this entry is the same as that in the interface that receives the message, Device checks whether intra-VLAN proxy ND is enabled on interface 1.
     + If intra-VLAN proxy ND is enabled on interface 1, Device sends the MAC address of interface 1 to HostA.
       
       After receiving an NA message from Device, HostA considers that this message is from HostB. HostA then learns the MAC address of interface 1 from the message and uses this MAC address to send data packets to HostB.
     + If intra-VLAN proxy ND is not enabled on interface 1, Device discards the NS message.
   * If no ND entry for HostB is available, Device discards the NS message and checks whether intra-VLAN proxy ND is enabled on interface 1.
     + If intra-VLAN proxy ND is enabled, Device multicasts the NS message in VLAN 10. The destination IPv6 address of the NS message is the IPv6 address of HostB. After receiving an NA message from HostB, Device generates an ND entry indicating the mapping between the IPv6 and MAC addresses of HostB.
     + If intra-VLAN proxy ND is not enabled, Device does not perform any operations.

#### Application Scenarios

[Table 1](#EN-US_CONCEPT_0000001130622530__tab_dc_vrp_arp_feature_002901) describes the application scenarios of proxy ND. You can select a proper proxy ND type based on an application scenario.

**Table 1** Application scenarios of proxy ND
| Proxy ND Type | Application Scenario |
| --- | --- |
| Routed proxy ND | Two hosts that need to communicate belong to the same network segment but different physical networks, and the gateways to which they are connected have different IPv6 addresses. |
| Proxy ND anyway | Two VMs that need to communicate belong to the same network segment but different physical networks, and the gateways to which they are connected have the same IPv6 address. |
| Intra-VLAN proxy ND | Two hosts that need to communicate belong to the same network segment and the same VLAN in which user isolation is configured. |
| Inter-VLAN proxy ND | Two hosts that need to communicate belong to the same network segment but different VLANs. |