peer (RIP view)
===============

peer (RIP view)

Function
--------



The **peer** command specifies the IP address of a RIP neighbor on a non-broadcast multiple access (NBMA) network.

The **undo peer** command deletes the specified neighbor IP address.



By default, the IP address of a RIP neighbor on an NBMA network is not specified.


Format
------

**peer** *peer-address*

**undo peer** *peer-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the neighbor IP address. | The value must be the address of a natural network segment, in dotted decimal notation. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the peer command is configured, Update packets are sent to the neighbor in unicast mode.


Example
-------

# Specify the IP address of the neighbor as 10.0.0.1.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] peer 10.0.0.1

```