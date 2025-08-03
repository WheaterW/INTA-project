Understanding MLD SSM Mapping
=============================

Source-specific multicast (SSM) requires a device to know the multicast sources specified when hosts join a multicast group. A host running MLDv2 can specify a multicast source address in an MLDv2 Report message. However, in some cases, hosts can run only MLDv1. To enable these hosts to use the SSM service, a device needs to provide the MLD SSM mapping function.

MLD SSM mapping is implemented based on static SSM mapping entries. A device converts (\*, G) information in MLDv1 Report messages into (G, INCLUDE, (S1, S2...)) information to provide the SSM service.

After SSM mapping entries are configured, an MLD querier checks the group address G in each MLDv1 Report message received from a host, and processes the message based on the check result:

* If G is in the any-source multicast (ASM) group address range, the querier provides the ASM service for the host.
* If G is in the SSM group address range (FF3*x*::/32 by default, where *x* cannot be 1 or 2):
  + If the device has no SSM mapping entry matching G, it cannot provide the SSM service and therefore discards the message.
  + If the device has an SSM mapping entry matching G, it converts (\*, G) information in the Report message into (G, INCLUDE, (S1, S2...)) information and provides the SSM service.

#### Implementation of Static SSM Mapping

On the SSM network's user network segment shown in [Figure 1](#EN-US_CONCEPT_0000001538416578__fig_01), HostA, HostB, and HostC run MLDv2, MLDv1, and MLDv1, respectively. HostB and HostC cannot run MLDv2. To provide the SSM service for all the hosts on the network segment, enable MLD SSM mapping on the MLD querier (Device) and configure mapping rules.

**Figure 1** Network diagram of MLD SSM mapping  
![](figure/en-us_image_0000001589336537.png)

Assume that the following mappings are configured on Device.

| Multicast Group Address | Mapped Multicast Source Address |
| --- | --- |
| FF11::/16 | 2001:db8:1::1 |
| FF11:1::/32 | 2001:db8:2::2 |
| FF11:1::/32 | 2001:db8:3::3 |
| FF11:1:1::/64 | 2001:db8:4::4 |

When Device receives Report messages from HostB and HostC, it checks whether the group addresses in the messages are in the SSM group address range. If they are, Device generates multicast entries based on the configured mappings. If a group address is mapped to multiple sources, Device generates multiple (S, G) entries.

Device generates an entry based on each mapping entry that matches a group address. Therefore, Device generates four entries for FF11:1:1::8 and three entries for FF11:1:2::8.

| Group Address in an MLDv1 Report Message | Generated Multicast Entry |
| --- | --- |
| FF11:1:1::8 (from HostC) | (2001:db8:1::1, FF11:1:1::8)  (2001:db8:2::2, FF11:1:1::8)  (2001:db8:3::3, FF11:1:1::8)  (2001:db8:4::4, FF11:1:1::8) |
| FF11:1:2::8 (from HostB) | (2001:db8:1::1, FF11:1:2::8)  (2001:db8:2::2, FF11:1:2::8)  (2001:db8:3::3, FF11:1:2::8) |