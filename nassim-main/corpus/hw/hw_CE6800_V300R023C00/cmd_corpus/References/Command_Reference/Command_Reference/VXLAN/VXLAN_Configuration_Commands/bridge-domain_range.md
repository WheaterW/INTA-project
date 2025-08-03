bridge-domain range
===================

bridge-domain range

Function
--------



The **bridge-domain range** command creates a temporary BD range and displays the BD range view.



By default, no temporary BD range is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bridge-domain range** { *bdIdBgn* [ **to** *bdIdEnd* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bdIdBgn* | Specifies the start BD ID. | The value is an integer ranging from 1 to 4094. |
| **to** *bdIdEnd* | Specifies the end BD ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When replacing a TRILL network with a VXLAN network, you need to configure multiple VXLAN-related commands in each BD. Even if you bind a BD profile to a BD to simplify the configuration, the configuration is difficult when a large number of BDs are required. In addition, manual configuration or maintenance by the network administrator is labor-intensive and cannot ensure configuration consistency. To improve maintenance efficiency and simplify configuration, run the **bridge-domain range** command to create a temporary BD range and bind a BD profile to the BD range. After the binding is successful, the configuration is delivered to all BDs in the BD range in batches.

**Precautions**

After the **bridge-domain range** command is run, the system does not generate a configuration file. After a service is configured in the BD range view and committed, a configuration file is generated for each BD in the BD range.A BD range can contain a maximum of 100 BDs.


Example
-------

# Create a temporary BD range with IDs 10 to 20 and enter the BD range view.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain range 10 to 20

```