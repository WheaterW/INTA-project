ospf suppress-reachability
==========================

ospf suppress-reachability

Function
--------



The **ospf suppress-reachability** command enables an OSPF interface to suppress the advertisement of interface addresses.

The **undo ospf suppress-reachability** command enables an OSPF interface to advertise its interface addresses.



By default, an OSPF interface will advertise its interface addresses.


Format
------

**ospf suppress-reachability** [ **disable** ]

**undo ospf suppress-reachability** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables OSPF from suppressing the advertisement of interface addresses. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable an OSPF interface to suppress the advertisement of interface addresses, run the **ospf suppress-reachability** command.


Example
-------

# Enable the interface to suppress the advertisement of interface addresses.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf suppress-reachability

```