display rip neighbor last-nbr-down
==================================

display rip neighbor last-nbr-down

Function
--------



The **display rip neighbor last-nbr-down** command displays information about the last neighbors that went Down in a RIP process.

The **display ripng neighbor last-nbr-down** command displays information about the last neighbors that went Down in a RIPng process.




Format
------

**display rip** *process-id* **neighbor** **last-nbr-down**

**display ripng** *process-id* **neighbor** **last-nbr-down**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays neighbors of a specified process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about the last 10 RIP neighbors that went Down and the reason why they went Down, run the **display rip neighbor last-nbr-down** command.To check information about the last 10 RIPng neighbors that went Down and the reasons why they went Down, run the **display ripng neighbor last-nbr-down** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the last neighbors that went Down in a RIPng process.
```
<HUAWEI> display ripng 1 neighbor last-nbr-down
Neighbor down index              : 1
Neighbor Link local Address      : FE80::2E0:B7FF:FE5B:8242
Interface                        : 100GE1/0/1
Reason for Neighbor down         : Interface Down
Time at which neighbor went down : 2011-06-02 12:03:40+03:00 DST

```

# Display information about the last neighbors that went Down in a RIP process.
```
<HUAWEI> display rip 1 neighbor last-nbr-down
Neighbor down index              : 1
Neighbor IP Address              : 2.2.2.2
Interface                        : 100GE1/0/1
Reason for Neighbor down         : Interface Down
Time at which neighbor went down : 2013-05-22 11:06:09-08:00

```

**Table 1** Description of the **display rip neighbor last-nbr-down** command output
| Item | Description |
| --- | --- |
| Neighbor down index | Index of the neighbor that went Down. |
| Neighbor Link local Address | IPv6 address of an interface connected to a neighbor. |
| Neighbor IP Address | IP address of a neighbor. |
| Interface | Interface on which a neighbor was present. |
| Reason for Neighbor down | Reason why a neighbor went Down:   * Interface Down: The interface went Down. * Configuration Change: The configuration changed. * Time Out (Normal): The neighbor timed out expectedly. * Time Out (Message Processing Failed): The neighbor timed out because packets failed to be forwarded. * Received Worst Metric Routes: Routes with the worst metrics were received. |
| Time at which neighbor went down | Time when a neighbor went Down. |