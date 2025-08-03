display rip neighbor
====================

display rip neighbor

Function
--------



The **display rip neighbor** command displays neighbor information.

The **display ripng neighbor** command displays information about RIPng neighbors.




Format
------

**display rip** *process-id* **neighbor** [ **neighbor-address** *neighbor-address* ] [ **verbose** ]

**display ripng** *process-id* **neighbor** [ **neighbor-address** *neighbor-address* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id. | The value is an integer ranging from 1 to 4294967295. |
| **neighbor-address** *neighbor-address* | Specifies the IP address of a neighbor. | The value is in dotted decimal notation. |
| **verbose** | Displays detailed information about a neighbor. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After basic RIP functions are configured, running the **display rip neighbor** command displays information about the established neighbor relationship. If the neighbor relationship is not established as required, check the neighbor configuration.If verbose is specified, you can also view the number of routes in active, holddown, and garbage states.

**Precautions**

If the directly connected network segment interface between two directly connected devices has been configured with the **rip enable** command, although the RIP process has been enabled on the interface at this time, the corresponding neighbor information cannot be viewed through the **display rip neighbor** command. If you want to view the neighbor information of two devices, you need to configure the **rip enable** command on the other interface (not belonging to the same network segment) of one of the devices to enable the RIP process of that interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about neighbors in RIPng process 1.
```
<HUAWEI> display ripng 1 neighbor

 Neighbor : FE80::A0A:201:1 100GE/1/0
    Protocol : RIPNG

```

# Display detailed information about the neighbor in RIPng process 1.
```
<HUAWEI> display ripng 1 neighbor verbose

 Neighbor : FE80::A0A:201:1 100GE/1/0
    Protocol : RIPNG
    Number of Active routes      : 2
    Number of routes in holddown : 0
    Number of routes in garbage  : 0

```

# Display detail information of all neighbors in RIP 1.
```
<HUAWEI> display rip 1 neighbor verbose
----------------------------------------------------------------
IP Address         Interface Type          Type       Last Heard Time
----------------------------------------------------------------
10.1.1.2           100GE1/0/1    RIPV2      0:0:37
Number of RIP routes          :1
Number of routes in holddown  : 0
Number of routes in garbage   : 0
Last Received Sequence Number : 0x0

```

**Table 1** Description of the **display rip neighbor** command output
| Item | Description |
| --- | --- |
| Neighbor | IPv6 address and interface type of the interface of the neighbor. |
| Protocol | Routing protocol running on the interface. |
| Number of Active routes | Number of routes in the active state. |
| Number of routes in holddown | Number of routes in the holddown state. |
| Number of routes in garbage | Number of routes in the garbage state. |
| Number of RIP routes | Number of RIP routes. |
| IP Address | IP address of the neighboring interface. |
| Interface Type | Interface type and number of the interface. |
| Type | Routing protocol used to establish an adjacency with a neighbor:   * RIPV1. * RIPV2. * RIP V1 Compatible. |
| Last Heard Time | Time since the last time packets are received from neighbors. |
| Last Received Sequence Number | Sequence number of the last received RIP packet. |