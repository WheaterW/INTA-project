Configuring a Cable Length Test
===============================

Configuring a Cable Length Test

#### Context

If a cable is faulty, the interface goes down, or the interface rate is abnormal even if the interface is up. Virtual cable test (VCT) technology uses time domain reflectometry (TDR) to detect the cable status. When pulse signals are transmitted in a cable, some energy of the signals is reflected at the end or a failure point on the cable. This phenomenon is called TDR. The VCT algorithm measures the time spent on transmitting pulses over cables, reaching the failure point, and returning the pulses. The measured time is converted to the distance. You can configure a cable length test to help locate a cable fault.

* If a cable works properly, the total length of the cable is displayed.
* If a cable fault occurs, the length of the cable between the interface and failure point is displayed, which is shorter than the total length of the cable.

![](public_sys-resources/note_3.0-en-us.png) 

* After the [**virtual-cable-test**](cmdqueryname=virtual-cable-test) command is run on an interface, the interface goes down, and services on the interface may be affected in a short period of time. After the test succeeds, the interface goes up.
* The margin of error in the VCT test is about 10 m. The test result is for reference only and does not guarantee the accuracy for cables produced by all manufacturers. You are advised to use a cable tester for an accurate test.
* Before performing a cable test, remove the network cable from the remote interface. Otherwise, signals from the remote interface may make the test result inaccurate.
* Only GE electrical interfaces or optical interfaces that have GE copper modules installed support this function.


#### Procedure

1. (Optional) Check the cable length test result.
   
   
   ```
   [display interface](cmdqueryname=display+interface) { interface-type interface-number | interface-name } virtual-cable-test
   ```
2. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Configure a cable length test.
   
   
   ```
   [virtual-cable-test](cmdqueryname=virtual-cable-test)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

Run the [**reset interface**](cmdqueryname=reset+interface) { *interface-type* *interface-number* | *interface-number* } **virtual-cable-test** command to clear the cable length test result.