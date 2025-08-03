dei enable
==========

dei enable

Function
--------



The **dei enable** command maps the drop eligible indicator (DEI) field in a VLAN tag to the drop priority.

The **undo dei enable** command cancels the configuration of the DEI field in a VLAN tag as the drop priority.



By default, the DEI field in a VLAN tag is not used as the drop priority.


Format
------

**dei enable**

**undo dei enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The DEI is also called the Canonical Format Indicator (CFI) field in a VLAN tag and its value is 0 or 1. The DEI field in a VLAN tag is used as the drop priority of packets in certain situations. When the rate of packets on certain devices exceeds the CIR value, the DEI field is set to 1. In this case, the drop priority of the packets is high. When congestion occurs, subsequent devices first discard the packets whose DEI field is 1.


Example
-------

# Configure the DEI field in the VLAN tag as the drop priority on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dei enable

```