timer retry
===========

timer retry

Function
--------



The **timer retry** command sets the interval for retrying to set up a Multicast Source Discovery Protocol (MSDP) peer relationship.

The **undo timer retry** command restores the default value.



By default, the interval for retrying to set up an MSDP peer relationship is 30 seconds.


Format
------

**timer retry** *timeRetryInterval*

**undo timer retry** [ *timeRetryInterval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timeRetryInterval* | Specifies the interval for retrying to set up an MSDP peer relationship. | The value is an integer ranging from 1 to 60, in seconds. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The TCP connection needs to be set up between the MSDP peers. MSDP requires the peer with the larger IP address to listen at the port 639, and the peer with the smaller IP address to start a connection. If the connection fails, the peer restarts the connection after a period of time. Such a period of time is called interval retrying to set up an MSDP peer relationship.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.The status of the TCP connection between MSDP peers is Up.


Example
-------

# In the public network instance, set the interval for retrying to set up an MSDP peer relationship to 60 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] timer retry 60

```