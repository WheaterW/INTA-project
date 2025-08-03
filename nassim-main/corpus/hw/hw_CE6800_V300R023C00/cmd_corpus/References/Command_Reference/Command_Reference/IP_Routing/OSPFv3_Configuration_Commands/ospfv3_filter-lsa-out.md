ospfv3 filter-lsa-out
=====================

ospfv3 filter-lsa-out

Function
--------



The **ospfv3 filter-lsa-out** command configures an OSPFv3 interface to filter outgoing LSAs.

The **undo ospfv3 filter-lsa-out** command disables an OSPFv3 interface from filtering outgoing LSAs.



By default, an OSPFv3 interface does not filter outgoing LSAs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 filter-lsa-out lsa-type** *type-value* [ **instance** *instanceId* ]

**undo ospfv3 filter-lsa-out lsa-type** *type-value* [ **instance** *instanceId* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instanceId* | Specifies the ID of an OSPFv3 instance to which an interface belongs. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **lsa-type** *type-value* | Specifies the type of LSAs to be filtered in the outbound direction of an interface. | The value is in hexadecimal notation. Currently, only the following values are supported:   * 8028: E-Link LSA * a00a: Intra-area TE LSA * a00c: Router-information LSA * a021: E-Router LSA * a022: E-Network LSA * a023: E-Inter-Area-Prefix LSA * a024: E-Inter-Area-Router LSA * a027: E-Type-7 LSA * a029: E-Intra-Area-Prefix LSA * a02a: Locator LSA * c00c: AS-Router-Information LSA * c025: E-AS-External LSA |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a scenario where a Huawei device interworks with a non-Huawei device, if the non-Huawei device receives unidentified packets and its processing behavior does not comply with the protocol, the neighbor relationship may fail to be established. OSPFv3 provides an escape method. You can run the **ospfv3 filter-lsa-out** command on an OSPFv3 interface to filter out LSAs that cannot be identified by non-Huawei devices in the outbound direction of the OSPFv3 interface. In this manner, the neighbor relationship can be quickly established.

**Configuration Impact**

If the **ospfv3 filter-lsa-out** command is run to configure an OSPFv3 interface not to send specified LSAs to neighbors in the outbound direction, the LSDBs of the neighbors do not contain the corresponding LSAs. As a result, routing problems may occur due to LSDB inconsistency on the entire network. Therefore, this command can only be used as a best-effort method. Exercise caution when using this command in normal scenarios.

**Precautions**

* After the **ospfv3 filter-lsa-out** command is run, the OSPFv3 interface does not send the specified LSA to the neighbor in the outbound direction. The neighbor does not delete the specified LSA immediately. The LSA is deleted only after it ages.
* After the **undo ospfv3 filter-lsa-out** command is run, an OSPFv3 interface does not immediately send specified LSAs to neighbors in the outbound direction. Instead, the OSPFv3 interface needs to wait for LSAs to be updated or neighbors need to be manually restarted to synchronize LSDBs.
* If a non-Huawei device cannot identify LSAs and its processing behavior does not comply with the protocol, the neighbor relationship cannot be established. In this case, you are advised to run this command on all interfaces of the device that advertises the LSAs. Delete the configuration after the fault on the non-Huawei device is rectified.

Example
-------

# Configure 100GE1/0/1 to filter the outgoing E-Router LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[~HUAWEI-ospfv3-1] router-id 2.2.2.2
[~HUAWEI-ospfv3-1] area 0
[~HUAWEI-ospfv3-1-area-0.0.0.0] quit
[~HUAWEI-ospfv3-1] quit
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ipv6 enable
[~HUAWEI-100GE1/0/1] ospfv3 1 area 0
[~HUAWEI-100GE1/0/1] ospfv3 filter-lsa-out lsa-type a021

```