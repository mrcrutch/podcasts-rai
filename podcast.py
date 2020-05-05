#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

podcasts = []

html_header="""

<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title>Podcast RAI</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        #outlook a {
            padding: 0;
        }

        body {
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        table,
        td {
            border-collapse: collapse;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
            -ms-interpolation-mode: bicubic;
        }

        p {
            display: block;
            margin: 13px 0;
        }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet">
    <style>
        @import url(https://fonts.googleapis.com/css?family=Roboto:300,400,500,700);
        @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
    </style>
    <style>
        @media only screen and (min-width:480px) {
            .mj-column-per-100 {
                width: 100% !important;
                max-width: 100%;
            }

            .mj-column-per-50 {
                width: 50% !important;
                max-width: 50%;
            }
        }
    </style>
    <style>
    </style>
    <style>
        .main-container {
            width: 40%;
        }

        .header {
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
        }

        p {
            line-height: 1.4em;
        }

        h2 {
            font-weight: 500;
        }

        .footer p {
            font-size: 12px;
            margin-bottom: 0;
            margin-top: 0em;
        }

        @media screen and (max-width: 800px) {
            .main-container {
                width: 90%;
            }

            #button-password,
            #button-client {
                height: 80px !important;
            }
        }

        @media screen and (max-width: 354px) {
            #buttons-container {
                display: flex !important;
                flex-direction: column !important;
                align-content: center !important;
                justify-items: center !important;
                align-items: center !important;
            }

            .button-wrapper {
                width: 300px !important;
            }

            #button-password,
            #button-client {
                width: 300px;
            }
        }
    </style>
</head>

<body style="background-color:#f3f3f3;">
    <div style="background-color:#f3f3f3;">
        <div style="background:#499Be6;background-color:#499Be6;margin:0px auto;max-width:100%;">
            <table align="center" cellpadding="0" cellspacing="0" role="presentation"
                style="background:#499Be6;background-color:#499Be6;width:100%;">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px; padding: 20px 0 100;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                                    width="100%">
                                    <tr>
                                        <td align="center" class="header"
                                            style="font-size:0px;padding:10px 25px;word-break:break-word; height: 50px;">
                                            <div
                                                style="font-family:roboto;font-size:20px;line-height:1;text-align:center;color:black;">
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div style="margin:0px auto;max-width:100%;">
            <table align="center" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                                    width="100%">
                                    <tr>
                                        <td align="center"
                                            style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                            <div
                                                style="font-family:roboto;font-size:20px;line-height:1;text-align:center;color:black;">
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center"
                                            style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                            <div
                                                style="font-family:roboto;font-size:20px;line-height:1;text-align:center;color:black;">
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="main-container" style="background:#fefefe;background-color:#fefefe;margin:0px auto;max-width:100%;">
            <table align="center" cellpadding="0" cellspacing="0" role="presentation"
                style="background:#fefefe;background-color:#fefefe;width:100%;">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding: 30px 0 0px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                                    width="100%">
                                    <tr>
                                        <td align="center"
                                            style="font-size:0px;padding:0px 25px 10px 25px;word-break:break-word;">
                                            <div
                                                style="font-family:roboto;font-size:14px;line-height:1;text-align:center;color:black;">
                                                <h2 style="margin-top: 0;">Podcast RAI</h2>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                            <div
                                                style="font-family:roboto;font-size:14px;line-height:1;text-align:left;color:black;">


"""

html_footer = """

                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>

"""


f = open("podcasts.html", "w")
f.write(html_header)


for i in range(300):
    i = str(i)
    link = "http://www.radio.rai.it/rss/podcast/rssradio.jsp?id="+i
    linkreq = requests.get(link)

    soup = BeautifulSoup(linkreq.text, 'html.parser')
    titolo = soup.find('title')
    if titolo is not None:
        if "Radio1" in soup.text or "Radio 1" in soup.text:
           channel="RF1"
        elif "Radio2" in soup.text or "Radio 2" in soup.text:
           channel="RF2"
        elif "Radio3" in soup.text or "Radio 3" in soup.text:
           channel="RF3"
        else:
           channel=""

        link = link+"&channel="+channel
        f.write("<p align=""left""><a href="+link+">"+titolo.string+"</a></p>")


f.write(html_footer)
f.close()
