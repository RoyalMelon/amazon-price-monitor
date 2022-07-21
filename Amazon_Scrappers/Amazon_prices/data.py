# [name, price, url]
mouse_data = [
    ['Logitech G PRO', 129.99, 'https://www.amazon.co.uk/Logitech-Wireless-Lightweight-Programmable-compatible/dp/B07G5XJLWK/ref=sr_1_1_sspa?crid=1SGOM1P0A1JYR&keywords=logitech+g+pro&qid=1657569967&sprefix=logitech+g+pro%2Caps%2C87&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN1VQNThMWlhHTkIxJmVuY3J5cHRlZElkPUEwMDA3MzEzMTNCTVdEMlRETUo2SSZlbmNyeXB0ZWRBZElkPUEwNDYxMzY3MjFBSVpFSk9MTlRJSSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='],
    ['Logitech G502 HERO', 79.99, 'https://www.amazon.co.uk/Logitech-Programmable-Buttons-Computer-Adjustable/dp/B07GS6ZB7T/ref=sr_1_2?crid=29Y4M15BHCEKL&keywords=logitech+g502&qid=1657570007&sprefix=logitech+g502+%2Caps%2C107&sr=8-2'],
    ['Logitech G502 LIGHTSPEED', 129.99, 'https://www.amazon.co.uk/Logitech-G502-Wireless-Programmable-Next-Generation/dp/B07QKC4WWD/ref=sr_1_1_sspa?crid=29Y4M15BHCEKL&keywords=logitech+g502&qid=1657570040&sprefix=logitech+g502+%2Caps%2C107&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSVVhJNjdZSE9SWlAmZW5jcnlwdGVkSWQ9QTA0Njg2ODUzSTNLNUY5Nk1DUERKJmVuY3J5cHRlZEFkSWQ9QTAxOTcwMzkzSTk1TzFTWkdXRlVNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='],
    ['Razer Basilisk X Hyperspeed', 59.99, 'https://www.amazon.co.uk/Razer-Basilisk-Hyperspeed-Wireless-Technology/dp/B07Y8QWZDW/ref=sr_1_2?crid=1SX1FV6MKTE5W&keywords=Razer+Basilisk+X+Hyperspeed&qid=1657570069&sprefix=razer+basilisk+x+hyperspeed%2Caps%2C107&sr=8-2'],
    ['Razer DeathAdder V2', 69.99, 'https://www.amazon.co.uk/Razer-DeathAdder-Programmable-Best-class/dp/B081QX9V2Y/ref=sr_1_1_sspa?crid=S1GLZLUKBWEU&keywords=Razer+DeathAdder+V2&qid=1657570101&sprefix=razer+deathadder+v2%2Caps%2C72&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQ0dKVUhBV0pORlE3JmVuY3J5cHRlZElkPUEwMzkwMTg5MVlBQ1ZGUk9YSE1BMCZlbmNyeXB0ZWRBZElkPUEwMTI2NzM2MkhLWEExS0ZSSVg4MiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='],
    ['HyperX Pulsefire Haste', 49.99, 'https://www.amazon.co.uk/HyperX-Pulsefire-Haste-Ultra-Lightweight-Programmable/dp/B08NSJFNSS/ref=sr_1_1_sspa?crid=3E3QQKH1AASR&keywords=HyperX+Pulsefire+Haste&qid=1657570123&sprefix=hyperx+pulsefire+haste%2Caps%2C81&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTDdFVElCVUxSNk00JmVuY3J5cHRlZElkPUEwNDk0MTQzMUpPV1pHUUVKWktJMSZlbmNyeXB0ZWRBZElkPUEwNjIwMTYxMlVCTExZNUFPTjVGSCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='],    
    ['SteelSeries Rival 3 - Gaming Mouse', 34.99, 'https://www.amazon.co.uk/SteelSeries-Rival-TrueMove-Optical-Programmable/dp/B082XQHPCL/ref=sr_1_2_sspa?crid=3KEN8YDFBEL69&keywords=steelseries+mouse&qid=1658402481&s=computers&sprefix=steel+series+mouses%2Ccomputers%2C79&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMFlQTEZRRFgxV1FEJmVuY3J5cHRlZElkPUExMDQwMDQ2RTBKQVhCSjlVWko2JmVuY3J5cHRlZEFkSWQ9QTAyNTIyNTVSVEZJMUJUQkwwVUUmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl']
]

kindle_data = [
    ['Kindle Paperwhite', 139.99, 'https://www.amazon.co.uk/kindle-paperwhite-8-gb-now-with-a-68-display-and-adjustable-warm-light-without-ads/dp/B08N36XNTT/ref=sr_1_1?crid=ELTD0JJJ9P65&keywords=kindle&qid=1657569863&smid=A3P5ROKL5A1OLE&sprefix=kindle%2Caps%2C84&sr=8-1']
]

alexa_data = [
    ['Echo Dot (4th generation)', 49.99, 'https://www.amazon.co.uk/all-new-echo-dot-4th-generation-smart-speaker-with-alexa-twilight-blue/dp/B084J4T28D/ref=sr_1_1?crid=3EBFI43V0EFBD&keywords=alexa&qid=1657569832&smid=A3P5ROKL5A1OLE&sprefix=alexa%2Caps%2C121&sr=8-1']
]

stylist_data = [
    ['Apple pencil (1st gen)', 89.00, 'https://www.amazon.co.uk/Apple-MU8F2ZM-A-Pencil-Generation/dp/B07K2PK3BV/ref=sr_1_3?crid=N9Z0Y52ZKDOO&keywords=apple+pen&qid=1657569811&sprefix=apple+pen%2Caps%2C91&sr=8-3'],
    ['Apple pencil (2nd gen)', 119.00, 'https://www.amazon.co.uk/Apple-MU8F2ZM-A-Pencil-Generation/dp/B07K2PK3BV/ref=sr_1_3?crid=N9Z0Y52ZKDOO&keywords=apple+pen&qid=1657569811&sprefix=apple+pen%2Caps%2C91&sr=8-3']
]

usb_data = [
    ['USB Hub BYEASY Leather Black', 13.99, 'https://www.amazon.co.uk/gp/product/B07FH7XJCD/ref=sw_img_1?smid=A24ZEWS70EBJCV&psc=1'],
    ['USB Hub CableCreation', 15.99, 'https://www.amazon.co.uk/CableCreation-4-Port-Aluminum-Durable-Braided-Black-4-8ft/dp/B01FJQGFK8/ref=sw_ttl_sspa_dk_huc_pt_expsub_2?_encoding=UTF8&pd_rd_i=B01FJQGFK8&pd_rd_w=cj5vb&pf_rd_p=6d4f32b8-6ffe-4e27-83fb-fbb33d1685f5&pf_rd_r=VTDM96SJD6D75PM1HRDV&pd_rd_wg=tJQqu&pd_rd_r=150b7872-1dcc-499c-a6aa-1e1bb676974c&content-id=amzn1.sym.6d4f32b8-6ffe-4e27-83fb-fbb33d1685f5&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMUI3UzdZV1pDVVlXJmVuY3J5cHRlZElkPUEwMDc4MTM5MkJMWjdBQ0U1Rk1FRyZlbmNyeXB0ZWRBZElkPUEwODkwNzQ5M09JUzFPWldMRTk5OSZ3aWRnZXROYW1lPXNwX2h1Y19tcmFpJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='],
    ['USB C Multiport Adapter, Lemorele', 30.99, 'https://www.amazon.co.uk/dp/B09B3GSRHV/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B09B3GSRHV&pd_rd_w=OaKnt&content-id=amzn1.sym.b48bef75-fcb4-4c94-965b-6a222af847b4&pf_rd_p=b48bef75-fcb4-4c94-965b-6a222af847b4&pf_rd_r=4DGWS6SQC5N9Z30Y2N0D&pd_rd_wg=BjxbO&pd_rd_r=3f5dd56d-d3b3-4d74-abf9-83d3ffcb6f37&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE3OVBHN0ZLMU44RUkmZW5jcnlwdGVkSWQ9QTAwMTA0NzdNN0VEUkJLTjdON0UmZW5jcnlwdGVkQWRJZD1BMDYzMTk4ODE1SDlDMTI2NTlHWiZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='],
]

gaming_wheel_data = [
    ['Logitech G29, Racing Wheel and Floor Pedals', 329.99, 'https://www.amazon.co.uk/Logitech-Driving-Force-Racing-Steering/dp/B00YUIM2J0/ref=sr_1_16?crid=URV7GF4QPJT6&keywords=gaming+wheel&qid=1658400598&sprefix=gaming+wheel%2Caps%2C87&sr=8-16'],
    ['Logitech G Driving Force Shifter', 49.99, 'https://www.amazon.co.uk/Logitech-Driving-Force-Shifter-G920/dp/B00ZWOUH4S/ref=sr_1_16?crid=AAI3V6TN3TWO&keywords=gaming+wheel+stick&qid=1658400892&sprefix=gaming+wheel+stick%2Caps%2C96&sr=8-16'],
    ['Logitech G920, Racing Wheel & Pedals Plus Gear Shifter', 348.99, 'https://www.amazon.co.uk/Logitech-Driving-Racing-Shifter-UK-Plug/dp/B01LSKDGVA/ref=sr_1_13?crid=AAI3V6TN3TWO&keywords=gaming+wheel+stick&qid=1658400954&sprefix=gaming+wheel+stick%2Caps%2C96&sr=8-13'],
    ['PXN V9 Racing Wheel with Pedals and Shifter', 179.99, 'https://www.amazon.co.uk/Steering-PXN-Vibration-Feedback-Nintendo/dp/B09PYGP4WZ/ref=sr_1_4?crid=AAI3V6TN3TWO&keywords=gaming+wheel+stick&qid=1658400954&sprefix=gaming+wheel+stick%2Caps%2C96&sr=8-4'],
]

keyboard_data = [
    ['HK GAMING GK61 Mechanical Gaming Keyboard 60 Percent', 79.00, 'https://www.amazon.co.uk/GK61-Swappable-Mechanical-Gaming-Keyboard/dp/B07R1PZRKH/ref=sr_1_2_sspa?crid=1GFEFVNF9JCC0&keywords=ducky+gaming+keyboard&qid=1658401222&sprefix=ducky+gaming+keyboards%2Caps%2C63&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExS0JUQ1U3S1RUVjhNJmVuY3J5cHRlZElkPUEwNzMwMTg3MjZCN1pJNDk5SlExUiZlbmNyeXB0ZWRBZElkPUEwOTM0MTg0SjlENEpNSkZJVlBKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='],
    ['EPOMAKER SKYLOONG SK61 61 Keys Hot Swappable Mechanical Keyboard', 64.99, 'https://www.amazon.co.uk/EPOMAKER-SKYLOONG-Swappable-Mechanical-water-resistant/dp/B08P2L6CCQ/ref=sr_1_5?crid=1GFEFVNF9JCC0&keywords=ducky+gaming+keyboard&qid=1658401334&sprefix=ducky+gaming+keyboards%2Caps%2C63&sr=8-5'],
    ['Snpurdiri K60 60% Gaming Keyboard', 29.99, 'https://www.amazon.co.uk/Snpurdiri-Keyboard-Illuminated-Waterproof-keyboard/dp/B09MYXMWQR/ref=sr_1_3?crid=1GFEFVNF9JCC0&keywords=ducky+gaming+keyboard&qid=1658401334&sprefix=ducky+gaming+keyboards%2Caps%2C63&sr=8-3'],
    ['Minimalist MK-Box Ice Blue, Portable 60% Gaming Mechanical Keyboard', 34.99, 'https://www.amazon.co.uk/dp/B0B3HC8HHY/ref=sspa_dk_detail_3?pd_rd_i=B09J2DDMHM&pd_rd_w=vNlul&content-id=amzn1.sym.1d17a7d9-68f2-46c6-a55b-f888c57f8c2e&pf_rd_p=1d17a7d9-68f2-46c6-a55b-f888c57f8c2e&pf_rd_r=XHBDZP3BNQNCHMXR5K6R&pd_rd_wg=uQPZO&pd_rd_r=9d328654-ba93-4bcc-916c-8c2fe22dafb2&s=computers&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWU9aVFNNRDI2OVhRJmVuY3J5cHRlZElkPUEwODQ1MDAyMUU2Q1lJQUkzOEdGRyZlbmNyeXB0ZWRBZElkPUEwNzEwNzgzMkpKRDcwR1YwSlZUWiZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'],
]

gaming_headsets_data = [
    ['Razer BlackShark V2, Headset', 99.99, 'https://www.amazon.co.uk/Razer-Blackshark-USB-sound-card-Black/dp/B089SSH6L6/ref=sr_1_2_sspa?crid=3731ILM1K3QBZ&keywords=razer+headset&qid=1658401939&s=computers&sprefix=razer+h%2Ccomputers%2C308&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTTdIOVhQWjA3U1lSJmVuY3J5cHRlZElkPUEwMTc4NDg3ODVZODFQUTY4MkdaJmVuY3J5cHRlZEFkSWQ9QTA3MDE3MzkxMFdFQUpEUTU4QzQwJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='],
    ['Razer Kraken, Gaming Headset', 79.99, 'https://www.amazon.co.uk/Razer-Kraken-Headset-Cooling-Ambitious/dp/B07MJFZS9V/ref=sr_1_4?crid=3731ILM1K3QBZ&keywords=razer+headset&qid=1658401984&s=computers&sprefix=razer+h%2Ccomputers%2C308&sr=1-4'],
    ['Razer Kraken X for Console - Wired Console Gaming Headset', 49.99, 'https://www.amazon.co.uk/Razer-Kraken-Headset-Cooling-Ambitious/dp/B0968RDPLG/ref=sr_1_4?crid=3731ILM1K3QBZ&keywords=razer%2Bheadset&qid=1658401984&s=computers&sprefix=razer%2Bh%2Ccomputers%2C308&sr=1-4&th=1'],
    ['Razer Kraken V3 HyperSense Wired USB Gaming Headset', 129.99, 'https://www.amazon.co.uk/Razer-Kraken-Hypersense-Technology-Black-RGB-Chroma/dp/B09D45HQ8N/ref=sr_1_29?crid=3731ILM1K3QBZ&keywords=razer+headset&qid=1658401984&s=computers&sprefix=razer+h%2Ccomputers%2C308&sr=1-29'],
]

mouse_pads_data = [
    ['Hcman RGB Large Gaming Mouse Mat', 14.99, 'https://www.amazon.co.uk/800%C3%97300%C3%974mm-Hcman-Extended-Mousepad-Non-Slip/dp/B07MMLTMXX/ref=sr_1_4?crid=WT63I1VOQUPH&keywords=gaming+mouse+pads&qid=1658402217&s=computers&sprefix=gaming+mouse+pads%2Ccomputers%2C80&sr=1-4'],
    ['TITANWOLF - XXL Speed Gaming Mouse Pad - Mouse Mat', 11.99, 'https://www.amazon.co.uk/TITANWOLF-Gaming-rubber-surfaces-non-slip-black/dp/B07D18Q2HQ/ref=sr_1_15?crid=WT63I1VOQUPH&keywords=gaming+mouse+pads&qid=1658402217&s=computers&sprefix=gaming+mouse+pads%2Ccomputers%2C80&sr=1-15'],
    ['SteelSeries QcK XXL Cloth Gaming Mouse Pad - Mat', 29.99, 'https://www.amazon.co.uk/SteelSeries-QcK-XXL-Gaming-Rubber/dp/B00WAA2704/ref=sr_1_22?crid=WT63I1VOQUPH&keywords=gaming+mouse+pads&qid=1658402217&s=computers&sprefix=gaming+mouse+pads%2Ccomputers%2C80&sr=1-22'],
]

data = [mouse_data, kindle_data, alexa_data, stylist_data, usb_data, gaming_wheel_data, keyboard_data, gaming_headsets_data, mouse_pads_data]
