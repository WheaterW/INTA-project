protected-instance
==================

protected-instance

Function
--------



The **protected-instance** command configures an ERP instance for an ERPS ring.

The **undo protected-instance** command deletes the configured ERP instance.



By default, no ERP instance is configured on an ERPS ring.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**protected-instance** { **all** | { *instance-id1* [ **to** *instance-id2* ] } &<1-10> }

**undo protected-instance** { **all** | { *instance-id1* [ **to** *instance-id2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Specifies all ERP instances. | - |
| *instance-id1* | Specifies the ID1 of an ERP instance. | The value is an integer ranging from 0 to 4094.  The value of instIdEnd must be greater than or equal to instId. |
| **to** *instance-id2* | Specifies the ID2 of an ERP instance. | The value is an integer ranging from 0 to 4094.  The value of instIdEnd must be greater than or equal to instId. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a device running ERPS, the VLAN in which ERPS BPDUs and data packets are transmitted must be mapped to a protected instance so that ERPS forwards or blocks these packets based on rules. Otherwise, VLAN packets probably cause broadcast storms on the ring network. This will cause the network to be unavailable.

**Configuration Impact**

If the **protected-instance** command is run more than once on an ERPS ring to configure ERP instances, all these ERP instances take effect.If any port has been added to the ERPS ring, no ERP instance can be modified. If the configured ERP instance needs to be deleted, run the undo erps ring command in the interface view or the **undo port** command in the ERPS ring view, and run the **undo protected-instance** command to delete the ERP instance.

**Follow-up Procedure**

Configure the mapping between the instance and VLAN. Ensure that the control VLAN belongs to the configured ERP instance. The procedure is as follows:

* Configure the mapping between the ERP instance and VLAN in the MST region view.

1. Run the **stp region-configuration** command to enter the MST region view.
2. Run the **instance instance-id vlan** command to configure the mapping between the MSTI and VLAN.A VLAN cannot be mapped to multiple instances. If a VLAN that has been mapped to an instance is mapped to another instance, the original mapping is canceled.The **vlan-mapping modulo modulo** command can be used to configure the mapping between MSTIs and VLANs based on the default algorithm. However, the mapping configured using this command cannot always meet the actual demand. Therefore, running this command is not recommended.

* Perform the following steps to configure the mapping between the ERP instance and VLAN in the VLAN instance view:

1. Run the **vlan instance** command to enter the VLAN instance view.
2. Run the **instance instance-id vlan** command to configure the mapping between the instance and VLAN. The **vlan instance** command and the **stp region-configuration** command are mutually exclusive. If the mapping between the instance and VLAN has been configured by running the **stp region-configuration** command, you need to delete the mapping before running the **vlan instance** command.
3. (Optional) Run the check vlan instance mapping command to check whether the configuration is correct.

**Precautions**

If a configured protection instance is deleted, a broadcast storm may occur in the protection instance.


Example
-------

# Configure ERP instance 5 for ERPS ring 1.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1
[*HUAWEI-erps-ring1] protected-instance 5

```