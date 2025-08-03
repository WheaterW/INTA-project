Establishing the EVC Model
==========================

The EVC model is established to forward Layer 2 services.

#### Usage Scenario

Traditional Ethernet access models have the drawbacks:

* Service access points
  
  Sub-interfaces and Layer 2 interfaces, which have various types and require different configurations.
* Broadcast domains
  
  + Global virtual local area network (VLAN) for traditional Layer 2 services:
    
    In a metro Ethernet network, VLANs are used to prevent broadcast storms. The VLAN tag field defined in IEEE 802.1Q has 12 bits and identifies only a maximum of 4096 VLANs, which is insufficient for a great number of users in the metro Ethernet.
    
    QinQ was developed to address the shortage of VLAN ID resources. However, QinQ must be used with the virtual private LAN service (VPLS) to provide local switching services, and QinQ cannot implement local switching services and Layer 3 packet termination services at the same time.
  + Virtual switching instance (VSI) for VPLS services:
    
    - After a VSI is sold as a whole to a customer, the customer has to plan VLANs and traffic within the VSI.
    - When VLAN services are carried within a VSI, the VLANs are not isolated, posing security risks. If the same MAC address exists in multiple VLANs of a VSI, MAC address flapping occurs, affecting services.

To overcome the drawbacks, the NE40E implements the EVC model. The EVC model is established to forward Layer 2 services.

#### Pre-configuration Tasks

Before establishing the EVC model, connect interfaces between devices and set interface parameters so that the physical status of the interfaces can be up.



[Creating a Bridge Domain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0004.html)

In the EVC model, Layer 2 services are transmitted within a bridge domain.

[Configuring a Service Access Point](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0005.html)

An EVC Layer 2 sub-interface is used as an EVC service access point, on which traffic encapsulation types and behaviors can be flexibly combined. A traffic encapsulation type and behavior are grouped into a traffic policy. Traffic policies help implement flexible Ethernet service access.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0006.html)

After establishing an EVC model, you can view the bridge domain configurations, including information about traffic encapsulation types and behaviors configured on an EVC Layer 2 sub-interface.