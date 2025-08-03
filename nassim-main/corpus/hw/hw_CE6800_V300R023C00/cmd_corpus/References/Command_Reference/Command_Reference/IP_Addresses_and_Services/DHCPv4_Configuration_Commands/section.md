section
=======

section

Function
--------

The **section** command configures the IP address segment in an IP address pool.

The **undo section** command deletes the configured IP address segment in an IP address pool.

By default, the IP address segment in an IP address pool is not configured.



Format
------

**section** *section-id* *start-address* [ *end-address* ]

**undo section** *section-id*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *section-id* | Specifies the ID of the address segment in the IP address pool. | The value is an integer ranging from 0 to 255. |
| *start-address* | Specifies the start IP address of an address segment. | The value is in dotted decimal notation. |
| *end-address* | Specifies the end IP address of the address segment.  The end IP address must be larger than the start IP address. If the end IP address is not entered, there is only one address in the address segment. | The value is in dotted decimal notation. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

An IP address pool consists of one or more IP address segments. The IP addresses on each address segment cannot overlap. If both network and section are configured, the available address range is the same as that configured in section.



Example
-------

# Configure an IP address segment 10.1.1.10-10.1.1.15 with the ID 0 for the IP address pool abc.
```
<HUAWEI> system-view
[~HUAWEI] ip pool abc
[*HUAWEI-ip-pool-abc] network 10.1.1.1 mask 24
[*HUAWEI-ip-pool-abc] section 0 10.1.1.10 10.1.1.15

```