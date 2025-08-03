Understanding IGMP SSM Mapping
==============================

Source-specific multicast (SSM) requires a device to know the multicast sources specified when hosts join a multicast group. A host running IGMPv3 can specify a multicast source address in an IGMPv3 Report message. In some cases, hosts can run only IGMPv1 or IGMPv2. To enable these hosts to use the SSM service, a device needs to provide the IGMP SSM mapping function.

IGMP SSM mapping is implemented based on static SSM mapping entries. A device converts (\*, G) information in IGMPv1 and IGMPv2 Report messages into (G, INCLUDE, (S1, S2...)) information to provide the SSM service.

After SSM mapping entries are configured, an IGMP querier checks the group address G in each IGMPv1 or IGMPv2 Report message received from a host, and processes the message based on the check result:

* If G is in the any-source multicast (ASM) group address range, the querier provides the ASM service for the host.
* If G is in the SSM group address range (232.0.0.0 to 232.255.255.255 by default):
  + If the device has no SSM mapping entry matching G, it cannot provide the SSM service and discards the message.
  + If the device has an SSM mapping entry matching G, it converts (\*, G) information in the Report message into (G, INCLUDE, (S1, S2...)) information and provides the SSM service.

#### Implementation of Static SSM Mapping

On the SSM network's user network segment shown in [Figure 1](#EN-US_CONCEPT_0000001130784208__fig_01), HostA, HostB, and HostC run IGMPv3, IGMPv2, and IGMPv1, respectively. HostB and HostC cannot run IGMPv3. To provide the SSM service for all the hosts on the network segment, enable IGMP SSM mapping on the IGMP querier (Device) and configure mapping rules.

**Figure 1** Network diagram of IGMP SSM mapping  
![](figure/en-us_image_0000001130784234.png)

Assume that the following mappings are configured on Device.

| Multicast Group Address | Mapped Multicast Source Address |
| --- | --- |
| 232.0.0.0/8 | 10.10.1.1 |
| 232.1.0.0/16 | 10.10.2.2 |
| 232.1.0.0/16 | 10.10.3.3 |
| 232.1.1.0/24 | 10.10.4.4 |

When Device receives Report messages from HostB and HostC, it checks whether the group addresses in the messages are in the SSM group address range. If so, Device generates multicast entries based on the configured mappings. If a group address is mapped to multiple sources, Device generates multiple (S, G) entries.

Device generates an entry based on each mapping entry that matches a group address. Therefore, Device generates four entries for 232.1.1.1 and three entries for 232.1.2.2.

| Group Address in an IGMPv1/IGMPv2 Report Message | Generated Multicast Entry |
| --- | --- |
| 232.1.1.1 (from HostC) | (10.10.1.1, 232.1.1.1)  (10.10.2.2, 232.1.1.1)  (10.10.3.3, 232.1.1.1)  (10.10.4.4, 232.1.1.1) |
| 232.1.2.2 (from HostB) | (10.10.1.1, 232.1.2.2)  (10.10.2.2, 232.1.2.2)  (10.10.3.3, 232.1.2.2) |