Understanding OSPF Multi-area Adjacency
=======================================

Understanding OSPF Multi-area Adjacency

#### Context

OSPF uses the shortest path first (SPF) algorithm but preferentially selects an intra-area path even if an inter-area path is the shortest. For example, if there are two paths to a destination address, one is an inter-area path that passes through a high-speed link, and the other is an intra-area path that passes through a low-speed link, OSPF will preferentially select the intra-area path according to OSPF route selection rules. To allow OSPF to preferentially select the inter-area path passing through the high-speed link, you can configure multiple sub-interfaces and add them to different areas. However, this method increases the total number of routes because an independent IP address needs to be configured for each sub-interface and many IP addresses will be advertised. To address this issue, OSPF multi-area adjacency is introduced.

OSPF multi-area adjacency allows an OSPF interface to be added to and shared by multiple areas.

**Figure 1** Traffic forwarding paths before and after OSPF multi-area adjacency is configured  
![](figure/en-us_image_0000001176743015.png)

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130783260__fig_feature_mdj002231722501), the link between DeviceA and DeviceB in area 1 is a high-speed link.

Before OSPF multi-area adjacency is configured ([Figure 1](#EN-US_CONCEPT_0000001130783260__fig_feature_mdj002231722501) a), traffic from DeviceA to DeviceB in area 2 is forwarded along the path DeviceA->DeviceC->DeviceD->DeviceB in the area, passing through the low-speed link.

After OSPF multi-area adjacency is configured ([Figure 1](#EN-US_CONCEPT_0000001130783260__fig_feature_mdj002231722501) b), multi-area adjacency interfaces are created between DeviceA and DeviceB and belong to area 2. This allows traffic from DeviceA to DeviceB in area 2 to be forwarded along the high-speed link of DeviceA->DeviceB.

OSPF multi-area adjacency has the following advantages:

* Allows the same interface to be used for multiple areas, thereby reducing the consumption of OSPF interface resources in multi-area deployment.
* Prevents traffic from being routed through a low-speed link and allows a high-speed link to transmit multi-area traffic, thereby optimizing the OSPF network.


#### Related Concepts

Multi-area adjacency interface: An OSPF logical interface created by enabling multi-area adjacency on an OSPF primary interface (an OSPF-enabled interface). It is also called a secondary interface. The multi-area adjacency interface has the following characteristics:

* The multi-area adjacency interface and the OSPF primary interface belong to different OSPF areas.
* The network type of the multi-area adjacency interface can only be P2P. The multi-area adjacency interface runs an independent interface state machine and neighbor state machine.
* The multi-area adjacency interface on a P2P primary interface sends OSPF packets in multicast mode.
* The multi-area adjacency interface on a non-P2P primary interface sends OSPF packets in unicast mode.


#### Fundamentals

**Figure 2** Conceptual diagram of OSPF multi-area adjacency  
![](figure/en-us_image_0000001176743017.png)

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001130783260__fig_feature_mdj002231722502), the link between DeviceA and DeviceB in area 1 is a high-speed link. In area 2, traffic from DeviceA to DeviceB is forwarded along the low-speed link of DeviceA->DeviceC->DeviceD->DeviceB within the area. To allow traffic from DeviceA to DeviceB in area 2 to be forwarded along the high-speed link of DeviceA->DeviceB, deploy OSPF multi-area adjacency.

This function is implemented by creating OSPF multi-area adjacency interfaces on the primary interfaces of DeviceA and DeviceB and specifying area 2 for the multi-area adjacency interfaces so that they belong to this area.

1. An adjacency is established between the multi-area adjacency interfaces of DeviceA and DeviceB. The establishment process is the same as that of the basic OSPF protocol. For details, see [Adjacency Establishment](vrp_ospf_cfg_0006.html#EN-US_CONCEPT_0000001130623482__section_02).
2. OSPF performs route calculation. The calculation process is the same as that of the basic OSPF protocol. For details, see [Route Calculation](vrp_ospf_cfg_0006.html#EN-US_CONCEPT_0000001130623482__section_03).

The optimal path calculated by OSPF in area 2 is the path DeviceA -> DeviceB. Therefore, traffic from DeviceA to DeviceB is forwarded along the high-speed link DeviceA -> DeviceB. In this manner, this high-speed link can be shared by area 1 and area 2.


For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.

![](../public_sys-resources/note_3.0-en-us.png) 

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

The following commands can be used only after the weak security algorithm/protocol feature package is installed.

| Command | Parameters Available Only After Feature Package Installation |
| --- | --- |
| [**authentication-mode**](cmdqueryname=authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *KeyID* { **plain** *SPlainText* | [ **cipher** ] *SCipherText* } ] | **md5** and **hmac-****md5** |
| [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] **multi-area** { *area-id* | *area-id* } | **md5** and **hmac-****md5** |