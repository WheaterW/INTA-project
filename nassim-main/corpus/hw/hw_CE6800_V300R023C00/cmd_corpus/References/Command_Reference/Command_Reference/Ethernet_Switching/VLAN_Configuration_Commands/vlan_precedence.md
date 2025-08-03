vlan precedence
===============

vlan precedence

Function
--------



The **vlan precedence** command configures an interface to prefer MAC address-based VLAN classification or IP subnet-based VLAN classification.

The **undo vlan precedence** command restores the default configuration.



By default, MAC address-based VLAN classification is preferred.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vlan precedence** { **ip-subnet-vlan** | **mac-vlan** }

**undo vlan precedence**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-subnet-vlan** | Prefers IP subnet-based VLAN classification. | - |
| **mac-vlan** | Prefers MAC address-based VLAN classification. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MAC address-based VLAN classification and IP subnet-based VLAN classification have the same priority.By default, MAC address-based VLAN classification has a higher priority than IP subnet-based VLAN classification. To enable an interface to prefer IP subnet-based VLAN classification, run the **vlan precedence** command.

**Precautions**

Port-based VLAN classification has the lowest priority, but is most commonly used.


Example
-------

# Configure an interface to prefer IP subnet-based VLAN classification.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] undo shutdown
[*HUAWEI-100GE1/0/1] vlan precedence ip-subnet-vlan

```