Overview of IPSG
================

Overview of IPSG

#### Definition

IP Source Guard (IPSG) implements source IP address filtering based on Layer 2 interfaces to prevent unauthorized hosts from using IP addresses of authorized hosts or specified IP addresses to access or attack the network.


#### Purpose

As the network scale continues to grow, many attackers are forging source IP addresses to initiate IP address spoofing attacks. In order to obtain network access rights and access networks, attackers forge the IP addresses of authorized users. As a result, authorized users cannot access networks and sensitive information may be leaked. IPSG provides a mechanism to effectively defend against IP address spoofing attacks.

[Figure 1](#EN-US_CONCEPT_0000001563769601__fig7838831020) illustrates how IPSG defends against attacks from an unauthorized host, which obtains network access rights by forging an authorized host's IP address. IPSG is configured on the Device's user-side interface or VLAN. With this configuration, the Device checks the IP packets received by the interface and discards the packets from unauthorized hosts, preventing IP address spoofing attacks.

**Figure 1** Typical implementation of IPSG  
![](figure/en-us_image_0000001564009529.png)

#### Benefits

* IPSG reduces costs for ensuring normal network operations and information security.
* IPSG provides secure network environments and more stable network services.