activate warranty (warranty view)
=================================

activate warranty (warranty view)

Function
--------



The **activate warranty** command activates a warranty.




Format
------

**activate warranty serial-number** *serial-number-value* **start-date** *start-date-value* **life-span** *life-span-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **start-date** *start-date-value* | Specifies the time when a warranty is activated. | The time format is XXXX/XX/XX. |
| **life-span** *life-span-value* | Specifies the warranty period of a warranty. | The value is a 32-bit integer ranging from 1 to 600. |
| **serial-number** *serial-number-value* | Specifies the serial number of the device or component to be activated. The serial number must be in the serial-number-value\_serial-number-value format. | The value is a string of 1 to 100 characters without spaces. |



Views
-----

warranty view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The warranty activated can be used to obtain the electronic copy of the product's or component's service life committed to customers.You can determine whether the warranty of a device or a part is activated based on the serial number.

**Precautions**



You can run the **display device elabel brief** command to check the serial number (serial-number-value) of a device or component.

The electronic label of a device must be in the serial-number-value\_serial-number-value format.The electronic label of a component must be in the serial-number-value format.




Example
-------

# Activates the warranty of a device or component.
```
<HUAWEI> system-view
[~HUAWEI] warranty
[~HUAWEI-warranty] activate warranty serial-number 026GDU10K9000007 start-date 2020/10/10 life-span 10
Info: Operating, please wait for a moment...
Info: The digital warranty is successfully activated.

```