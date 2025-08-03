graceful-restart (OSPF view)
============================

graceful-restart (OSPF view)

Function
--------



The **graceful-restart** command configures a device as a GR helper.

The **undo graceful-restart** command cancels the configuration.



By default, the device does not function as a GR helper.


Format
------

**graceful-restart** [ **helper-role** { { { **ip-prefix** *ip-prefix-name* | **acl-number** *acl-number* | **acl-name** *acl-name* } | **ignore-external-lsa** | **planned-only** } \* } ]

**graceful-restart helper-role never**

**graceful-restart non-ietf**

**undo graceful-restart** [ **helper-role** [ { { **ip-prefix** [ *ip-prefix-name* ] | **acl-number** [ *acl-number* ] | **acl-name** [ *acl-name* ] } | **ignore-external-lsa** | **planned-only** } \* ] ]

**undo graceful-restart helper-role never**

**undo graceful-restart non-ietf**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **helper-role** | Indicates the GR Helper mode. | - |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The name is a string of 1 to 169 case-sensitive characters except spaces. When double quotation marks are used to include the string, spaces are allowed in the string. |
| **acl-number** *acl-number* | Specifies the basic ACL number. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ignore-external-lsa** | Prevents the device from checking Type 5 and Type 7 LSAs. | - |
| **planned-only** | Indicates that the device supports only planned GR. | By default, the device supports both planned GR and unplanned GR. |
| **never** | Indicates that the router does not support the Helper mode. | - |
| **non-ietf** | Enables the non-IETF mode. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an OSPF process is restarted through GR, the restarter and the helper reestablish the neighbor relationship, exchange routing information, synchronize LSDBs, and update routing tables and FIBs to ensure network stability.

**Prerequisites**

The Opaque-LSA capability has been enabled using the **opaque-capability enable** command.

**Precautions**

The graceful-restart non-ietf and graceful-restart [ helper-role { { { { ip-prefix | acl-number | acl-name } | ignore-external-lsa | planned-only } \* } | never } ] commands are mutually exclusive.If the GR restarter fails to complete GR within 1800s, the GR helper in non-IETF mode exits the helper mode.In non-IETF mode, only broadcast interfaces can be simulated as P2P interfaces.


Example
-------

# Configure a device as an OSPF GR helper and configure the helper to support only planned GR.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] opaque-capability enable
[*HUAWEI-ospf-1] graceful-restart helper-role planned-only

```