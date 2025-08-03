reset ip ip-prefix
==================

reset ip ip-prefix

Function
--------



The **reset ip ip-prefix** command resets the statistics of the specified IPv4 prefix list.

If ip-prefix-name is not specified, you can reset the statistics of all the IPv4 prefix lists.




Format
------

**reset ip ip-prefix** [ *pfName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pfName* | Specifies the name of the IPv4 prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To reset timers in permit and deny modes of an IPv4 prefix list, run the reset ip ip-prefix command.




Example
-------

# Reset the statistics of the specified IPv4 prefix list.
```
<HUAWEI> reset ip ip-prefix abc

```