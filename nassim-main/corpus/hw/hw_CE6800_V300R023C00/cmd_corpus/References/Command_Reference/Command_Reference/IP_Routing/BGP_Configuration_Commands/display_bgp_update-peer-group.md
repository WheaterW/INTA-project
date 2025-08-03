display bgp update-peer-group
=============================

display bgp update-peer-group

Function
--------



The **display bgp update-peer-group** command displays information about update peer-groups. If no address family is specified, information about the update peer-groups of the IPv4 unicast address family is displayed by default.




Format
------

**display bgp** [ **vpnv4** **vpn-instance** *vpn-instance-name* | **vpnv4** **all** ] **update-peer-group** [ **index** *index-value* ]

**display bgp instance** *instance-name* [ **vpnv4** **vpn-instance** *vpn-instance-name* | **vpnv4** **all** ] **update-peer-group** [ **index** *index-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Displays information about the BGP update peer-groups of a VPNv4 instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all** | Displays information about all the update peer-groups in current address family. | - |
| **index** *index-value* | Specifies the index of an update peer-group. | The value is an integer that ranges from 0 to 65535. |
| **instance** *instance-name* | Specifies the name of a BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp update-peer-group** command is used to view information about all the update-groups in the IPv4 unicast address family on the public network.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the update peer-group with a specified index.
```
<HUAWEI> display bgp update-peer-group index 0
 Group ID : 0
 BGP Version : 4
 Group Type : external
 Addr Family : IPv4-UNC
 Total Peers : 1
 AdvMinTimeVal : 30
 Leader Peer : 192.168.1.2

 Total format packet number : 3
 Total send packet number : 3
 Total replicate packet number : 0
 The replication percentages(%) : 0

 Peers List : 192.168.1.2

```

# Display information about the update peer-groups in a specified address family.
```
<HUAWEI> display bgp update-peer-group
The Public instance's update peer group number : 1
 Keep buffer update peer group number : 0
 BGP Version : 4

 Update peer group number :1 
 Group ID : 0 
 Group Type : external 
 Addr Family : IPv4-UNC 
 AdvMinTimeVal : 30 
 Total Peers : 1 
 Leader Peer : 192.168.1.2 
 Peers List : 192.168.1.2

```

**Table 1** Description of the **display bgp update-peer-group** command output
| Item | Description |
| --- | --- |
| Group ID | Update group ID of the BGP peer. |
| Group Type | Type of an update peer-group:   * external: EBGP. * internal: IBGP. * unknown: unknown type. |
| BGP Version | BGP version. |
| Addr Family | Address family. |
| AdvMinTimeVal | Minimum interval at which Update messages with the same route prefix are sent. |
| Total Peers | Indicates the total number of peers in an update-group. |
| Total format packet number | Total format packet number. |
| Total send packet number | Total number of sent packets. |
| Total replicate packet number | Number of replicated packets. The value equals the total number of sent packets minus the total number of packets. |
| Peers List | List of peers. |
| Leader Peer | IP addresses of peers in an update peer-group. |
| The Public instance's update peer group number | Number of update peer-groups in an instance. |
| The replication percentages(%) | Replication percentage: (Total number of sent packets - Total number of formatted packets) x 100/Total number of formatted packets. |
| Keep buffer update peer group number | Number of update peer-groups stored in the batch buffer. |
| Update peer group number | Number of update peer-groups. |