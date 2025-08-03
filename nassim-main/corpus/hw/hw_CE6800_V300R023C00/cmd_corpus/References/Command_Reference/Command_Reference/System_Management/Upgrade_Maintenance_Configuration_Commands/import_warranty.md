import warranty
===============

import warranty

Function
--------



The **import warranty** command activates the electronic warranty policy based on the imported file.




Format
------

**import warranty file** *ewmfile*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **file** *ewmfile* | Specifies the file name of the electronic warranty policy. | The value is a string of 5 to 127 characters, spaces not supported. |



Views
-----

warranty view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To better serve users in the information era, the equipment provides electronic warranty policies. An electronic warranty policy is an electronic record of the service life committed to customers for products and components. You can use the electronic warranty policy function to view the electronic records of the hardware activation date, hardware service life committed to the customer, and hardware warranty status. To activate the electronic warranty function, run the **import warranty** command. The device can determine whether the electronic warranty policy of the device or component is to be activated based on the specified serial number.

**Precautions**



The specified file must be stored in /opt/vrpv8/home.




Example
-------

# Activate the electronic warranty of the device.
```
<HUAWEI> system-view
[~HUAWEI] warranty
[~HUAWEI-warranty] import warranty file warranty.csv
Info: Operating, please wait for a moment...............
Info: Successfully imported the electronic warranty file, total number of valid service life records imported: 1.

```