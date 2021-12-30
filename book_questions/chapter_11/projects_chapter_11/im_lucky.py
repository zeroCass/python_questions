import bs4
import webbrowser
import requests
import sys
import os



def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    assert len(sys.argv) > 1, 'Error! The command cannot be empty'

    headers = {
        #'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; HSID=AenmNVZxnoADsXz_x; SSID=AjbLhhwkjh8f3FOM8; APISID=IqkNtUA0V2DXlees/A0tA9iPSadMC2X6dt; SAPISID=8-N4B06I_D5N1mvR/AleccT6Zt0QllrukC; CONSENT=YES+UA.en+; OTZ=5204669_48_48_123900_44_436380; SID=rAd3UAFN_dCIGQ87HqDZZGiNyxdz0dL4dZKy_XquqSr_CHTzqSzfDdNTfLmA2xCMEZOZMA.; ANID=AHWqTUnDWUSHdvWhJiIoPxMAKYXmVtHCQIq7LBMYgiSlZZr3AMGTwY2aVUdjeY7z; NID=193=QImFbOa1vnKpflG8yJytqPXbJYJ9k8fWbIzQMGExsMa4g5oJwdnI56WNjgEVFAyAPJ1SEEOQ-zlW4HAUv-JLj0yAUImTgeT1syDIgFTMWAqxdz10lWRlzFC-3Fmjv6xJcqm2o6RKI50dmb7GetiheNdSAYPkAjng_c0lOHoXZLmtMwFOpkPTrQwVyUW8R2x4o1ux3OW3_kEbR_BREowRV8lVqrsnyo1ffC_Pm40zf81k7aS0cv9esYweGHF6Lxd532z4wA; 1P_JAR=2019-12-06-16; DV=k7BRh0-RaJtZsO9g7sjbrkcKoUjC7RYhxDh5AdfYgQAAAID1UoVsAVkvPgAAAFiry7niUB6qLgAAAGCQehpdCXeKnikKAA; SEARCH_SAMESITE=CgQIvI4B; SIDCC=AN0-TYv-lU3aPGmYLEYXlIiyKMnN1ONMCY6B0h_-owB-csTWTLX4_z2srpvyojjwlrwIi1nLdU4',
        'cookie': 'SEARCH_SAMESITE=CgQIhJQB; OTZ=6275120_68_68__68_; SID=FAgLuW_71bvgv32EDUx-xgIH7N8A89BIh3xp5iFpIdcmxo26tt5U7FneRwFpgBXWIgzmkw.; __Secure-1PSID=FAgLuW_71bvgv32EDUx-xgIH7N8A89BIh3xp5iFpIdcmxo26YtDY7s-X9ybuIObHw2R7JA.; __Secure-3PSID=FAgLuW_71bvgv32EDUx-xgIH7N8A89BIh3xp5iFpIdcmxo26dmUxI9T1OalAHSU2DGXC-Q.; HSID=Afn-Nv2ATUqA36sMA; SSID=AbhSH1tNWFXHFvFYy; APISID=jsDQLQE0VaCrqhyR/A6UGvirXlz3IAPg0J; SAPISID=HqnJ__qzNR7OMxGb/AT_kMpZjM_5RzVMZr; __Secure-1PAPISID=HqnJ__qzNR7OMxGb/AT_kMpZjM_5RzVMZr; __Secure-3PAPISID=HqnJ__qzNR7OMxGb/AT_kMpZjM_5RzVMZr; OGPC=19025003-1:; NID=511=ZuCpdsDu1reiBBjWN0Z56CLclWZyKoI8dUyQ_rNPiCucEY-sfX2gRYJVSJH0Rd6BWqXnvJmL4ANRhjmKtRhrNcG3_VsAMPnl5DsuHCbcSfhXHft0xTJOiwOXUSJXCvhsG9NhOibR5zAoPebRi6CvW7LStOjq-ChLinaEV83K4z0iRMrlY533gF9pImMGREDu5hH03JFfJbe50CI93ODSLVDV2WLq8WSOXAYZ0f6w7C697QgOZRvEmhOtljJBTy4c6GMTcJOB4W1posYLVxXWfh2yR9c3YxrSm-bIJLREvHHgGQ-0zAXnKqeM1H9i8euzVpNVEhWr; 1P_JAR=2021-12-29-20; DV=U9a_dp_ZC61BkFjbmuSQit4o-KF94Jf69YyshsVrDQEAALBLt0wajdG3lQAAAAhSt0bRcateSwAAAA; SIDCC=AJi4QfEcTZLd9ybdo6lVy3XE0JGbSx0jWrYs0ek5W6NM3IbrOkC11MYMa57yPNa3bCMilzYwPJYq; __Secure-3PSIDCC=AJi4QfHfFehm8uW9FBcvYiWbThPaFbPNVVWIFGYcLoiSsomF4-sOKJzR-tIFr_yorXKMMpAjbXc',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.142 Chrome/75.0.3770.142 Safari/537.36'
    }

    res = requests.get('https://www.google.com/search', headers=headers, params={'q': ''.join(sys.argv[1:])})
    res.raise_for_status()

    for element in bs4.BeautifulSoup(res.text, 'html.parser').select('div.yuRUbf a'):
        link = element.get('href')
        if 'webcache' not in link and 'search' not in link and '#' not in link:
            webbrowser.open(link)

if __name__ == '__main__':
    main()

