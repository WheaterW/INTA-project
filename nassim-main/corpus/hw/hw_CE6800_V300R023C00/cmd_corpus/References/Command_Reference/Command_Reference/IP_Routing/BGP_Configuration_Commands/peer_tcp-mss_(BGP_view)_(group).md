peer tcp-mss (BGP view) (group)
===============================

peer tcp-mss (BGP view) (group)

Function
--------



The **peer tcp-mss** command configures a TCP MSS value used when the local device establishes TCP connections with a peer group.

The **undo peer tcp-mss** command deletes the configured TCP MSS value.



By default, no TCP MSS is configured for the local device to establish TCP connections with a peer group.


Format
------

**peer** *group-name* **tcp-mss** *tcp-mss-number*

**undo peer** *group-name* **tcp-mss**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *tcp-mss-number* | Specifies the TCP MSS value used for TCP connection establishment. | The value is an integer ranging from 176 to 4096, in bytes. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer tcp-mss** command to configure a TCP MSS value used during TCP connection establishment with the specified peer group. The value ranges from 176 to 4096 and is used to fragment TCP packets when the path MTU is unavailable. Such configuration improves network performance.

**Precautions**

If you change the tcp-mss-number value, the TCP connection will be re-established.If both the peer tcp-mss and peer path-mtu auto-discovery commands are run, note the following rules:

* If the local device obtains the path MTU, the smaller value of TCP MSS and path MTU takes effect.
* If the local device fails to obtain the path MTU, TCP MSS takes effect.


Example
-------

# Configure a TCP MSS value for the local device to establish TCP connections with the peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] peer test tcp-mss 200

```