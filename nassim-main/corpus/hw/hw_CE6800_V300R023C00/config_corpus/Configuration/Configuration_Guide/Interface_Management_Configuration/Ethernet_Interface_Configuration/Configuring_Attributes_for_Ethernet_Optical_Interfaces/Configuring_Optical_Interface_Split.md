Configuring Optical Interface Split
===================================

Configuring Optical Interface Split

#### Context

The interface split function splits a high-bandwidth physical interface on a device into multiple independent low-bandwidth interfaces. Users can select the high- or low-bandwidth interface based on the interface type on the remote device. This allows for flexible networking and lowers hardware costs.

The interface view is not changed after interface split. For example, after 100GE x/y/n is split into four 25GE interfaces, the 25GE interfaces are still in the 100GE interface view and are numbered 100GE x/y/n:1, 100GE x/y/n:2, 100GE x/y/n:3, and 100GE x/y/n:4.

**Interfaces That Can Be Split on a Device**

One 100GE interface can be split into four 25GE interfaces or two 50GE interfaces. When a 40GE 1-to-4 medium is installed on the four 25GE interfaces split from the 100GE interface, the interfaces automatically work at 10 Gbit/s. This is similar to the situation where the interface is split into four 10GE interfaces.

One 200GE interface can be split into two 100GE interfaces or four 50GE interfaces.

One 400GE interface can be split into four 100GE interfaces or two 200GE interfaces. Only CloudEngine 8800 series switches support this function.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6820H, CE6820S, CE6881H, and CE6863H do not support this configuration.

Among 100GE interfaces numbered from 1 to 32 on the CE8851-32CQ4BQ and CE8855, every four consecutive interfaces form a group. In each group, each odd-numbered interface can be split into four 25GE interfaces, and the even-numbered interfaces are unavailable. For example, interfaces 1 to 4 form a group in which interfaces 1 and 3 can be split and interfaces 2 and 4 are unavailable. Among 100GE interfaces numbered from 33 to 36, every two consecutive interfaces form a group. In each group, each interface can be split into four 25GE interfaces.

**Dynamic Interface Split**

Dynamic interface split takes effect without needing to restart the device.

You can determine whether dynamic interface split is supported according to the message displayed after the [**port split**](cmdqueryname=port+split) command is run. If the message "Warning: This operation will delete current port(s) and create new port(s). New port(s) will be offline before the board of slot 1 is reset." is displayed, the device needs to be restarted for dynamic interface split to take effect. If the message "Warning: This operation will delete current port(s) and create new port(s)." is displayed, dynamic interface split is supported, and the device does not need to be restarted.

**Interface Split Precautions**

After you configure or cancel interface split on an interface, the interface no longer exists, and its original configurations are lost and cannot be restored using the [**rollback configuration**](cmdqueryname=rollback+configuration) command. To restore the configurations, you have to configure them again. Therefore, exercise caution when configuring interface split.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure interface split.
   
   
   ```
   [port split](cmdqueryname=port+split) dimension [interface](cmdqueryname=interface) { interface-type interface-number1 [ to interface-type interface-number2 ] } &<1-24> [ split-type split-type ]
   ```
   
   Before running this command, you must ensure that the [**device card**](cmdqueryname=device+card) configuration exists in the corresponding slot on the device. Otherwise, the command configuration fails.
   
   When a subcard is available, the device generates the [**device card**](cmdqueryname=device+card) configuration by default. When a subcard is unavailable, you can run the [**device card**](cmdqueryname=device+card) *slot-id* **card-type** *type* command to create an offline subcard of a specified type in a specified slot.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display port split**](cmdqueryname=display+port+split) [ **all** | { **slot** *slot-id* } ] command to check interface split information.