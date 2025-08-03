Verifying the Configuration of Outputting Information to a Local Device
=======================================================================

After configuring information management, verify the configuration.

#### Prerequisites

Information has been output to the local device.


#### Procedure

* Run the [**display channel**](cmdqueryname=display+channel) [ *channel-number* | *channel-name* ] command to check the channel through which information is output.
* Run the [**display info-center**](cmdqueryname=display+info-center) [ **statistics** ] command to check the information that information management records.
* Run the [**display logbuffer**](cmdqueryname=display+logbuffer) [ **security** ] [ **slot** *slot-id* | **module** *module-name* | **starttime** *starttime-value* [ **endtime** *endtime-value* ] | **level** { *severity* | { **emergencies** | **alert** | **critical** | **error** | **warning** | **notification** | **informational** | **debugging** } } | **size** *value* ] \* command to check the log information recorded in the log display area.
* Run the [**display trapbuffer**](cmdqueryname=display+trapbuffer) [ **size** *value* ] command to check trap information in the trap buffer.
* Run the [**display logfile**](cmdqueryname=display+logfile) *path* [ *offset* ] command to check information in the information file.