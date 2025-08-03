display interface transceiver
=============================

display interface transceiver

Function
--------



The **display interface transceiver** command displays optical module information on the interfaces of a device.




Format
------

**display interface** { *interface-name* | *interface-type* *interface-number* } **transceiver** [ **verbose** ]

**display interface slot** *slot-id* **transceiver** [ **verbose** ]

**display interface transceiver** [ **non-certified** ] [ **verbose** ]

**display interface transceiver brief**

**display interface** { *interface-name* | *interface-type* *interface-number* } **transceiver** **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies an interface type. | The value must be set according to the device configuration. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| **verbose** | Displays detailed optical module information on interfaces, including basic information, manufacturing information, alarm information, and diagnostic information. | - |
| **slot** *slot-id* | Specifies the ID of a slot to be queried. | The value is a string of 1 to 23 characters that can contain case-insensitive letters, underscores (\_), and digits. |
| **non-certified** | Displays information about optical modules that are not certified for Huawei. | - |
| **brief** | Displays brief optical module information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can view basic information, manufacturing information, and alarm information about optical modules on interfaces of the device by using the display interface transceiver command. If the verbose parameter is specified, diagnostic information is also displayed.

**Prerequisites**

The optical module is in position. If the optical module is not in position, the command output is empty.

**Precautions**

The temperature, voltage, current, and optical power of some cables cannot be viewed due to different manufacturers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display basic information, manufacturing information, alarm information and diagnostic information about the optical module on a specified interface.
```
<HUAWEI> display interface 10ge 1/0/1 transceiver

 10GE1/0/1 transceiver information:
-------------------------------------------------------------------
 Common information:
   Transceiver Type                      :10GBASE_SR
   Connector Type                        :LC
   Wavelength (nm)                       :850
   Transfer Distance (m)                 :30(62.5um/125um OM1)
                                          80(50um/125um OM2)
                                          300(50um/125um OM3)
                                          400(50um/125um OM4)
   Digital Diagnostic Monitoring         :YES
   Vendor Name                           :HUAWEI
   Vendor Part Number                    :02318169
   Ordering Name                         :
-------------------------------------------------------------------
 Manufacture information:
   Manu. Serial Number                   :AQG269Y
   Manufacturing Date                    :2013-10-20
   Vendor Name                           :HUAWEI
-------------------------------------------------------------------
 Alarm information:
   Non-Huawei-certified transceiver
-------------------------------------------------------------------
 Warning information:
-------------------------------------------------------------------

```

# Display brief information about the optical module on a specified interface.
```
<HUAWEI> display interface 10ge 1/0/1 transceive brief

10GE1/0/1 transceiver diagnostic information:
-------------------------------------------------------------------
   Temperature (Celsius)                 :21.39
   Voltage (V)                           :3.29
   Bias Current (mA)                     :22.80
   Current RX Power (dBm)                :-40.00
   Current TX Power (dBm)                :-3.33
-------------------------------------------------------------------

```

# Display brief information about all optical modules on the device.
```
<HUAWEI> display interface transceiver brief

10GE1/0/2 transceiver diagnostic information:                                                                                      
-------------------------------------------------------------------                                                                 
   Temperature (Celsius)                 :41.88                                                                                     
   Voltage (V)                           :3.30                                                                                      
   Bias Current (mA)                     :34.43|33.06  (Lane0|Lane1)                                                                
                                          35.61|31.17  (Lane2|Lane3)                                                                
   Current RX Power (dBm)                :0.89|1.90    (Lane0|Lane1)                                                                
                                          2.55|2.71    (Lane2|Lane3)                                                                
   Current TX Power (dBm)                :2.75|2.18    (Lane0|Lane1)                                                                
                                          2.24|2.42    (Lane2|Lane3)                                                                
-------------------------------------------------------------------                                                                 
                                                                                                                                    
10GE1/0/3 transceiver diagnostic information:                                                                                      
-------------------------------------------------------------------                                                                 
   Temperature (Celsius)                 :33.25                                                                                     
   Voltage (V)                           :3.30                                                                                      
   Bias Current (mA)                     :45.39|60.52  (Lane0|Lane1)                                                                
                                          43.26|60.76  (Lane2|Lane3)                                                                
   Current RX Power (dBm)                :1.17|-0.91   (Lane0|Lane1)                                                                
                                          0.88|0.90    (Lane2|Lane3)                                                                
   Current TX Power (dBm)                :1.69|1.23    (Lane0|Lane1)                                                                
                                          0.42|2.25    (Lane2|Lane3)                                                                
-------------------------------------------------------------------

```

**Table 1** Description of the **display interface transceiver** command output
| Item | Description |
| --- | --- |
| Common information | Basic information about an optical module. |
| Transceiver Type | Type of the optical module. |
| Connector Type | Interface type. |
| Wavelength (nm) | Optical wavelength of the optical module. |
| Transfer Distance (m) | Transmission distance of the optical wave. Xum/Yum indicates the diameter of an optical fiber. OM1 to OM4 indicate multi-mode optical fibers, and SMF indicates single-mode optical fibers. |
| Digital Diagnostic Monitoring | Whether diagnostic information about the optical module is monitored. |
| Diagnostic information | Diagnostic information about the optical module.  If this field displays -, querying diagnostic information about this optical module is not supported or diagnostic information is incorrect. |
| Vendor Name | Vendor name of the optical module.  On a switch, if this field displays HUAWEI, the optical module is certified for Huawei. If this field displays other contents, the optical module is not certified for Huawei. |
| Vendor Part Number | Vendor part number of the optical module. |
| Ordering Name | External name of the optical module. |
| Manufacture information | Manufacturing information of an optical module. |
| Manu. Serial Number | Serial number of the optical module. |
| Manufacturing Date | Manufacturing date of an optical module. |
| Alarm information | Alarm information about an optical module. |
| Warning information | Warning information about the optical module. |
| Temperature (Celsius) | Current temperature of an optical module. |
| Voltage (V) | Current voltage of the optical module. |
| Bias Current (mA) | Bias current of the optical module.  If an interface can be split and has an optical module installed, the bias current of each lane of the optical module is displayed. |
| Bias High Threshold (mA) | Upper bias current threshold of the optical module. |
| Bias Low Threshold (mA) | Lower bias current threshold of the optical module. |
| Current RX Power (dBm) | Current receive power of the optical module.  If an interface can be split and has an optical module installed, the current receive power of each lane of the optical module is displayed. |
| Current TX Power (dBm) | Current transmit power of the optical module.  If an interface can be split and has an optical module installed, the current transmit power of each lane of the optical module is displayed. |
| Default RX Power High Threshold (dBm) | Default upper threshold of the receive power of the optical module. |
| Default RX Power Low Threshold (dBm) | Default lower threshold of the receive power of the optical module. |
| Default TX Power High Threshold (dBm) | Default upper threshold of the transmit power of the optical module. |
| Default TX Power Low Threshold (dBm) | Default lower threshold of the transmit power of the optical module. |