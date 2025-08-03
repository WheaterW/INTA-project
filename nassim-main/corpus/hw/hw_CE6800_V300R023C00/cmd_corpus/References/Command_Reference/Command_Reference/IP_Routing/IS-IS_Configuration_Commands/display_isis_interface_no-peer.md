display isis interface no-peer
==============================

display isis interface no-peer

Function
--------



The **display isis interface no-peer** command displays information about IS-IS interfaces that are Up but have no neighbors.




Format
------

**display isis** *process-id* **interface** **no-peer**

**display isis interface no-peer** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295.  If no IS-IS process is specified, information about interfaces in all local IS-IS processes is displayed. |
| **no-peer** | Displays information about IS-IS interfaces that are Up but have no neighbors. | - |
| **vpn-instance** *vpn-instance-name* | Displays interface information about an IS-IS multi-instance process in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information on IS-IS interfaces, including the interface name, IP address, link status of each interface, run the display isis interface command. If verbose is specified, the output of this command also covers IS-IS parameter configurations for each interface, such as the CSNP broadcast interval, hello packet broadcast interval, and the number of IS-IS Hello packets sent by the neighbor before IS-IS should declare the neighbor Down.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IS-IS interfaces that are Up but have no neighbors.
```
<HUAWEI> display isis interface no-peer
Interface information for ISIS(1)
                        ---------------------------------
 Interface     IPV4.State       L1/L2.V4Peer       IPV6.State          L1/L2.V6Peer
 100GE1/0/1           Up           Dn/Dn                  --              --/--
 100GE1/0/2           Up           Up/Dn                  Up              Up/Dn

```

**Table 1** Description of the **display isis interface no-peer** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of an interface. |
| IPV4.State | IPv4 link status. |
| L1/L2.V4Peer | Status of Level-1 and Level-2 IPv4 neighbors:   * Up: There are Level-1 and Level-2 IPv4 neighbors. * Dn: There are no Level-1 nor Level-2 IPv4 neighbors. |
| IPV6.State | IPv6 link status. |
| L1/L2.V6Peer | Status of Level-1 and Level-2 IPv6 neighbors:   * Up: There are Level-1 and Level-2 IPv6 neighbors. * Dn: There are no Level-1 nor Level-2 IPv6 neighbors. * --: IPv6 is not enabled. |