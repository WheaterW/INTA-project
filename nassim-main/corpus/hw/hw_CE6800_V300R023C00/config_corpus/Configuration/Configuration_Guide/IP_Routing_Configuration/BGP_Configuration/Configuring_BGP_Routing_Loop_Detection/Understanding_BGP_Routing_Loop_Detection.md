Understanding BGP Routing Loop Detection
========================================

Understanding BGP Routing Loop Detection

#### Fundamentals of BGP Routing Loop Detection

Once a routing loop occurs on a Layer 3 network, packets cannot be forwarded, which may cause losses to carriers or users.

To detect potential routing loops on the network, BGP defines the Loop-detection attribute. The fundamentals of BGP routing loop detection are as follows:

1. After BGP routing loop detection is enabled, the local device generates a random number, adds the Loop-detection attribute to the routes to be advertised to EBGP peers or the locally imported routes to be advertised to peers, and encapsulates the attribute with the random number and the local **vrfID**. The local **vrfID** is automatically generated and globally unique. In the public network scenario, the **vrfID** is 0. In the private network scenario, the **vrfID** is automatically generated after a VPN instance is created. When OSPF/IS-IS routes are imported to BGP, the routing loop attributes of the OSPF/IS-IS routes are inherited.
2. When the local device receives a route with the Loop-detection attribute from another device, the local device performs the following checks:
   * Compares the Loop-detection attribute of the received route with the combination of the **vrfID** and random number that are locally stored.
     + If they are the same, the local device determines that a routing loop occurs.
     + If they are different, the local device determines that no routing loop occurs, and the route participates in route selection.
   * Checks whether the received route has a routing loop record.![](public_sys-resources/note_3.0-en-us.png) 
     
     Routing loop records are affected by the following commands:
     
     + For the routes that already have routing loop records before routing loop alarms are cleared using the **clear route loop-detect bgp alarm** command, the records always exist.
     + For the routes that have routing loop records but no longer carry the routing loop attribute of the local device after routing loop alarms are cleared using the **clear route loop-detect bgp alarm** command, the records of these routes are deleted.
     + If the **undo route loop-detect bgp enable** command is run, the routing loop records of all looped routes are deleted.
     + If a route has a routing loop record, a routing loop once occurred. Such a route is considered to be a looped route even if it does not carry the routing loop attribute of the local device.
     + If there is no routing loop record and the Loop-detection attribute of the received route is different from the combination of the **vrfID** and random number that are locally stored, the local device determines that no routing loop occurs, and the route participates in route selection.
     + If there is no routing loop record but the Loop-detection attribute of the received route is the same as the combination of the **vrfID** and random number that are locally stored, the local device determines that a routing loop occurs.
3. If a routing loop is detected and the looped route is preferentially selected, the local device reports an alarm to notify the user of the routing loop risk, enters the loop prevention state, and performs the following operations:
   * Preferentially selects non-looped routes when the BGP routing table contains multiple routes with the same destination as the looped route.
   * Increases the MED value and reduces the local preference of the looped route when advertising it.
4. After the device processes a looped route, the routing loop may be resolved. If the routing loop persists, you need to locate the cause of the loop and resolve the loop. As the device cannot detect when the loop risk is eliminated, the routing loop alarm will not be cleared automatically. To manually clear the alarm after the loop risk is eliminated, you can run a related command.

#### Implementation

The Loop-detection attribute is a private BGP attribute. It uses a reserved value (type=255) to implement routing loop detection in some scenarios. [Figure 1](#EN-US_CONCEPT_0000001196503391__fig3677420152013) shows the Loop-detection attribute TLV, and [Table 1](#EN-US_CONCEPT_0000001196503391__table1755319320291) describes the fields in it.

![](public_sys-resources/note_3.0-en-us.png) 

Currently, the Loop-detection attribute is supported only in the BGP IPv4 public network, BGP IPv4 private network, BGP IPv6 public network, BGP IPv6 private network, BGP VPNv4, and BGP VPNv6 address families.


**Figure 1** Loop-detection attribute TLV extension  
![](figure/en-us_image_0000001196424949.png)

**Table 1** Fields in the Loop-detection attribute TLV
| Field | Description |
| --- | --- |
| Attr.Flags | Attribute flag, which occupies one byte (eight bits). The meaning of each bit is as follows:  O (Optional bit): defines whether the attribute is optional. The value 1 indicates an optional attribute, whereas the value 0 indicates a well-known attribute.  T (Transitive bit): defines whether the attribute is transitive. For an optional attribute, the value 1 indicates that the attribute is transitive, whereas the value 0 indicates that the attribute is non-transitive. For a well-known attribute, the value must be set to 1.  P (Partial bit): defines whether the attribute is partial. If the optional transitive attribute is partial, the value is set to 1; if the attribute is complete, the value is set to 0. For well-known attributes and for optional non-transitive attributes, the value must be set to 0.  E (Extended Length bit): defines whether the length (Attr. Length) of the attribute needs to be extended. If the attribute length does not need to be extended, the value is set to 0 and the Attr. Length is 1 octet. If the attribute length needs to be extended, the value is set to 1 and the Attr. Length is 2 octets.  U (Unused bits): indicates that the lower-order 4 bits are not used. These bits must be set to 0s upon transmission and ignored upon receipt. |
| Attr.Type Code | Attribute type, which occupies one byte. The value is an unsigned integer, with the initial value being 0xFF. |
| Attr.Length | Length of the attribute. |
| Attr.Value | Huawei's organizationally unique identifier (OUI), with the value being 0x0030FBB8, which is used to differentiate Huawei from other vendors. |

BGP also defines a sub-TLV for Attr.Value to identify the device that detects a routing loop. [Figure 2](#EN-US_CONCEPT_0000001196503391__fig1413194121720) shows the sub-TLV, and [Table 2](#EN-US_CONCEPT_0000001196503391__table4161185582017) describes the fields in the sub-TLV.

![](public_sys-resources/note_3.0-en-us.png) 

A maximum of four Loop-detection attribute sub-TLVs can be carried. If more than four sub-TLVs exist, they are overwritten according to the first-in-first-out rule.


**Figure 2** Loop-detection attribute sub-TLV  
![](figure/en-us_image_0000001150585080.png)

**Table 2** Fields in the Loop-detection attribute sub-TLV
| Field | Description |
| --- | --- |
| Attr.Type | The value is 0xFF. |
| Attr.Length | Length of the attribute. The value is 0x08, 0x10, 0x18, or 0x20. |
| Attr.Value | ``` 0            31            63 +-------------+-------------+ | vrfID | Random number | +-------------+-------------+ ```  **vrfID** specifies a system-allocated VPN ID. The value ranges from 0 to 0xFFFFFFFF.  NOTE:  For BGP VPNv4 and BGP VPNv6 routes, the system only checks the random number when determining whether a routing loop occurs; that is, it does not check the **vrfID**. |



#### Application Scenario

BGP routing loops may occur in the following scenarios. You are advised to enable BGP routing loop detection during network planning.

* On the network shown in [Figure 3](#EN-US_CONCEPT_0000001196503391__fig12318936133717), DeviceA and DeviceC belong to AS 100, and DeviceB belongs to AS 200. An export policy is configured on DeviceB to delete the original AS numbers from the routes to be advertised to DeviceC. After receiving a BGP route that originates from DeviceC, DeviceA advertises the route to DeviceB. After receiving the route, DeviceB advertises the route back to DeviceC. As a result, a BGP routing loop occurs on DeviceC. After BGP routing loop detection is enabled on the entire network, DeviceC adds Loop-detection attribute 1 to the BGP route (locally imported) before advertising the route to DeviceA. After receiving the route, DeviceA adds Loop-detection attribute 2 to the route before advertising the route to DeviceB (EBGP peer). After receiving the route, DeviceB adds Loop-detection attribute 3 to the route before advertising the route to DeviceC (EBGP peer). After receiving the Loop-detection attributes, DeviceC discovers that these attributes contain Loop-detection attribute 1 which was added by itself, and then reports a routing loop alarm.**Figure 3** Typical networking 1 with a BGP routing loop  
  ![](figure/en-us_image_0000001150425258.png)
* On the network shown in [Figure 4](#EN-US_CONCEPT_0000001196503391__fig1076313911216), DeviceA resides in AS 100; DeviceB resides in AS 200; DeviceC and DeviceD reside in AS 300. An export policy is configured on DeviceD to delete the original AS numbers from the routes to be advertised to DeviceB. In this scenario, a BGP routing loop occurs on DeviceB.**Figure 4** Typical networking 2 with a BGP routing loop  
  ![](figure/en-us_image_0000001196504839.png)
* On the network shown in [Figure 5](#EN-US_CONCEPT_0000001196503391__fig127071748161714), the PE advertises a VPN route through VPN1, and then receives this route through VPN1, indicating that a routing loop occurs on the PE.**Figure 5** Typical networking 3 with a BGP routing loop  
  ![](figure/en-us_image_0000001196424947.png)
* On the network shown in [Figure 6](#EN-US_CONCEPT_0000001196503391__fig20671159523), DeviceA, DeviceB, and DeviceC belong to AS 100. An IBGP peer relationship is established between DeviceA and the RR, between the RR and DeviceB, and between the RR and DeviceC. OSPF runs on DeviceB and DeviceC. DeviceB is configured to import BGP routes to OSPF, and DeviceC is configured to import OSPF routes to BGP. An export policy is configured on DeviceA to add AS numbers to the AS\_Path attribute for the routes to be advertised to the RR. After receiving a BGP route from DeviceA, the RR advertises this route to DeviceB. DeviceB then imports the BGP route to convert it to an OSPF route and advertises the OSPF route to DeviceC. DeviceC then imports the OSPF route to convert it to a BGP route and advertises the BGP route to the RR. When comparing the route advertised by DeviceA and the route advertised by DeviceC, the RR prefers the one advertised by DeviceC because the AS\_Path of the route advertised by DeviceA is longer than that of the route advertised by DeviceC. As a result, a stable routing loop occurs.
  
  To avoid this problem, enable BGP routing loop detection on DeviceC. After BGP routing loop detection is enabled, DeviceC adds Loop-detection attribute 1 to the BGP route imported from OSPF and advertises the BGP route to the RR. After receiving this BGP route, the RR advertises it (carrying Loop-detection attribute 1) to DeviceB. As OSPF routing loop detection is enabled by default, when the BGP route is imported to become an OSPF route on DeviceB, the OSPF route inherits the routing loop attribute of the BGP route and has an OSPF routing loop attribute added as well before the OSPF route is advertised to DeviceC. Upon receipt of the OSPF route, DeviceC imports it to convert it to a BGP route. Because BGP routing loop detection is enabled, the BGP route inherits the routing loop attributes of the OSPF route. Upon receipt of the route, DeviceC finds that the routing loop attributes in the received route contain its own routing loop attribute and therefore determines that a routing loop has occurred. In this case, DeviceC generates an alarm, and reduces the local preference and increases the MED value of the route before advertising the route to the RR. After receiving the route, the RR compares this route with the route advertised by DeviceA. Because the route advertised by DeviceC has a lower local preference and a larger MED value, the RR preferentially selects the route advertised by DeviceA. This resolves the routing loop.
  
  When the OSPF route is transmitted to DeviceC again, DeviceC imports it to convert it to a BGP route. At this point, the route carries only the OSPF routing loop attribute added by DeviceB. However, DeviceC still considers the route as a looped route because the route has a routing loop record. In this case, the RR does not preferentially select the route after receiving it from DeviceC. Then routes converge normally.
  
  **Figure 6** Typical networking 4 with a BGP routing loop  
  ![](figure/en-us_image_0000001150425260.png)

![](public_sys-resources/note_3.0-en-us.png) 

This function is not supported in the following scenarios:

* When BGP is configured to advertise the default route, the Loop-detection attribute is not added to the default route.
* When BGP Add-Path is configured, the Loop-detection attribute is not added to routes.
* When the route server function is configured, the Loop-detection attribute is not added to the routes advertised by the server.
* The Loop-detection attribute is not added to the received routes to be advertised to IBGP peers.