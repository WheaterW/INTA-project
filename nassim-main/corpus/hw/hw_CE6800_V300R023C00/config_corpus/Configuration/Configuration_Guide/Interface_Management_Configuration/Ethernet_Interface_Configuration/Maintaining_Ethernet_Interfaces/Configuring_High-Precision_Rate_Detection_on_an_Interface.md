Configuring High-Precision Rate Detection on an Interface
=========================================================

Configuring High-Precision Rate Detection on an Interface

#### Context

If packet loss occurs on an interface, enable high-precision rate detection on the interface to perform millisecond-level high-precision rate detection on the interface traffic for a certain period. This helps analyze packet loss on the interface.

![](public_sys-resources/note_3.0-en-us.png) 

* High-precision rate detection can be enabled on only one interface at a time.
* After high-precision rate detection is enabled on an interface, the previous detection result on the interface is cleared and the previous statistics cannot be restored. Therefore, exercise caution when you perform this operation.


#### Procedure

1. Enable high-precision rate detection for a specified period of time on an interface.
   
   
   ```
   [port high-precision rate detection interface](cmdqueryname=port+high-precision+rate+detection+interface) { interface-name | interface-type interface-num } [duration](cmdqueryname=duration) detect-value
   ```
   
   By default, high-precision rate detection is disabled on an interface.

#### Verifying the Configuration

Run the [**display port high-precision rate detection result**](cmdqueryname=display+port+high-precision+rate+detection+result) command to check the high-precision rate detection result on interfaces.