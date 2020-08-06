<?php
//post
$url="http://www.way2sms.com/api/v1/sendCampaign";
$message = urlencode("message-text");// urlencode your message
$curl = curl_init();
curl_setopt($curl, CURLOPT_POST, 1);// set post data to true
curl_setopt($curl, CURLOPT_POSTFIELDS, "apikey=[H8X86V4G7YVP1YMIHLDK3N8J80I3I23T]&secret=[1GO0MOA8DFQDYI8S]&usetype=[stage]&phone=[$mobile]&senderid=[vgoel116@gmail.com]&message=[$message]");// post data
// query parameter values must be given without squarebrackets.
 // Optional Authentication:
curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
$result = curl_exec($curl);
curl_close($curl);
echo $result;
?>