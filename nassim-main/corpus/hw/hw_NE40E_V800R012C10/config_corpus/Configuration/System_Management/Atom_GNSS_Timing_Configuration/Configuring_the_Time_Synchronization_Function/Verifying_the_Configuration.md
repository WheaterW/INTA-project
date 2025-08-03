Verifying the Configuration
===========================

Verifying the Configuration

#### Context

After configuring the SyncE function of the Atom GNSS timing system, check the configurations.


#### Procedure

* Run the [**display ptp**](cmdqueryname=display+ptp) **all** [ **state** | **config** ] command to check the time synchronization status and configurations of the involved device.
* Run the [**display ptp**](cmdqueryname=display+ptp) **interface** *interface-type* *interface-number* command to check the time synchronization information about the specified interface.
* Run the [**display smart-clock**](cmdqueryname=display+smart-clock) **interface** *interface-type* *interface-number* command to check information about the Atom GNSS module on the specified interface.