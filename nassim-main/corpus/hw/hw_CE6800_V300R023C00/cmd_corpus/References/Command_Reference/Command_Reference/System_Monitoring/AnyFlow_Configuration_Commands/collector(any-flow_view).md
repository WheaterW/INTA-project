collector(any-flow view)
========================

collector(any-flow view)

Function
--------



The **collector** command binds an analyzer with a specified ID in the Any-Flow view.

The **undo collector** command unbinds an analyzer with a specified ID in the Any-Flow view.



By default, no analyzer is bound in the Any-Flow view.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**collector collect** *collect-id*

**undo collector collect** [ *collect-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *collect-id* | Specifies the analyzer ID. | The value is an integer ranging from 1 to 5. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To use an analyzer to collect traffic statistics and detect and analyze abnormal traffic, run the collector command in the Any-Flow view to bind an analyzer with a specified ID.

**Prerequisites**

An analyzer has been created and analyzer rules have been configured.

**Precautions**

If the collector command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Configure analyzer 3 and bind it in the Any-Flow view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] commit
[~HUAWEI-vpn-instance-vpn1] ipv4-family
[~HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1] commit
[~HUAWEI-vpn-instance-vpn1-ipv6] quit
[~HUAWEI-vpn-instance-vpn1] quit
[~HUAWEI] collector collect 3
[*HUAWEI-collect-3] source ip 192.168.1.2 export host ip 10.0.0.2 udp-port 100 vpn-instance vpn1
[*HUAWEI-collect-3] quit
[*HUAWEI] any-flow
[*HUAWEI-any-flow] collector collect 3

```