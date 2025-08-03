display rip database
====================

display rip database

Function
--------



The **display rip database** command displays all the active routes in RIP database. These routes are sent as regular RIP update packets.

The **display ripng database** command displays all the routes in the RIPng database.




Format
------

**display rip** *process-id* **database** [ **verbose** ] [ **destination-address** *ipv4-destination-address* [ *mask-length* ] ] [ **interface** { *interface-name* | *interface-type* *interface-number* } [ **neighbor** *ipv4-neighbor-address* ] ]

**display ripng** *process-id* **database** [ **verbose** ] [ **destination-address** *ipv6-destination-address* [ *ipv6-mask-length* ] ] [ **interface** { *interface-name* | *interface-type* *interface-number* } [ **neighbor** *ipv6-neighbor-address* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id. | The value is an integer ranging from 1 to 4294967295. |
| **verbose** | Displays detailed information about the routes that are advertised to neighbors. | - |
| **destination-address** *ipv4-destination-address* | Displays routes to the specific destination IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the IP address mask for the destination. | The value is an integer ranging from 0 to 32. |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. | - |
| **neighbor** *ipv4-neighbor-address* | Specifies the IP address of the neighbor. | The value is in dotted decimal notation. |
| *ipv6-destination-address* | Displays routes to a specific destination IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *ipv6-mask-length* | Specifies the mask of a specific destination IPv6 address. | It is an integer ranging from 0 to 128. |
| *ipv6-neighbor-address* | Displays routes to a specific IPv6 neighbor. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **display rip database** command to view the following information:

* Routes to a particular destination.
* Routes advertised to a particular neighbor.
* Routes advertised by a specified interface.To check information about the routes to different destination network addresses, run the **display ripng database** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information of RIP database.
```
<HUAWEI> display rip 1 database verbose
   10.0.0.0/8, cost 1, ClassfulSumm
   10.1.1.0/24, cost 1
     NextHop :192.168.1.2      Intf :100GE1/0/1
     EntryID :NA               Tag:0
     State   :NA
   10.2.1.0/24, cost 1
     NextHop :192.168.1.2      Intf :100GE1/0/1
     EntryID :NA               Tag:0
     State   :NA
   172.16.0.0/16, cost 0, ClassfulSumm
   172.16.1.0/24, cost 0, Rip-interface
     NextHop :0.0.0.0          Intf :LoopBack0
     EntryID :NA               Tag:0
     State   :NA
   172.17.0.0/16, cost 0, ClassfulSumm
   172.17.1.0/24, cost 0, Rip-interface
     NextHop :0.0.0.0          Intf :LoopBack1
     EntryID :NA               Tag:0
     State   :NA
   192.168.1.0/24, cost 0, ClassfulSumm
   192.168.1.0/24, cost 0, Rip-interface
     NextHop :0.0.0.0          Intf :100GE1/0/1
     EntryID :NA               Tag:0
     State   :NA

```

# Displays RIP database information about a specified IPv4 address.
```
<HUAWEI> display rip 1 database destination-address 192.168.1.0 24
   192.168.1.0/24, cost 0, ClassfulSumm
   192.168.1.0/24, cost 0, Rip-interface

```

# Display RIP database information.
```
<HUAWEI> display rip 100 database
10.0.0.0/8, cost 1, ClassfulSumm
10.0.0.0/24, cost 1, nexthop 10.0.0.1, Rip-interface
172.16.0.0/16, cost 1, ClassfulSumm
172.16.0.0/24, cost 1, nexthop 10.0.0.1, Imported

```

# Display the routes in the RIPng database.
```
<HUAWEI> display ripng 100 database
   2001:DB8:8::8/128,
        cost 0, Imported
   2001:DB8:10::/64,
       via FE80::2E0:E6FF:FE1B:8242, cost 1
   2001:DB8:10::/64,
       via FE80::2E0:E6FF:FE1B:8242, cost 1
   2001:DB8:10::/64,
       via FE80::2E0:E6FF:FE1B:8142, cost 1
   2001:DB8:10::/64,
       via FE80::2E0:E6FF:FE1B:8142, cost 1
   2001:DB8:12::/64,
        cost 0, RIPng-interface

```

**Table 1** Description of the **display rip database** command output
| Item | Description |
| --- | --- |
| cost | Cost of the route. |
| ClassfulSumm | Classful summarized route. |
| Intf | Interface name. |
| EntryID | Rec index. |
| State | Route state. |
| Rip-interface | Address of the local interface. |
| destination-address | Destination addresses. |
| nexthop | Next reachable IP address for the route. |
| Imported | Routes imported from some other protocols. |
| via | Link-local address of the next hop. |
| RIPng-interface | Routes generated by RIPng. |
| 2001:DB8:8::8/128 | IPv6 destination address. |
| Tag | Tag of the route. |