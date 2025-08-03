inof bfd(iNOF view)
===================

inof bfd(iNOF view)

Function
--------



The **inof bfd** command sets parameters used to establish BFD sessions in the iNOF system.

The **undo inof bfd** command restores the default settings of BFD session parameters in the iNOF system.



By default, the minimum interval for sending BFD packets is 1000 ms, the minimum interval for receiving BFD packets is 1000 ms, and the local detection multiplier is 3 in the iNOF system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**inof bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *detect-multiplier* } \*

**undo inof bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *detect-multiplier* } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *min-tx-interval* | Specifies the minimum interval for sending BFD packets to the peer end. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000. |
| **min-rx-interval** *min-rx-interval* | Specifies the minimum interval for receiving BFD packets from the peer. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *detect-multiplier* | Specifies a local detection multiplier. | The value is an integer that ranges from 3 to 50. The default value is 3. |



Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the BFD for iNOF function is enabled, the iNOF system uses the default BFD session parameter settings to establish a BFD session.In actual applications, the default BFD session parameter settings may not meet the requirements of all networks. Therefore, you can run this command to adjust BFD session parameter settings. If a device does not receive BFD packets from a neighbor within the local BFD detection interval, the device announces that this neighbor goes down.

**Prerequisites**

Before running this command, ensure the following operations have been performed:

* BFD has been globally enabled using the **bfd** command in the system view.
* iNOF has been enabled and the iNOF view has been entered using the **inof** command in the AI service view.
* The BFD for iNOF function has been enabled using the **inof bfd enable** command in the iNOF view.

**Precautions**

BFD for iNOF depends on global BFD. BFD for iNOF takes effect only after BFD is enabled globally.This command can be configured on the iNOF client, but the parameter settings do not take effect. The BFD for iNOF configuration on the client is subject to the configuration synchronized from the iNOF reflector.


Example
-------

# Set the minimum interval for sending BFD packets to 900 ms, the minimum interval for receiving BFD packets to 900 ms, and the local detection multiplier to 4 for the BFD for iNOF function.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] inof bfd min-tx-interval 900 min-rx-interval 900 detect-multiplier 4

```