display system tcam acl group-information
=========================================

display system tcam acl group-information

Function
--------



The **display system tcam acl group-information** command displays supported matching fields and actions when a traffic policy is applied in each view.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display system tcam acl group-information** { **interface-view** { **port** | **vlanif** | **eth-trunk** | **l3-subif** | **l2-subif** } | **vlan-view** | **vpn-view** | **global-view** | **qos-group-view** **member** { **port** | **vlanif** | **l3-subif** | **l2-subif** | **vlan** | **ip** } } **inbound** **slot** *slot-id*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display system tcam acl group-information** { **interface-view** { **port** | **vlanif** | **eth-trunk** | **l3-subif** | **l2-subif** } | **vlan-view** | **global-view** | **qos-group-view** **member** { **port** | **vlanif** | **l3-subif** | **vlan** } } **outbound** **slot** *slot-id*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display system tcam acl group-information** { **interface-view** **vbdif** | **bridge-domain-view** } **inbound** **slot** *slot-id*

**display system tcam acl group-information** { **interface-view** **vbdif** | **bridge-domain-view** } **outbound** **slot** *slot-id*

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display system tcam acl group-information** { **interface-view** { **port** | **vlanif** | **eth-trunk** | **l3-subif** | **l2-subif** } | **vlan-view** | **vpn-view** | **global-view** | **qos-group-view** **member** { **port** | **vlanif** | **l3-subif** | **l2-subif** | **vlan** } } **inbound** **slot** *slot-id*

For CE6885-LL (low latency mode):

**display system tcam acl group-information** { **interface-view** { **port** | **vlanif** | **eth-trunk** } | **vlan-view** | **vpn-view** | **global-view** | **qos-group-view** **member** { **port** | **vlanif** | **vlan** } } **inbound** **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface-view** | Indicates that a traffic policy is applied to the interface view. | - |
| **port** | Indicates that a traffic policy is applied to the specified PORT view. | - |
| **vlanif** | Indicates that a traffic policy is applied to the specified VLANIF view. | - |
| **eth-trunk** | Indicates that a traffic policy is applied to the specified Eth-Trunk view. | - |
| **l3-subif** | Indicates that a traffic policy is applied to the Layer 3 sub-interface view.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vlan-view** | Indicates that a traffic policy is applied to the VLAN view. | - |
| **bridge-domain-view** | Indicates that a traffic policy is applied to the BD view.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vpn-view** | Indicates that a traffic policy is applied to the VPN instance view. | - |
| **global-view** | Indicates that a traffic policy is applied to the system view. | - |
| **inbound** | Indicates that a traffic policy is applied to the inbound direction. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **outbound** | Indicates that a traffic policy is applied to the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **l2-subif** | Indicates that a traffic policy is applied to the Layer 2 sub-interface view.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **qos-group-view** | Indicates that a traffic policy is applied to the view of the QoS group view. | - |
| **member** | QoS group view member information. | - |
| **vlan** | Indicates that a traffic policy is applied to the specified VLAN view. | - |
| **ip** | Indicates that a traffic policy is applied to the specified IP view.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **vbdif** | Indicates that a traffic policy is applied to the specified VBDIF view.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command is used to display supported matching fields and actions when a traffic policy is applied in each view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display supported matching fields and actions when a traffic policy is applied in the Ethernet view.
```
<HUAWEI> display system tcam acl group-information interface-view port inbound slot 1
--------------------------------------------------------------------------------
Group  : 29                                                                     
--------------------------------------------------------------------------------
Key    : DSTMAC,SRCMAC,ETHERTYPE,OUTERVLANID,OUTERPRI,IPV4,IPV6,GID,GPORT,VDCID,
         UNIT                                                                   
Action : PERMIT,DENY,REDIRECT_GPORT,REDIRECT_COPYTOCP,REDIRECT_TOCP,REDIRECT_VRF
         ,REDIRECT_REINDEX,REDIRECT_VSI,REDIRECT_VLL,REDIRECT_NHP,REDIRECT_NST,V
         ALID,CAR_STAT_CMD,CAR_FIRSTCAR,CAR_SECONDCAR,ACL_STAT,ANYFLOW          
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display system tcam acl group-information** command output
| Item | Description |
| --- | --- |
| Group | Group ID. |
| Key | Supported matching field. |
| Action | Supported action. |