Overview of MLD
===============

Overview of MLD

#### Definition

The Multicast Listener Discovery (MLD) protocol is used to manage IPv6 multicast members. It sets up and maintains member relationships between IPv6 hosts and their directly connected multicast devices.

There are currently two versions of MLD: MLDv1 and MLDv2. Both versions support the Any-Source Multicast (ASM) model. MLDv2 can be directly applied to the Source-Specific Multicast (SSM) model, whereas MLDv1 needs to use the SSM mapping mechanism to support the SSM model.

MLD can be regarded as the IPv6 version of IGMP, and their implementation modes are similar. For example, MLDv1 is similar to IGMPv2, and MLDv2 is similar to IGMPv3.

In MLD and IGMP, the following functions are implemented in the same way. This document mainly describes only MLD-specific functions.

* MLD Router-Alert
* MLD prompt-leave
* MLD static group
* MLD group policy
* MLD SSM mapping

MLD-specific functions include MLD querier election and MLD group compatibility.

Configuring an ACL6 filtering rule is mandatory for source addressâbased MLD message filtering, whereas it is optional for source address-based IGMP message filtering.


#### Purpose

On an IPv6 network, after MLD is configured on receiver hosts and the multicast device to which the hosts are directly connected, the hosts can dynamically join a multicast group and the multicast device can manage members in the group.