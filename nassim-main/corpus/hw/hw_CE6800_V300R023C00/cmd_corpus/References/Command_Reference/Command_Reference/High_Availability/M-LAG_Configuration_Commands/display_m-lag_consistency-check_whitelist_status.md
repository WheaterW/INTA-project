display m-lag consistency-check whitelist status
================================================

display m-lag consistency-check whitelist status

Function
--------



The **display m-lag consistency-check whitelist status** command displays the M-LAG configuration consistency check whitelist.




Format
------

**display m-lag consistency-check whitelist status**


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

To view the M-LAG configuration consistency check whitelist, run this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the whitelist for M-LAG configuration consistency check.
```
<HUAWEI> display m-lag consistency-check whitelist status
-----------------------------------------------------------------------------------
module           service-type                     whitelist
-----------------------------------------------------------------------------------
m-lag            m-lag-member-num                 Y   
                 m-lag-id                         Y   
                 peer-link-exclude-vlan           Y   
                 m-lag-ipv4-address               Y   
                 m-lag-ipv6-address               Y   
                 m-lag-election-mode              Y   
-----------------------------------------------------------------------------------
vlan             vlan-configuration               Y   
                 port-vlan-relation               Y   
-----------------------------------------------------------------------------------
stp              stp-m-lag-priority               Y   
-----------------------------------------------------------------------------------
mac              mac-aging-time                   Y   
                 static-mac                       Y   
-----------------------------------------------------------------------------------
arp              arp-aging-time                   Y   
                 static-arp                       Y   
-----------------------------------------------------------------------------------
vlanif           vlanif-configuration             Y   
                 ipv4-address                     Y   
                 ipv6-address                     Y   
                 vrrp4                            Y   
                 virtual-mac                      Y   
                 vlanif-status                    Y   
                 vlanif-bypass                    Y   
                 arp-timeout                      Y   
-----------------------------------------------------------------------------------
vxlan            bd-configuration                 Y   
                 vbdif-configuration              Y   
                 ipv4-address                     Y   
                 ipv6-address                     Y   
                 virtual-mac                      Y   
                 vbdif-status                     Y   
-----------------------------------------------------------------------------------

```

# Display the whitelist for M-LAG configuration consistency check (for the CE6820H, CE6820H-K, and CE6820S).
```
<HUAWEI> display m-lag consistency-check whitelist status
-----------------------------------------------------------------------------------
module           service-type                     whitelist
-----------------------------------------------------------------------------------
m-lag            m-lag-member-num                 Y   
                 m-lag-id                         Y   
                 peer-link-exclude-vlan           Y   
                 m-lag-ipv4-address               Y   
                 m-lag-ipv6-address               Y   
                 m-lag-election-mode              Y   
-----------------------------------------------------------------------------------
vlan             vlan-configuration               Y   
                 port-vlan-relation               Y   
-----------------------------------------------------------------------------------
stp              stp-m-lag-priority               Y   
-----------------------------------------------------------------------------------
mac              mac-aging-time                   Y   
                 static-mac                       Y   
-----------------------------------------------------------------------------------
arp              arp-aging-time                   Y   
                 static-arp                       Y   
-----------------------------------------------------------------------------------
vlanif           vlanif-configuration             Y   
                 ipv4-address                     Y   
                 ipv6-address                     Y   
                 vrrp4                            Y   
                 virtual-mac                      Y   
                 vlanif-status                    Y   
                 arp-timeout                      Y   
-----------------------------------------------------------------------------------

```

# Display the whitelist for M-LAG configuration consistency check (for the CE6885-LL in low latency mode).
```
<HUAWEI> display m-lag consistency-check whitelist status
-----------------------------------------------------------------------------------
module           service-type                     whitelist
-----------------------------------------------------------------------------------
m-lag            m-lag-member-num                 Y   
                 m-lag-id                         Y   
                 peer-link-exclude-vlan           Y   
                 m-lag-ipv4-address               Y   
                 m-lag-election-mode              Y   
-----------------------------------------------------------------------------------
vlan             vlan-configuration               Y   
                 port-vlan-relation               Y   
-----------------------------------------------------------------------------------
stp              stp-m-lag-priority               Y   
-----------------------------------------------------------------------------------
mac              mac-aging-time                   Y   
                 static-mac                       Y   
-----------------------------------------------------------------------------------
arp              arp-aging-time                   Y   
                 static-arp                       Y   
-----------------------------------------------------------------------------------
vlanif           vlanif-configuration             Y   
                 ipv4-address                     Y   
                 vrrp4                            Y   
                 virtual-mac                      Y   
                 vlanif-status                    Y   
                 arp-timeout                      Y   
-----------------------------------------------------------------------------------

```

**Table 1** Description of the **display m-lag consistency-check whitelist status** command output
| Item | Description |
| --- | --- |
| whitelist | Whether the configuration has been added to the M-LAG configuration consistency check whitelist:   * Y: The configuration has been added to the whitelist, and the configuration consistency check will not be performed for it. * N: The configuration has not been added to the whitelist, and the configuration consistency check will be performed for it. |
| module | Module name. |
| service-type | Configuration type. |