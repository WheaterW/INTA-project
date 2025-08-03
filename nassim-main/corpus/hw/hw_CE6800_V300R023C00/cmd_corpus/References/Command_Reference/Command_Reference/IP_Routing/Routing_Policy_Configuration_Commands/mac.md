mac
===

mac

Function
--------



The **mac** command adds a MAC address to a MAC address list.

The **undo mac** command deletes a MAC address from a MAC address list.



By default, no MAC address is added to a MAC address list.


Format
------

**mac** *macValue*

**undo mac** *macValue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *macValue* | Specifies a MAC address. | The value is in the format of H-H-H, in which each H is a 4-digit hexadecimal number, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The value cannot be an all-F, all-zero, or multicast MAC address. |



Views
-----

MAC set view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A MAC address list-based filtering policy can be configured to filter EVPN routes. To add a MAC address to the MAC address list, run the **mac** command.




Example
-------

# Add the MAC address 1-1-1 to a MAC address list.
```
<HUAWEI> system-view
[~HUAWEI] filter-list mac abc
[~HUAWEI-mac-list-abc] mac 1-1-1

```