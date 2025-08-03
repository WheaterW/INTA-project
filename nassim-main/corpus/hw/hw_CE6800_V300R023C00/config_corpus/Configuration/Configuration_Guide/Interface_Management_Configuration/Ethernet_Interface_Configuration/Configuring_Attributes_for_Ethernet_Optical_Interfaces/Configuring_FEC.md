Configuring FEC
===============

Configuring FEC

#### Context

Forward error correction (FEC) is a bit error correction technology that adds correction information to data packets at the transmit end, and corrects bit errors generated during transmission of data packets at the receive end based on the correction information. While FEC improves the signal quality, it also increases the delay of signal transmission. You can enable or disable this function as required.

Devices support the following FEC modes: Base-R FEC, Reed-Solomon Forward Error Correction (RS-FEC), and NONE.

* Base-R FEC: The Base-R FEC function can be enabled or disabled on the following interfaces:
  
  + 25GE interfaces working at 25 Gbit/s, 50GE interfaces, and 25GE interfaces split from a 100GE interface
  + 100GE interfaces working at 50 Gbit/s and 50GE interfaces split from a 100GE interface![](public_sys-resources/note_3.0-en-us.png) 
  
  A 100GE interface and 25GE interfaces split from the 100GE interface on the CE8855, CE8851-32CQ4BQ, CE6885-SAN, CE6885, CE6885-T, CE6885-LL, CE6855-48XS8CQ, and CE6863E-48S8CQ do not support the Base-R FEC function.
* RS-FEC: The RS-FEC function can be enabled or disabled on the following interfaces:
  
  + 25GE interfaces working at 25 Gbit/s, 50GE interfaces and 25GE interfaces split from a 100GE interface
  + 100GE interfaces working at 50 Gbit/s and 50GE interfaces split from a 100GE interface
  + 100GE, 200GE, and 400GE interfaces working at 100 Gbit/s
* NONE: FEC is disabled.

FEC is a function requiring auto-negotiation on an interface. If auto-negotiation is enabled, the local and remote interfaces negotiate whether to enable or disable FEC. If auto-negotiation is disabled, the default FEC mode is used. You can configure Base-R FEC, RS-FEC, or NONE (disabling FEC) on an interface based on the interface's support for FEC. If FEC is enabled at one end of a link, it must also be enabled at the other end of the link. If the interfaces at both ends of a link support both Base-R FEC and RS-FEC, the interfaces work in RS-FEC mode after auto-negotiation.

The FEC enabling configuration is mutually exclusive with auto-negotiation and interface rate configurations on an interface, and is automatically deleted when auto-negotiation is enabled or a rate is configured on the interface.

![](public_sys-resources/note_3.0-en-us.png) 

* The default FEC mode on an interface varies according to the device model and connection medium. You can run the [**display interface**](cmdqueryname=display+interface) command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check whether the FEC function is enabled on an interface based on the **Fec** field in the command output.
* Interfaces at both ends of a link must work in the same FEC mode; otherwise, the interfaces do not go up. If their FEC modes are different, configure the same FEC mode on the interfaces when they work in non-auto-negotiation mode.
* The FEC mode can be changed only after auto-negotiation is disabled.
* When interfaces are connected using 25GE media, enable the FEC function at both ends of each involved link to reduce the transmission bit error rate and error packets on each link.


#### Procedure

* Enable the Base-R FEC function.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the Ethernet interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Enable the Base-R FEC function.
     
     
     ```
     [fec mode base-r](cmdqueryname=fec+mode+base-r)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable the RS-FEC function.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the Ethernet interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Enable the RS-FEC function.
     
     
     ```
     [fec mode rs](cmdqueryname=fec+mode+rs)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable the FEC function.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the Ethernet interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Disable the FEC function.
     
     
     ```
     [fec mode none](cmdqueryname=fec+mode+none)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The **fec mode none** command disables the FEC function, and the **undo fec mode** command restores the default FEC status. If the default FEC status is "disabled" for an optical module, the **fec mode none** and **undo fec mode** commands both can be used to disable FEC.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check the FEC information of the interface based on the **Fec** field in the command output.