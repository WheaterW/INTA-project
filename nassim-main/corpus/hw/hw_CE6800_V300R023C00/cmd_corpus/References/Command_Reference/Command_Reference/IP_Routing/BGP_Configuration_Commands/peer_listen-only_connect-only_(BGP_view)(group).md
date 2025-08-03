peer listen-only connect-only (BGP view)(group)
===============================================

peer listen-only connect-only (BGP view)(group)

Function
--------



The **peer listen-only** command enables a peer to listen to connection requests but not to send connection requests.

The **undo peer listen-only** command restores the default setting.

The **peer connect-only** command enables a peer to send connection requests but not to accept connection requests.

The **undo peer connect-only** command restores the default setting.



By default, a peer group listens to and accepts connection requests and sends connection requests.


Format
------

**peer** *group-name* { **listen-only** | **connect-only** }

**undo peer** *group-name* { **listen-only** | **connect-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a peer group to listen to connection requests but not to send connection requests, run the **peer listen-only** command.To enable a peer group to send connection requests but not to accept connection requests, run the **peer connect-only** command.

**Configuration Impact**

If the peer listen-only and **peer connect-only** commands are both run, the latest configuration overrides the previous one.

**Precautions**

The **peer connect-only** command or the **peer listen-only** command cannot be run on both devices that are peers of each other. Otherwise, the peer relationship cannot be established.


Example
-------

# Enable a peer group to send connection requests but reject connection requests.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] peer test connect-only

```