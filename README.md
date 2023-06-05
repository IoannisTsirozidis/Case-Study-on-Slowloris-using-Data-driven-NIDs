# ABSTRACT

This thesis focuses on the conceptual framework of Denial of Service (DoS) attacks, particularly the Slowloris attack and its characteristics. It introduces terminologies related to threat detection and countermeasures in modern network traffic environments. The research’s scope also includes the intrinsic characteristics of related DoS attacks and proposes data analysis techniques for their detection. Moreover, a Python implementation of a majority Isolation Forest model is proposed as a detection methodology for Slowloris attacks, which achieves an accuracy of 94.3% on a deliberately selected dataset. The thesis also explores visualization techniques for network traffic analysis to gain insights into Slowloris behavior and provides real-time simulation guides for launching a Slowloris attack from a local computer, resulting in a denial of service on the local Apache server.

<br>


The Statistical Majority Isolation Forest model was employed to detect Slowloris attacks in data-at-rest. Through the utilization of network metrics aligned with Slowloris behavior, the model achieved an accuracy of 94.36%, with a precision of 99.36% and a recall of 94.91%. These results were obtained by deliberately selecting data specifically designed to exhibit Slowloris characteristics. 
<img src="https://github.com/IoannisTsirozidis/Study-on-Slowloris-using-data-driven-NID/blob/main/Statistics%20and%20Graphs/tree.png" alt="Alt Text" width="300" height="200">
<img src="https://github.com/IoannisTsirozidis/Study-on-Slowloris-using-data-driven-NID/blob/main/Statistics%20and%20Graphs/anomaly_i.png" alt="Alt Text" width="140" height="200">

<br>
<br>

The graphical analysis further confirmed the role of a Denial of Service (DoS) attack like Slowloris. It was observed that this attack gradually induces congestion on the receiver's end by sending incomplete HTTP packets, ultimately rendering it incapable of responding to legitimate requests. As a consequence, network performance declines significantly.


<div style="display:flex">
    <img src="https://github.com/IoannisTsirozidis/Study-on-Slowloris-using-data-driven-NID/blob/main/Statistics%20and%20Graphs/graphical_after_slowhttptest.png" alt="Alt Text" width="200" height="150" style="margin-right:10px;">
    <img src="https://github.com/IoannisTsirozidis/Study-on-Slowloris-using-data-driven-NID/blob/main/Statistics%20and%20Graphs/flow%20iat%20max.png" alt="Alt Text" width="200" height="150">
</div>



