Verifying the Configuration
===========================

After configuring TWAMP, verify the configuration.

#### Prerequisites

All configurations of TWAMP are complete.


#### Procedure

* Run the [**display twamp global-info**](cmdqueryname=display+twamp+global-info) command to check global information about TWAMP.
* Run the [**display twamp control-session**](cmdqueryname=display+twamp+control-session) [ **verbose** | **client-ip** *client-ip-address* **client-port** *client-port-number* [ **vpn-instance** *vpn-instance-name* ] ] command to check information about TWAMP control sessions on the Server.
* Run the [**display twamp test-session**](cmdqueryname=display+twamp+test-session) [ **verbose** | **reflector-ip** *reflector-ip-address* **reflector-port** *reflector-port-number* [ **vpn-instance** *vpn-instance-name* ] ] command to check information about TWAMP test sessions on the Session-Reflector.