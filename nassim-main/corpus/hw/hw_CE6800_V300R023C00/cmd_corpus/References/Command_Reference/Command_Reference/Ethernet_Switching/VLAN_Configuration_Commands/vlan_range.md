vlan range
==========

vlan range

Function
--------



The **vlan range** command creates a temporary VLAN range and displays the VLAN-range view.



By default, no temporary VLAN ranges are created.


Format
------

**vlan range** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the end VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a great number of VLANs need to be created on devices on a large Layer 2 network, the configuration and maintenance workload is heavy, and configuration inconsistencies may occur. To improve maintenance efficiency and simply configurations, run the **vlan range** command to create a temporary VLAN range. You can then configure services in the VLAN-range view. After services are configured, they are delivered in batches to all the VLANs in the VLAN range.

**Precautions**

The **vlan range** command configuration is not saved in the configuration file. After services are configured and committed in the VLAN-range view, the service configurations are saved for all the VLANs in the VLAN range.A VLAN range contains a maximum of 512 VLANs.


Example
-------

# Create a VLAN range 10-20 and enter the VLAN-range view.
```
<HUAWEI> system-view
[~HUAWEI] vlan range 10 to 20

```