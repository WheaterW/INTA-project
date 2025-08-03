(Optional) Configuring Automatic Board Powering Off Under High Temperature
==========================================================================

(Optional) Configuring Automatic Board Powering Off Under High Temperature

#### Context

The high-temperature working environment reduces the board lifespan. You can run the [**display temperature**](cmdqueryname=display+temperature) command to check the temperature alarm thresholds on each board. The alarm levels are minor, major, and fatal. When the board temperature is higher than a specific threshold, the corresponding level of alarm occurs. When the temperature is 5°C below the alarm threshold, the alarm is cleared. After the [**high-temperature power-off**](cmdqueryname=high-temperature+power-off) command is run to enable automatic board powering off under high temperature, the board powers off automatically when temperatures of three or more monitoring nodes on the board are 5°C above the fatal high temperature alarm threshold.

In VS mode, this configuration process is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**high-temperature power-off**](cmdqueryname=high-temperature+power-off) **enable**
   
   
   
   Automatic board powering off under high temperature is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Run the [**display temperature**](cmdqueryname=display+temperature) command to check the board temperature.