c-bsr global
============

c-bsr global

Function
--------



The **c-bsr global** command configures a router as a candidate-bootstrap router (C-BSR) in the global domain and sets a priority and hash mask length for the C-BSR.

The **undo c-bsr global** command restores the default configuration.



By default, no C-BSR is configured in the global domain.


Format
------

**c-bsr global priority** *priority*

**c-bsr global priority** *priority* **hash-length** *hash-length*

**c-bsr global hash-length** *hash-length* **priority** *priority*

**c-bsr global hash-length** *hash-length*

**c-bsr global**

**undo c-bsr global**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority* | Specifies a priority for the C-BSR in the global domain. A larger value indicates a higher C-BSR priority. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **hash-length** *hash-length* | Specifies a hash mask length for the C-BSR in the global domain. | The value is an integer ranging from 0 to 32. The default value is 30. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, each PIM-SM domain has only one BSR to serve all routers in the entire PIM-SM domain. To implement better device management, a PIM-SM domain can be divided into one global domain and multiple BSR administrative domains.Each BSR administrative domain maintains a BSR, serving the multicast groups on the network segment 239.0.0.0/8. Multicast packets for groups on this network segment cannot go across a BSR administrative domain border. Addresses of the multicast groups that different BSR administrative domain serve can overlap. The overlapped multicast groups are similar to private group addresses and take effect only in local BSR administrative domains. Multicast groups that do not belong to any BSR administrative domain belong to the global domain. The global domain maintains a BSR, serving all other multicast groups not on the network segment 239.0.0.0/8.To enable a router in the global domain to participate in BSR election, run the c-bsr global command to configure the router as a C-BSR.In BSR election in the global domain, C-BSRs compare their priorities and IP addresses:

* The C-BSR with the highest priority is elected as the BSR.
* If the C-BSRs have same priority, the C-BSR with the largest IP address is elected as the BSR.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.C-BSRs are configured in each BSR administrative domain.

**Configuration Impact**

If the c-bsr global command is run more than once, the latest configuration overrides the previous one.After the undo pim command or the undo **multicast routing-enable** command is run in the system view, the C-BSRs in the global domain are automatically disabled.

**Precautions**

This command takes effect only in the BSR administrative domains. If a router in the BSR administrative domain needs to accept multicast data for the groups not on the network segment 239.0.0.0/8, you can run this command.


Example
-------

# In the public network instance, configure a router as a C-BSR in the global domain and set the priority of the C-BSR to 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-bsr global priority 1

```