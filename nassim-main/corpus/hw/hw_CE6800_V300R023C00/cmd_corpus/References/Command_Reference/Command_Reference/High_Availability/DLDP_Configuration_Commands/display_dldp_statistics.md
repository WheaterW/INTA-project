display dldp statistics
=======================

display dldp statistics

Function
--------



The **display dldp statistics** command displays statistics about DLDPDUs on a specific interface.




Format
------

**display dldp statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about DLDPDUs on a specific port.   * If a port is not specified, DLDPDUs on all DLDP-enabled ports are displayed. * If a port is specified, DLDPDUs on a specific port are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If DLDP negotiation fails, run the display dldp statistics command to view statistics about DLDPDUs. The display dldp statistics command displays statistics about DLDPDUs on a specific interface after the preceding statistics about this interface are cleared using the **reset dldp statistics** command.

**Prerequisites**

DLDP has been enabled both globally and on interfaces using the **dldp enable** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about all DLDPDUs on the devices.
```
<HUAWEI> display dldp statistics
2022-12-02 17:16:10.586

Interface  100GE1/0/1
Packets sent                           : 3977
Packets received
  Total                                : 3976
  Invalid version                      : 0
  Invalid interval                     : 0
  Invalid authentication               : 0
  Invalid operation code               : 0
  Loop packets                         : 0
Statistics last cleared                : never

Interface  100GE1/0/4
Packets sent                           : 3966
Packets received
  Total                                : 3966
  Invalid version                      : 0
  Invalid interval                     : 0
  Invalid authentication               : 0
  Invalid operation code               : 0
  Loop packets                         : 0
Statistics last cleared                : 2022-12-02 11:45:03

```

# Display statistics about DLDP packets on 100GE 1/0/1.
```
<HUAWEI> display dldp statistics interface 100GE 1/0/1
2022-12-02 17:15:23.26

Interface  100GE1/0/1
Packets sent                           : 3968
Packets received
  Total                                : 3966
  Invalid version                      : 0
  Invalid interval                     : 0
  Invalid authentication               : 0
  Invalid operation code               : 0
  Loop packets                         : 0
Statistics last cleared                : never

```

**Table 1** Description of the **display dldp statistics** command output
| Item | Description |
| --- | --- |
| Interface | Name of a DLDP-enabled port. |
| Packets sent | Total number of DLDPDUs to be sent. |
| Packets received | Number of received DLDPDUs. |
| Total | Total number of received DLDPDUs. |
| Invalid version | Number of received DLDPDUs carrying incorrect versions. |
| Invalid interval | Number of received DLDPDUs carrying incorrect intervals. |
| Invalid authentication | Number of DLDPDUs that fail to be authenticated. |
| Invalid operation code | Number of received DLDPDUs carrying error code fields. |
| Loop packets | Total number of received DLDPDUs that are transmitted in a loop. |
| Statistics last cleared | Time when the last statistics were cleared. |