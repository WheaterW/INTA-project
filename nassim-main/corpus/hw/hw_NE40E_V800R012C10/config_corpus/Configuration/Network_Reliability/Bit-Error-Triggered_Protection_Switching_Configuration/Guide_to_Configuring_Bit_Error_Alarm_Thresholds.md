Guide to Configuring Bit Error Alarm Thresholds
===============================================

This section describes common principles and methods for selecting bit error alarm and alarm clear thresholds.

A device detects the BER on an inbound interface. If the BER exceeds the bit error alarm threshold configured on the interface, the device determines that bit errors have occurred on the interface. When the BER of the interface falls below the bit error alarm clear threshold, the device determines that the bit errors have been cleared from the interface. To achieve the optimum effects of bit-error-triggered protection switching, select bit error alarm and alarm clear threshold properly.

An IP RAN may carry various types of base stations (such as BTSs, NodeBs, and eNodeBs) or different vendors' base stations. No uniform QoS standards are available for various base stations. Therefore, how to select bit error alarm and alarm clear thresholds is difficult for bit-error-triggered protection switching. The following selection principles can be used:

1. If a network carries different vendors' base stations, configure bit error alarm and alarm clear thresholds according to the most strict threshold requirements.
2. If voice and data services share channels on a network, configure bit error alarm and alarm clear thresholds according to the QoS requirements for voice services (because voice services are more sensitive).

The following describes common methods for selecting bit error alarm and alarm clear thresholds.

#### Wireless Vendors Can Provide Reference Thresholds

The most effective method for selecting bit error alarm and alarm clear thresholds is to directly obtain wireless vendors' standards for quality.

* Bit error alarm threshold
  
  Use the QoS indicator BER or PLR provided by a wireless vendor in some cases as a reference value of the bit error alarm threshold. These cases are that voice quality severely deteriorates, base stations are degraded, and base stations are out of service. To better protect services against bit errors, decrease the bit error alarm threshold. 80% of the critical BER is recommended as the bit error alarm threshold.
  
  If a PLR is provided, directly use the PLR as the bit error alarm threshold.
* Alarm clear threshold
  
  Use the QoS indicator BER or PLR provided by a wireless vendor in good voice quality cases as a reference value of the alarm clear threshold. In actual deployment, directly use 1/10 of the bit error alarm threshold as the alarm clear threshold.

#### Wireless Vendors Cannot Provide Reference Thresholds

For mainstream wireless vendors, it is recommended that you perform tests to obtain reference thresholds. Test methods are as follows:

* Test the impact of link bit errors on wireless services.
  
  Test procedure
  
  1. Prepare a test environment, and configure user services on IP RAN devices and on the wireless side.
  2. Enable the NodeB in the test environment.
  3. Configure basic functions on network devices, with bit-error-triggered protection switching not deployed. Check that services are normal and the NodeB does not generate any alarms.
  4. Connect a BER tester (generally network impairment emulator) between P devices.
  5. Use the BER tester to insert continuous BERs (such as 3e-5, 5e-5, 7e-5, 8e-5, 9e-5, 1e-4, 5e-4, and 1e-3) in two directions (NodeB and RNC directions).
  6. Observe for at least 5 minutes to check whether the NodeB generates an alarm.
  
  Test precautions
  
  1. The observation time can be changed as required (specially, the detection time requirement on the NodeB).
  2. It is recommended that you enable the bit error alarm function on the network devices to only report alarms but not to trigger protection switching. You can disable interface threshold settings to forcibly clear alarms after each test. Observe for 2 to 3 minutes before each test.
  3. It is recommended that you set the same time for devices, assign different engineers to observe and record the bit error insertion time, alarm times on the NodeB and network devices, and reserve the alarm logs on the NodeB and network devices.
* Test bit-error-triggered protection switching.
  
  Test procedure
  
  1. Prepare a test environment, and configure user services on IP RAN devices and on the wireless side.
  2. Enable the NodeB in the test environment.
  3. Configure basic functions on network devices. Check that services are normal and the NodeB does not generate any alarms.
  4. Connect a BER tester (generally network impairment emulator) between P devices.
  5. Enable bit error detection on interfaces, and set test alarm thresholds. It is recommended that you set the test alarm threshold to 9e-5 and the alarm clear threshold to 3e-5. Enable bit-error-triggered RSVP-TE tunnel switching if an RSVP-TE tunnel exists.
  6. Switchover test: Use the BER tester to insert continuous BERs (such as 3e-5, 5e-5, 7e-5, 8e-5, 9e-5, 1e-4, 5e-4, and 1e-3) in two directions. Then, observe bit error alarms on the network devices and alarms on the NodeB.
  7. Switchback test: Use the BER tester to insert continuous BERs (such as no bit error, 1e-5, and 2e-5) in two directions. Then, observe bit error alarms on the network devices and alarms on the NodeB.
  
  Repeat Step 5 through Step 7 to adjust the test alarm threshold and alarm clear threshold until finding an appropriate bit error alarm threshold and alarm clear threshold.
  
  Test precautions
  
  1. It is recommended that you set the same time for devices, assign different engineers to observe and record the bit error insertion time, alarm times on the NodeB and network devices, and reserve the alarm logs on the NodeB and network devices.
  2. For a switchover test, you can disable interface threshold settings to forcibly clear alarms after each test. Observe for 2 to 3 minutes before each test.