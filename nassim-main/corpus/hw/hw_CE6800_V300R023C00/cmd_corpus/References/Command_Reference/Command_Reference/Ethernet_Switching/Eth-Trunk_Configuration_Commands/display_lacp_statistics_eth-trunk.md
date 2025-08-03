display lacp statistics eth-trunk
=================================

display lacp statistics eth-trunk

Function
--------



The **display lacp statistics eth-trunk** command displays statistics about LACPDUs on an Eth-Trunk interface in static LACP mode or on its member interface.




Format
------

**display lacp statistics eth-trunk** [ *trunk-id* [ **interface** { *interface-type* *interface-number* | *interface-name* } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk interface in static LACP mode. | The value is an integer in the range from 0 to 1023. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **interface** *interface-name* | Specifies the name of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After an Eth-Trunk interface in static LACP mode is configured, you can run the display lacp statistics command to view the statistics about received and sent LACPDUs and Marker packets on the Eth-Trunk interface.The Marker protocol prevents mis-sequence of received frames after traffic switches from one link to another.When using the display lacp statistics command, note that:

* If no optional parameter is specified, the statistics about LACPDUs and Marker packets on all Eth-Trunk interfaces in static LACP mode are displayed.
* If trunk-id is specified only, the statistics about LACPDUs and Marker packets on a specified Eth-Trunk interface in static LACP mode are displayed.
* If trunk-id and interface interface-type interface-number are specified, the statistics about LACPDUs and Marker packets on a specified member interface of a specified Eth-Trunk interface in static LACP mode are displayed.

**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode. Before checking the statistics about LACPDUs on an Eth-Trunk member interface, ensure that the member interface exists.



**Precautions**



If there are many traffic statistics on Eth-Trunk interfaces, it is recommended that you specify trunk-id or interface interface-type interface-number to filter output information.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the statistics about LACPDUs on all Eth-Trunk interfaces in static LACP mode.
```
<HUAWEI> display lacp statistics eth-trunk
Eth-Trunk1's PDU statistic is:
------------------------------------------------------------------------------
Port                   LacpRevPdu LacpSentPdu MarkerRevPdu MarkerSentPdu
100GE1/0/1                             17         189            0             0
100GE1/0/2                             17         189            0             0
100GE1/0/3                               0         186            0             0
Eth-Trunk2's PDU statistic is:
------------------------------------------------------------------------------
Port                  LacpRevPdu LacpSentPdu MarkerRevPdu MarkerSentPdu
100GE1/0/4                            15          17            0             0
100GE1/0/5                            15          17            0             0

```

# Display the statistics about LACPDUs on Eth-Trunk 1 in static LACP mode.
```
<HUAWEI> display lacp statistics eth-trunk 1
Eth-Trunk1's PDU statistic is:
------------------------------------------------------------------------------
Port                   LacpRevPdu LacpSentPdu MarkerRevPdu MarkerSentPdu
100GE1/0/1                             17         189            0             0
100GE1/0/2                             17         189            0             0
100GE1/0/3                               0         186            0             0

```

# Display statistics about LACPDUs on the member interface 100GE 1/0/1 of Eth-Trunk 1 in static LACP mode.
```
<HUAWEI> display lacp statistics eth-trunk 1 interface 100ge 1/0/1
100GE1/0/1's PDU statistic is:
 ------------------------------------------------------------------------------
 Port                    LacpRevPdu   LacpSentPdu  MarkerRevPdu MarkerSentPdu
100GE1/0/1                               17           189             0             0

```

**Table 1** Description of the **display lacp statistics eth-trunk** command output
| Item | Description |
| --- | --- |
| Port | Member interface of the Eth-Trunk interface. |
| LacpRevPdu | Number of received LACPDUs. |
| LacpSentPdu | Number of sent LACPDUs. |
| MarkerRevPdu | Number of received Marker packets. |
| MarkerSentPdu | Number of sent Marker packets. |