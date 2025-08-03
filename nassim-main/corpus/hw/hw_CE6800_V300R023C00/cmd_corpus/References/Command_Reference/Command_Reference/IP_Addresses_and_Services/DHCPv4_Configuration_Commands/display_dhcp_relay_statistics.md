display dhcp relay statistics
=============================

display dhcp relay statistics

Function
--------



The **display dhcp relay statistics** command displays message statistics on DHCP relay agents connected to DHCP servers in a specified DHCP server group.




Format
------

**display dhcp relay statistics** [ **server-group** *dhcp-server-group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **server-group** *dhcp-server-group-name* | Displays message statistics on DHCP relay agents connected to DHCP servers in a specified DHCP server group.  If this parameter is not specified, message statistics on DHCP relay agents connected to all DHCP servers are displayed. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, and can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot use "-" and "--" as names. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Run the **display dhcp relay statistics** command to check whether the client is correctly configured or the network is connected.

* display dhcp relay statistics server-group *dhcp-server-group-name*: displays message statistics on DHCP relay agents connected to DHCP servers in a DHCP server group. You need to specify the name of the DHCP server group. You can run the reset dhcp relay statistics server-group *group-name*command to clear the statistics.
* display dhcp relay statistics: displays message statistics on all DHCP relay agents. You can run the **reset dhcp relay statistics** command to clear the statistics.

**Follow-up Procedure**

If packet statistics on a DHCP relay agent are incorrect, run the reset dhcp relay statistics [ server-group *group-name*] command to clear the existing packet statistics on the DHCP relay agent.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display message statistics on a DHCP relay agent.
```
<HUAWEI> display dhcp relay statistics
  The statistics of DHCP RELAY:
    DHCP packets received from clients    : 0
        DHCP DISCOVER packets received    : 0
        DHCP REQUEST packets received     : 0
        DHCP RELEASE packets received     : 0
        DHCP INFORM packets received      : 0
        DHCP DECLINE packets received     : 0
    DHCP packets sent to clients          : 0
        Unicast packets sent to clients   : 0
        Broadcast packets sent to clients : 0
    DHCP packets received from servers    : 0
        DHCP OFFER packets received       : 0
        DHCP ACK packets received         : 0
        DHCP NAK packets received         : 0
    DHCP packets sent to servers          : 0
    DHCP Bad packets received             : 0

```

**Table 1** Description of the **display dhcp relay statistics** command output
| Item | Description |
| --- | --- |
| DHCP packets received from clients | DHCP messages received from clients. |
| DHCP DISCOVER packets received | DHCP Discover messages received from clients. |
| DHCP REQUEST packets received | DHCP Request messages received from clients. |
| DHCP RELEASE packets received | DHCP Release messages received from clients. |
| DHCP INFORM packets received | DHCP Inform messages received from clients. |
| DHCP DECLINE packets received | DHCP Decline messages received from clients. |
| DHCP packets sent to clients | DHCP messages sent to clients. |
| DHCP packets received from servers | DHCP messages received from servers. |
| DHCP OFFER packets received | DHCP Offer messages received from servers. |
| DHCP ACK packets received | DHCP ACK messages received from servers. |
| DHCP NAK packets received | DHCP NAK messages received from servers. |
| DHCP packets sent to servers | DHCP messages sent to servers. |
| DHCP Bad packets received | DHCP error messages received. |
| Unicast packets sent to clients | Unicast packets sent to clients. |
| Broadcast packets sent to clients | Broadcast packets sent to clients. |