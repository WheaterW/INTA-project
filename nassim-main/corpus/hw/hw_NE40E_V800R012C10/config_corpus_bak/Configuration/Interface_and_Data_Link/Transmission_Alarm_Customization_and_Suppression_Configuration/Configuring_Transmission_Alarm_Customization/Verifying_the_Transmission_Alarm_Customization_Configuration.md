Verifying the Transmission Alarm Customization Configuration
============================================================

After configuring transmission alarm customization, verify the configuration and check the alarm status and statistics on an interface.

#### Prerequisites

Transmission alarm customization has been configured. The transmission alarm suppression function has been enabled using the [**transmission-alarm damping**](cmdqueryname=transmission-alarm+damping) command.


#### Procedure

* To check the alarm configuration on a POS interface, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) **pos** *interface-number* [ **auais** | **b1tca** | **b2tca** | **b3tca** | **lais** | **lcd** | **lof** | **lom** | **lop** | **los** | **lrdi** | **lrei** | **oof** | **pais** | **prdi** | **prei** | **pplm**| **puneq** | **rdool** | **rrool** | **sdbere** | **sfbere** | **trool** | **wlnk** ] \* command.
* To check the alarm configuration on a 10GE WAN interface, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) **wan** *interface-number* [ **auais** | **b3tca** | **lais** | **lcd** | **lof** | **lom** | **lop** | **los** | **lrdi** | **lrei** | **oof** | **pais** | **prdi** | **prei** | **pplm**| **puneq** | **rdool** | **rrool** | **sdbere** | **sfbere** | **trool** | **wlnk** ] \* command.
* To check the alarm configuration on a WDM interface, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) **wdm** *interface-number* [ **odu-ais** | **odu-lck** | **odu-oci** | **otu-ais** | **otu-lom** | **otu-sd-ber** | **otu-sf-ber** | **pm-bdi** | **pm-tim** | **r-lof** | **r-los** | **r-oof** | **sm-bdi** | **sm-iae** | **sm-tim** | **prefec-tca** | **odu-sd-ber** ] \* command.
* To check the alarm configuration on an E1 interface, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) **e1** *interface-number* [ **los** | **lof** | **pais** | **prai** ] \* command.
* To check the alarm configuration on a CPOS interface, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) **cpos** *interface-number* [ **auais** | **b1tca** | **b2tca** | **b3tca** | **lais** | **lof** | **lom** | **lop** | **los** | **lrdi** | **lrei** | **oof** | **pais** | **pplm** | **prdi** | **prei** | **puneq** | **rrool** | **sdbere** | **sfbere** ] command.
* To check the alarm configuration on an E3 interface, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) **e3** *interface-number* [ **los** | **lof** | **ais** | **rai** ] \* command.