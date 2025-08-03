ssm-mapping
===========

ssm-mapping

Function
--------



The **ssm-mapping** command configures static source-specific multicast (SSM) mappings.

The **undo ssm-mapping** command deletes static SSM mappings.



By default, no SSM mappings are configured.


Format
------

**ssm-mapping** *group-address* { *mask* | *mask-length* } *source-address*

**undo ssm-mapping** { *group-address* { *mask* | *mask-length* } [ *source-address* ] | **static** **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies a multicast group address. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| *mask* | Specifies the mask of a multicast group address. | The value ranges from 224.0.1.0 to 255.255.255.255, in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a multicast group address. | The value is an integer that ranges from 5 to 32. |
| *source-address* | Specifies a multicast source address. | The value is in dotted decimal notation. |
| **static** | Deletes static SSM mappings. | - |
| **all** | Deletes all SSM mappings. | - |



Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The default SSM group address range is from 232.0.0.0 to 232.255.255.255. If a host supports only IGMPv1/v2 Report messages, the host cannot join groups in the SSM group address range. If you want an IGMPv1/v2 host to join groups in the SSM group address range, run the ssm-mapping command configure static SSM mappings.Group addresses not in the SSM group address range apply to the ASM model.The configured SSM source/group address mapping entries take effect only after the igmp ssm-mapping enable command is run on the interface.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

The ssm-mapping command can be repeatedly run to configure multiple static SSM mappings. New configurations take effect without overriding the previous one.Running the **undo ssm-mapping static all** command deletes all static SSM mappings. Therefore, exercise caution when using this command.


Example
-------

# In the public network instance, configure an SSM mapping between the source address 10.1.6.0 and the group address 225.5.5.5/24.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] ssm-mapping 225.5.5.5 24 10.1.6.1

```