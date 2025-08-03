eth-tag
=======

eth-tag

Function
--------



The **eth-tag** command adds an Ethernet tag value to an Ethernet tag list.

The **undo eth-tag** command deletes an Ethernet tag value from an Ethernet tag list.



By default, no Ethernet tag value is added to an Ethernet tag list.


Format
------

**eth-tag** *ethTagValue*

**undo eth-tag** *ethTagValue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ethTagValue* | Specifies an Ethernet tag value. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

Eth-Tag set view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On an EVPN, an Ethernet tag list can be applied to an if-match clause to control route advertisement and receiving. To add an Ethernet tag value to an Ethernet tag list, run the **eth-tag** command.




Example
-------

# Add the Ethernet tag value 10 to an Ethernet tag list.
```
<HUAWEI> system-view
[~HUAWEI] filter-list eth-tag ethtag
[*HUAWEI-eth-tag-list-ethtag] eth-tag 10

```