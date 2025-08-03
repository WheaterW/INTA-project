Configuring IGMP Snooping Report Message Suppression
====================================================

After IGMP snooping Report message suppression is configured on a device, the device sends only one IGMP Report message to the upstream device when responding to IGMP Query messages sent by the upstream device. This effectively saves network bandwidth.

#### Usage Scenario

A Layer 3 device and user hosts exchange IGMP messages to generate forwarding entries. When a large number of user hosts exist on the network, processing redundant IGMP messages increase the burden on the Layer 3 device.

To solve this problem, you can configure IGMP snooping Report message suppression on a Layer 2 device between the Layer 3 device and user hosts.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001628655262__fig_dc_vrp_l2mc_cfg_002101), the CE functions as a user host of the upstream Layer 3 device (PE). The IGMP snooping Report message suppression function enables the CE to summarize information about user hosts' joining or leaving multicast groups before sending Report or Leave messages to the PE. With the function, when sending Report messages to the PE for the first time, the CE sends a robustness variable number of Report message copies. Subsequently, when periodically responding to IGMP Query messages from the PE, the CE sends only one IGMP Report message to the PE, regardless of the number of user ports in the corresponding multicast group. If a large number of users frequently join or leave multicast groups, the CE suppresses Report and Leave messages, reducing message processing workload of the PE.

**Figure 1** Network diagram of IGMP snooping Report message suppression  
![](figure/en-us_image_0000001628815206.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The CE in the figure is a Layer 2 device on which IGMP snooping Report message suppression needs to be configured.



#### Pre-configuration Tasks

Before configuring IGMP snooping Report message suppression, complete the following tasks:

* Ensure that interfaces are up at the link layer.
* Enable IGMP snooping globally.


[Enabling IGMP Snooping Report Message Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0291.html)

The querier function enables a device to send Query messages on behalf of an upstream device and respond to IGMP messages sent by a downstream device.

[(Optional) Configuring Transparent Transmission of Protocol Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0292.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0293.html)

After configuring IGMP snooping Report message suppression, verify the configuration.