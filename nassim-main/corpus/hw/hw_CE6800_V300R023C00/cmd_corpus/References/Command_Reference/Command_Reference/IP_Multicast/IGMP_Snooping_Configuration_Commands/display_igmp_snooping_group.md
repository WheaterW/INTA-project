display igmp snooping group
===========================

display igmp snooping group

Function
--------



The **display igmp snooping group** command displays multicast group information dynamically learned on a local interface or a remote peer.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping group interface** { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ]

**display igmp snooping group interface** { *interface-type* *interface-number* | *interface-name* } [ **pe-vid** *pevid* ] [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ]

**display igmp snooping group**

**display igmp snooping group interface** { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ] **brief**

**display igmp snooping group brief**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping group interface** { *interface-type* *interface-number* | *interface-name* } [ **pe-vid** *pevid* [ **ce-vid** *cevid* ] ] **bridge-domain** *bd-id* [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ]

**display igmp snooping group peer** *ip-address* **bridge-domain** *bd-id* [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping group interface** { *interface-type* *interface-number* | *interface-name* } [ **pe-vid** *pevid* [ **ce-vid** *cevid* ] ] **bridge-domain** *bd-id* [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ] **brief**

**display igmp snooping group peer** *ip-address* **bridge-domain** *bd-id* [ [ **source-address** *source-ip-address* ] **group-address** *group-address* ] **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Displays dynamically learned multicast group information of a specified interface. | - |
| **vlan** *vlan-id* | Displays dynamically learned multicast group information of a specified VLAN. | The value is an integer ranging from 1 to 4094. |
| **source-address** *source-ip-address* | Displays dynamically learned information about a multicast group to which a specified multicast source sends data. | The value can be a class A, B, or C address, in dotted decimal notation. |
| **group-address** *group-address* | Displays dynamically learned information about a specified multicast group. | The value is a class D address, in dotted decimal notation. |
| **interface** *interface-type* *interface-number* | Displays dynamically learned multicast group information of a specified interface. | - |
| **pe-vid** *pevid* | Displays dynamically learned multicast group information of a sub-interface that has a specified outer VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **brief** | Displays summary information. | - |
| **ce-vid** *cevid* | Displays dynamically learned multicast group information of a sub-interface that has a specified inner VLAN ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |
| **bridge-domain** *bd-id* | Displays dynamically learned multicast group information of a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **peer** *ip-address* | Displays dynamically learned multicast group information of a specified peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To display multicast group information of a local interface or a remote peer dynamically learned by a device, run this command.

**Precautions**



This command has output only after the device has dynamically learned multicast group information of a local interface or a remote peer.The display igmp snooping group command displays information about multicast groups dynamically learned by all instances.If only the interface parameter is specified in the display igmp snooping group interface command, this command displays information about multicast groups dynamically learned by the main interface of a VSI.The display igmp snooping group interface bridge-domain command displays information about multicast groups dynamically learned by a BD instance.The display igmp snooping group interface vlan command displays information about multicast groups dynamically learned by a VLAN instance.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dynamically learned multicast group information of PE VLAN 2 on 10GE 1/0/1.1.
```
<HUAWEI> display igmp snooping group interface 10GE1/0/1.1 pe-vid 2
Group 234.5.6.7 information:
 Uptime: 00h00m09s
 Expire: 00h02m01s
 Group timer: Exist
 Retran count: 0
 Last member query: No
  Router filter mode: Exclude
 Compat mode: V2
 V1 host timer: Not exist
 V2 host timer: Not exist
 Source last member query: No
 Last member query timer: Not exist
 Last reporter address: --

```

# Display dynamically learned multicast group information of VLAN 10 on 10GE 1/0/1.
```
<HUAWEI> display igmp snooping group interface 10GE 1/0/1 vlan 10
Group 232.1.1.1 information:
 Uptime: 00h04m03s
 Expire: --
 Group timer: Not exist
 Retran count: 0
 Last member query: No
 Router filter mode: Include
 Compat mode: V3
 V1 host timer: Not exist
 V2 host timer: Not exist
 Source last member query: No
 Last member query timer: Not exist
 Last reporter address: 10.110.1.5
 Explicit-tracking state: valid
  Source 10.1.1.2 infor:
   Uptime: 00h04m04s
   Expire: 00h01m06s
   Source timer: Exist
   Retran count: 0
   Source last member query: No

```

# Display dynamically learned multicast group information.
```
<HUAWEI> display igmp snooping group
The group information of port Eth-Trunk1.1(PE:100) on VLAN 123:
Group 226.0.0.1 information:
 Create time: 01:55:44
 Expire time: 00:01:56
 Group timer: Exist
 Retran count: 0
 Last member query: No
 Router filter mode: Exclude
 Compat mode: V2
 V1 host timer: Not exist
 V2 host timer: Not exist
 Source last member query: No
 Last member query timer: Not exist
 Last reporter address: 10.110.1.5

```

# Display brief information about dynamically learned multicast groups.
```
<HUAWEI> display igmp snooping group brief
The group information of port Eth-Trunk1.1(PE:100) on VLAN 123:
   Group Address   Last Reporter   Uptime      Expires
   225.0.0.1       10.110.1.5      00:58:01    00:02:08

```

**Table 1** Description of the **display igmp snooping group** command output
| Item | Description |
| --- | --- |
| Group | Multicast group address. |
| Group timer | Whether a group timer exists. |
| Group Address | Multicast group IP address. |
| Retran count | Number of times group-specific query messages are sent. |
| Last member query | Whether the multicast group has a member. |
| Last member query timer | Whether a timer exists for the interval of querying the last member. |
| Last Reporter | IP address of the host that recently joined the multicast group. |
| Last reporter address | IP address of the host that recently joined the multicast group. |
| Router filter mode | Filtering mode of the multicast group. |
| Compat mode | Multicast group compatibility mode. |
| V2 host timer | Whether a timer exists for IGMPv2-capable hosts. |
| V1 host timer | Whether a timer exists for IGMPv1-capable hosts. |
| Source last member query | Whether to send IGMP Query messages to a specified multicast source/group. |
| Source | Multicast source address. |
| Source timer | Whether a source timer exists. |
| Explicit-tracking state | Whether the host tracking function takes effect.   * valid: The function has taken effect. * invalid: The function does not take effect currently. |
| Create time | Time when the group is created. |
| Expire | Time before the multicast group expires. |
| Expire time | Time before the multicast group expires. |
| Uptime | Time since the multicast group was created. |