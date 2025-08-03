Understanding Static ND
=======================

Understanding Static ND

#### Definition

Static ND allows a network administrator to create a mapping between IPv6 and MAC addresses.


#### Related Concepts

The main difference between static ND and dynamic ND lies in how ND entries are generated and maintained. That is, dynamic ND entries are automatically generated and maintained using ND messages, whereas static ND entries are manually configured and maintained by network administrators. [Table 1](#EN-US_CONCEPT_0000001130622502__table811145961914) describes the advantages and disadvantages of dynamic ND and static ND.

**Table 1** Advantages and disadvantages of dynamic ND and static ND
| Type | Advantage | Disadvantage |
| --- | --- | --- |
| Dynamic ND | Dynamic ND entries do not need to be manually configured or maintained by network administrators. When a network device fails or the NIC of a host is replaced, ND entries can be dynamically updated in real time, greatly reducing the maintenance workload of network administrators. | * Dynamic ND entries can be aged or overwritten by new dynamic ND entries. Due to this, communication stability and security cannot be ensured. * The execution of dynamic ND consumes certain network resources. Therefore, dynamic ND does not apply to networks with insufficient bandwidth resources, and this may negatively affect user services on such networks. |
| Static ND | * Static ND entries are not aged or overwritten by dynamic ND entries, ensuring communication stability. * With static ND, IPv6 and MAC addresses are bound to prevent network attackers from tampering with ND entries through ND messages, ensuring communication security. * Static ND eliminates the execution of dynamic ND, reducing network resource consumption. | Static ND entries must be manually configured by network administrators. In scenarios where network structures frequently change, the maintenance workload of network administrators is heavy. |


To ensure communication stability and security, deploy static ND based on actual requirements and network resources.

* IPv6 addresses can be bound to the MAC address of a specified gateway to ensure that only this gateway forwards the IPv6 datagrams destined for these IPv6 addresses.
* The destination IPv6 addresses of certain IPv6 datagrams sent by a specified host can be bound to a nonexistent MAC address, helping filter out unnecessary IPv6 datagrams.


#### Application Scenarios

Configuring static ND entries improves communication security. If a static ND entry is configured on a device, the device can communicate with the peer device using only the specified MAC address. This improves communication security, because network attackers cannot modify the mapping between the IPv6 and MAC addresses using ND messages.

Static ND is applicable to the following networks:

* Network with a simple topology and high stability

* Network with high information security requirements