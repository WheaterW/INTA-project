Understanding Multicast Static Routes
=====================================

Multicast static routes are an important basis for RPF checks. The following describes their functions in different application scenarios.

#### Changing RPF Routes

Multicast static routes can be configured on a network to change RPF routes. With this configuration, transmission paths different from unicast routing paths can be created for multicast data.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130782770__fig_dc_fd_mrm_000601), the RPF neighbor of DeviceC to the multicast source is DeviceA. Multicast packets sent from the source are transmitted along the path Source -> DeviceA -> DeviceC. After a multicast static route that specifies DeviceB as the RPF neighbor of DeviceC is configured on DeviceC, the transmission path of the multicast packets sent from the source is changed to Source -> DeviceA -> DeviceB -> DeviceC, which is different from the original unicast routing path.**Figure 1** Example for configuring a multicast static route to change the RPF route  
![](figure/en-us_image_0000001130623014.png)


#### Connecting RPF Routes

When unicast routes on a multicast network are blocked, multicast data flow forwarding will be interrupted due to a lack of an RPF route. In this case, multicast static routes can be configured to generate new RPF routes so that new multicast forwarding entries can be generated on the device to guide multicast data forwarding.

In [Figure 2](#EN-US_CONCEPT_0000001130782770__fig_dc_fd_mrm_000602), Domain1 and Domain2 are routing domains (RIP and OSPF domains for example) that have no unicast route to each other. As a result, the receivers in Domain2 cannot receive data from the multicast source. To address this issue, a multicast static route can be configured on DeviceC and Device D in Domain2 to re-specify RPF neighbors (DeviceB as the RPF neighbor of DeviceC and DeviceC as the RPF neighbor of DeviceD). In this manner, the receivers can receive multicast data from the multicast source.**Figure 2** Example for configuring multicast static routes to connect RPF routes  
![](figure/en-us_image_0000001130782804.png)

![](public_sys-resources/note_3.0-en-us.png) 

Multicast static routes take effect only on the configured multicast devices and are not imported or broadcast to other devices on the network.