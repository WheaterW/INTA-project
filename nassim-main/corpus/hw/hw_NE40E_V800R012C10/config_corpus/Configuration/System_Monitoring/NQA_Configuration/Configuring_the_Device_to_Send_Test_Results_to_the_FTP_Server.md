Configuring the Device to Send Test Results to the FTP Server
=============================================================

The NMS needs to obtain test results of devices. If the NMS cannot poll test results in time, test results are lost. Delivering the test results to the FTP server can save the test results to the maximum extent.

#### Usage Scenario

The result table of NQA test instances records results of each test type. A maximum of 5000 test result records are supported in total. If the number of records reaches 5000, test results are uploaded, and the new test result overwrites the earliest one. If the NMS cannot poll test results in time, test results are lost. You can configure the device to send test results to the FTP server through FTP when their number reaches the maximum capacity of local storage or periodically. This effectively prevents the loss of test results and facilitates network management based on the analysis of test results at different times.


#### Pre-configuration Tasks

Before configuring the device to send test results to the FTP server, complete the following tasks:

* Configure the FTP server.
* Configure a reachable route between the NQA client and the NMS.
* Configure a test instance.

#### Data Preparation

Before configuring the device to send test results to the FTP server, you need the following data.

| No. | Data |
| --- | --- |
| 1 | IP address of the FTP server |
| 2 | Username and password used for logging in to the FTP server |
| 3 | Name of a file in which test results are saved through FTP |
| 4 | Interval at which test results are uploaded through FTP |



[Setting Parameters for Configuring the Device to Send Test Results to the FTP Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0067.html)

Before starting a test instance, set the IP address of the FTP server that receives test results, username and password for logging in to the FTP server, name of the file in which test results are saved, interval at which test results are uploaded, and number of retransmissions.

[Starting a Test Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0068.html)

After a test instance is started, test results are periodically recorded in files.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0069.html)

After configuring the device to send test results to the FTP server, you can view the related configuration.