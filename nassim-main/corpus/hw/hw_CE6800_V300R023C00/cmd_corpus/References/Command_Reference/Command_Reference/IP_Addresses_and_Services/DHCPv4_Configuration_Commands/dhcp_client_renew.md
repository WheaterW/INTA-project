dhcp client renew
=================

dhcp client renew

Function
--------



The **dhcp client renew** command renews the lease of the IP address obtained by a DHCP client.



By default, the lease of DHCP client does not get changed.


Format
------

**dhcp client renew**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

* Manually renewing the lease: If a DHCP server assigns the original IP address to the client, only the lease is renewed. If another DHCP server assigns an IP address to the client, the client obtains a new IP address and related network parameters.
* Updating the IP address: When the DHCP client is migrated from a network segment to another network segment and the original IP address lease does not expire, the client needs to update the IP address.After the **dhcp client renew** command is run, the DHCP client sends a lease renewal request to the DHCP server.
* If the DHCP client receives a positive reply from the server, the client updates the parameters such as the lease duration.
* If the DHCP client receives a negative reply from the server, the client releases the applied parameters and re-applies to the DHCP server for an IP address and other network parameters.
* If no reply is received, the client does not perform any operation.The **dhcp client renew** command can be normally run only after the DHCP client function is enabled on the interface and an IP address is obtained.

Example
-------

# Renew the IP address lease on interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address dhcp-alloc
[*HUAWEI-100GE1/0/1] dhcp client renew

```