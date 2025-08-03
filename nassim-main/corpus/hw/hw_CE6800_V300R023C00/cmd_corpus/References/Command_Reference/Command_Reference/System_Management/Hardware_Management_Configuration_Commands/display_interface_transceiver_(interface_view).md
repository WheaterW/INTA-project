display interface transceiver (interface view)
==============================================

display interface transceiver (interface view)

Function
--------

The **display interface transceiver** command displays optical module information on a specified interface.



Format
------

**display interface transceiver**

**display interface transceiver verbose**

**display interface transceiver brief**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed optical module information on interfaces, including basic information, manufacturing information, alarm information, and diagnostic information. | - |
| **brief** | Displays brief optical module information. | - |




Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

You can view basic information, manufacturing information, and alarm information about optical modules on interfaces of the device by using the display interface transceiver command. If the verbose parameter is specified, diagnostic information is also displayed.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display brief information about the optical module on a specified interface.
```
<HUAWEI> system-view
[HUAWEI] interface 10GE0/0/0
[HUAWEI-10GE0/0/0] display interface transceiver

 10GE0/0/0 transceiver information:
-------------------------------------------------------------------
 Common information:
   Transceiver Type                      :10GBASE_USR
   Connector Type                        :LC
   Wavelength (nm)                       :850
   Transfer Distance (m)                 :20(62.5um/125um OM1)
                                          50(50um/125um OM2)
                                          100(50um/125um OM3)
   Digital Diagnostic Monitoring         :YES
   Vendor Name                           :Hisense
   Vendor Part Number                    :LTF8501-BC+
   Ordering Name                         :
-------------------------------------------------------------------
 Manufacture information:
   Manu. Serial Number                   :U7MA6H18357
   Manufacturing Date                    :2020-6-8
   Vendor Name                           :Hisense
-------------------------------------------------------------------
 Alarm information:
    Non-Huawei-certified transceiver
-------------------------------------------------------------------
 Warning information:
-------------------------------------------------------------------

```

# Display detailed information about the optical module on a specified interface.
```
<HUAWEI> system-view
[HUAWEI] interface 10GE0/0/0
[HUAWEI-10GE0/0/0] display interface transceiver verbose

 10GE0/0/0 transceiver information:
-------------------------------------------------------------------
 Common information:
   Transceiver Type                      :10GBASE_USR
   Connector Type                        :LC
   Wavelength (nm)                       :850
   Transfer Distance (m)                 :20(62.5um/125um OM1)
                                          50(50um/125um OM2)
                                          100(50um/125um OM3)
   Digital Diagnostic Monitoring         :YES
   Vendor Name                           :Hisense
   Vendor Part Number                    :LTF8501-BC+
   Ordering Name                         :
-------------------------------------------------------------------
 Manufacture information:
   Manu. Serial Number                   :U7MA6H18357
   Manufacturing Date                    :2020-6-8
   Vendor Name                           :Hisense
-------------------------------------------------------------------
 Alarm information:
    Non-Huawei-certified transceiver
-------------------------------------------------------------------
 Warning information:
-------------------------------------------------------------------
 Diagnostic information:
   Temperature (Celsius)                 :30.90
   Voltage (V)                           :3.28
   Bias Current (mA)                     :6.44
   Bias High Threshold (mA)              :15.00
   Bias Low Threshold (mA)               :0.00
   Current RX Power (dBm)                :-3.07
   Default RX Power High Threshold (dBm) :2.50
   Default RX Power Low Threshold (dBm)  :-12.70
   Current TX Power (dBm)                :-2.64
   Default TX Power High Threshold (dBm) :1.00
   Default TX Power Low Threshold (dBm)  :-9.30
-------------------------------------------------------------------

```

# Display brief information about the optical module on a specified interface.
```
<HUAWEI> system-view
[HUAWEI] interface 10GE0/0/0
[HUAWEI-10GE0/0/0] display interface transceiver brief

10GE0/0/0 transceiver diagnostic information:
-------------------------------------------------------------------
   Temperature (Celsius)                 :30.91
   Voltage (V)                           :3.28
   Bias Current (mA)                     :6.44
   Current RX Power (dBm)                :-3.07
   Current TX Power (dBm)                :-2.64
-------------------------------------------------------------------

```


**Table 1** Description of the
**display interface transceiver (interface view)** command output

| Item | Description |
| --- | --- |
| Common information | Basic information about an optical module. |
| Transceiver Type | Type of the optical module. |
| Connector Type | Interface type. |
| Wavelength (nm) | Optical wavelength of the optical module. |
| Transfer Distance (m) | Transmission distance of the optical wave. Xum/Yum indicates the diameter of an optical fiber. OM1 to OM4 indicate multi-mode optical fibers, and SMF indicates single-mode optical fibers. |
| Digital Diagnostic Monitoring | Whether diagnostic information about the optical module is monitored. |
| Diagnostic information | Diagnostic information about the optical module.  If this field displays -, querying diagnostic information about this optical module is not supported or diagnostic information is incorrect. |
| Vendor Name | Vendor name of an optical module.  If HUAWEI is displayed, the optical module is a Huawei-certified optical module. If other information is displayed, the optical module is a non-Huawei-certified optical module. |
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