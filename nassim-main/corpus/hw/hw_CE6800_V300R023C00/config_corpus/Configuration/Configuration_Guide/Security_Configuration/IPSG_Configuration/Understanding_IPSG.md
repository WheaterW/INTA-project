Understanding IPSG
==================

Understanding IPSG

#### IPSG Fundamentals

IPSG checks IP packets on Layer 2 interfaces against a binding table that contains the bindings of source IP addresses, source MAC addresses, VLANs, and inbound interfaces. Only packets matching binding entries are forwarded, and other packets are discarded.

[Table 1](#EN-US_CONCEPT_0000001513049278__table15634419201) describes two types of binding tables: static and dynamic binding tables.

**Table 1** Binding tables
| Type | Description | Application Scenario |
| --- | --- | --- |
| Static binding table | A static binding table is manually configured using the **user-bind static** command. | A network with a few IPv4 hosts that use static IP addresses. |
| DHCP snooping binding table | After DHCP snooping is configured, hosts request IP addresses from the DHCP server. The device dynamically generates DHCP snooping binding entries according to the DHCP reply packets returned by the DHCP server. | A network with many IPv4 hosts that obtain IP addresses from the DHCP server. |

After the binding table is generated, IPSG delivers ACL rules to the specified interface or VLAN according to the binding table, and then checks all IP packets against the ACL rules. The device forwards only the packets that match binding entries. When the binding table is modified, IPSG delivers the ACL rules again. By default, if IPSG is enabled but no binding table is generated, the device forwards IP protocol packets (except for IGMP protocol packets) and rejects all IP data packets.

![](public_sys-resources/note_3.0-en-us.png) 

IPSG checks only the IP packets. It does not check non-IP packets such as ARP packets.

[Figure 1](#EN-US_CONCEPT_0000001513049278__fig166683434714) illustrates the IPSG working mechanism. When an unauthorized host forges an authorized host's IP address to send packets to the Device, the Device discards these packets because they do not match binding entries.

**Figure 1** IPSG working mechanism  
![](figure/en-us_image_0000001513169274.png)

Typically, IPSG is configured on the interfaces or VLANs of the user-side access device.

* After IPSG is enabled on a user-side interface, it checks all IP packets received by the interface against binding entries.

* After IPSG is enabled in a user-side VLAN, it checks the IP packets received by all interfaces in the VLAN against binding entries.
* If the user-side access device does not support IPSG, you can configure IPSG on the interfaces or in VLANs of the upper-layer device.

#### IPSG Interface Roles

IPSG can be configured only on Layer 2 physical interfaces or in VLANs. It also checks the packets only on the untrusted interfaces with IPSG enabled and considers all interfaces to be untrusted by default (you can specify trusted interfaces). The trusted and untrusted interfaces in IPSG are the same as those used in DHCP snooping. In addition, these interfaces are also valid for IPSG based on a static binding table.

[Figure 2](#EN-US_CONCEPT_0000001513049278__fig31701652165715) shows the IPSG interface roles.

* Interface1 and Interface2 are untrusted interfaces with IPSG enabled. The Device performs an IPSG check on the packets received by these interfaces.
* Interface3 is an untrusted interface with IPSG disabled. The device does not perform an IPSG check on the packets received by this interface. Consequently, Interface3 is prone to attacks.
* Interface4 is a trusted interface specified by users. The device does not perform an IPSG check on the packets received by this interface; however, it is not prone to attacks. On a network with DHCP snooping configured, the interfaces directly or indirectly connected to a valid DHCP server are generally configured as trusted interfaces.

**Figure 2** IPSG interface roles  
![](figure/en-us_image_0000001694854929.png)

#### IPSG Filtering

A binding entry contains the following items: MAC address, IP address, VLAN ID, and inbound interface. IPSG checks received packets against all items in a static binding table. For a dynamic binding table, this is also the default implementation, but you can additionally specify the items against which IPSG performs checks. [Table 2](#EN-US_CONCEPT_0000001513049278__table488634913455) describes some common check items.

**Table 2** IPSG filtering
| Item | Description |
| --- | --- |
| Source IP address | The device forwards only the packets whose source IP addresses match binding entries. |
| Source MAC address | The device forwards only the packets whose source MAC addresses match binding entries. |
| Source IP address + source MAC address | The device forwards only the packets whose source IP and MAC addresses match binding entries. |
| Source IP address + source MAC address + interface | The device forwards only the packets whose source IP addresses, source MAC addresses, and interfaces match binding entries. |
| Source IP address + source MAC address + interface + VLAN | The device forwards only the packets whose source IP addresses, source MAC addresses, interfaces, and VLANs match binding entries. |