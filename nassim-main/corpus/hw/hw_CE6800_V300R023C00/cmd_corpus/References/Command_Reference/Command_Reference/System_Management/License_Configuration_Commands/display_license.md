display license
===============

display license

Function
--------



The **display license** command displays information about an active license file.




Format
------

**display license**

**display license verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays details about a license file. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



A license file determines whether some product features are available. To view information about an active license file, run the display license command. The information includes the name, version, valid time, and configuration items of the license file.<note: <br=""> The encoding format used to display license information in the current version is GBK. To prevent garbled characters when you use a different terminal to log in to the device and Chinese characters are displayed, change the terminal's encoding format to GBK.For example, if you use the PuTTY tool as the terminal, set its encoding format to Use font encoding, and the operating system's default encoding format must be GBK. After the encoding format is set to GBK, Chinese information about the license can be correctly displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the verbose information about an active license file which Sales and display are consistent.
```
<HUAWEI> display license verbose
 Active license    : flash:/LICXXXX
 License state     : Demo
 Revoke ticket     : No ticket
 License mode      : common

 Product name      : ****
 Product version   : V300R023C00
 License file ESN  : 391091068000297
 License Serial No : LIC20190424S0G55M
 Creator           : Huawei Technologies Co., Ltd.
 Created Time      : 2020-04-07 15:03:32
 Country           : English
 Custom            : RD of Huawei Technologies Co., Ltd.
 Office            : ShenZhen
 
 Feature name      : Trial0
 Authorize type    : demo
 Expired date      : 2020-07-12
 Trial days        : --
 Sale name         : *****0VA5C00
 Item name         : *****LCK00
 Item type         : Function
 Control value     : 1
 Used value        : 1
 Item state        : Demo
 Item expired date : 2020-07-12
 Item trial days   : 60
 Description       : *****LCK00
 
 Sale name         : *****0VA5C00
 Item name         : *****40VA5C00
 Item type         : Resource
 Control value     : 80
 Used value        : 0
 Item state        : Demo
 Item expired date : 2020-07-12
 Item trial days   : 60
 Description       : XXXX Host License for 5 Client
 
 Sale name         : *****0VA1C00
 Item name         : *****40VA1C00
 Item type         : Resource
 Control value     : 400
 Used value        : 0
 Item state        : Demo
 Item expired date : 2020-07-12
 Item trial days   : 60
 Description       : XXXX Host License for 1 Client

```

# Display information about an activated license file in the system in cloud mode.
```
<HUAWEI> display license
 License state     : Normal
 License mode      : cloud
 Product name      : ****
 Product version   : V300R023C00
 Expired date      : Permanent
 Trial days        : --
 -------------------------------------------------------------


 Item name          Item type      Value      Description
 -------------------------------------------------------------

 ****SX0IPS5C2        --             1          ****** Tunnel Quantity License(500 Tunnels)

 Master board license state: Normal.

```

# Display detailed information about an activated license file in the system in cloud mode.
```
<HUAWEI> display license verbose
 License state     : Normal
 License mode      : cloud
 Product name      : ****
 Product version   : V300R023C00
 Expired date      : Permanent
 Trial days        : --
 -------------------------------------------------------------

 Sale name         : ****SX0IPS5C2
 Item name         : ****SX0IPS5C2
 Item type         : Resource
 Control value     : 1
 Used value        : 0
 Item state        : Normal
 Item expired date : 2022-06-23
 Item trial days   : 60
 Description       : ***** Tunnel Quantity License(500 Tunnels)

```

# Display information about the activated license file in the current system.
```
<HUAWEI> display license
 Active License    : flash:/LICXXXX
 License state     : Demo
 Revoke ticket     : No ticket 
 License mode      : common

 RD of Huawei Technologies Co., Ltd.

 Product name      : ****
 Product version   : V300R023C00
 License Serial No : LIC20140227016150
 Creator           : Huawei Technologies Co., Ltd.
 Created Time      : 2019-07-11 22:47:08
-------------------------------------------------------------
 Feature name      : CXFEA03
 Authorize type    : demo
 Expired date      : 2020-05-20
 Trial days        : --

 Item name          Item type      Value      Description
 ------------------------------------------------------------- 
 *****0200VA00      Function       1          *****0200VA00
 *****02VA1C00      Resource       1          *****02VA1C00     

 Item name          (View)Resource License Command-line
 ------------------------------------------------------------- 
 *****02VA1C00      (License)Active va slot slot-id

 Master board license state: Demo. The license for the current configuration will expire in 62 day(s).
 Apply for authentic license before the current license expires.

```

# Display the information about an active license file which Sales and display are consistent.
```
<HUAWEI> display license
 Active License    : flash:/LICXXXX
 License state     : Demo
 Revoke ticket     : No ticket
 License mode      : common

 RD of Huawei Technologies Co., Ltd.

 Product name      : ****
 Product version   : V300R023C00
 License Serial No : LIC20190424S0G55M
 Creator           : Huawei Technologies Co., Ltd.
 Created Time      : 2019-04-24 15:03:32
-------------------------------------------------------------
 Feature name      : Trial0
 Authorize type    : demo
 Expired date      : 2020-07-12
 Trial days        : --

 Item name          Item type      Value      Description
 -------------------------------------------------------------
 *****0VA5C00       --             8          XXXX Host License for 5 Client
  *****LCK00        Function       YES        *****LCK00
  *****40VA5C00     Resource       80         XXXX Host License for 5 Client
 *****0VA1C00       --             40         XXXX Host License for 1 Client

```

# Display the verbose information about an activated license file.
```
<HUAWEI> display license verbose
 Active license    : flash:/LICXXXX
 License state     : Demo
 Revoke ticket     : No ticket
 License mode      : common

 Product name      : ****
 Product version   : V300R023C00
 License file ESN  : 391091068000297
 License Serial No : LIC20190424S0G55M
 Creator           : Huawei Technologies Co., Ltd.
 Created Time      : 2020-04-07 15:03:32
 Country           : English
 Custom            : RD of Huawei Technologies Co., Ltd.
 Office            : ShenZhen
 
 Feature name      : Trial0
 Authorize type    : demo
 Expired date      : 2020-07-12
 Trial days        : --
 Sale name         : *****0VA5C00
 Item name         : *****LCK00
 Item type         : Function
 Control value     : 1
 Used value        : 1
 Item state        : Demo
 Item expired date : 2020-07-12
 Item trial days   : 60
 Description       : *****LCK00
 
 Sale name         : *****0VA5C00
 Item name         : *****40VA5C00
 Item type         : Resource
 Control value     : 80
 Used value        : 0
 Item state        : Demo
 Item expired date : 2020-07-12
 Item trial days   : 60
 Description       : XXXX Host License for 5 Client
 
 Sale name         : *****0VA1C00
 Item name         : *****40VA1C00
 Item type         : Resource
 Control value     : 400
 Used value        : 0
 Item state        : Demo
 Item expired date : 2020-07-12
 Item trial days   : 60
 Description       : XXXX Host License for 1 Client

```

**Table 1** Description of the **display license** command output
| Item | Description |
| --- | --- |
| Active License | Name of the activated license file in the display license command output. |
| Active license | Name of the activated license file in the display license verbose command output. |
| License state | Status of a license file:   * Normal: indicates the normal activation state.   The license file on the live network must be in the Normal state. Otherwise, the license file has potential problems and needs to be checked.   * Trial: indicates the trial state.   + A license file enters the trial state if the ESN in the license file does not match the ESN of the device. A license file can be used for 60 days only. In this case, you need to apply for a license file matching the ESN and activate it.   + A temporary license file expires and enters the Trial state. In this case, you need to apply for a formal license file and activate it.   + A license file becomes invalid and enters the Trial state. In this case, you need to apply for a new license file based on the revocation code and activate the license file.   + If you replace a board but do not replace the license file that matches the ESN, the license file enters the trial state. In this case, you need to apply for a license file matching the ESN and activate the license file. * Demo: indicates the demo state.   When you activate a temporary license file, the file is in Demo state. The Demo status exists only for a demo license file used for test and deployment.  In this case, the functions can be used properly, but the license file has a validity period. Ensure that the license file is replaced with a commercial license file before the license file expires.   * Default: indicates no license file is activated or the license file expires.   After a license file is activated, the license file enters the default state due to expiration or invalidity. As a result, services are interrupted.  No matter whether the license file expires or becomes invalid, you need to apply for a new license file and activate it. |
| License Serial No | Serial number of a license file. |
| License file ESN | Device serial number. |
| License mode | License mode.  common: non-cloud license.  cloud: cloud license. |
| Revoke ticket | License revocation code. |
| Product name | Product ID of the license entitlement, which is not the actual model of the device. |
| Product version | Version of the product corresponding to the license file. |
| Creator | Creator of the file. |
| Created Time | Time when the file was created. |
| Country | Country of user. |
| Custom | User name. |
| Office | Use location. |
| Feature name | Name of the feature corresponding to the license. |
| Authorize type | Authorization type:   * demo: license file for trial use. * comm: license file for commercial use. |
| Expired date | Expiration date of a license file, in the format of yyyy-mm-dd PERMANENT indicates that the license is permanently valid. |
| Trial days | Grace (trial) period. If the license module enters the Trial state from Demo state, the license module is allowed to run based on the authorization strategy in Normal or Demo state before the grace period expires. |
| Sale name | Sales name. |
| Item name | Name of a control item. |
| Item type | Type of a license control item.  Resource: license control item, indicating a resource control service license. The item name in the line is indented.  Function: license control item, indicating a function control service license. The item name in the line is indented.  --: license sales item The item name in the line is not indented. |
| Item state | Status of a license item. |
| Item expired date | Annual fee date of a license item. |
| Item trial days | Trial period of a license item. |
| Control value | Value of a licensed configuration item. |
| Used value | Value of a control item. |
| Description | Description of a control item. |
| Value | License function item. For a functional license, this item is displayed as YES, indicating the license function item is enabled. For a resource license, the value of this item indicates the supported control item specifications. |
| Master board license state | Status of a license file. |