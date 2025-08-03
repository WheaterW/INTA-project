mac-in-mac (load balancing profile view)
========================================

mac-in-mac (load balancing profile view)

Function
--------



The **mac-in-mac** command configures a load balancing mode for MAC-in-MAC packets in a load balancing profile.

The **undo mac-in-mac** command restores the default load balancing mode of MAC-in-MAC packets in a load balancing profile.



By default, MAC-in-MAC packets are load balanced based on outer-header.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-in-mac** { **outer-header** | **inner-header** }

**undo mac-in-mac** [ **outer-header** | **inner-header** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **outer-header** | Specifies load balancing based on the outer header. | - |
| **inner-header** | Specifies load balancing based on the inner header. | - |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

For MAC-in-MAC packets,you can run the mac-in-mac command to configure hash calculation based on the outer or inner header in the specified load balancing profile.


Example
-------

# Configure load balancing for MAC-in-MAC packets based on inner-header in a load balancing profile.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile abc
[*HUAWEI-load-balance-profile-abc] mac-in-mac inner-header

```