display arp anti-attack gateway-duplicate item
==============================================

display arp anti-attack gateway-duplicate item

Function
--------



The **display arp anti-attack gateway-duplicate item** command displays the ARP bogus gateway attack defense entries.




Format
------

**display arp anti-attack gateway-duplicate item**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view ARP bogus gateway attack defense entries, run the display arp anti-attack gateway-duplicate item command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ARP bogus gateway attack defense entries.
```
<HUAWEI> display arp anti-attack gateway-duplicate item


 Interface               IP address       MAC address     Bridge type   Bridge id    Aging time 
--------------------------------------------------------------------------------------------
 Ethernet1/0/1           10.1.1.1         xxxx-xxxx-xxxx  VLAN          2            150
 Ethernet1/0/1           10.1.1.2         xxxx-xxxx-xxxx  VLAN          2            170
--------------------------------------------------------------------------------------------
The number of record(s) in gateway conflict table is 2

```

**Table 1** Description of the **display arp anti-attack gateway-duplicate item** command output
| Item | Description |
| --- | --- |
| Interface | Inbound interface of ARP packets. |
| IP address | Gateway address. |
| MAC address | Source MAC address of ARP packets. |
| Bridge type | Bridge type. |
| Bridge id | Bridge id. |
| Aging time | Entry aging time. |