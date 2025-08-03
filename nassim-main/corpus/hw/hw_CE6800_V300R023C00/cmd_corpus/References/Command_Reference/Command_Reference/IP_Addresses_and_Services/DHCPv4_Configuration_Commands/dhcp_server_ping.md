dhcp server ping
================

dhcp server ping

Function
--------

The **dhcp server ping** command configures the maximum number of ping packets that a DHCP server can send and the maximum timeout period of each ping reply.

The **undo dhcp server ping** command restores the default configuration.

By default, the DHCP server sends 2 ping packets and the maximum response time is 500 ms.



Format
------

**dhcp server ping** { **packet** *number* | **timeout** *milliseconds* } \*

**undo dhcp server ping** { **packet** | **timeout** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet** *number* | Specifies the maximum number of ping packets to be sent. | The value is an integer ranging from 0 to 10. The value 0 indicates that no ping operation is performed. |
| **timeout** *milliseconds* | Specifies the maximum response time of a ping packet. | The value is an integer that ranges from 0 to 10000, in milliseconds. The value 0 indicates that no ping operation is performed. |




Views
-----

System view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. To prevent IP address conflicts caused by repeated IP address allocation, run the **dhcp server ping** command to enable the DHCP server to send ping packets to detect the IP address usage before allocating an IP address to a client. Address detection indicates whether the DHCP server can receive a ping response within a specified period. If there is no response after a certain period of time, the DHCP server continues to send ping packets to this address until the number of ping packets reaches the maximum value. If there is still no response, the DHCP server considers that the IP address is not in use. This ensures that the IP address assigned to the client is unique.

**Prerequisites**

DHCP has been enabled using the **dhcp enable** command.



Example
-------

# Set the maximum number of ping packets to 3 and the maximum response time to 400 ms.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp server ping packet 3
[*HUAWEI] dhcp server ping timeout 400

```