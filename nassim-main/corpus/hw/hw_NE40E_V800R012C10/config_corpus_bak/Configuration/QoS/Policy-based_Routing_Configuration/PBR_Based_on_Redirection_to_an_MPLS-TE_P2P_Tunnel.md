PBR Based on Redirection to an MPLS-TE P2P Tunnel
=================================================

This section describes the usage scenario and configuration procedures of policy-based routing (PBR) based on redirection to an MPLS-TE P2P tunnel.

#### Usage Scenario

As networks rapidly develop and services become increasingly diversified, multiple service flows share the same network resource. In some scenarios, incoming or ongoing traffic on a network needs to be classified. For example, voice, video, and data services must be distinguished and allocated different bandwidth values because they have different requirements on the delay. Traffic from different users must be distinguished and allocated different bandwidth values and priorities. The traffic policy defined for behavior aggregate (BA) classification can hardly meet such requirements. To address this issue, PBR based on redirection to an MPLS-TE P2P tunnel can be configured.


#### Pre-configuration Tasks

Before configuring PBR based on redirection to an MPLS-TE P2P tunnel, complete the following tasks:

* Configure physical parameters of relevant interfaces to ensure that physical links work properly.
* Configure link layer attributes of relevant interfaces to ensure their proper functioning.
* Configure IP addresses for relevant interfaces.
* Configure routing protocols to implement IP interworking.


[Configuring PBR Rules](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_7005.html)



[Configuring Actions for PBR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_7006.html)



[Applying PBR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_7007.html)



[Verifying the Configuration of PBR Based on Redirection to an MPLS-TE P2P Tunnel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_7008.html)

After configuring policy-based routing (PBR), check the configurations.