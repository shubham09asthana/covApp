## CovApp (Vaccine slots from WhatsApp)

### Components:
    - Flask API for Python Web Framework
    - Requests for HTTP request generation
    - Flask Restful for REST API (Extension to Flask)
    - python-decouple to store config & secret values in .env


### Basic Idea:
    Setup a Sandbox (External to this project) to receive WhatsApp calls and transfer them in JSON format to this API. Later use that data to query availability of vaccination centers and slot counts. Finally return the filtered data to query originating sender.
    
### Sandbox used and setup:
The sandbox used here is "Vonage" (earlier Nexmo).
<svg class="Vlt-site-logo__vonage" width="91.3px" height="20.0px" viewBox="0 0 913 200" version="1.1" xmlns="http://www.w3.org/2000/svg" data-di-res-id="1e8d8655-39a8c671" data-di-rand="1621185562685">
<path fill="currentColor" d="M45.3408,0 L-0.0002,0 L64.6808,146.958 C65.1748,148.081 66.7718,148.07 67.2508,146.942 L88.7628,96.337 L45.3408,0 Z"></path>
<path fill="currentColor" d="M183.4502,0 C183.4502,0 113.9562,159.156 104.6482,173.833 C93.8292,190.896 86.6592,197.409 73.3912,199.496 C73.2682,199.515 73.1772,199.621 73.1772,199.746 C73.1772,199.886 73.2912,200 73.4312,200 L114.9552,200 C132.9432,200 145.9152,184.979 153.1042,171.714 C161.2742,156.637 229.5902,0 229.5902,0 L183.4502,0 Z"></path>
<path fill="currentColor" d="M365.0527,127.6431 C364.9567,127.8531 364.6577,127.8531 364.5617,127.6431 L330.0887,52.2061 L310.7207,52.2061 C310.7207,52.2061 346.2497,132.2541 349.7987,138.2351 C353.2667,144.0801 357.4637,148.8991 364.8077,148.8991 C372.1517,148.8991 376.3487,144.0801 379.8167,138.2351 C383.3657,132.2541 418.8947,52.2061 418.8947,52.2061 L399.5267,52.2061 L365.0527,127.6431 Z"></path>
<path fill="currentColor" d="M470.187,134.2002 C451.454,134.2002 439.186,121.9992 439.186,99.9992 C439.186,77.9992 451.454,65.8002 470.187,65.8002 C488.853,65.8002 501.186,77.9992 501.186,99.9992 C501.186,121.9992 488.853,134.2002 470.187,134.2002 M470.187,50.0002 C440.854,50.0002 421.987,69.0002 421.987,99.9992 C421.987,131.0002 440.854,150.0002 470.187,150.0002 C499.453,150.0002 518.387,131.0002 518.387,99.9992 C518.387,69.0002 499.453,50.0002 470.187,50.0002"></path>
<polygon fill="currentColor" points="617.4829 52.2002 617.4829 147.8002 597.6299 147.8002 551.3499 77.9072 551.3499 147.8002 534.4169 147.8002 534.4169 52.2002 554.3359 52.2002 600.6169 122.5592 600.6169 52.2002"></polygon>
<path fill="currentColor" d="M662.8662,108.6001 L679.5432,69.5551 C679.6372,69.3361 679.9462,69.3361 680.0392,69.5551 L696.7162,108.6001 L662.8662,108.6001 Z M679.7912,51.1071 C672.8172,51.1071 668.5552,56.3981 665.7452,61.6891 C662.8662,67.1111 628.4302,147.8001 628.4302,147.8001 L646.1242,147.8001 L656.0112,124.6511 L703.5712,124.6511 L713.4582,147.8001 L731.1512,147.8001 C731.1512,147.8001 696.7162,67.1111 693.8372,61.6891 C691.0272,56.3981 686.7642,51.1071 679.7912,51.1071 L679.7912,51.1071 Z"></path>
<path fill="currentColor" d="M779.0156,110.9336 L809.3046,110.9336 C809.1626,125.7876 795.2966,134.2006 780.5996,134.2006 C762.1676,134.2006 750.0976,121.9986 750.0976,99.9996 C750.0976,76.2466 761.2716,65.6606 781.6336,65.6606 C794.3806,65.6606 804.9786,70.8726 807.2096,82.8856 L824.7716,82.8856 C821.6926,61.8536 802.3226,49.9996 780.5996,49.9996 C751.7376,49.9996 733.1746,68.9996 733.1746,99.9996 C733.1746,130.9996 751.7376,149.6286 780.5996,149.6286 C792.7686,149.6286 805.0416,143.1036 809.3636,136.2116 L809.3076,147.7996 L825.5076,147.7996 L825.5076,118.3036 L825.5076,96.3036 L779.0156,96.3036 L779.0156,110.9336 Z"></path>
<polygon fill="currentColor" points="912.5908 68.1992 912.5908 52.2002 843.8578 52.2002 843.8578 147.8002 912.5908 147.8002 912.5908 131.7992 860.7908 131.7992 860.7908 106.6672 908.5508 106.6672 908.5508 90.6662 860.7908 90.6662 860.7908 68.1992"></polygon>
</svg>

    Signup and setup an account. You'll get a Virtual phone number and a Topic to subscribe. Send the Topic to the number from your WhatsApp. Now, we are ready to hit our API from WhatsApp.
  

    Store the apiKey and apiSecret in the .env file.
  

### How to Use CovApp?
    
1. Rename the .env.template file to .env and put the api & secter keys there.
2. From your WhatsApp send **join hung cola** to **+1(415)738-6170**
or click   [Join.](https://web.whatsapp.com/send?phone=14157386170&text=Join%20hung%20cola)
3. send a hi/Hello to get operation instructions.




#### TO DO:
1. When sending senddata(), store the respose from server to a send_data.logs file.

2. Store the logs of /got acknowledgement to server_msg_ack.logs file.


### Requirement Dependencies  
1. Requirements for Package: **flask**  
click==8.0.0  
colorama==0.4.4  
Flask==2.0.0  
itsdangerous==2.0.0  
Jinja2==3.0.0  
MarkupSafe==2.0.0  
Werkzeug==2.0.0  

2. Requirements for Package: **flask_restful**  
aniso8601==9.0.1  
Flask-RESTful==0.3.8  
pytz==2021.1  
six==1.16.0  
  
3. Requirements for Package: **requests**  
certifi==2020.12.5   
chardet==4.0.0  
idna==2.10  
requests==2.25.1  
urllib3==1.26.4  

4. Requirements for Package: **python-decouple**  
python-decouple==3.4  

