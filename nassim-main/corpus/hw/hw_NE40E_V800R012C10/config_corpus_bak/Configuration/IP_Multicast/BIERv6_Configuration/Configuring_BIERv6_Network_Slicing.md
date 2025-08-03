Configuring BIERv6 Network Slicing
==================================

With BIERv6 network slicing, different slices can be used to isolate different multicast services and assure SLAs.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This function is supported only by the following: NE40E-M2F, NE40E-M2H, NE40E-M2K, NE40E-M2K-B.

BIERv6 network slicing can divide a BIERv6 tunnel into multiple isolated slice planes to carry various multicast services. Before planning network slices, you need to create network slice instances and allocate slice IDs. A physical network is divided into multiple network slices by dividing interface forwarding resources.

As shown in [Figure 1](#EN-US_TASK_0000001385494220__fig8274193314262), two specific multicast streams need to be forwarded through slices. Therefore, network slice instances need to be created on PE1, PE2, PE3, and the P, network slice interfaces need to be allocated, network slice instances need to be bound, and forwarding resources such as bandwidth need to be reserved. After BIERv6 network slicing is enabled globally and slice IDs are specified for network slices, multicast service packets are forwarded through the network slice interface corresponding to each slice ID.

**Figure 1** BIERv6 network slicing  
![](figure/en-us_image_0000001386015982.png)


[Configuring Network Slice Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bierv6_cfg_1007.html)

Configuring network slice instances is the first step for implementing network slicing. Interfaces can be added to network slices only after network slice instances are configured.

[Configuring Network Slice Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bierv6_cfg_1008.html)

You can configure network slice interfaces and specify the network slice instances to which they belong.

[Enabling BIERv6 Network Slicing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bierv6_cfg_1009.html)

After BIERv6 network slicing is enabled globally and slice IDs are specified, multicast packets are forwarded through specified network slices.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_bierv6_cfg_1014.html)

After configuring BIERv6 network slicing, check the committed configurations and whether they have taken effect.