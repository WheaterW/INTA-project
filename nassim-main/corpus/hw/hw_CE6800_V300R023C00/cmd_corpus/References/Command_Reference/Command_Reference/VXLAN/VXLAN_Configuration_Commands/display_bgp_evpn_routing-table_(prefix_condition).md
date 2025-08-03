display bgp evpn routing-table (prefix condition)
=================================================

display bgp evpn routing-table (prefix condition)

Function
--------



The **display bgp evpn routing-table** command displays information about BGP EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn all routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* { **community-list** | **ext-community** | **large-community** | **cluster-list** | **advertised-peer** | **as-path** }

**display bgp** [ **instance** *instance-name* ] **evpn** **all** **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* { **community-list** | **ext-community** | **large-community** | **cluster-list** | **advertised-peer** | **as-path** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ad-route** | Displays information about all Ethernet auto-discovery routes. | - |
| **es-route** | Displays information about Ethernet segment routes. | - |
| **inclusive-route** | Displays information about inclusive multicast routes. | - |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| **prefix-route** | Displays information about prefix routes. | - |
| *prefix* | Specifies the prefix of an EVPN route. | An EVPN route prefix has the following formats:  IP prefix route. The value is in the format of L:X.X.X.X:M or L:[X:X::X:X]:M, where:   * L is fixed at 0. * X.X.X.X indicates the host IP address. * M indicates the mask length of the host IP address. * X:X::X:X indicates the IPv6 host address. |
| **community-list** | Displays the community list of BGP EVPN routes. | - |
| **ext-community** | Displays the extended community list of BGP EVPN routes. | - |
| **large-community** | Displays the extended community attribute of BGP EVPN routes. | - |
| **cluster-list** | Displays the cluster list of BGP EVPN routes. | - |
| **advertised-peer** | Displays the advertised peer list of BGP EVPN routes. | - |
| **as-path** | Displays the AS\_Path attribute of BGP EVPN routes. | - |
| **all** | Displays information about EVPN routes of all EVPN instances. | - |
| **instance** *instance-name* | Displays information about EVPN routes of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about EVPN routes, including active and inactive routes, run the **display bgp evpn routing-table** command.Information about specified EVPN routes can be displayed by specifying different parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the large-community attribute of inclusive routing.
```
<HUAWEI> display bgp evpn all routing-table inclusive-route 0:32:10.5.5.5 large-community

 Routes of Route Distinguisher(1:1):
 
 BGP routing table entry information of 0:32:10.5.5.5:
 Imported route.
 From: ::
 Large-Community: <1:1:1>

```

**Table 1** Description of the **display bgp evpn routing-table (prefix condition)** command output
| Item | Description |
| --- | --- |
| Routes of Route Distinguisher | Routing information for the specified RD. |
| BGP routing table entry information of | Routing entry information. |
| Imported route | The routes imported. |
| From | IP address of the device that advertised routes. |
| Large-Community | Specifies the extended community attribute of BGP EVPN routes. |