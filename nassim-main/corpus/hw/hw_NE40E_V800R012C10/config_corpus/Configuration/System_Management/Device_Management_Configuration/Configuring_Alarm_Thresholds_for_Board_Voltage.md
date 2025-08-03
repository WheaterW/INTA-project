Configuring Alarm Thresholds for Board Voltage
==============================================

Configuring Alarm Thresholds for Board Voltage

#### Context

Generally, the default alarm threshold range for board voltage is large. When the voltage of the external power supply is unstable and fluctuates greatly, the device may restart. However, before the device restarts, the board voltage may not reach the alarm threshold. As a result, no voltage alarm is reported in a timely manner. In this scenario, you can configure an alarm threshold for board voltage based on the environment conditions. In this way, when the board voltage reaches the alarm threshold, an alarm is generated to prompt the maintenance personnel to adjust the working environment variables of the device in a timely manner.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**voltage-threshold**](cmdqueryname=voltage-threshold) **slot** *slot-id* **i2cid** *i2c-id* **address** *address* **channel** *channel-id* **low-major** *low-major-value* **low-fatal** *low-fatal-value* **high-major** *high-major-value* **high-fatal** *high-fatal-value*
   
   
   
   An alarm threshold is configured for board voltage.
   
   
   
   To restore the default alarm threshold for board voltage, run the [**undo voltage-threshold**](cmdqueryname=undo+voltage-threshold) **slot** *slot-id* **i2cid** *i2c-id* **address** *address* **channel** *channel-id* command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the **[**display voltage**](cmdqueryname=display+voltage)** [ **slot** *slot-id* ] command to check the configured alarm thresholds for board voltage.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before running the [**voltage-threshold**](cmdqueryname=voltage-threshold) command to configure an alarm threshold for board voltage, run the **[**display voltage**](cmdqueryname=display+voltage)** [ **slot** *slot-id* ] command to check the values of the **FatalL**, **MajorL**, **FatalH**, and **MajorH** fields in the command output.

* **MajorL**: default original threshold for a major undervoltage alarm.
* **FatalL**: default original threshold for a critical undervoltage alarm.
* **MajorH**: default original threshold for a major overvoltage alarm.
* **FatalH**: default original threshold for a critical overvoltage alarm.

After running the [**voltage-threshold**](cmdqueryname=voltage-threshold) command to configure an alarm threshold for board voltage, run the **[**display voltage**](cmdqueryname=display+voltage)** [ **slot** *slot-id* ] command to check the values of the **FatalL**, **MajorL**, **FatalH**, and **MajorH** fields in the command output.

* **MajorL**: threshold for a major undervoltage alarm, which is obtained by multiplying the original threshold for a major undervoltage alarm by *low-major-value*.
* **FatalL**: threshold for a critical undervoltage alarm, which is obtained by multiplying the original threshold for a critical undervoltage alarm by *low-fatal-value*.
* **MajorH**: threshold for a major overvoltage alarm, which is obtained by multiplying the original threshold for a major overvoltage alarm by *high-major-value*.
* **FatalH**: threshold for a critical overvoltage alarm, which is obtained by multiplying the original threshold for a critical overvoltage alarm by *high-fatal-value*.