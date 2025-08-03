Verifying the Basic FR Function Configuration
=============================================

After configuring basic FR functions, verify the configuration.

#### Prerequisites

Basic FR functions have been configured.
#### Procedure

* Run the [**display fr interface**](cmdqueryname=display+fr+interface) [ *interface-type* *interface-number* ] command to check FR protocol status and interface information on a specific interface.
* Run the [**display fr pvc-info**](cmdqueryname=display+fr+pvc-info) [ **interface** *interface-type* *interface-number* ] [ **dlci** *dlci-number* ] command to check VC configurations and statistics.
* Run the [**display fr lmi-info**](cmdqueryname=display+fr+lmi-info) [ **interface** *interface-type* *interface-number* ] command to check statistics about received and sent LMI packets.
* Run the [**display fr statistics**](cmdqueryname=display+fr+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics about received and sent data.