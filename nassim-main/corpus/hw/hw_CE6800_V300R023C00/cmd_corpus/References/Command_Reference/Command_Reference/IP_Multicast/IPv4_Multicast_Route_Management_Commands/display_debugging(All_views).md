display debugging(All views)
============================

display debugging(All views)

Function
--------



The **display debugging** command displays the debugging status.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display debugging** { **pim** | **pim6** | **igmp** | **mld** | **msdp** | **snpg** }

For CE6885-LL (low latency mode):

**display debugging** { **pim** | **igmp** | **msdp** | **snpg** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pim** | PIM protocol. | - |
| **pim6** | PIM6 protocol.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **igmp** | IGMP protocol. | - |
| **mld** | MLD protocol.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **msdp** | MSDP protocol. | - |
| **snpg** | SNPG. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

* When a large amount of information is output, you can run the **display debugging pim6** command to view information about enabled PIM IPv6 debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* If a large amount of information is output, run the **display debugging mvpn** command to check information about enabled NG MVPN debugging functions. You can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging mld** command to view information about enabled MLD debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging msdp** command to view information about enabled MSDP debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging pim** command to view information about enabled PIM debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging igmp** command to view information about enabled IGMP debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* If a large amount of information is output, run the **display debugging mvpn6** command to check information about enabled IPv6 NG MVPN debugging functions. You can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging md** command to view information about enabled MD debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.

* When a large amount of information is output, you can run the **display debugging pim6** command to view information about enabled PIM IPv6 debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging mld** command to view information about enabled MLD debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging pim** command to view information about enabled PIM debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.
* When a large amount of information is output, you can run the **display debugging igmp** command to view information about enabled IGMP debugging functions. Then you can disable some unnecessary debugging functions to minimize the debugging information output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about current PIM debugging functions.
```
<HUAWEI> display debugging pim
PIM(_public_) nsr message [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) nsr event [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) bfd event debugging switch is on
PIM(_public_) bfd delete debugging switch is on
PIM(_public_) bfd create debugging switch is on
PIM(_public_) rp receive debugging switch is on
PIM(_public_) rp send debugging switch is on
PIM(_public_) routing-table [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) register [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) neighbor receive [ Filter:(source=*) ] debugging switch is on
PIM(_public_) neighbor send [ Filter:(source=*) ] debugging switch is on
PIM(_public_) msdp [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) join-prune receive [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) join-prune send [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) event [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) assert receive [ Filter:(source=*, group=*) ] debugging switch is on
PIM(_public_) assert send [ Filter:(source=*, group=*) ] debugging switch is on

```

# Display information about all IGMP snooping debugging functions.
```
<HUAWEI> display debugging snpg
IGMP snooping nsr event [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on
IGMP snooping nsr message [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on
IGMP snooping packet [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on
IGMP snooping timer [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on
IGMP snooping leave [ Filter:(group=*) , interface=all-interface, VPN-instance=* ] debugging switch is on
IGMP snooping report [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on
IGMP snooping query [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on
IGMP snooping event [ Filter:(source=*, group=*) , interface=all-interface , VPN-instance=* ] debugging switch is on

```

**Table 1** Description of the **display debugging(All views)** command output
| Item | Description |
| --- | --- |
| switch | Indicates whether the debugging function is enabled. On indicates that the function is enabled. |