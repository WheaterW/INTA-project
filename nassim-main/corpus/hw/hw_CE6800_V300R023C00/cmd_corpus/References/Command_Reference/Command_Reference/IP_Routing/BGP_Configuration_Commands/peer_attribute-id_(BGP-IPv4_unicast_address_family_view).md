peer attribute-id (BGP-IPv4 unicast address family view)
========================================================

peer attribute-id (BGP-IPv4 unicast address family view)

Function
--------



The **peer attribute-id** command configures the mode of processing a specified path attribute or an incorrect path attribute.

The **undo peer attribute-id** command restores the default setting.



By default, BGP path attributes are processed according to a standard protocol.


Format
------

**peer** *peerIpv4Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** }

**peer** *peerIpv4Addr* **treat-with-error** **attribute-id** *id* **accept-zero-value**

**undo peer** *peerIpv4Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> [ **discard** | **withdraw** | **treat-as-unknown** ]

**undo peer** *peerIpv4Addr* **treat-with-error** **attribute-id** *id* [ **accept-zero-value** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **path-attribute-treat** | Processes path attribute packets. | - |
| **attribute-id** *id* | Specifies an attribute ID. | The value is an integer, which can be as follows:  0: Reserved  5: LOCAL\_PREF  6: ATOMIC\_AGGREGATE  7: AGGREGATOR  9: ORIGINATORID  10: CLUSTER\_LIST  11: DPA  12: ADVERTISER  13: RCID\_PATH / CLUSTER\_ID  16: Extended Communities  17: AS4\_PATH  18: AS4\_AGGREGATOR  19: SAFI Specific Attribute (SSA)  20: Connector Attribute  21: AS\_PATHLIMIT  22: PMSI\_TUNNEL  23: Tunnel Encapsulation Attribute  24: Traffic Engineering  25: IPv6 Address Specific Extended Community  26: AIGP  27: PE Distinguisher Labels  28: ELC  29: LS\_TYPE  30: REMOTE\_NEXTHOP  32: LARGE\_COMMUNITY  40: PREFIX\_SID  128: ATTR\_SET  129: WIDE\_COMMUNITY  255: Reserved for development  31, 33-39, 41-127, 130-254: Unassigned |
| **to** *id2* | Specifies an end attribute ID. | The value is an integer, which can be as follows:  0: Reserved  5: LOCAL\_PREF  6: ATOMIC\_AGGREGATE  7: AGGREGATOR  9: ORIGINATORID  10: CLUSTER\_LIST  11: DPA  12: ADVERTISER  13: RCID\_PATH / CLUSTER\_ID  16: Extended Communities  17: AS4\_PATH  18: AS4\_AGGREGATOR  19: SAFI Specific Attribute (SSA)  20: Connector Attribute  21: AS\_PATHLIMIT  22: PMSI\_TUNNEL  23: Tunnel Encapsulation Attribute  24: Traffic Engineering  25: IPv6 Address Specific Extended Community  26: AIGP  27: PE Distinguisher Labels  28: ELC  29: LS\_TYPE  30: REMOTE\_NEXTHOP  32: LARGE\_COMMUNITY  40: PREFIX\_SID  128: ATTR\_SET  129: WIDE\_COMMUNITY  255: Reserved for development  31, 33-39, 41-127, 130-254: Unassigned |
| **discard** | Discards messages carrying specified attributes. | - |
| **withdraw** | Withdraws the routes with the specified attribute. | - |
| **treat-as-unknown** | Processes the specified attributes as unknown attributes. If a specified attribute is optional transitive, the BGP device accepts this attribute and advertises it to other peers; if the specified attribute is of any other type, the BGP device discards this attribute. | - |
| **treat-with-error** | Processes packets with incorrect path attributes. | - |
| **accept-zero-value** | Indicates to accept the path attributes with a value of 0. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP Update messages contain various path attributes. If the local device receives any Update message with an incorrect format, BGP session flapping may occur. To enhance reliability, you can run this command to configure a processing mode for specified BGP path attributes.The path-attribute-treat command is used to specify a processing mode for path attributes. The processing modes are as follows:

* discard: discarding messages carrying specified attributes.
* withdraw: withdrawing routes with specified attributes.
* treat-as-unknown: Processing specified attributes as unknown attributes

treat-with-error is used to specify the processing mode of incorrect path attributes. The processing modes are as follows:

* accept-zero-value: accepting the path attribute with the value of 0.

**Precautions**

Running this command may cause path attributes to be discarded or routes to be withdrawn. Therefore, exercise caution when running this command.This function takes effect immediately for the routes received after this command is executed. However, it does not take effect immediately for the routes received before this command is run; to make it take effect immediately, you need to run the **refresh bgp** command.Currently, attribute-id id in the **treat-with-error** command supports only the Originator\_ID attribute.


Example
-------

# Configure a mode in which a device processes specified path attributes in received BGP Update messages.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 path-attribute-treat attribute-id 19 to 21 discard

```