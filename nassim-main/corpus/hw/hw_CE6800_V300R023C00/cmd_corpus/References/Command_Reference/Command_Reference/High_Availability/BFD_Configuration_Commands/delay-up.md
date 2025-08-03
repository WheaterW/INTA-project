delay-up
========

delay-up

Function
--------



The **delay-up** command sets the delay before a BFD session goes Up.

The **undo delay-up** command deletes the configured delay.



By default, no delay is set before a BFD session goes Up.


Format
------

**delay-up** *seconds*

**undo delay-up** [ *seconds* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *seconds* | Specifies the time that elapses when the BFD session is delayed to become Up. | The value is an integer ranging from 1 to 600, in seconds. The default value is 0, indicating that the BFD session immediately goes Up. |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In scenarios in which a Huawei device and a non-Huawei device are connected, if the Huawei device or its interface board restarts, traffic needs to be switched from an active link to a standby link. After the Huawei device or its interface board successfully restarts, the traffic needs to be switched from the standby link to the active link. In this case, the BFD session on the active link is Up. On certain non-Huawei devices, a link switchover is performed according to the BFD session status, the route to the Huawei devices may not be generated on the non-Huawei devices. As a result, traffic is dropped. To prevent this problem, the BFD session can be created and go Up through the negotiation after a delay.

**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view.

**Configuration Impact**

This command takes effect only on the configuration of the BFD sessions to be established but does not affect the established BFD sessions.

**Precautions**

The **delay-up** command applies only to scenarios in which Huawei devices interwork with non-Huawei devices and takes effect only after the Huawei device or its interface board restarts.If the secondary link fails after traffic has been switched to it from the primary link, traffic may fail to be switched back because the BFD session that monitors the primary link is in the delay-up state. In this case, you are advised to configure a best-effort path.


Example
-------

# Set the delay before a BFD session goes Up to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] delay-up 120

```