Verifying the Configuration
===========================

After the service type and optional parameters of a PVC are configured, you can check the configuration of the service type template and the statistics.

#### Procedure

* Run the [**display interface atm**](cmdqueryname=display+interface+atm) [ *interface-number* [.*subinterface* ] ] command to check the configuration and status of the ATM interface or sub-interface.
* Run the [**display atm service**](cmdqueryname=display+atm+service) [ *service-name* ] command to check the configuration of the service type template.
* Run the [**display atm**](cmdqueryname=display+atm) { **pvc** | **pvp** } **statistics interface** **atm** *interface-number* [ **pvc** *vpi/vci* | **pvp** *vpi* ] command to check PVC or PVP statistics.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**display interface atm**](cmdqueryname=display+interface+atm) command displays the statistics of all the packets discarded on an interface. The [**display atm pvc statistics**](cmdqueryname=display+atm+pvc+statistics) command displays only the statistics about the packets dropped on the PVC or PVP due to traffic congestion. Therefore, run the commands as required.